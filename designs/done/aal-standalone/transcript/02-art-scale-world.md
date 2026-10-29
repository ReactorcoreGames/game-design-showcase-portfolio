# Standalone notebook transcript: Art style, effects, textures, scale and world features

This chunk covers the visual side of Standalone, in scan order: the "Ultra Simple Graphics Style" pages that define a deliberately low-poly, flat-colour look built from white rectangles, 2-sided planes and basic primitives (A1–A2), a sheet of micro-art scenery sketches and a list of terrain/planetary scenery ideas (A3–A4), asset naming conventions and a first asset list (A5), a pixel-art scenery pack list (A6) and a two-stage model/graphics spec (A7); then misc graphics ideas: scaling enemy size (A8), exclusion areas as inverted spheres (A9), a Great Fox booster effect (A10), an expanding water-splash explosion (A11) and Star Fox 64 destruction effects (A12); then effect-texture planning: a sticky note of effect textures (A13), a grid of texture thumbnails with Substances/Energy lists (A14) and texture creation guidelines (A15); the "Basic Primitives Mega Pack" checklist marked COMPLETE (A16); world scale pages with mothership dimensions, Unity world-size limits, speeds and ReWaR/weapon sizes (A17–A18); and finally three older "AoY" pages in blue pen listing world features and environment types, planetary vs space (A19–A21).

## A1 — Ultra Simple Graphics Style, Part 1 (`1 deliberate low poly artstyle (1).jpg`)

Grid paper, black pen, ring-binder punch holes on the left, portrait.

**Ultra Simple Graphics Style** PART 1 &nbsp;&nbsp; | Check Proteus | *(boxed in the top-right corner)*

[drawing: an empty square] = white rectangle. Use color tint & opacity to represent its meaning. scaling and rotation to animate it.
(Untextured) *(with an arrow pointing up to the square)*

**Fire animation fx (billboards)**: a vertical stack of five small overlapping squares, growing from a tiny one at the top to a larger one at the bottom. A vertical arrow on the left runs from "BIG SOLID" (bottom) up to "Small & Trasparent" (top). Bracketed colour labels on the right, top to bottom: black, grey, yellow, orange, Red.

**Scaled 2-sided planes.** (~~planes~~ crossed out under the heading)

Sketches: three long thin rectangles/strips at various angles and a tilted square (left group), and three thin triangles/slivers (right group).

Left column (under the rectangles):
- Projectiles
- Beams
- Barriers
- RECTANGLES
- Gibs, mechs

Right column (under the triangles):
- Blades
- Boosters
- Muzzle flashes
- Projectiles
- TRIANGLES
- Gibs, organics

**Basic Primitives**: sketches of a large wireframe sphere (lat/long grid), a hexagonal crystal/capsule shape, a small cube, a small wedge, a tall thin spike/obelisk, a small round wheel-like shape and a tiny boxed cross.

- Larger effects, explosions, large projectiles, big gibs

## A2 — Ultra Simple Graphics Style, Part 2 (`1 deliberate low poly artstyle (2).jpg`)

Grid paper, black pen, punch holes on the left, portrait.

**Ultra Simple Graphics Style** PART 2

**Additional extensions ++**

Three animation strips (frame-by-frame, left to right):
- A full circle that is progressively "eaten" by an inner circle sliding to one side until only a thin crescent remains (7 frames).
- A small dot in a circle growing into concentric rings, the ring thinning out until just an outline (7 frames).
- A square with horizontal lines that move down through it, frame by frame, with down arrows at both ends of the strip (6 frames) *(interpretation: a wipe/scanline animation)*.

Beside them: Simple single color animations [NO GRADIENTS] (Anime-explosions)

**Simple Gradient effects ++2**

Sketches: a small circle with fuzzy concentric dashed rings around it (glow), a rectangle with soft dashed top edge and dark bottom edge (gradient fade), and a circle with blotchy shading and a lighter centre (shockwave/flash disc).
- Flashes
- Booster Glows
- Glows
- Shockwaves
- Waves
- Advanced beams/projectiles

**Anime effect anims + simple gradients ++3**

A strip of 7 frames: a small dot inside a circle grows into a ring with a ragged inner edge, which widens and finally fades into a dashed outline circle. Bottom left: a tall narrow rectangle with a large downward arrow inside and a dark shaded block near the top *(interpretation: a beam or column with a scrolling texture moving down)*.

## A3 — Microart Style Scenery (`1 deliberate low poly artstyle (3).jpg`)

Grid paper, black pen, punch holes on the left, portrait. Almost entirely a dense grid of small scenery doodles (roughly 100), drawn in a simple faceted low-poly style.

**Microart Style Scenery**

Only labels on the page: "anim. tornado" (with a scribbled-over first attempt at "anim"), "(monoligth)" [sic], "cabbage", "boulder".

Sketch categories, roughly top to bottom:
- **Crystals and spikes**: tiny gem/crystal pebbles, a tall hexagonal crystal, a cluster of tall spikes, spiky crystal shards, a fan of tall thin shards, a cactus-like branching crystal, an asterisk/star shape.
- **Odd formations**: a flat tile with blobs on it (crater/pond patch), a stump with roots, a lollipop tree, stacked slab towers (mesa-like pillars), a mushroom-shaped table rock, a tall box pillar, crowns of spikes in bowls (spiky nests), a block cluster.
- **Mounds and domes**: low hills/mounds, a geodesic/wireframe dome, rounded boulder piles, a jellyfish/tentacled dome, a spiky seed pod, a round bush cluster.
- **Weird features**: a ring-shaped arch with a creature/figure in it, a spiky half-dome, a cactus-like spiky stalk, the "anim. tornado" (a stacked funnel of slanted segments with curly arrows showing rotation), a stack of rounded blobs, cone pine trees and a tiered fir tree, a cut tree stump, a pyramid/cone stump, a flat-topped trapezoid.
- **Monolith row**: a tall slab "(monoligth)", a T-shaped flat-topped tree, mushroom/umbrella plates, a jagged zigzag twisted pillar, a knotted loop shape, a flat diamond tile with a squiggle (rough terrain piece), a palm tree, a low split dome.
- **Trees**: a fungal stalk with a wavy cap, the "cabbage" (a small ball of leaves), a flat disc on a stalk, many low-poly trees with round or blob canopies, a stacked-block tower tree, a tall triple-lobed poplar, a layered pagoda-like tree, a spiky palm/bundle tree, a tall truncated cone, a sharp faceted cone, a flat table-top canopy on a stalk, the "boulder" (a round rock with cracks).
- **Rocks**: many angular and rounded low-poly boulders and rock piles, layered slab rocks, a small barrel-shaped rock, flat stones, a rock arch, a rock with a cave.
- **Mountains and desert**: twin peaks, a small range, a truncated volcano cone, a rock outcrop with a cave, a crate-like block.
- **Plants and cacti**: a spiked egg/pod, saguaro-style cacti, prickly pear clusters, a round barrel cactus, grass tufts, reed/stalk clumps, a tall spiky column cactus, a round shrub cluster, a fan of leaves, a spotted pear cactus, small bushes, a dome cactus with spines, a cluster of round bulbs.
- **Small bits**: small round trees on stalks, a short pillar, a flat coiled/stacked disc (shell or layered rock).

## A4 — Terrain/Planetary scenery ideas (`1 deliberate low poly artstyle (4).jpg`)

Grid paper, black pen, punch holes on the right, portrait.

[drawing: a wireframe sphere built from a cube, i.e. a quad-sphere] = Simple sphere cube shape — explosion, rock scenery, Sun... 2-4m radius

**Terrain/Planetary scenery**

(Ideas:) *(circled)*

Scattered list of words, as written left to right, top to bottom:

Rock pillars, Hills, Trees, Stumps, Geysers, Bushes, Crystals, Explosive gas bubble trees, Spikes, Arches/Formations, Floating islands, Fog blobs, Clouds, Mist patches, Rough terrain pieces, Huge domes, Gas puffs, Static tornadoes/whirlpools, Liquid puddles, Cracks, Grass patches/shrubs, Craters/Impact marks, Alien flora/tentacles/huge bean stalks/fungus, large flat clouds, Cliffs (red alert style), Tiberium/Gems, underwater cactus, Surface anomalies, energy pylons, lightning obelisks, Vertical Plasma Beams, Buoys

## A5 — SA Naming conventions / Assets (`1 deliberate low poly artstyle (5).jpg`)

Grid paper, black pen, punch holes on the left, portrait; a pink sticky note at the bottom, written in a lighter/greyer pen.

**SA-Naming conventions** &nbsp;&nbsp; [ASSETS] *(boxed)*

```
 TYPE    A     B    C
 tex _ Rock Large 1
 mesh _ Grass Blue 5
      |
  underscore
```

- A - Generic identifier
- B - Detailing identifier
- C - Variant number

Pink sticky note:

**Assets** &nbsp; Cloud &nbsp; * *(star/asterisk drawn next to Cloud)*
- Rewar (Humanoid)
- Mothership
- Rifle (Simple/Advanced)
- Shield
- Tree/Rock pillar
- Basic enemy
- EM missile *(written at an angle to the right)*
- Gun turret
- Bomblet / Fusion bomb

## A6 — Pixel art scenery pack (`1 deliberate low poly artstyle (6).jpg`)

Grid paper, black pen, landscape-ish cut of a page; faint show-through from the other side.

~~Tiling textures packages~~ Pixel art scenery pack

Pixel art style, smallscale.

- Plants
- Rocks
- Foliage
- Vines
- Formations
- Pillars

Multiple packages, different themes, generic, flexible

## A7 — Models – Graphics (`1 deliberate low poly artstyle (7).jpg`)

Grid paper, black pen, punch hole on the left.

**Models – Graphics**

**Stage 1:** [sketch: a simple faceted figure made of a few flat polygons, a box head on a triangular body]
- Ultra simple geometry
- Flat colors
- 1 color/polygon
- No detail
- No bevel
- Modular - Mechs &nbsp; • Fused - Organics

**Stage 2.** [sketch: the same kind of figure with pixel-pattern texture on its polygons]
- Low-size pixel textures
- Hand made
- Size 32 - 64 - 128 — with "MIN" under 32 and "MAX" under 128; brackets: 32–64 "(small)", 64–128 "(medium-large)", 128 → "(seamless tex, large models)"
- Crisp
- Detailed/Simple.
- Polycount <1000, ideal 100-500 (double underlined; the digits are overwritten, apparently corrected from something like "1000-300")

## A8 — Enemy Idea: Scaling enemy size (`2 misc gfx ideas (1).jpg`)

Grid paper with blue grid, **blue ballpoint**, spiral binding on the right (different notebook from A1–A7). A loose scrap of the same paper with a cut corner lies over the bottom of the page.

**Enemy Idea: Scaling enemy size**

Excellent for biological type constructs. (organic)

[drawing: a small circle and a large circle with a double-headed arrow between them; a line down from the arrow to the range] −0.5–3.0+

Not only the chassis is scaled, but so are the hardpoints, thruster and abilities. As well as the attributes of these items may also scale with chassis size.

Bigger chassis → Bigger guns → Bigger Power! (and vise-versa)

Overlaid scrap (bottom): **Payload 2.** ~~Energy~~ Bomb (Nuke-ish) / Particle — a "3" to the right, and a tiny stick figure next to a large circle *(interpretation: a person beside a ball or bomb, for scale)*.

## A9 — Exclusion areas (`2 misc gfx ideas (2).jpg`)

Grid paper, black pen, a small cropped strip.

**Exclusion areas**

[drawing: a wireframe sphere] Inverted spheres (Face normals point inside)

## A10 — Great Fox booster effect (`2 misc gfx ideas (3).jpg`)

Grid paper, black pen, small crop.

**Great Fox booster effect**

Five sketches: a round disc with a star/flower pattern radiating from a small central circle (booster seen from behind); a rectangle containing a pointed flame/lens shape (side view of the flame); a larger rectangle with a longer flame shape inside, bracket on its left end (flame plane stretched); a rounded square with a four-pointed star/cross at its centre (flare sprite); a short cylinder/nozzle seen from the side with a flat disc at one end.

## A11 — Expanding water splash (`2 misc gfx ideas (4).jpg`)

Grid paper, black pen, small crop.

(explosion)
**Expanding water splash**

[drawing: a ring of flat angled quads/petals around an oval, like a crown splash seen from above, with arrows pointing outward in all directions]

## A12 — Star Fox 64 destruction effects (`2 misc gfx ideas (5).jpg`)

Grid paper, black pen, punch holes on the left, portrait.

**Star fox 64 destruction effects**

- Dual Shockwave rings [sketch: a flattened ring in perspective and a set of concentric rings]
- Flash red on hit / • Turn to red when killed (Gun Arms)
- Animated fire-smoke particles [sketch: a sequence of puffs, dense and spiky at first, then rounder, then breaking into scattered wisps]
- Animated explosion particles [sketch: a sequence from a small jagged burst to growing circles fading out]
- 2-sided plane gibs [sketch: a small square inside a dotted bracket] (+Scale variations) [sketch: a few tilted square/rectangular plates]
  - \* squares for mechanicals &nbsp; \* rounded for organics
- Space mega blast

[diagram for the space mega blast, left to right *(interpretation)*: a thin horizontal line/disc, then a longer one with arrows pointing left and right (an expanding flat ring seen edge-on); a small circle and a larger circle (a sphere growing); a large circle with a thin horizontal disc cutting through its middle and a small circle at the centre (sphere plus flat shockwave ring); a very large blob below it; a large circle on the right with dashes inside and dashed streaks trailing off to the bottom-right (the blast breaking up and fading)]

- Animated electric lightning sparks [sketch: a row of short jagged zigzag lines, each larger than the last]
  (the lightning moves like a worm, the tail follows the head.) ("tail" written above a scribbled-out word)
- Expanding & fading Sphere w/ animated scrolling firetexture [sketch: a tiny circle, a medium sphere, a larger sphere, then a square texture swatch with vertical flame streaks and down arrows beside it]

## A13 — Effect textures (sticky note) (`i already built this too (1).jpg`)

A single pink sticky note on grid paper, black pen, stapled through the middle.

**Textures:** Microrocks, dust particles, micro organisms.. floating micro space debris. Radiation

**Effects** — Grayscale 50% transparent visual effect textures

- Clouds✓, Gas✓, Mist✓, Haze✓, Rain✓, Snow✓
- Energy✓, Plasma✓, Lightning, Water✓, Sparks✓
- Jet boost [sketch: a cluster of streaky horizontal flame lines]
- Weapon projectile [sketches in the margin: scattered small x/star sparks, a small dot burst with rays, a ring, a circle, an eye/lens-shaped bolt, a spiky burst, an asterisk starburst, a short bar]
- Bush [sketch: a small square swatch with leafy blobs] Grass [sketch: a swatch of vertical blades] Impact marks
- Blood splats [sketch: an eight-pointed starburst] signal flashes

(The ✓ ticks are small check marks written after each word; Lightning appears not to have one.)

## A14 — Texture thumbnails, Substances and Energy (`i already built this too (2).jpg`)

Grid paper, black pen, punch holes on the right, portrait. The top two thirds are a grid of 18 square texture thumbnails (rows of 4, 4, 4, 4, 2), unlabelled. Faint show-through text from the reverse side.

Thumbnail grid *(descriptions are interpretation)*:
- Row 1: scattered short wavy lines (wisps); a marbled/cellular blob network; dense diagonal hatching; scattered small rings and dots (bubbles).
- Row 2: circles joined by lines (molecules/particles); long horizontal wavy lines (waves); vertical streaks (rain or heat); a central blob with arrows pointing inward from all sides (implosion/gravity).
- Row 3: sparse dots and specks (dust); a cracked network of irregular cells; densely packed small circles/pebbles with a few spilling out below (grains); a central circle with rays and arrows radiating outward (burst/flare).
- Row 4: faint vertical wavy lines (heat distortion); loose loopy outlines (cloud/gas); tight tangled scribble loops over diagonal lines; a solid, darkly hatched square (void/dark matter).
- Row 5: a tangle of overlapping loops (smoke or plasma); fine dense stippling (static/noise/dust).

**SUBSTANCES**
- Gas &nbsp; • Grains
- Liquids
- Dusts
- Solids
- Basic elements
- Haze
- Mist
- Fog
- Radioactive glow
- Waves
- Bubbles

**ENERGY**
- Heat distorsion
- Electricity/EMP
- Plasma
- Energy Particles (GN Drive) Low/High density
- Void/Dark Matter
- E-projectiles - Round/Directional
- Lightning
- Fire/Flames
- Gravitons
- Beams (Devices/Weapons/Utility)

## A15 — Texture creation guidelines (`i already built this too (3).jpg`)

Grid paper, black pen, punch holes on the left, portrait.

**Texture creation guidelines**
- Alpha-transparent BG
- Screen Effect textures must be seamless (Static) ("Must be" inserted above the line)
- No clipping seams on particle effect textures
- Effect texture size ~~256x256 px~~ 64 > 128 [sketch: a square containing a ring with a textured band, the margin around it labelled "CLEAR" *(interpretation: the effect must sit inside the square with clear transparent edges)*]
- Gray-scale, value-based mostly.
- Generic in style.
- Blend pieces of photo to get shapes (OPTIONAL)
- Use a more harder brush for stylized looks (OPTIONAL)
- Animated Sequences use 001, 002, 003 at end of file name.
- Use very soft edges for particle textures
  - 64x64 particle textures
  - 128x128 seamless tiling textures

## A16 — Basic Primitives Mega Pack (`i already built this.jpg`)

Grid paper, black pen, punch holes on the left, portrait. A checklist: almost every item has a ✓ tick. Two faint thin pencil lines run diagonally across the upper part (from the boxed notes down to "cloud" and to "flat pyramids"), apparently just connecting lines.

**Basic Primitives Mega Pack**

Boxed notes top right: [Animation / None / 0-Frames] [All in glorious .OBJ-format (FBX sux)] [No seperate UV files]

- plane [sketches: diamond, circle, triangle] ✓
- cube [cube] ✓ [ring/torus-like octagon] ✓
- pyramid [pyramid] ✓
- cross [cross-plane box] ✓
- cloud [crossed planes cluster] ✓
- sphere - lorez - mid rez - ico ✓ [wireframe sphere] — size 32/64 (32 written above 64) — 1/2 sphere [half-dome sketches], 1/4 sphere [quarter-dome sketches] ✓
- triange-pyramid [triangular pyramid] ✓ [inverted] ✓ &nbsp; • cones 5-8 + 20 sides [cone, top view] ✓
- ramps [wedge ramps and steps] ✓ &nbsp; • slopes [concave and convex slope profiles, a U-channel, a curved half-pipe, a quarter curve] ✓
- In the left margin: a flat box/tray and two inverted spikes (one with a cap) ✓
- flat pyramids [low frustums, flat trapezoid slabs] ✓; [two stacked box/panel shapes, circled]; [a U-shaped block and a step block labelled 2 / 1] ✓
- cylinders 5-8 + 12 + 18 + 24 [cylinder, octagonal prism, triangular prism] ✓
- flat cones [ring top view, frustum] 3-8 + ~~12~~ + ~~18~~ + 24 32 + 64 (16 written above; "maybe" over 64) ✓
- [an open cylindrical band] rings (2-sided normals) ~~12+24+36~~ 16 + 32 [ring top view, thick ring] • Donut ✓
- Large 2-sided normal sphere [wireframe sphere] (ordinary + ~~cubemapped~~) ✓ (hollow sphere) ✓
- Two-sided plane [square] ✓ &nbsp; [curved band] • half-ring, inner/outer ✓
- Diamonds [octahedron] ✓ 3-8 &nbsp; [quarter arc, bent plate] • quater-ring, inner/outer ✓
- Polyhedra (Plugin to generate them?) ✓
- Barrels [faceted barrel, octagon] ✓ with small numbers 1/2/1 beside a side profile, [an X-braced box, a box] ✓
- Gems [brilliant-cut gem, table-cut gem, square cut] 6 + 8 + 24 ✓

**COMPLETE** (large, underlined, at the bottom)

## A17 — Mothership scale / world size (`too small scale oops (1).jpg`)

Grid paper, black pen, punch holes on the right, portrait; a pink sticky note (stapled) in the lower left, its top half written in pencil.

**Mothership scale** — 16m lenght; 8-6m (bracketed span across the top); ~~[?]~~ width

[drawing: a side view of the mothership, a long hull with a stepped, boxy rear section with fins and a big engine block on the left, a long flat deck in the middle and a slanted bow on the right. Dimension labels: 2m (a rear block), 3m, 0.2m, 2.2m, 9m (the long deck), 1m (the bow tip); a bracket on the right "3.4 height"; an arrow pointing at the bow linked to "width". Overdrawn with many loose lines and a big circle mid-hull.]

Below the hull: an angled detailed drawing of a boxy turret module with barrels and panel lines, labelled "Main def turret x2" (arrow) and "sideways positron cannon" (arrow); a double-headed vertical arrow labelled "longer"; to the right, a small gun/cannon sketch (barrel with a grip/mount).

Left margin: three tall thin spike/blade shapes (a long faceted spike, a longer blade, a double-pronged spike) *(interpretation: missiles or projectiles at scale)*. Right side: "3x3m" with a small turret block; a small low box with a bracket and a domed turret with a long barrel, labelled "[?2].4m" (the first digit is overwritten). Lower right: a long gun shape (boxy receiver with a long barrel over a flat blade-like base) *(interpretation: the arm rifle)*. Bottom left: a long, low flat hull silhouette with a raised bump at one end.

Pink sticky note:

Left column (powers of two): 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048

Written vertically beside it: 90.000,00m — and at the bottom of that line "90x90km"

In pencil: 1 blender = 1m UNITY — 1 blender cube (Dimension 2) = .5 Unity cube

In pen:
- Earth size 40.000 km (Circumference)
- Max stable unity world size
- 7 point float precision 123.4567
- 200.000 km (an "m" overwritten into "km") — 200km \ 20km

## A18 — Scale: speeds, ReWaR and weapon sizes (`too small scale oops (2).jpg`)

Grid paper, black pen, punch holes on the left, portrait.

[sketch: running stick figure with an arrow] **Human** — Normal running speed 5m/s — Top —"— 10m/s

360m/s = supersonic (1296 km/h) — 4,16 minutes to travel 90km/90.000m

}+100.000 m MAX / 0.01m MIN (double underlined) — grouped by a brace

Scale 1cm Precision (~~precision~~ crossed out and rewritten above)

- [square] = cube 1x1x1m
- [crossed planes star shape] = cloud scenery 10m³ / 3 double planes
- [a large wireframe box drawn in thin pen] = world max stable 90km³
- [front view of the ReWaR mecha, 2m tall, 1.2m wide, .5m deep] = ReWaR 1.2x2x.5m

**WEPS:**
- RIFLE: [gun shape] 0.6m long, .2m high
- SHIELD: [rectangular panel with a circle and two slots] 1.1m wide, .5m high, .1m thick
- EM|IM: [small missile] .02m wide (digit overwritten), .1 tall *(EM/IM: probably EM missile / micromissile, not explained)*
- Fusion Bomb: [capsule] .03m wide, .4m tall
- CM bomblet: [tiny cylinder] .002m, .01m

Right margin column of speed conversions:
- 100km/h = 27.78m/s
- 600km/h = 166,67m/s
- 800km/h = 222.22m/s

[sketch: a large flat quad in thin pen] = Simple layer plane / 2 tris — 1x1m (replacing a crossed-out "~~100x100m~~") — Terrain, billboard effects....

## A19 — AoY World Features (`world features (1).jpg`)

Grid paper with blue grid, **blue ballpoint**, older notebook. A blurred area covers the top-right corner.

**AoY** (underlined)
**World Features**

[diagram: "Enviro" in an oval at the top, with arrows down to two ovals, "Planetary" (left) and "Space" (right)]

Planetary:
- ~~Gravity~~
- ~~Always solid ground~~
- Ground populated with destuctible scenery objects
- Possible areas of liquid (water, lava, acid, other) (surface level/depth only)
- Weather (rain, snow, lightning, meteors, tornado..)
- Fog & Clouds

Space:
- ~~No gravity~~
- Possible large objects as non-interactive scenery
- Possible floating destuctible scenery objects.
- Possible areas of special effect (gas, magnetic radiation fields.)
- Active space phenomena (Solar flares, meteor storm, wormholes)
- Nebula fog

## A20 — AoY Enviro listing, page 1 (`world features (2).jpg`)

Grid paper with blue grid, blue ballpoint, spiral binding on the left, portrait. A two-column table, "Planetary" | "Space", each entry with a small landscape sketch.

**AoY**
**Enviro listing**

| Planetary | Space |
|---|---|
| ~~Desert~~ **Crater Desert** — sketch: flat ground with low craters and rock mounds | **Asteroid Field** — sketch: scattered irregular rock blobs of different sizes |
| **Coal Mountains** — sketch: a jagged mountain range with a crater bowl; note "(possibly lava)" | **Ice Field** — sketch: large jagged-edged ice slabs and small fragments, labelled "fog" between them |
| **Sea World** — sketch: a wavy waterline over a seabed with rock/coral mounds | **Gas Nebula** — sketch: a large faint lumpy cloud mass |
| **Gas Geysers** — sketch: ground with a geyser spout, cracks and a scribbled cloud; notes "(acid) pockets of fog / smoke" | **Planetary Ring** — sketch: a dense band of hatched debris with a few rocks |
| **Cloud World** — sketch: layers of horizontal cloud streaks; notes "(very similar to space) (No terrain) (Almost 0-Grav) (Gas giant)" | **Dusty Planetoid** — sketch: a few floating rock blobs over a rolling ground line; note "(0 Gravity)" |

## A21 — AoY Enviro listing, page 2 (`world features (3).jpg`)

Grid paper with blue grid, blue ballpoint, spiral binding on the left, portrait. Continuation of the A20 table (no headers).

| Planetary | Space |
|---|---|
| **Crystal Valley** — sketch: a heavily scribbled mass of crossing crystal shards above, and below it tall crystal pillars with a tiny stick figure for scale; notes "(Giant Crystals) (Barren, rocky ter[rain])" | **Solar Corona** — sketch: faint curling flame loops |
| **Ice Mountains** — sketch: angular slanted ice slabs/peaks with an ice floe below; notes "(water) or (snow)", "(ice bergs)" | **Empty Space** — sketch: a few faint dashes, otherwise empty |
| **Dusty Rocks** — sketch: low rolling dunes with a few small rocks; notes "(moon) (mars) (craters) (dust) (rocks)" | **Giant gas bubbles** — sketch: several circles of different sizes with small inner circles, among wavy gas streaks |
| **Flying Islands** — sketch: two floating chunks of rock with jagged undersides over a wavy horizon | |
| **Bubble World** — sketch: bubbles rising from bumpy ground, two of them bursting with "POP!" labels | |

## Glossary additions

- **Ultra Simple Graphics Style**: the deliberate low-poly look: untextured white rectangles tinted by colour/opacity, scaled 2-sided planes (rectangles for mechanical things, triangles for organic things), basic primitives, single-colour "anime" effect animations, then simple gradients as later extensions (++, ++2, ++3).
- **Microart style scenery**: tiny, simple, faceted scenery objects (A3).
- **Stage 1 / Stage 2 (models)**: Stage 1 = flat colours, 1 colour per polygon, no detail; Stage 2 = hand-made low-size pixel textures (32–128), polycount < 1000.
- **Asset naming**: `type_GenericDetailVariant`, e.g. `tex_RockLarge1`, `mesh_GrassBlue5` (A = generic identifier, B = detailing identifier, C = variant number).
- **Gibs**: debris pieces from destroyed things; squares for mechanicals, rounded/triangles for organics.
- **Exclusion areas**: zones made from inverted spheres (normals pointing inward).
- **Space mega blast**: a large SF64-style explosion with expanding sphere and flat shockwave ring.
- **GN Drive**: referenced for "Energy Particles" (low/high density); from Gundam 00 (particle-emitting drive), not explained on the page.
- **Basic Primitives Mega Pack**: a set of OBJ primitive meshes (no animation, no separate UV files), marked COMPLETE.
- **EM / EM missile, EM|IM**: a missile weapon at ReWaR scale; EM|IM appears to be a pair of missile types (EM missile and probably micromissile), not defined here.
- **CM bomblet**: countermeasure bomblet (CM as in the existing glossary).
- **Weps**: weapons (rifle, shield, EM|IM, fusion bomb, CM bomblet).
- **Enviro**: environment type; split into Planetary and Space.
- **Proteus**: "Check Proteus" on A1; presumably the 2013 minimalist exploration game as a style reference (not stated).
- **Red Alert style cliffs / Tiberium**: Command & Conquer references for scenery (A4).

## Open questions

- A1 "Check Proteus": is this the game Proteus (2013) as a visual reference, or something else?
- A7 polycount "ideal 100-500": the digits are overwritten; was the earlier value something like "1000-300"?
- A8 overlaid scrap "Payload 2. Bomb (Nuke-ish) / Particle", "3" and the stick figure with a circle: what list does this belong to, and is it from the same notebook as A8?
- A14: are the 18 texture thumbnails meant to map to the Substances/Energy lists (and if so, which is which)?
- A13/A16 ticks and the scan names "i already built this" / "i already built this too": do the ticks mean the textures and primitives were actually made (and do those assets still exist)?
- A17: the "sideways positron cannon" and "Main def turret x2": are these mothership weapons in the final design? The page's scan name "too small scale oops" suggests the scale (16m mothership, 2m ReWaR, 90km world) was later judged too small; what scale replaced it?
- A17 sticky note: "200.000km \ 200km \ 20km": are these candidate world sizes, and which applies?
- A18 "EM|IM": exact meaning (EM missile and IM = ?).
- A20 "Coal Mountains": is "Coal" intended (or "Cool")?
- A19 crossed out "Gravity" / "No gravity": does this mean both environment types were later meant to share the same flight physics?

