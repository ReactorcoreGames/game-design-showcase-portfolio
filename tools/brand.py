"""Brand assets for the site theme: web fonts, logo, favicons and icon masks.

Sources live in the gitignored assets/ folder; this tool writes only the optimized
files the site uses.

    python tools/brand.py fonts                 WOFF2 Latin subsets into site/fonts/
    python tools/brand.py logo                  header logo + favicon set into site/
    python tools/brand.py book-logo             the book's green mark into site/book/
    python tools/brand.py icons name ...        game-icons PNG -> alpha mask into site/icons/
    python tools/brand.py all                   fonts + logo + every icon already in site/icons/

Icon names are file names in assets/icons/ without ".png" (e.g. reactor-sbed).
Icons are white-on-black greyscale; the mask keeps the luminance as alpha, so
CSS mask-image can tint one file any colour.
"""

from __future__ import annotations

import argparse
import base64
import io
import sys
from pathlib import Path

from PIL import Image

REPO = Path(__file__).resolve().parent.parent
ASSETS = REPO / "assets"
SITE = REPO / "site"

# Latin, matching Google Fonts' "latin" range.
LATIN = ("U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,"
         "U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD")

# (source in assets/fonts, output name, variable-axis pin, renamed family or None)
# Orbitron has the Reserved Font Name "Orbitron", so the modified (pinned + subset) build
# must ship under another name.
FONTS = [
    ("Oxanium-Medium.ttf", "oxanium-medium.woff2", None, None),
    ("Oxanium-SemiBold.ttf", "oxanium-semibold.woff2", None, None),
    ("Orbitron[wght].ttf", "rc-display-black.woff2", {"wght": 900}, "RC Display"),
    # Project pages' own display fonts (see workflow/page-brief.md). Check each font's
    # embedded licence first; prefer CC0 and SIL OFL ones.
    ("Stormfaze.otf", "stormfaze.woff2", None, None),                       # CC0, AAL-Bunkerships, greensteelcommander
    ("OperationNapalm-Regular.ttf", "operation-napalm.woff2", None, None),  # CC0, AAL-Bunkerships
    ("Zero Hour.otf", "zero-hour.woff2", None, None),                       # CC0, graviton-mayhem
    ("Squares Bold Free.otf", "squares-bold.woff2", None, None),            # SIL OFL, graviton-mayhem, smash-droids
    ("Radio Stars.otf", "radio-stars.woff2", None, None),                   # CC0, AAL-Stealth-Sector, cyberdungeon, starforge-legion
    ("Unique.ttf", "unique.woff2", None, None),                             # SIL OFL, AAL-Stealth-Sector
    ("Dendritic Voltage.otf", "dendritic-voltage.woff2", None, None),       # CC0, AALSuperweapon, colossal_devastators
    ("TurretRoad-Bold.ttf", "turret-road-bold.woff2", None, None),          # SIL OFL, AALSuperweapon
    ("Anklepants.otf", "anklepants.woff2", None, None),                     # CC0, ChainReactionDemolitionPunch, bunkership, thunderstrike-justice
    ("6809 Chargen.otf", "chargen-6809.woff2", None, None),                 # CC0, ChainReactionDemolitionPunch, tile-mechs
    ("Audiowide-Regular.ttf", "audiowide.woff2", None, None),               # SIL OFL, City Buster, spacelancer
    ("Jersey10-Regular.ttf", "jersey-10.woff2", None, None),                # SIL OFL, City Buster, colossal_devastators, roomspace, smash-droids
    ("Exo2.0-Black.otf", "exo2-black.woff2", None, None),                   # SIL OFL, Collidotron
    ("Electrolize-Regular.ttf", "electrolize.woff2", None, None),           # SIL OFL, Collidotron, bunkership, roomspace
    ("Spectrashell.otf", "spectrashell.woff2", None, None),                 # CC0, Custom Dismount, Underground Brawl, lattice-walker
    ("ShareTechMono-Regular.ttf", "share-tech-mono.woff2", None, None),     # SIL OFL, Custom Dismount, greensteelcommander
    ("Hydrogen Whiskey.otf", "hydrogen-whiskey.woff2", None, None),         # CC0, EradicationWars, RussiBiomonster, unhinged_lander_heist_scifi
    ("Aldrich-Regular.ttf", "aldrich.woff2", None, None),                   # SIL OFL, EradicationWars
    ("Fragile Bombers.otf", "fragile-bombers.woff2", None, None),           # CC0, Halberd_Suit_Wars, Skullhead
    ("Iceland-Regular.ttf", "iceland.woff2", None, None),                   # SIL OFL, Halberd_Suit_Wars, lattice-walker
    ("ExpletusSans-Bold.ttf", "expletus-sans-bold.woff2", None, None),      # SIL OFL, HazardMissionTeam (2)
    ("MatrixTypeDisplay-Bold.ttf", "matrixtype-display-bold.woff2", None, None),  # CC0, Justice Will Glass Them
    ("Micro5-Regular.ttf", "micro5.woff2", None, None),                     # SIL OFL, Justice Will Glass Them, tile-mechs
    ("OperationNapalm-Italic.ttf", "operation-napalm-italic.woff2", None, None),  # CC0, Mafia_Takedown
    ("TurretRoad-Medium.ttf", "turret-road-medium.woff2", None, None),      # SIL OFL, Mafia_Takedown
    ("Exo2.0-BoldItalic.otf", "exo2-bold-italic.woff2", None, None),        # SIL OFL, Megalodon
    ("MatrixType-Bold.ttf", "matrixtype-bold.woff2", None, None),           # CC0, Megalodon
    ("Skateblade-RegularItalic.ttf", "skateblade-italic.woff2", None, None),  # SIL OFL, Mosh_Pit_Mayhem (with Anklepants)
    ("Zeroes Two.otf", "zeroes-two.woff2", None, None),                     # CC0, MutantLoveQuest, unhinged_lander_heist_scifi
    ("ExpletusSans-Medium.ttf", "expletus-sans-medium.woff2", None, None),  # SIL OFL, MutantLoveQuest
    ("Skateblade-Regular.ttf", "skateblade.woff2", None, None),             # SIL OFL, Planetary Ring Miner, kickblade
    ("exo.regular.otf", "exo-regular.woff2", None, None),                   # SIL OFL, Planetary Ring Miner
    ("World of Water.otf", "world-of-water.woff2", None, None),             # CC0, Poo Storm Janitor Powersuit
    ("Exo2.0-ExtraBoldItalic.otf", "exo2-extrabold-italic.woff2", None, None),  # SIL OFL, Poo Storm Janitor Powersuit
    ("Zeroes One.otf", "zeroes-one.woff2", None, None),                     # CC0, StardustAssault, shape-smasher
    ("MatrixTypeDisplay-Regular.ttf", "matrixtype-display.woff2", None, None),  # CC0, StardustAssault
    ("Unsteady Oversteer.otf", "unsteady-oversteer.woff2", None, None),     # CC0, Zero Space Robo Derby, shape-smasher
    ("Zeroes Three.otf", "zeroes-three.woff2", None, None),                 # CC0, Zero Space Robo Derby
    ("Cranberry Gin.otf", "cranberry-gin.woff2", None, None),               # CC0, abyssal_caretaker
    ("ExpletusSans-SemiBoldItalic.ttf", "expletus-sans-semibold-italic.woff2", None, None),  # SIL OFL, abyssal_caretaker
    ("Exo2.0-BlackItalic.otf", "exo2-black-italic.woff2", None, None),      # SIL OFL, admiralwars, vectorthunder
    ("TurretRoad-Regular.ttf", "turret-road.woff2", None, None),            # SIL OFL, admiralwars
    ("MatrixType-Regular.ttf", "matrixtype.woff2", None, None),             # CC0, antigrav_deconstruction
    ("Exo2.0-ExtraBold.otf", "exo2-extrabold.woff2", None, None),           # SIL OFL, astro_industry
    ("ExpletusSans-SemiBold.ttf", "expletus-sans-semibold.woff2", None, None),  # SIL OFL, astro_industry
    ("Exo2.0-MediumItalic.otf", "exo2-medium-italic.woff2", None, None),     # SIL OFL, cyberdungeon
    ("ExpletusSans-BoldItalic.ttf", "expletus-sans-bold-italic.woff2", None, None),  # SIL OFL, kickblade
    ("Zector.ttf", "zector.woff2", None, None),                             # SIL OFL, spacelancer
    ("Exo2.0-Bold.otf", "exo2-bold.woff2", None, None),                     # SIL OFL, starforge-legion
    ("Exo2.0-Medium.otf", "exo2-medium.woff2", None, None),                 # SIL OFL, thunderstrike-justice
    ("ExpletusSans-MediumItalic.ttf", "expletus-sans-medium-italic.woff2", None, None),  # SIL OFL, vectorthunder
]
FONT_LICENSES = [("Oxanium-OFL.txt", "OFL-oxanium.txt"), ("Orbitron-OFL.txt", "OFL-orbitron.txt")]

LOGO_SRC = ASSETS / "avatars identity" / "rcg logo color (1).png"  # the cyan variant
BOOK_LOGO_SRC = ASSETS / "avatars identity" / "rcg logo color (4).png"  # green: the book's own colour
LOGO_BG = (32, 32, 32)
ICON_SIZE = 256


def rename_family(font, family: str) -> None:
    style = font["name"].getDebugName(2) or "Regular"
    for rec in font["name"].names:
        if rec.nameID in (1, 16):
            rec.string = family
        elif rec.nameID == 4:
            rec.string = f"{family} {style}"
        elif rec.nameID in (3, 6):
            rec.string = f"{family.replace(' ', '')}-{style.replace(' ', '')}"


def build_fonts() -> None:
    from fontTools import subset
    from fontTools.ttLib import TTFont

    out = SITE / "fonts"
    out.mkdir(exist_ok=True)
    for src, name, pin, family in FONTS:
        font = TTFont(ASSETS / "fonts" / src)
        if pin:
            from fontTools.varLib.instancer import instantiateVariableFont
            font = instantiateVariableFont(font, pin)
        if family:
            rename_family(font, family)
        font.reader.tables.pop("SVG ", None)   # colour-glyph table; the pages use the plain outlines
        font.tables.pop("SVG ", None)
        opts = subset.Options()
        opts.flavor = "woff2"
        opts.layout_features = ["*"]
        opts.name_IDs = ["*"]
        opts.notdef_outline = True
        sub = subset.Subsetter(opts)
        sub.populate(unicodes=subset.parse_unicodes(LATIN))
        sub.subset(font)
        font.flavor = "woff2"
        font.save(out / name)
        print(f"  {name}: {(out / name).stat().st_size // 1024} KB")
    for src, name in FONT_LICENSES:
        (out / name).write_bytes((ASSETS / "fonts" / src).read_bytes())


def keyed(src: Image.Image) -> Image.Image:
    """The mark with its dark background keyed out, so the blueprint grid shows through the gaps."""
    mark = src.copy()
    mark.putdata([(0, 0, 0, 0) if p[:3] == LOGO_BG else p for p in mark.getdata()])
    return mark


def build_logo() -> None:
    src = Image.open(LOGO_SRC).convert("RGBA")
    w, h = src.size

    keyed(src).save(SITE / "logo.png", optimize=True)

    # Favicons keep the dark square, so the mark reads on light browser chrome too.
    def padded(size: int, scale: int) -> Image.Image:
        canvas = Image.new("RGBA", (size, size), LOGO_BG + (255,))
        big = src.resize((w * scale, h * scale), Image.NEAREST)
        canvas.paste(big, ((size - big.width) // 2, (size - big.height) // 2))
        return canvas

    padded(180, 2).convert("RGB").save(SITE / "apple-touch-icon.png", optimize=True)
    padded(192, 2).save(SITE / "icon-192.png", optimize=True)
    padded(512, 5).save(SITE / "icon-512.png", optimize=True)
    small = src.resize((96, 96), Image.LANCZOS)
    small.save(SITE / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])

    # SVG favicon wrapping the pixel art, so existing pages that link favicon.svg get the new mark.
    buf = io.BytesIO()
    src.save(buf, "PNG", optimize=True)
    b64 = base64.b64encode(buf.getvalue()).decode()
    (SITE / "favicon.svg").write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">'
        f'<image width="{w}" height="{h}" style="image-rendering:pixelated" '
        f'href="data:image/png;base64,{b64}"/></svg>\n', encoding="utf-8")
    print("  logo.png, favicon.svg, favicon.ico, apple-touch-icon.png, icon-192.png, icon-512.png")


def build_book_logo() -> None:
    # The site keeps the cyan logo everywhere, header included; the green mark is the book's cover branding.
    out = SITE / "book"
    out.mkdir(exist_ok=True)
    keyed(Image.open(BOOK_LOGO_SRC).convert("RGBA")).save(out / "book-logo.png", optimize=True)
    print("  book/book-logo.png")


def build_icons(names: list[str]) -> None:
    out = SITE / "icons"
    out.mkdir(exist_ok=True)
    missing = [n for n in names if not (ASSETS / "icons" / f"{n}.png").exists()]
    if missing:
        sys.exit(f"not in assets/icons: {', '.join(missing)}")
    for name in names:
        lum = Image.open(ASSETS / "icons" / f"{name}.png").convert("L").resize((ICON_SIZE, ICON_SIZE), Image.LANCZOS)
        mask = Image.new("LA", lum.size, 255)
        mask.putalpha(lum)
        mask.save(out / f"{name}.png", optimize=True)
    print(f"  {len(names)} icons into site/icons/")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("fonts")
    sub.add_parser("logo")
    sub.add_parser("book-logo")
    p = sub.add_parser("icons")
    p.add_argument("names", nargs="+")
    sub.add_parser("all")
    args = ap.parse_args()

    if args.cmd in ("fonts", "all"):
        build_fonts()
    if args.cmd in ("logo", "all"):
        build_logo()
    if args.cmd in ("book-logo", "all"):
        build_book_logo()
    if args.cmd == "icons":
        build_icons(args.names)
    if args.cmd == "all":
        existing = sorted(p.stem for p in (SITE / "icons").glob("*.png")) if (SITE / "icons").exists() else []
        if existing:
            build_icons(existing)


if __name__ == "__main__":
    main()
