"""Render the book's itch.io images with headless Edge into book/release/.

    python tools/book_promo.py

Builds the release first (tools/book.py release), then:
- promo/cover.jpg (1280x720) and promo/thumbnail.jpg (630x500): art pages in the book's own look,
  drawn from the offline stylesheet so the fonts and icons are the real ones;
- promo/screenshot-N.jpg (1920x1080): pages of the offline edition, opened from dist/ over file://,
  which doubles as the check that the download works without a server;
- epub-cover.jpg (1600x2560), then rebuilds the EPUB so it carries the new cover.

Each image is saved as JPEG or PNG, whichever is smaller. Needs Microsoft Edge (or set EDGE=path).
"""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).parent))
import book  # noqa: E402

PROMO = book.RELEASE_SRC / "promo"
OFFLINE_BOOK = book.DIST / book.ZIP_FOLDER / "book"
EDGE = os.environ.get("EDGE", r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

# (output name, offline page) for the screenshots, in the order itch.io shows them.
SCREENSHOTS = [
    ("screenshot-1", "index.html"),
    ("screenshot-2", "c09-understanding-human-beings.html"),
    ("screenshot-3", "c10-fun-is-the-fulfillment-of-needs.html"),
    ("screenshot-4", "b1-needs-at-a-glance.html"),
    ("screenshot-5", "p4-designing-the-game.html"),
]

ART = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<link rel="stylesheet" href="{css}">
<style>
    html, body {{ margin: 0; width: {w}px; height: {h}px; overflow: hidden; }}
    body {{ position: relative; background: radial-gradient(ellipse at 30% 40%, #0a2a16 0%, #040b16 60%) #040b16; }}
    .grid {{ position: absolute; inset: 0; background-image: linear-gradient(rgba(57,255,90,.07) 1px, transparent 1px),
             linear-gradient(90deg, rgba(57,255,90,.07) 1px, transparent 1px); background-size: {cell}px {cell}px; }}
    .titles {{ position: absolute; inset: -40% -30%; transform: rotate(-12deg); display: flex; flex-wrap: wrap; gap: 0.2em 1.1em;
               align-content: center; font-family: var(--font-ui); font-weight: 600; text-transform: uppercase;
               letter-spacing: .12em; font-size: {tsize}px; line-height: 1.5; color: rgba(57,255,90,.13); }}
    .titles b {{ color: rgba(19,255,230,.2); font-weight: 600; }}
    .book-icon {{ position: absolute; {icon_pos}; width: {icon}px; height: {icon}px; background: rgba(57,255,90,.08);
                  -webkit-mask: var(--icon-open-book-lorc) center / contain no-repeat; mask: var(--icon-open-book-lorc) center / contain no-repeat; }}
    .vignette {{ position: absolute; inset: 0; background: radial-gradient(ellipse at center, transparent 35%, rgba(2,6,12,.88) 100%); }}
    .art {{ position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; gap: {gap}px; flex-direction: {dir}; text-align: {align}; }}
    .logo {{ width: {logo}px; height: {logo}px; image-rendering: pixelated;
             filter: drop-shadow(0 0 14px rgba(57,255,90,.75)) drop-shadow(0 0 48px rgba(57,255,90,.35)); }}
    h1 {{ font-family: var(--font-head); font-weight: 900; text-transform: uppercase; color: #fff; margin: 0;
          font-size: {h1}px; line-height: 1.02; letter-spacing: .02em;
          text-shadow: 0 0 3px #000, 0 4px 10px rgba(0,0,0,.9), 0 0 22px rgba(57,255,90,.6), 0 0 60px rgba(57,255,90,.35); }}
    .sub {{ font-family: var(--font-ui); font-weight: 600; text-transform: uppercase; letter-spacing: .14em; color: #39ff5a;
            font-size: {sub}px; margin: .35em 0 0; text-shadow: 0 0 3px #000, 0 2px 8px #000, 0 0 18px rgba(57,255,90,.5); }}
    .tag {{ font-family: var(--font-body); color: #e6f6ea; font-size: {tag}px; margin: .7em 0 0; line-height: 1.35;
            text-shadow: 0 0 3px #000, 0 2px 8px #000; }}
    .by {{ font-family: var(--font-ui); font-weight: 600; text-transform: uppercase; letter-spacing: .2em; color: #13ffe6;
           font-size: {by}px; margin: .9em 0 0; text-shadow: 0 0 3px #000, 0 2px 8px #000; }}
    .bar {{ position: absolute; left: 0; right: 0; bottom: 0; padding: {barpad}px 0; text-align: center; background: rgba(2,8,14,.82);
            border-top: 2px solid #39ff5a; box-shadow: 0 0 30px rgba(57,255,90,.35); font-family: var(--font-ui); font-weight: 600;
            text-transform: uppercase; letter-spacing: .14em; color: #fff; font-size: {barsize}px; }}
    .bar span {{ color: #39ff5a; padding: 0 .5em; }}
</style>
</head>
<body class="book">
    <div class="grid"></div>
    <div class="titles">{titles}</div>
    <div class="book-icon"></div>
    <div class="vignette"></div>
    <div class="art">
        <img class="logo" src="{logo_src}" alt="">
        <div>
            <h1>{title}</h1>
            <p class="sub">The Holy Grail of Fun</p>
            {extra}
        </div>
    </div>
    {bar}
</body>
</html>
"""

VARIANTS = {
    # name: size, layout and type sizes. Big type only; the dense detail is the background.
    "cover": dict(w=1280, h=720, dir="row", align="left", gap=56, logo=300, h1=92, sub=34, tag=30, by=22, tsize=22, cell=40,
                  icon=560, icon_pos="right: -90px; top: -60px", title="Game Design<br>Technology",
                  extra='<p class="tag">Where fun really comes from,<br>and how to design for it on purpose.</p>',
                  barsize=26, barpad=16, bar_text="A book by Reactorcore<span>·</span>34 chapters<span>·</span>HTML + EPUB"),
    "thumbnail": dict(w=630, h=500, dir="column", align="center", gap=10, logo=150, h1=60, sub=25, tag=0, by=0, tsize=15, cell=30,
                      icon=360, icon_pos="right: -80px; top: -40px", title="Game Design<br>Technology", extra="",
                      barsize=19, barpad=10, bar_text="A book by Reactorcore"),
    "epub-cover": dict(w=1600, h=2560, dir="column", align="center", gap=80, logo=640, h1=168, sub=72, tag=64, by=56, tsize=40, cell=80,
                       icon=1300, icon_pos="right: -380px; top: -200px", title="Game<br>Design<br>Technology",
                       extra='<p class="tag">Where fun really comes from,<br>and how to design for it on purpose.</p>'
                             '<p class="by">Reactorcore</p>',
                       barsize=0, barpad=0, bar_text=""),
}


def shoot(url: str, w: int, h: int, out: Path, profile: str) -> None:
    subprocess.run([EDGE, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--no-first-run",
                    f"--user-data-dir={profile}", f"--window-size={w},{h}", "--virtual-time-budget=4000",
                    f"--screenshot={out}", url], check=True, capture_output=True)


def save_smallest(png: Path, name: str, folder: Path) -> Path:
    img = Image.open(png).convert("RGB")
    for old in folder.glob(f"{name}.*"):
        old.unlink()                         # the other format from an earlier run
    jpg, alt = folder / f"{name}.jpg", folder / f"{name}.png"
    img.save(jpg, quality=90, optimize=True, progressive=True)
    img.save(alt, optimize=True)
    keep, drop = (jpg, alt) if jpg.stat().st_size <= alt.stat().st_size else (alt, jpg)
    drop.unlink()
    return keep


def main() -> None:
    if not Path(EDGE).exists():
        sys.exit(f"Edge not found at {EDGE}; set EDGE to a Chromium-based browser")
    book.cmd_release(None)
    pages, _ = book.load_all()
    titles = " ".join(f"<b>{p.number}</b> {book.esc(p.label)}" if p.number else book.esc(p.label) for p in pages)
    PROMO.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        profile = str(tmp / "edge")
        for name, v in VARIANTS.items():
            page = tmp / f"{name}.html"
            bar = f'<div class="bar">{v["bar_text"]}</div>' if v["bar_text"] else ""
            page.write_text(ART.format(css=(OFFLINE_BOOK / "assets" / "book.css").as_uri(),
                                       logo_src=(OFFLINE_BOOK / "assets" / "book-logo.png").as_uri(),
                                       titles=" ".join([titles] * 3), bar=bar, **v), encoding="utf-8")
            shoot(page.as_uri(), v["w"], v["h"], tmp / f"{name}.png", profile)
            out = save_smallest(tmp / f"{name}.png", name, book.RELEASE_SRC if name == "epub-cover" else PROMO)
            print(out.relative_to(book.REPO).as_posix())
        for name, target in SCREENSHOTS:
            shoot((OFFLINE_BOOK / target).as_uri(), 1920, 1080, tmp / f"{name}.png", profile)
            print(save_smallest(tmp / f"{name}.png", name, PROMO).relative_to(book.REPO).as_posix())

    if (book.RELEASE_SRC / "epub-cover.png").exists():
        sys.exit("epub-cover came out as PNG; tools/book.py expects epub-cover.jpg")
    book.cmd_release(None)                   # again, so the EPUB carries the new cover


if __name__ == "__main__":
    main()
