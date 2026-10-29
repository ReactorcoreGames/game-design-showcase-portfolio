# AAL Universe: art and presentation

How the game is meant to look, kept short: PSRC and the 3M system have their own documentation in the project folder (`5 PSRC Condensed Info Pack`) and in `designs/done/ALREADY DONE Pixel Sprites ala ReactorCore.txt`. This file keeps what the game design depends on. Sources: `!info Pixel Sprites ala Reactorcore.txt`, `!PSRC and 3M System Info.txt`, `PSRC 3M System Origin Musing Document.docx`, `PW ScaleSpriteRepresentGameplay.rtf`, `PSRC_tilesetfrosting.rtf`, EUR, the 2011 V2 overview, scans W2-13, W2-31, W2-32, PS-2 to PS-8, PS-20, PS-21, PS-57, and the PSRC production pages by title only (see [index.md](index.md)).

## The two halves

- **PSRC (under 3 m)**: hand-drawn pixel sprites at one universal scale, semi-realistic with some cartoony expressiveness, neutral top-right ambient shading so any lighting works, greyscale templates tinted in-engine, zoomable to 600%. One sprite per object, used as the physics object, the inventory icon and everything else. Animation is procedural (rotate, move, scale parts) instead of hand-drawn frames, and reactions use particles and effects, so thousands of objects stay affordable. Anyone can extend the set by following the palette and principles.
- **3M (over 3 m, later also smaller mundane things)**: primitive shapes (rect, circle, triangle, few polygons) stretched, rotated, layered, filled with seamless 16 or 32 px pixel textures and tinted. "Pixel art is unsustainable for objects beyond 3 meter size": a 20 m jet fighter at 32 px/m is out of reach, a cruise liner impossible. Huge things get three representations: a far-horizon silhouette, a section model of the nearby part, and the local model you stand on.
- **3M design guide** (PS-20): everything over 3 m is physically a rect or circle; polygons and sprites refine the shape minimally; track polygon density per 4 m²; decoration may overflow the shape by at most 4 px on top and 16 px underneath; "do NOT hide" the rect or circle, "be proud of" it.
- **LOD** (PS-8): L1 max 4 polygons, L2 10–40, L3 10–100, L4 100–400, the rest filled with seamless textures and sprites on quads; hand-made mipmaps per object.
- **Tileset frosting** (2015): a 16×6 overlay sprite on a 16×16 tile for snow, grass, goo, sand or tar (inverted for grime and rust), rotated by the engine for the other three sides.

## Scale

The scale changed over the years; the latest is the standard:

| Source | Scale |
|---|---|
| 2011 V2 / `MolSys` 2016 | human about 60 px; "30 px = 1 m"; 1 px ≈ 4–5 cm |
| `PW ScaleSpriteRepresentGameplay.rtf` 2015 | 40 px/m under 3 m, 20 px/m for 2–10 m, 10 px/m for 5–20 m (an early tiered idea) |
| W2-13, PS-57 | 40 px = 1 m; a 1024×768 screen shows 25 × 20 m |
| **EUR, PS-21, PSRC packs (current)** | **32 px = 1 m; human 60 px (about 1.75 m); screen 1280×1024 = 40 × 32 m** (5:4 on purpose, for the omnidirectional universe); zoom 600% to 25%, unmipmapped 400% to 50% |

EUR also caps component-built objects at 10 m: bigger things use the chunk/region/continent system.

## Layers and look

- **Render order** (EUR): background < ethereal terrain (gas) < projectiles < liquid terrain < solid terrain < objects < characters < effects < HUD.
- **System layers** (W2-19) and **load layers** (PS-5) are in [simulation.md](simulation.md).
- **The background** is a live far-vision view, not decoration: desaturated, only ambient light, things that grow and drift toward the edge they come from. See [simulation.md](simulation.md).
- **Inspection Mode** (W2-30) zooms past full detail on one object to show markings and wear as clues.
- **Taste**: the timeless SNES look of Super Metroid and Super Mario World (`Planet Warfare.txt`); "the audiovisual presentation is comfortable and timeless" (the Super Game starter pack).

## Production notes (title level)

About 36 PSRC scans are about producing and selling sprite packs: workflow, sheet types (optimized, marked, in-depth), package criteria, alignment, palettes, drawing styles, screenshot guidelines, product naming, muscle shapes for limbs, clothing and visual background types, animated phenomena and particle effect tiles. They aren't transcribed; the info pack's text and guide images cover the same ground. The [index.md](index.md) source table lists them.
