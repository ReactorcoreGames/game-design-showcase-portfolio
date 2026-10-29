"""Image pipeline for showcase pages: spec -> BAIG -> resized JPEGs in site/.

Each project has a spec at image-prompts/<slug>.json (format in workflow/image-brief.md).
The pages already reference the final file names, so this tool only has to
produce files at exactly those paths.

A spec with an "out" folder (relative to the repo) is a free-form section spec instead of a
project's five: any number of images, each with a "name", saved as <out>/<NN>-<name>.jpg
and no thumbnail. The AAL page (site/aal/) uses one, and so do the project pages' mini images:
those specs add "size" ([320, 240]: centre-crop and resize to exactly that), "quality" (JPEG,
default 82) and "lead" (text put in front of every prompt, for SDXL). An image's own "size"
overrides the spec's, so one spec can mix full-size and half-size images (a richer page's extras).

    python tools/images.py check  [slug ...]             validate specs, show lengths and image count
    python tools/images.py gen    slug ... [--dry-run]   generate through BAIG (klein4b, Standard tier)
                                   [--model M --only 1,6]  ... or reroll some images on another model
    python tools/images.py finish slug ... [--only 3]    resize + JPEG (+ thumbnail) into site/
    python tools/images.py collage slug ...              numbered contact sheet of finished images into wip/shots/
    python tools/images.py recompress [--apply]          re-encode existing site images (report only by default)

No slug given to check = every spec. gen refuses to queue more than --max images
(default 70: the Klein free allowance minus a margin that keeps SDXL usable).

An image with "model" in its spec (e.g. "nano-banana-2-lite") was rerolled on that model:
finish takes it from that model's output instead of --model.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import math
import os
import re
import subprocess
import sys
from pathlib import Path

from PIL import Image

REPO = Path(__file__).resolve().parent.parent
SPECS = REPO / "image-prompts"
WORK = REPO / "_work"
SITE_IMAGES = REPO / "site" / "projects" / "images"
SITE_THUMBS = REPO / "site" / "projects" / "thumbnails"
BAIG = Path(os.environ.get("BAIG_DIR", r"C:\ClaudeWorkspace\AI image gen batch program"))

ROLES = {1: "title", 2: "vignette", 3: "feature", 4: "boxart", 5: "story"}
RATIOS = {"16:9", "3:2", "1:1", "2:3", "9:16"}
TARGET_PIXELS = 1280 * 720  # every image is scaled to this area, whatever its ratio
THUMB_SIZE = (640, 360)
JPEG_QUALITY = 82
PROMPT_LIMIT = 1800  # prompt + style suffix; klein's encoder cuts off silently near 2000
DAILY_MAX = 70


def load_presets() -> dict[str, str]:
    cfg = BAIG / "config.json"
    if not cfg.exists():
        return {}
    return json.loads(cfg.read_text(encoding="utf-8")).get("style_presets", {})


def load_spec(slug: str) -> dict:
    path = SPECS / f"{slug}.json"
    if not path.exists():
        sys.exit(f"no spec: {path}")
    spec = json.loads(path.read_text(encoding="utf-8"))
    spec.setdefault("slug", slug)
    spec.setdefault("prefix", slug)
    return spec


def all_slugs() -> list[str]:
    return sorted(p.stem for p in SPECS.glob("*.json"))


def style_suffix(spec: dict, presets: dict[str, str], preset_override: str | None = None) -> str:
    """Preset text (by name, from BAIG's config) followed by the spec's own extra style words."""
    parts = []
    name = preset_override or spec.get("preset")
    if name:
        if name not in presets:
            sys.exit(f"{spec['slug']}: unknown BAIG preset {name!r}")
        parts.append(presets[name])
    if spec.get("style"):
        parts.append(spec["style"])
    return " ".join(p.strip() for p in parts if p.strip())


def dest_path(spec: dict, img: dict) -> Path:
    if spec.get("out"):
        return REPO / spec["out"] / f"{img['n']:02d}-{img['name']}.jpg"
    return SITE_IMAGES / f"{spec['prefix']}_{img['n']}_{img['role']}.jpg"


def validate(spec: dict, presets: dict[str, str]) -> list[str]:
    errors = []
    free = bool(spec.get("out"))
    nums = sorted(img.get("n") for img in spec.get("images", []))
    expected = list(range(1, len(nums) + 1)) if free else [1, 2, 3, 4, 5]
    if not nums or nums != expected:
        errors.append(f"images must be n={expected[0] if expected else 1}..{expected[-1] if expected else 'N'}, got {nums}")
    suffix = style_suffix(spec, presets)
    for img in spec.get("images", []):
        n = img.get("n")
        if free:
            if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", img.get("name", "")):
                errors.append(f"image {n}: needs a kebab-case name, got {img.get('name')!r}")
        elif img.get("role") != ROLES.get(n):
            errors.append(f"image {n}: role should be {ROLES.get(n)!r}, got {img.get('role')!r}")
        if img.get("ratio") not in RATIOS:
            errors.append(f"image {n}: bad ratio {img.get('ratio')!r}")
        prompt = img.get("prompt", "").strip()
        if not prompt or "\n" in prompt:
            errors.append(f"image {n}: prompt must be one non-empty line")
        total = len(prompt) + 1 + len(suffix)
        if total > PROMPT_LIMIT:
            errors.append(f"image {n}: prompt+style is {total} chars (limit {PROMPT_LIMIT})")
    return errors


def cmd_check(args) -> None:
    presets = load_presets()
    slugs = args.slugs or all_slugs()
    total = 0
    bad = False
    for slug in slugs:
        spec = load_spec(slug)
        suffix = style_suffix(spec, presets)
        errors = validate(spec, presets)
        longest = max((len(i.get("prompt", "")) for i in spec.get("images", [])), default=0)
        state = "OK " if not errors else "ERR"
        print(f"{state} {slug:32} preset={spec.get('preset')!r} style={len(suffix)}c longest prompt={longest}c")
        for e in errors:
            print(f"      - {e}")
        bad |= bool(errors)
        total += len(spec.get("images", []))
    print(f"\n{len(slugs)} specs, {total} images")
    if bad:
        sys.exit(1)


def ratio_tag(ratio: str) -> str:
    return "p" + ratio.replace(":", "x")


def cmd_gen(args) -> None:
    presets = load_presets()
    plan = []
    for slug in args.slugs:
        spec = load_spec(slug)
        errors = validate(spec, presets)
        if errors:
            sys.exit(f"{slug}: spec invalid, run check")
        plan.append(spec)
    only = {int(n) for n in args.only.split(",")} if args.only else None
    for spec in plan:
        spec["images"] = [i for i in spec["images"] if only is None or i["n"] in only]
    count = sum(len(s["images"]) for s in plan)
    print(f"{count} images across {len(plan)} projects, model {args.model}")
    if count > args.max and not args.dry_run:
        sys.exit(f"refusing: {count} > --max {args.max}")

    failed = []
    for spec in plan:
        suffix = style_suffix(spec, presets, args.preset)
        out = WORK / spec["slug"] / f"raw-{args.model}"
        out.mkdir(parents=True, exist_ok=True)
        groups: dict[str, list[dict]] = {}
        for img in sorted(spec["images"], key=lambda i: i["n"]):
            groups.setdefault(img["ratio"], []).append(img)
        for ratio, imgs in groups.items():
            pdir = prompt_dir(spec["slug"], args.model)
            pdir.mkdir(parents=True, exist_ok=True)
            # an --only run gets its own short prompt file name (BAIG keeps 16 characters and turns - into _).
            # The prompts are part of the hash, so a reworded retry is a new batch, not the old failed one.
            key = ",".join(str(i["n"]) for i in imgs) + "|" + "|".join(i["prompt"] for i in imgs)
            run = "_" + hashlib.md5(key.encode()).hexdigest()[:6] if only else ""
            pfile = pdir / f"{ratio_tag(ratio)}{run}.txt"
            lead = args.lead or spec.get("lead", "")
            lines = [(lead + img["prompt"].strip()) for img in imgs]
            pfile.write_text("\n".join(lines) + "\n", encoding="utf-8")
            # line number -> image n, so finish can map BAIG's output back
            (pfile.with_suffix(".map.json")).write_text(json.dumps([i["n"] for i in imgs]))
            cmd = [
                sys.executable, str(BAIG / "cli.py"), "dry-run" if args.dry_run else "run",
                str(pfile), "-o", str(out), "--model", args.model, "--ratio", ratio,
                "--tier", "standard", "--style-text", suffix,
            ]
            print(f"\n== {spec['slug']} {ratio} ({len(imgs)} images)")
            # a failed job (e.g. a false-positive content flag) shouldn't stop the other ratio groups
            if subprocess.run(cmd, cwd=BAIG).returncode != 0:
                failed.append(f"{spec['slug']} {ratio}")
    if failed:
        sys.exit("some jobs failed (see above), rerun them with --only: " + ", ".join(failed))


def prompt_dir(slug: str, model: str) -> Path:
    """Where gen writes a model's prompt files and line maps. Klein's stay at the top of the
    project's work folder; other models get their own folder, so a reroll never overwrites the
    line map another model's output depends on. Prompt file names stay short because BAIG
    squeezes the stem it puts in output names to 16 characters."""
    return WORK / slug if model == "klein4b" else WORK / slug / f"prompts-{model}"


def find_raw(slug: str, model: str, n: int) -> Path:
    """The newest output for image n across every gen run of this model (full runs and --only)."""
    hits = []
    for mapfile in prompt_dir(slug, model).glob("p*.map.json"):
        order = json.loads(mapfile.read_text())
        if n in order:
            stem = mapfile.name.removesuffix(".map.json")
            line = order.index(n) + 1
            hits += [h for h in (WORK / slug / f"raw-{model}").glob(f"{stem}-{line:03d}-*.*")
                     if h.suffix.lower() in (".jpg", ".jpeg", ".png")]
    if not hits:
        sys.exit(f"{slug}: no {model} output for image {n} (run gen first)")
    return max(hits, key=lambda p: p.stat().st_mtime)


def scale_to_area(im: Image.Image, pixels: int = TARGET_PIXELS) -> Image.Image:
    w, h = im.size
    if w * h <= pixels:
        return im
    k = math.sqrt(pixels / (w * h))
    size = (round(w * k / 2) * 2, round(h * k / 2) * 2)
    return im.resize(size, Image.LANCZOS)


def fit_size(im: Image.Image, size: list[int]) -> Image.Image:
    """Centre-crop to the size's aspect ratio, then resize to exactly that size (mini images)."""
    w, h = im.size
    tw, th = size
    if w * th > h * tw:
        cw = round(h * tw / th)
        im = im.crop(((w - cw) // 2, 0, (w - cw) // 2 + cw, h))
    else:
        ch = round(w * th / tw)
        im = im.crop((0, (h - ch) // 2, w, (h - ch) // 2 + ch))
    return im.resize((tw, th), Image.LANCZOS)


def save_jpeg(im: Image.Image, path: Path, quality: int = JPEG_QUALITY) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    im.convert("RGB").save(path, "JPEG", quality=quality, optimize=True, progressive=True)
    return path.stat().st_size


def cmd_finish(args) -> None:
    for slug in args.slugs:
        spec = load_spec(slug)
        prefix = spec["prefix"]
        only = {int(n) for n in args.only.split(",")} if args.only else None
        for img in sorted(spec["images"], key=lambda i: i["n"]):
            if only is not None and img["n"] not in only:
                continue
            src = find_raw(slug, img.get("model", args.model), img["n"])
            size = img.get("size") or spec.get("size")
            im = fit_size(Image.open(src), size) if size else scale_to_area(Image.open(src))
            dest = dest_path(spec, img)
            kb = save_jpeg(im, dest, spec.get("quality", JPEG_QUALITY)) // 1024
            print(f"{dest.relative_to(REPO)}  {im.size[0]}x{im.size[1]}  {kb} KB")
            if img["n"] == 2 and not spec.get("out"):
                thumb = Image.open(src).convert("RGB")
                thumb.thumbnail((THUMB_SIZE[0] * 4, THUMB_SIZE[1] * 4))
                thumb = thumb.resize(THUMB_SIZE, Image.LANCZOS)
                tdest = SITE_THUMBS / f"{prefix}_2_vignette_thumb.jpg"
                tsize = save_jpeg(thumb, tdest)
                print(f"{tdest.relative_to(REPO)}  {THUMB_SIZE[0]}x{THUMB_SIZE[1]}  {tsize // 1024} KB")


def cmd_collage(args) -> None:
    """A numbered contact sheet of a spec's finished images, for reviewing a batch at a glance."""
    from PIL import ImageDraw
    out_dir = REPO / "wip" / "shots"
    out_dir.mkdir(parents=True, exist_ok=True)
    for slug in args.slugs:
        spec = load_spec(slug)
        tiles = []
        for img in sorted(spec["images"], key=lambda i: i["n"]):
            path = dest_path(spec, img)
            if path.exists():
                tiles.append((img["n"], Image.open(path).convert("RGB")))
        if not tiles:
            sys.exit(f"{slug}: no finished images yet")
        tw = max(t.size[0] for _, t in tiles)
        th = max(t.size[1] for _, t in tiles)
        cols = min(len(tiles), args.cols)
        rows = math.ceil(len(tiles) / cols)
        pad = 8
        sheet = Image.new("RGB", (cols * (tw + pad) + pad, rows * (th + pad) + pad), (24, 24, 24))
        draw = ImageDraw.Draw(sheet)
        for i, (n, t) in enumerate(tiles):
            x, y = pad + (i % cols) * (tw + pad), pad + (i // cols) * (th + pad)
            sheet.paste(t, (x, y))
            draw.rectangle((x, y, x + 34, y + 26), fill=(0, 0, 0))
            draw.text((x + 8, y + 6), f"{n:02d}", fill=(255, 255, 255))
        dest = out_dir / f"{slug}.png"
        sheet.save(dest)
        print(dest.relative_to(REPO))


def cmd_recompress(args) -> None:
    before = after = 0
    for path in sorted(SITE_IMAGES.glob("*.jpg")):
        data = path.read_bytes()
        im = scale_to_area(Image.open(io.BytesIO(data)))
        buf = io.BytesIO()
        im.convert("RGB").save(buf, "JPEG", quality=JPEG_QUALITY, optimize=True, progressive=True)
        before += len(data)
        new = buf.getvalue()
        if len(new) < len(data):
            after += len(new)
            if args.apply:
                path.write_bytes(new)
        else:
            after += len(data)
    verb = "rewrote" if args.apply else "would shrink"
    print(f"{verb} site images: {before / 1e6:.1f} MB -> {after / 1e6:.1f} MB")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("check")
    p.add_argument("slugs", nargs="*")
    p.set_defaults(func=cmd_check)

    p = sub.add_parser("gen")
    p.add_argument("slugs", nargs="+")
    p.add_argument("--model", default="klein4b")
    p.add_argument("--preset", help="override the spec's preset (e.g. a photo/watercolor one for sdxl)")
    p.add_argument("--lead", default="", help="text put in FRONT of every prompt (sdxl only reads ~300 chars)")
    p.add_argument("--only", help="comma-separated image numbers to generate, e.g. 1,6,9")
    p.add_argument("--max", type=int, default=DAILY_MAX)
    p.add_argument("--dry-run", action="store_true")
    p.set_defaults(func=cmd_gen)

    p = sub.add_parser("finish")
    p.add_argument("slugs", nargs="+")
    p.add_argument("--model", default="klein4b")
    p.add_argument("--only", help="finish only these image numbers (a rewrite that regenerated some of them)")
    p.set_defaults(func=cmd_finish)

    p = sub.add_parser("collage")
    p.add_argument("slugs", nargs="+")
    p.add_argument("--cols", type=int, default=5)
    p.set_defaults(func=cmd_collage)

    p = sub.add_parser("recompress")
    p.add_argument("--apply", action="store_true")
    p.set_defaults(func=cmd_recompress)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
