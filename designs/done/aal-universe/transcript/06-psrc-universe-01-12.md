# Transcript chunk 6: PSRC universe-engine notebook, scans 1–12

Source folder: `C:\08 Projects\Project_Planet Warfare\2 FotoScan_PSRC - needed an art system for PW\`, files `Image (1).jpg` to `Image (12).jpg`. From PS-4 on, most scans are two-page spreads with small paper notes glued onto the pages; each note gets its own sub-section. Where a note was upside down or sideways in the photo it was rotated before reading, and that is mentioned.

## PS-1 — PSRC / Megastructures / PW-Universe Engine Design / 3M/96px System Detailed
Source: `Image (1).jpg`

**Text:** (notebook cover)

PSRC

MEGASTRUCTURES

PW-UNIVERSE ENGINE DESIGN

3M/96px System Detailed *(this last line in blue ink, added later)*

**Diagrams:** none; the cover is a grey pixel-mosaic pattern (large grey squares of varying shade).

**Notes:** "3M/96px" ties the 3M system to a 96 px scale (3 m at 32 px/m = 96 px), i.e. 3 m is the threshold where pixel sprites stop and the 3M primitive system starts.

## PS-2 — Over 3m research & megastructures
Source: `Image (2).jpg`

**Text:**

Over 3m research & megastructures

**Factors:**
- Gravity
- Thermal/Cool
- Pressure
- Radiation (projection)
- Energy/Electric (charge)
- Weather/Entropy
- Material types & availability/density
- Material states (gas, liquid, solid, plasma)
- *(the eight items above are bracketed together and labelled vertically "ENVIRONMENT")*
- Chaos mitigation
- 2D world practicality
- Artifial [Artificial] & natural (origin)
- Character lives/using wear n' tear/durability
- Atmospheric conditions (vacuum, atmo, composition)

**Requirements:**
- support any scale:
  - sub 3M Level details
  - 3m & over general scale
  - larger buildings, vehicles, bridges, fauna, flora, trees, boulders, mechs.
  - huge structures, systems, vehicles, freighter, skyscrapers, starships.
  - islands, continents, infrastructure city systems, mountains, reefs.
  - moons, planets, stars, megastructures, celestials
  - nebulae, galaxies, clusters.
- support physics/dynamics
- support destruction & creation via gibbing.
- support digging, modify, construction, fuse, cut, combine, split *(combine and split written small below)*
- support seamless worlds
- diverse configurations
- performance limitations

**Diagrams:** none.

**Notes:** Requirements list for the 3M/megastructure system. "Chaos mitigation" links to the Chaos System.

## PS-3 — More factors
Source: `Image (3).jpg`

**Text:**

More factors:
- Illumination/Light/Dark
- Saltiness
- Humidity
- Macrobiology (large lifeforms)
- Microbiology (small bacteria)
- Basic physics
  - Friction, Bounce, Adhesion
  - Brittleness, Volatility (chemistry)
  - Sharpness, gib limits, hazardnes/safety
- Anomalies
- Astral forces
- Civilization/Behaviours/Preferences/AI
- Old ruins/left overs/derelicts
- Magnetism
- Disasters/Catastrophies/Quakes
- Celestial properties (on/nearby)
- Tech level/eras of progress (space age ↔ stone age)

**Diagrams:** tiny doodles under "Celestial properties (on/nearby)": a small round planet-like shape, and a cluster of small objects with a little star/sparkle, *(interpretation)* a planet and nearby celestial bodies.

**Notes:** Continues the factor list of PS-2.

## PS-4 — [Chunk shape solutions and scales] (spread of four notes)
Source: `Image (4).jpg`

### PS-4a — General Chunks: TRI-BASED SOLUTION (top-left note)

**Text:**
- any thickness
- exterior (solid bg)
- interior (hollow exclusion)
- etc. (three times, beside the polygon examples)
- [1 interior tri per 1 solid tri]
- [min cut size 10m pieces]
- [If tri collisions not feasible, do same with squares/circles.]
- [Tilemap sectors possible combine?]
- General Chunks
- TRI-BASED SOLUTION

**Diagrams:** a row of shapes made of an outer solid outline with a hatched inner shape: a rectangle with inner rectangle, two stacked squares, a square split along its diagonal, rectangles split diagonally with a hatched inner triangle, and right triangles with a hatched inner triangle ("any thickness" points at these, the gap between outer and inner shape being the wall thickness). A second row shows triangles split into a solid outer triangle and a hatched interior triangle ("1 interior tri per 1 solid tri"). Left column: a pentagon/star shape, a hexagon and an octagon, each with a hatched inner polygon, labelled "exterior (solid bg)" for the outer shell and "interior (hollow exclusion)" for the hatched inner area. *(interpretation)* Each chunk is a solid triangle shell with a matching hollow triangle cut out of it, so chunks can be hollow (caves, rooms).

### PS-4b — ALTERNATIVE CIRCLE-RECT SOLUTION (bottom-left note)

**Text:**
- ALTERNATIVE CIRCLE-RECT SOLUTION
- What is most performant tech solution possible?
- Maybe use CIRCLE-RECT for mega-class, while reserve TRI for micro-class?
- Tilemaps/chunks possible at micro level. Bitmap for highest universe map sector too?

**Diagrams:** combinations of rectangles and circles, each with a hatched interior: a rectangle with a hatched inner rectangle; a rectangle with a hatched inner circle; a rectangle with a hatched half-circle at its top; two overlapping rectangles (hatched); a large circle containing a hatched rectangle; a circle containing a small square; a circle containing a hatched off-centre circle (crescent-like exterior).

### PS-4c — Different scales of: [PSRC MEGAS] (top-right note, written sideways)

**Text:**

Different scales of: [PSRC MEGAS]
- Buildings (has interior)
- Bridges
- Flora (bushes, trees)
- Boulders, mountains
- Cargo vehicles
- Asteroids
- Pipes
- Piles o' stuff
- space stations
- bunkers
- weapons

**Diagrams:** none.

### PS-4d — [Levels L0–L4 and sector types] (bottom-right note, sideways; read rotated)

**Text:**
- L0, L1a, L1b, L2a, L2b, L3a, L3b, L3c (level labels on the drawings)
- ALT ~~[scribbled word]~~, C
- ALT, R, (MEGASTRUCT)
- RC (combined)
- T
- overlap
- a) Tri-polygon sectors
- b) overlap Rects
- c) overlap Circles
- MAX DENSITY per sector 10000–1000km² *(the bracket groups b and c)*
- if dug, there is a BG canvas from directions where thing is flanked from.
- Dynamic = supports any shapes/sizes.
- L4: 10x10 splitting until 10m² min density reached. Can be further detailed with main/sub structs for smaller tunnels/holes etc.

**Diagrams:** a level-of-detail progression of a celestial body:
- L0: a single dot.
- L1a: a small circle; L1b: a small square.
- L2a: a circle divided into ~12 pie-slice triangles (labelled T, tri-based); L2b: a ring of small circles around a hollow centre (labelled C, an "ALT" version).
- A larger plain circle, linked to L2a by a line (*(interpretation)* the body's overall outline).
- ALT / R (MEGASTRUCT): a ring made of rectangles around a hollow centre.
- L3a: RC (combined): a ring of mixed circles and rectangles around a hollow centre.
- Zoom-ins on one wedge of the body at L3: L3a a long triangle (T) split by horizontal lines into strata; L3b a wedge built from stacked rectangles of shrinking width (R); L3c a wedge filled by overlapping circles (C, "overlap").
- A line from the T wedge's tip continues down to the L4 note.

*(interpretation)* A planet is stored as wedge-shaped sectors (triangles, rects or circles) radiating from its centre; each sector is cut into strata, and L4 subdivides those 10×10 until 10 m² pieces. Digging into it reveals a background canvas showing the sector walls from the side you came in.

**Notes:** Early form of the 3M LOD levels and the clump/chunk/region/continent hierarchy, with the "shadow background" idea ("BG canvas ... where thing is flanked from").

## PS-5 — [Layers, solid hierarchy, Equilibrium Universe] (spread of four notes; upper half upside down, read rotated)
Source: `Image (5).jpg`

### PS-5a — Layers (upper note, upside down)

**Text:**

Layers
- 0 - solid actual (terrain)
  - → Z-BG celestial flank canvas, huge matter mass shadow
    - → Farsight Horizon BG
- 0.5 Celestial render/load levels/mipmaps
- 1 main structs
  - 2 sub structs
    - 3 chars/obj/non-cockpit vehicles/powerarmor
      - 4 items/armor/accessories, addons/attachables/EXTRAS
        - 5 effects/emissions/texture

Also represents load-order: 5 is first to vanish, while 1 and above are last to unload.

Labels on the small drawing: "<1000km² hole", "(Huge matter mass)", "(terrain)".

**Diagrams:** top-right, a circle (a celestial body) with a dot near the centre (pointed to by "terrain") and a V-shaped wedge cut into its top edge, labelled "<1000km² hole"; "Huge matter mass" points at the body. A line from the circle leads to the "Z-BG celestial flank canvas" line. *(interpretation)* When you dig a hole (up to 1000 km²) into a celestial, the rest of its mass is shown as a background "flank canvas" shadow.

### PS-5b — Solid / Main structs hierarchy (upper note, upside down)

**Text:**
- (terrain) Solid / universe
  - Main structs (static / mobile) *(written as a stacked pair; "static" above a line, "mobile" below)* — hangars (carriers)
    - Sub structs (vehicles that can go inside carriers ↑)
      - Char/Objs/power Armor
        - Items\Armor\Accessories
        - Addons\Attachables\Extras

**Diagrams:** none beyond the indented tree.

**Notes:** Same layer stack as PS-5a; main structs can be hangars/carriers holding sub structs.

### PS-5c — Equilibrium Universe (lower-left note)

**Text:**
- Equilibrium Universe
- = [wilderness] (label on a small swirl drawing at the top)
- R, C (circled labels on the two drawings)
- 0.0xy (at the centre of the circle)
- normal universe
- (wilderness) = (randomly shifting ejected material return/reshuffle area.)
- [stable equilibrium zone]

**Diagrams:** two alternative universe shapes. Left, "R": a large square divided into a 3×3 grid (hatched interior), with a thin outer border strip divided into segments; an arrow from the border points up to a swirl icon "= [wilderness]", and another swirl icon at the bottom is "(wilderness)". Right, "C": a large circle with a hatched inner disc (centre marked "0.0xy", the coordinate origin) and an outer ring; the ring has an arrow to the wilderness icon; the inner disc is the "normal universe" / "stable equilibrium zone". *(interpretation)* Square (R) or circular (C) universe, both with a wilderness border band that ejects and reshuffles material.

### PS-5d — Equilibrium Universe Rules (lower-right note)

**Text:**

Equilibrium Universe Rules
- Driven towards stability.
- Aims to uniformize all matter via various forces and mechanisms.
- Randomized, but consistent, standardized and makes sense.
- Celestials and their parts slow down, resolve and settle themselves into more optimal configurations automatically over time.

**Diagrams:** none.

## PS-6 — [Celestial/continent compositions: type C and type R] (spread of four notes; upper half upside down)
Source: `Image (6).jpg`

### PS-6a — Celestials / Continents (upper-left note, upside down)

**Text:** Celestials / Continents

**Diagrams:** six combinations of a container shape with mixed children: a square containing two circles and two squares; a circle containing two squares and two circles; a circle containing a square divided into four quadrants; a square containing five loose circles; a square containing four overlapping circles; a circle containing four overlapping squares (spilling over the edge). *(interpretation)* A celestial or continent can be a rect or circle outline filled with any mix of rect and circle sub-parts.

### PS-6b — Disordered type R (upper-right note, upside down)

**Text:** Disordered type R

**Diagrams:** clusters of rotated, overlapping hatched squares, some subdivided into grids, each with a centre dot (centre of gravity): one big group of four large tilted grid-squares, a small separate 4×4 grid tile linked to it by a line, and four smaller clusters (a 2×2 tilted group, a 3×3 group with centre dot, an L-shaped group, and a diagonal stack). *(interpretation)* Rect-based bodies whose sub-rects are rotated and overlapping rather than aligned on a grid.

### PS-6c — type C (lower-left note)

**Text:**
- celestial
- continent
- region
- center of gravity
- ~~[scribbled word]~~ chunks
- type C

**Diagrams:** a central large drawing: a dashed outer circle (celestial) containing several big overlapping circles (continents), each filled with smaller circles (regions), with a dot at the centre (center of gravity). A thin line leads down to a cluster of many small overlapping circles labelled "chunks". Around it, five more circle-cluster bodies, each with a centre dot: elongated diagonal chains, a lopsided blob, a ring of circles around a centre, and a four-lobed shape. *(interpretation)* Type C = circle-based nesting: celestial → continents → regions → chunks, all circles, with a computed centre of gravity.

### PS-6d — Ordered type R (lower-right note)

**Text:**
- Ordered type R
- (tilemaps possible here)

**Diagrams:** axis-aligned square bodies built from grid squares, each with a centre dot: a 1×3 column, a 2×2 block with a hatched shadow strip on its right side, a 3×3 grid with a hatched centre, an L-shape inside a square with hatching, and a large 2×2 block of big squares each subdivided into a 4×4 grid, with a small separate 4×4 grid tile linked to it. *(interpretation)* Type R = rect-based nesting aligned to a grid, so tilemaps can be used.

**Notes:** Two sector/body types, C (circles) and R (rects; ordered or disordered), matching PS-4d's "overlap Rects / overlap Circles" options.

## PS-7 — [Loaded sphere, PSRC packs, Megastructure rules, PSRC 3M universe] (spread of four notes; upper half upside down)
Source: `Image (7).jpg`

### PS-7a — PSRC packs 3Mera (upper-right note, upside down)

**Text:**

PSRC packs 3Mera:

Value:
- Sprites
- Poly primitives
- *(a curve marks the two items above as "paid")*
- Guide on how to use/think
- Guide on how to create
  - \* sprites via free editor install
  - \* 3M objects programatically
- *(a curve marks the guides as "Free")*
- Ready-made various poly 3M objects as screenshots and (if possible) in Unity or other engines. [Paid/Free depends on use/volume.]

**Diagrams:** none apart from the paid/free curves.

**Notes:** A plan to sell PSRC as asset packs ("3Mera" = 3M era): paid sprites and primitives, free guides.

### PS-7b — Loaded sphere radius (upper-left note, upside down)

**Text:**
- L0, L1, L2, L3, L4
- Planet
- Loaded sphere radius
- LOADED IN DETAIL
- LOADED VAGUE (twice)
- too far, L1/L2 tier ops
- Planetary chunk
- Planetary sector
- continental Chunk
- 10000km (at the top of the L4 triangle)
- 1000km, 100km
- MAX DENSITY OF POLYGONS X/Y km²
- continental sector Layer

**Diagrams:** the LOD sequence again: L0 a dot, L1 a small diamond split in two triangles, L2 a circle of pie-slice triangles ("Planet"). A large faint circle is the "Loaded sphere radius". Inside it a big inverted triangle (a planetary sector, L3) is subdivided into many smaller triangles, densest at the top; the area right around it is "LOADED IN DETAIL", the hatched areas to both sides "LOADED VAGUE". An arrow pointing away to the lower left says "too far: L1/L2 tier ops". One small triangle in the sector is marked "planetary chunk", with an arrow down to an L4 inverted triangle ("10000km" across its top) cut into horizontal strata, labelled "continental sector Layer". Left of it, a strip of triangle-split squares is a "continental Chunk", and below that a large grid of triangle-split squares, labelled "1000km" across with one "100km" cell drawn separately, captioned "MAX DENSITY OF POLYGONS X/Y km²". *(interpretation)* Only the part of a planet within the loaded sphere around the player is built at full polygon detail; nearby parts are vague, and far bodies are run as simple L1/L2 objects.

### PS-7c — MEGASTRUCTURE RULES (lower-left note)

**Text:**

MEGASTRUCTURE RULES
- Cannot overlap → will collide
- Exist in BG but can be "activated" to apply forces/effects/collisions to things on the "normal" layer.
  - Artificially = weaponized intent.
  - Naturally = erratic cascade event.
- note: things/objects inside moving MEGAS are safe from forces, but still experience momentum etc.
- They have "FG" in the BG. Things can enter and be concealed by this FG, but things outside and infront see it all as BG.

**Diagrams:** none.

### PS-7d — PSRC 3M universe (lower-right note)

**Text:**

PSRC 3M universe
- 2D sideview/topdown-view (char/worlds) (space explo)
- supports farview & megastructures
- (use background as horizon for things beyond screen edges.)
- (Mipmaps = different levels of detail for thing further in the horizon - performance & visibility.)
- (Megastructures/celestials are loaded in various detail levels based on player focus/presence proximity. There is a Max Density cap on how much polygons can exist per certain area at once.)

**Diagrams:** under the first line: a side-view scene with a tall triangle-split tower, a running stick figure, and a box-shaped vehicle/cart on ground (side view, "char/worlds"); then a dividing line and a top-down scene with a triangular ship moving through space with a trail, a small circle and a diamond (top-down, "space explo").

## PS-8 — [Triangle building blocks, PSRC todo, size limits, Mipmaps] (spread of four notes; upper half upside down)
Source: `Image (8).jpg`

### PS-8a — PSRC over 3Meter triangle based building blocks (upper-left note, upside down)

**Text:**
- tiny - large objects
- ratio
- apply in-game
  - + color
  - + gradient
  - + seamless texture
- 10%, 12 (small labels near the big circles)
- huge (planets, moons, celestials etc.)
- PSRC over 3Meter triangle (3D polygon) based building blocks.
- Pixel Sprites ala Reactorcore

**Diagrams:** a catalogue of primitive shapes built from triangles: a square with a diagonal, right triangles and slanted quads with small bracket marks (*(interpretation)* adjustable edges/ratios), a triangle, a diamond, a hexagon, a long flattened hexagon, a pentagon and an octagon, each split into triangles; a small triangle in a square labelled "ratio"; one scribbled-out shape. Across a dashed divider: a large circle densely hatched with triangles ("10%", "12"), a 12-slice pie circle with dotted slices, and smaller star-of-David, diamond and split-diamond shapes; an arrow beside "gradient" shows the gradient direction. These big round ones are "huge (planets, moons, celestials etc.)".

### PS-8b — PSRC todo (upper-right note, upside down)

**Text:**

PSRC todo:
- Do the primitives in blender
- Design megastructure logic
  - \* creation (natural/artificial)
  - \* destruction
  - \* editing/fusing/cutting/splitting
  - \* transitions from/to MEGAS
  - \* interactions/dynamics between MEGAS (collisions, reactions, etc.)

**Diagrams:** none. (Faint bleed-through from the other side of the page is visible, not part of this note.)

### PS-8c — Over 3m size/significance limits (lower-left note)

**Text:**

Over 3m size/significance limits.
- L1 max 4 poly.
- L2 max 10-40 poly.
- L3 max 10-100 poly.
- L4 max 100-400 poly.
- [Rest of details filled with seamless tex and sprites on quads (uses polys)]

*(each L has a small tick mark above it)*

**Diagrams:** none.

### PS-8d — Mipmaps (custom made per obj.) (lower-right note)

**Text:**

Mipmaps (custom made per obj.)
- L0 . (a dot)
- L1: Large overall shape
- L2: Largest functional details (car, door, wheels)
- L3: Normal view - most big details/markings
- L4: Close up (non-regular view - inspection). Extras, doodads, small markings, decor. Special zoom-in.

**Diagrams:** L1 shown as a triangle, a rectangle split by a diagonal, and a diamond; L2 a simple car: a box body with a door square and two wheels, labelled "car / door / wheels"; L3 the same vehicle with more triangle panels; L4 a detailed version with many small panels, a "3" marking on the side and small extra parts.

**Notes:** PS-8c and PS-8d together define the 3M LOD levels L0–L4 and their polygon budgets.

## PS-9 — [Cause & effect nature, TEST, universe hierarchy] (spread of three notes)
Source: `Image (9).jpg`

### PS-9a — Cause & Effect influenced nature (top-left note)

**Text:** Cause & Effect influenced nature

**Diagrams:** a stick figure standing on a horizontal plank/beam; left of it a vertical bar segmented like a stack of blocks with an up-down double arrow, and a small T-shaped post above (*(interpretation)* a pillar or lift holding the beam). Next to it, trees built from primitives: a tall hatched triangle on a trunk (conifer), a tilted square on a trunk with a triangle inside (deciduous tree), a square split by a diagonal, a triangle in a box, a pentagon and a broken/split diamond. Below, two trees drawn falling or snapped in a V (two hatched triangles leaning toward each other). *(interpretation)* Natural objects made of primitives that react to cause and effect, e.g. trees that can be felled or broken.

### PS-9b — TEST (bottom-left note)

**Text:**
- ring
- Atmo, 1, 2, 3, 4, 5, 6, 7, 8 (numbers around a planet)
- P
- Atmo
- Planet
- No.
- TEST (in blue)

**Diagrams:** the whole note is crossed through with blue diagonal lines (rejected). Left: a big lumpy cluster of overlapping circles and tilted squares with a few small down-arrows (rejected "No."). Right: a planet "P" with a hatched core, a ring of numbered segments 1–8 around it ("Atmo"), and an outer "ring". Bottom: a circle "Planet" surrounded by a ring of small circles ("Atmo"), and an octagon made of rectangles around a hollow. A small blue scribbled circle cluster in the middle. *(interpretation)* Tests of drawing a planet with atmosphere bands as a ring of segments; marked as not the way.

### PS-9c — [Universe hierarchy C0–C4] (right note)

**Text:**
- Universe (C0)
  - → Superclusters (C1)
    - → Local Groups (C2) (collection of galaxies/voids) *(a crossed-out word after "galaxies/", possibly "nebula")*
      - → Galaxy / Void (C3)
        - → Cloud (Nebula) / Void (C4) (contain star clusters) either OR QUASAR\GAL NUCLEUS
          - → Solar Sys / Void (contain group of celestials)
            - → Celestials/Entities
              - → Contents. (the rest of it.)

**Diagrams:** none beyond the arrow tree.

**Notes:** The C0–C4 hierarchy from the glossary; here level C2 is called "Local Groups" (later "Local Cluster" on PS-10).

## PS-10 — [C0 Universe, C1 Supercluster, C2 Local Cluster] (spread of four notes)
Source: `Image (10).jpg`

### PS-10a — C0 (top-left note)

**Text:**
- C0
- [UNIFORM DENSITY]
- N, NE, E, SE, S, SW, W, NW (compass sectors around the ring)
- VOIDS
- wild sectors
- UNIVERSE (Parent)
- SUPERCLUSTERS (Child)

**Diagrams:** a large circle (the universe, parent) with an outer ring divided into 8 compass sectors N/NE/E/SE/S/SW/W/NW ("wild sectors", the wilderness band). Inside, seven roughly equal round cells packed together (a central one with six around it), each a supercluster (child); three lines point to dots in some cells labelled "VOIDS". Radiating dashes around "[UNIFORM DENSITY]" at the top-left. *(interpretation)* The universe is filled with uniformly sized superclusters surrounded by a compass-sectored wilderness ring.

### PS-10b — Supercluster C1 (bottom-left note)

**Text:**
- Supercluster C1
- UP THIS WAY ←, N (compass; the N arrow points left, with E/S/W letters drawn rotated around the circle)
- CENTER IS MOST DENSE
- local group (child of this SC)
- ALT 1
- ALT 2

**Diagrams:** a large circle packed with seven round cells (centre one plus six around it), the central cell marked "CENTER IS MOST DENSE", the outer cells "local group (child of this SC)". Two alternatives on the right: ALT 1, a circle divided by crossing straight lines into wedge sectors; ALT 2, a circle with a square grid (about 4×4) inside.

### PS-10c — C2 LOCAL CLUSTER (top-right note)

**Text:**
- C2
- LOCAL CLUSTER
- O = Galaxy Spawn
- ⊗ = Void Spawn
- 5:4 ratio ⊗/O
- Uses allocated matter budget for galaxies and void w/ priority bias to former.
- MIN WIDTH, max width, 75%, 50% (labels on the diagram)
- (IDEAL), A, B, C

**Diagrams:** a large circle with crosshair axes and dashed diagonals; spawn points along them: a ⊗ at the centre, O galaxy spawns on the axes (left, right, top, bottom) at about 50% radius, ⊗ void spawns on the diagonals at about 75% radius; "MIN WIDTH" and "max width" brackets measure a cell at the top. Below, three small packed-circle variants: A (IDEAL), B and C, each a circle with a mix of plain O galaxy cells and ⊗ void cells of varying size.

### PS-10d — LOCAL CLUSTER INFO (bottom-right note)

**Text:**
- LOCAL CLUSTER INFO
- a), b) (two diagrams)
- 5 void, 4 galaxy [RATIO] (Limited matter budget + UNI surplus)
- 1. Spawn in A pattern
- 2. Resize with min-max
- 3. Dynamically grow or shrink voids to compensate.

**Diagrams:** six circles, each packed with smaller circles in different arrangements (various sizes, one with a dark central circle, one with a central core and three big lobes), showing possible local cluster layouts. Diagrams a) and b): circles with hatched galaxy cells and ⊗ void cells of different sizes and positions.

**Notes:** C2 generation rule: 5 voids to 4 galaxies, galaxies get budget priority, voids flex in size to fill leftover space.

## PS-11 — [Ideas 2, Ideas 3, Solar system generation, TODO write Ideas 1] (spread of four notes; upper half upside down)
Source: `Image (11).jpg`

### PS-11a — IDEAS 2 (upper note, upside down)

**Text:**

IDEAS 2

At universe creation, a handful of random celestials will be flung accross space random direction and random vel.

Overlap spawns allowed → at universe start exciting chaos ensues and eventually cools/settles, resulting in bizarre places to visit.

Technology understanding cypher. Player chars may encounter relics that are too old/new to understand, so they need to gain a cypher(s) to use them or modify them.

**Diagrams:** a circle with an outer ring; small dots (celestials) inside with arrows pointing in random directions, and a few on the ring with arrows pointing inward.

### PS-11b — IDEAS 3 (upper note, upside down)

**Text:**

IDEAS 3
- Local juristiction cell level
- Rogue universe level juristiction (for loose celestials flying outside of local galactic/other cells and not having a home.)
  - Rogue celestials slow down weaker in voids and slow down stronger in nebula/gas clouds.

**Diagrams:** none.

**Notes:** "Jurisdiction" seems to mean which simulation cell owns/updates an object; homeless rogue celestials belong to the universe level.

### PS-11c — Solar system generation (lower-left note)

**Text:**

Solar system generation

0-6 stars at any distance from center in a ring. (with rarity checks & thresholds for normalcy.)

+ 0-16 celestials generated from center to edge along a single line = → 1.

Then a random angle offset from 0 to 360 → 2.

**Diagrams:** step 1: a circle with a vertical chain of small overlapping circles on a single line from centre to top edge. Arrow to step 2: a circle with a centre dot and radial lines going out at different angles, each ending in a small circle (the celestials rotated to random angles around the centre).

### PS-11d — TODO WRITE IDEAS 1 (lower-right note)

**Text:**

TODO WRITE IDEAS 1
- + simplified sprite ragdoll player/humanoid.
- + clothes system
- + limited limb angles

Galaxy/void
- 1st idea: CORE, EMPTY, (sector based), G, V
- 2nd idea: CORE QUASAR, VOID EMPTY, each dot is star system, (distance rarity based), star cluster, G, V

**Diagrams:** a blocky humanoid figure (square head, rectangular body, line limbs, round hands, oval feet) mid-walk. Galaxy/void 1st idea: G, a circle with seven round sectors, each containing a spiral, the central one darker ("CORE"); V, a circle with seven round sectors, the central one empty ("EMPTY"), the others with sparse dots. 2nd idea: G, a circle with a dense spiral core (labelled "CORE / QUASAR") and arrows pointing outward from it, dots scattered around; V, a circle with an empty central ring ("VOID / EMPTY"), arrows pointing inward toward it, dots (each a star system) denser toward the rim, and a faint circle near the edge labelled "star cluster". *(interpretation)* Galaxies thin out from a bright core; voids are empty at the centre with stars gathered at the edges.

## PS-12 — [Galaxy and Void C3 rules] (spread of four notes)
Source: `Image (12).jpg`

### PS-12a — Galaxy (top-left note)

**Text:**
- Galaxy 5:4 ratio or otherwise 50/50 is common, but not must.
- To move galaxy, you must move the [core] (to move it)
- (Budjet limits apply to this.)
- \* Atleast one core must exist in GALAXY.
- Any of these can be O or ⊗ of any size within min-max frame.
- Any can be designat as [CORE] which contains the AGN aka [Active Galactic Nucleus].
- ~~The core will eventually migrate to center and run its course, evolving via galaxy's lifecycle.~~ NOPE! *(this sentence is cross-hatched out, with "NOPE!" written above)*
- Galactic Sector
- Void
- (O = Cloud.)
- (⊗ = Part of galaxy but without cloud.)

**Diagrams:** a circle with seven round cells (centre and six around) plus small ⊗ cells in the gaps; a line from the centre cell to "To move galaxy... core"; lines label a round cell "Galactic Sector" and a ⊗ cell "Void".

### PS-12b — Various Galaxy Configs / More than 1 core possible (bottom-left note)

**Text:**
- Various Galaxy Configs
- More than 1 core possible

**Diagrams:** twelve circles, each packed with a different mix of plain O cells, ⊗ cells and hatched cells of varying sizes; some have a darker circled cell (a core); one has two. A small 4×4 grid with X marks in some cells sits in the bottom-right corner, and a small pair of brackets "( )" beside the last circle.

### PS-12c — Galaxy C3 (class 3) (top-right note)

**Text:**
- Galaxy C3 (class 3)
- 3x3=9
- IDEAL
- REQS
  - 1-9 cores present
  - \* commonly more than 50% is cloud, rather than void. *("30%" written above "50%", possibly a revision)*

**Diagrams:** a small "IDEAL" circle with a 3×3 = 9 arrangement of cells; a larger circle with nine cells: five bold O cloud cells in a plus/cross pattern (centre, left, right, top, bottom) and four ⊗ void cells in the corners.

### PS-12d — Void C3 (galactic anti-space) (bottom-right note)

**Text:**
- Void C3 (galactic anti-space)
- 3x3=9
- IDEAL
- REQS
  - no active cores
  - \* commonly less than 50% is cloud *("30%" written above "50%", possibly a revision)*

**Diagrams:** a small "IDEAL" circle with nine cells; a larger circle with nine cells: three bold O cloud cells (one top-centre, two in the bottom corners) and the remaining six ⊗ void cells.

**Notes:** C3 level: galaxy vs void defined by cloud share and whether it has active cores (AGN).

## New terms

- **3Mera**: "3M era", name for the PSRC asset packs (sprites, poly primitives, guides, ready-made 3M objects) meant to be sold/given away.
- **96px**: the 3 m threshold in pixels (3 m × 32 px/m); "3M/96px System" = the 3M primitive system that takes over above 96 px.
- **MEGAS**: short for megastructures (huge objects/celestials living in the background layer that can be "activated" to affect the normal layer).
- **Type C / Type R / RC / T**: body/sector construction types: C = built from overlapping circles, R = from rects (ordered = grid-aligned, tilemap-friendly; disordered = rotated/overlapping), RC = combined rects and circles, T = tri-polygon (triangle) sectors.
- **L0–L4 (3M levels)**: level of detail tiers: L0 dot, L1 overall shape (max 4 poly), L2 largest functional details (10–40 poly), L3 normal view (10–100 poly), L4 close-up/inspection (100–400 poly); for terrain, L4 = 10×10 splitting down to 10 m² pieces.
- **Layers 0–5 / load order**: 0 solid terrain (with Z-BG flank canvas and farsight horizon BG), 0.5 celestial render levels/mipmaps, 1 main structs, 2 sub structs, 3 chars/objects/power armor, 4 items/addons, 5 effects; 5 unloads first.
- **Z-BG celestial flank canvas / huge matter mass shadow**: the background image of a celestial's surrounding mass shown when you dig into it (same idea as the glossary's "shadow background").
- **Farsight Horizon BG**: the far-vision background horizon layer.
- **Loaded sphere radius / Loaded in detail / Loaded vague**: the area around the player where planet sectors are built at full detail, with a vaguer ring around it; beyond it bodies run as L1/L2 "tier ops".
- **Max density (of polygons)**: a cap on how many polygons may exist per area (sector) at once.
- **Wild sectors**: the eight compass sectors (N…NW) of the wilderness ring around the universe.
- **Galaxy spawn (O) / Void spawn (⊗)**: cell markers in the C2/C3 generator; in C3, O = cloud, ⊗ = part of the galaxy without cloud.
- **Core / AGN (Active Galactic Nucleus)**: the designated cell of a galaxy holding its nucleus; a galaxy needs at least one, may have several; moving a galaxy means moving its core. Voids have no active cores.
- **Galactic anti-space**: description of a C3 void.
- **UNI surplus**: the universe's leftover matter budget, added to a local cluster's limited budget.
- **Jurisdiction (local cell level / rogue universe level)**: which simulation level owns an object; homeless rogue celestials fall under the universe level.
- **Technology understanding cypher**: an item/knowledge a character needs to use or modify relics too old or too new for them.
- **Cause & effect influenced nature**: natural objects (trees etc.) built from primitives that react physically (fall, break).
