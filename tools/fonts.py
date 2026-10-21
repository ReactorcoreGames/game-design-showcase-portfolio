"""Font housekeeping for assets/fonts/ (the raw, gitignored font collection).

    python tools/fonts.py list           rebuild workflow/fonts/usage.md: every font, its licence class,
                                         and which page uses it (from the FONTS list in tools/brand.py)
    python tools/fonts.py scan           report fonts whose glyphs reach far outside their own metrics
    python tools/fonts.py scan --move    ... and move them (and fonts that fail to load) to assets/fonts/nah/

Why scan: a glyph drawn past its advance width, or above the font's ascent / below its descent,
spills out of the box the browser lays the text out in. On a page that means letters overlapping
the next word, clipped tops and tails, or a title that pushes past the screen edge on a phone even
though its measured width fits. Wide-but-well-behaved fonts are only listed, not moved: they work
at a smaller size (Zero Hour on graviton-mayhem does).
"""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
FONT_DIR = REPO / "assets" / "fonts"
NAH = FONT_DIR / "nah"
LICENCES = REPO / "workflow" / "fonts" / "licences.txt"
USAGE = REPO / "workflow" / "fonts" / "usage.md"
BRAND = REPO / "tools" / "brand.py"

SAMPLE = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789&?!"
SIDE_LIMIT = 0.20   # ink past the advance width (or left of the origin), in ems
VERT_LIMIT = 0.15   # ink above the ascent or below the descent, in ems
WIDE = 0.80         # average advance per em above this counts as "wide"
KNOWN_BAD = {"MotionControl-BoldItalic.otf": "its WOFF2 fails to decode in Edge and Chrome"}


def font_files() -> list[Path]:
    return sorted(p for p in FONT_DIR.iterdir() if p.is_file() and p.suffix.lower() in (".ttf", ".otf"))


def used_fonts() -> dict[str, str]:
    """Source file -> page(s), from the comments on brand.py's FONTS entries."""
    used = {}
    for line in BRAND.read_text(encoding="utf-8").splitlines():
        m = re.match(r'\s*\("([^"]+)",\s*"[^"]+".*?\),?\s*(?:#\s*(.*))?$', line)
        if m:
            note = (m.group(2) or "site theme").strip()
            used[m.group(1)] = note.split(",", 1)[1].strip() if "," in note else note
    return used


def licence_classes() -> dict[str, tuple[str, str]]:
    out = {}
    if LICENCES.exists():
        for line in LICENCES.read_text(encoding="utf-8").splitlines():
            parts = line.split("|")
            if len(parts) >= 4:
                out[parts[2]] = (parts[0].strip(), parts[3].strip())
    return out


def measure(path: Path) -> dict:
    from fontTools.pens.boundsPen import BoundsPen
    from fontTools.ttLib import TTFont

    with TTFont(path) as font:  # closed afterwards, or Windows refuses to move the file
        return _measure(font)


def _measure(font) -> dict:
    from fontTools.pens.boundsPen import BoundsPen

    upm = font["head"].unitsPerEm
    os2 = font["OS/2"] if "OS/2" in font else None
    ascent = os2.usWinAscent if os2 and os2.usWinAscent else font["hhea"].ascent
    descent = os2.usWinDescent if os2 and os2.usWinDescent else -font["hhea"].descent
    cmap = font.getBestCmap() or {}
    gs = font.getGlyphSet()
    hmtx = font["hmtx"]
    side = vert = 0.0
    widths = []
    for ch in SAMPLE:
        name = cmap.get(ord(ch))
        if not name:
            continue
        adv = hmtx[name][0]
        widths.append(adv)
        pen = BoundsPen(gs)
        gs[name].draw(pen)
        if not pen.bounds:
            continue
        x0, y0, x1, y1 = pen.bounds
        side = max(side, (x1 - adv) / upm, -x0 / upm)
        vert = max(vert, (y1 - ascent) / upm, (-y0 - descent) / upm)
    return {"side": side, "vert": vert, "width": (sum(widths) / len(widths) / upm) if widths else 0, "glyphs": len(widths)}


def cmd_scan(move: bool) -> None:
    used = used_fonts()
    bad, wide = [], []
    for path in font_files():
        if path.name in KNOWN_BAD:
            bad.append((path, KNOWN_BAD[path.name]))
            continue
        try:
            m = measure(path)
        except Exception as e:  # noqa: BLE001 - any font that won't parse is unusable
            bad.append((path, f"won't load ({type(e).__name__})"))
            continue
        why = []
        if m["glyphs"] < 26:
            why.append(f"only {m['glyphs']} of the basic Latin test glyphs")
        if m["side"] > SIDE_LIMIT:
            why.append(f"ink {m['side']:.2f} em past its advance")
        if m["vert"] > VERT_LIMIT:
            why.append(f"ink {m['vert']:.2f} em outside ascent/descent")
        if why:
            bad.append((path, "; ".join(why)))
        elif m["width"] > WIDE:
            wide.append((path, m["width"]))

    print(f"{len(bad)} fonts that spill or won't load:")
    for path, why in bad:
        flag = "  IN USE, kept" if path.name in used else ""
        print(f"  {path.name}: {why}{flag}")
    print(f"\n{len(wide)} wide fonts (fine, but need a smaller title size):")
    for path, w in wide:
        print(f"  {path.name}: {w:.2f} em per glyph")

    if move:
        NAH.mkdir(exist_ok=True)
        moved = 0
        for path, why in bad:
            if path.name in used:
                continue
            shutil.move(str(path), NAH / path.name)
            moved += 1
        (NAH / "README.txt").write_text(
            "Fonts moved here by `python tools/fonts.py scan --move`: their glyphs spill far outside their\n"
            "own metrics (letters overlap or get clipped, titles run off the screen) or they fail to load.\n"
            "Run the scan without --move to see the reason for each.\n", encoding="utf-8")
        print(f"\nmoved {moved} fonts to {NAH.relative_to(REPO)}")


def cmd_list() -> None:
    used = used_fonts()
    classes = licence_classes()
    rows = []
    for path in font_files():
        cls, lic = classes.get(path.name, ("", ""))
        rows.append((path.name, cls or "?", used.get(path.name, "")))
    safe = [r for r in rows if r[1] in ("CC0", "OFL")]
    lines = [
        "# Font usage",
        "",
        "Generated by `python tools/fonts.py list` from `licences.txt` and the `FONTS` list in `tools/brand.py`. Don't edit by hand; rerun it after adding a font to a page.",
        "",
        f"`assets/fonts/` holds {len(rows)} font files. {len(safe)} carry a CC0 or SIL OFL licence in the file itself, which is what the page brief prefers; {sum(1 for r in safe if r[2])} of those are in use. The rest have another licence (CC BY-SA, BY-ND, non-commercial, freeware) or none embedded at all (`?`), so check each one's terms at its source before using it. Fonts that spill outside their own metrics are in `assets/fonts/nah/` (see `python tools/fonts.py scan`).",
        "",
        "## CC0 and SIL OFL",
        "",
        "| Font file | Licence | Used by |",
        "|---|---|---|",
    ]
    lines += [f"| {n} | {c} | {u or 'unused'} |" for n, c, u in safe]
    lines += ["", "## Everything else", "", "| Font file | Licence | Used by |", "|---|---|---|"]
    lines += [f"| {n} | {c if c != '?' else 'none embedded'} | {u or 'unused'} |" for n, c, u in rows if (n, c, u) not in safe]
    USAGE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {USAGE.relative_to(REPO)}: {len(rows)} fonts, {len(safe)} CC0/OFL, {sum(1 for r in rows if r[2])} in use")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list")
    p = sub.add_parser("scan")
    p.add_argument("--move", action="store_true")
    args = ap.parse_args()
    if args.cmd == "list":
        cmd_list()
    else:
        cmd_scan(args.move)


if __name__ == "__main__":
    main()
