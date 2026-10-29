# TopVerse notebook transcript: Test Notes 1–12

This chunk is the opening of the chaotic brainstorm phase. It starts with three subgame toolkit lists (Teenage Tacticool Operator, Miner vs Beasts / Demolition expert, Super Warrior with the EMTAG weapon) and the Civilian Animal Crossing default "off-duty" mode, then moves into shared framework mechanics: building/structure collapse on an X-COM-style layered grid, a global fire spreading system, a "face up to the camera" character sprite idea, pixel sizes for grid cells and characters, support pillar types (corners/walls/center), the exterior-to-interior 3x3 cell mapping with one-way wall exits and NSWE landing zones, vehicle-layer damage (hull vs turret, on-foot/vehicle attackers vs exterior walls), and a first "Vehicle Setup" page describing a vehicle's Entrance (superstructure) layer. Scan (10) also holds a second, almost empty page headed "Exterior | Interior".

## Scan Topverse Test Notes (1).jpg

Single notebook page, grid paper, a bulleted equipment list on top and two lists (activities / context) below a dashed line.

**Teenage Tacticool Operator** (a small "s" is written above the end of "Operator", i.e. possibly "Operators") **(TTO)**

- knife/saw/--crowbar/window hammer
- omnitool (screw, allen, wrench, pliers)
- foam shooters (dart, ball, rocket)
- airsoft shooters (spring, AEG, grenades)
- fire maker (match, lighter, ~~[?t]~~ torch)
- water gun/spray [Shaky skill-based aiming reticle system]
- firework/smoke bombs/firecrackers/sparkl[ers] (word runs off the page edge)
- spy/com equipment (walkie, listening dish, mirror, loudspeaker, phone smart)
- foldable vehicle boot/shoes (ski, ice, skate, snow, fins)
- stick/spear (the word "stick" is traced over/bolded)

(all equip is bagged while in water) — bracketed note to the right of "stick/spear"

Below a dashed line, left column (a large bracket joins it to the context list):

- extinguish fires (minor)
- remove obstacles (fox/eagle) — "(fox/eagle)" written above, between "remove obstacles" and "repel pests"; it may belong to either line
- repel pests (max cat/dog)
- break in, sabotage/prank,
- steal, help, rescue, find
- playful, fun, goofin' around
- no people, enemies, beasts etc.
- no death, no serious crisis.
- cozy local urban/mall locale.

Right column, headed **- Context -**:

- Missions/Objectives
- Weather
- Enviros
- Don't get hurt,
- Don't get caught.
- Resupply

*(interpretation)* The left list reads as the activity scope and tone limits of TTO (harmless kid-scale "operations": pests up to cat/dog size, no human enemies, no death), and the right list is the framing that gives a session its goals and pressure.

## Scan Topverse Test Notes (2).jpg

Single page, one verb list. Faint mirror-image text from the other side of the sheet shows through on the right (not part of this page).

**Miner VS Beasts / Demolition expert** — "Demolition expert" is written after a heavy slash, as an alternative/companion title. A few strokes above "Beasts" are cut off by the top edge of the scan [illegible].

- weld/pin/connect/drive spike
- saw/cut/slice/trim
- smash/pound/shockwave
- drill/dig/shred/dismantle/rip
- burn/incinerate
- force push/shove
- tether pull/grab
- remote det/explosives
- chem/acid/weaken/dissolve
- water hose/foam spray (-push, wet, extinguish, obscure LOS, coating)

*(interpretation)* A list of tool verbs (action categories) for the miner/demolition subgame, each line being one tool family.

## Scan Topverse Test Notes (3).jpg

Single page, four sketches (two top views of floor 1, a side view, a top view of floor 2) with labels, and rules underneath.

**Building/Structure Collapse mechanics.**

*Diagram (top left, circled "1F", TOP VIEW):* a square room seen from above. Labels: "support" (pointing to four round pillars inside the room), "wall" (the outline), "door" (a door swing drawn on the top wall and another on the right wall), "window" (a strip in the bottom wall), "reinforcement" (pointing to the thick left wall), "stairs (to 2F)" (hatched steps in the bottom-left corner).

*Diagram (top right, circled "1F", after destruction):* the same room largely destroyed, a large X drawn across it. Labels: "rubble" (jagged piles across the room), "shattered glass" (small fragments near the bottom), "broken wall" (gaps in the left wall). An arrow from the "support" label on the left sketch points into this room. Boxed beside it:

> WARN! NOT FOR UNIGEN MEGA GAME. 1 floor inte[riors] (partly cut off; an arrow points up/right)

*Diagram (bottom left, SIDE VIEW):* a building of three floors, two columns wide, labelled 3F, 2F, 1F from top, with "roof" on top and "ground" under it. Down arrows in the 3F and 2F cells; 1F left cell shows a rubble pile, 1F right cell shows stairs. A big "X NO!" is written to the left of the side view.

*Diagram (bottom right, circled "2F", top view):* a 2F floor plan, mostly scribbled over (collapsed). Labels: "support collapsed in higher floor too, has [?]if lower is destroyed." (the line reads "support collapsed in higher floor too if lower is destroyed", with a small "has" squeezed in), "hole (fall to 1F)", "stairs (from 1F)" (box at bottom left), and "clue of hole above to access 3F if jump, flight or ladder deploy is possible for char." (pointing to a hole drawn in the middle).

Rules:

- walls & supports destructible
- floors + stairs collapse when no walls/supports available + floor strenght is less than weight of object on top of it.
- stairs are passthrough and usable via E press.
- world is layered like X-COM. and grid based.

*(interpretation)* The "NO!" on the side view and the boxed warning seem to say that full multi-floor collapse is out of scope for the Unigen "mega game", which would keep interiors to one floor; the 2F sketch still explores how stacked floors would behave. The small cloud doodle next to "floor strenght" is unlabelled.

## Scan Topverse Test Notes (4).jpg

Single page, a step-by-step diagram of fire spreading (1, 2a, 2b, 3) in dashed panels plus rules.

**Fire Spreading System**

*Diagram 1:* an "initial source" (a flame) inside a circle, ringed by small circles labelled "secondary flames (igniters)"; a nearby hatched shape labelled "flammable object" is touched by one of them.

*Diagram 2a:* the original source is now a "fading source" (crossed out with an X); the flammable objects it reached have become burning circles marked "x". Caption: "new source x1".

*Diagram 2b:* similar, the fading source marked with an "x", new burning objects marked "Y". Caption: "new-lesser-source".

> X - repeat infinitely until everything burned down into unburnable state.

> Y - less likely to ignite more object once self has burned. Auto-limiting fires.

*Diagram 3:* an arrow from the X text leads to a panel showing small dots with smoke wisps, labelled "burnt object".

- global fire manager -
- each source minimal AV-wise
- spread is slow, burn is slow,
- particles/fx/AV dispensed by global FireMan, not each individual source.
- spread, speed, burn time depend on burnable object.
- After X fire sources, enable fire merging by proximity.

*(interpretation)* Two spreading modes are compared: X (each burning object becomes a full new source, so fire runs until fuel is gone) and Y (each generation is weaker, so fires burn themselves out). "AV" likely means audio-visual (effects cost). "FireMan" = the global fire manager.

## Scan Topverse Test Notes (5).jpg

Single page, sketches of a top-down character with its face turned to the camera, pros/cons lists, and an alternative.

**Character Face on top-down view**

*Diagram:* three sketches: "(TOP)" a small figure seen from above with its face looking up at the viewer; "(SIDE)" a standing figure with its head tilted back so the face points up, with a dashed arrow pointing right (its facing direction); "(zoomed)" a larger version of the top view, a grinning spiky-haired face with arms out to the sides.

- head faces up towards camera. Eyes, nose, mouth, hair are visible.
- Rest of body facing normal as usual.

**Pros**
- Unique/Memorable
- Character visible (more relatable, emotional)
- Still works directionally
- Needs only one sprite (rotatable)
- Looks stupid (meme worthy)

**Cons**
- Looks stupid

**ALT - Head only chars** — dashed box with three round head-only characters (curly-haired, spiky-haired angry, smiling with a topknot), each with a small dark rectangle beside it (*(interpretation)* a held item or weapon).

*Diagram:* below the ALT box, an unlabelled sketch of a boxy blocky shape on legs (*(interpretation)* possibly a mech or creature seen from above).

**NOTE** — Applicable to animals, beasts, etc anything that has a face or mouth, too.

## Scan Topverse Test Notes (6).jpg

Single page, Super Warrior weapon loadout in three tiers.

**Super Warrior**

- EMTAG multi weapon (variable) ("multi" written above "weapon")
- electromagnetic thermo atomic graviton ....

PRIMARY ---
- pierce
- nuke
- spray/bombard
- beam/sword (akira) (sweep)

Notes beside the primary list:
- \* Primary Rifles 2x
  - Auto target/manual aim
  - Autofire/manual fire
- \* Mounted on secondary arms.
- \* [Ultima Protoss]

SECONDARY ---
- [ cold photon projectors (shields/Blades) (wrists/feet/heels/elbow)
- [ reflector beam suit-wide auto 360' suite (ATK / DEF)
- [ shoulder mounted indirect-fire homing/curve plasma-EM Beam launcher.

TERTIARY ---
- [ back mounted auto-turret EM-railgun pellet shooter.
- [ pull/push grav tethers, hooks (grab) — "grab" under pull/push, "hooks" under tethers; light projector suite (radial suit, helmet NV/thermal)
- [ Dozen versatile detonation devices (throwable) (sticky, roll, homing, remote, proxy, timed, impact)

*(interpretation)* The four primary modes are the EMTAG weapon's variable fire modes; "(akira)" and "[Ultima Protoss]" look like style references. "NV" = night vision.

## Scan Topverse Test Notes (7).jpg

Single page, a three-column table of the default civilian mode plus two rules.

**Civilian Animal Crossing** (OFFDUTY Character MODE)

- Decorator, Communicator, Facilitator. Default non-role character that ~~[?you]~~ I always revert to.

| Decorate | Communicate | Facilitator |
|---|---|---|
| Paint stuff | MMS style interaction system & dynamics with other inhabitants npc or online. | Find, Claim, Distribute, Convert, Dispose, Send Resources. |
| Move/Add/Delete Furniture | | Crafting, Manufacturing, Construction |
| Colors/Tint/Decals | | |
| Text/symbols/Signs. | | |

- Player can only be [other class] if respective changing station and supply system is available for use/deployment. (police, firefighter, soldier, engineer, etc)
- Player can enter/exit vehicles to pilot/command them any time. Maybe some require a key, suit, diploma/skill/ability or other element though.

*(interpretation)* "MMS" is unclear; possibly a typo for MMO/MMOS, or a specific game reference (see Open questions).

## Scan Topverse Test Notes (8).jpg

Short page (scan cropped to the top half), sprite and grid-cell size sketches, no heading.

- [icon] | 64px [grid cell — small square cell with a shaded blob in it
- [icon] | 32px [regular human — small circle (reads "132px", where the "1" is most likely the bracket stroke used on the other lines)
- [icon] | 64px [giant (human) — larger circle with a face (teeth/mouth marks)
- [icon] 128px gridcell 2X — a square with a shaded figure inside, small circles at its corners
- [icon] 192px gridcell 3X — a larger square, fully hatched, with small circles at corners and edge midpoints

*Diagram:* two more squares at the bottom left: one large square with a tiny figure (two small circles) in the middle, and a smaller square containing a figure with arms/limbs spread (*(interpretation)* a 64px giant filling a 64px cell vs a 32px human in a larger cell, showing relative scale).

*(interpretation)* The base cell is 64px; a regular human is 32px (half a cell), a giant human is 64px (a whole cell); larger objects or cells come in 2X (128px) and 3X (192px) multiples. The small circles at corners/edges in the 2X and 3X cells match the support-pillar positions on the next scan.

## Scan Topverse Test Notes (9).jpg

Single page, support pillar types by position, with a scribbled-out first attempt at top left.

*Diagram (top left, scribbled over):* a grid of circles, squares and triangles, labels "corner", "center", "wall center", all heavily scribbled out.

- \*Material used
- \*Thickness/size

**Support Pillars**

*Diagram:* a square cell with circles at its four corners, small rectangles at the middle of each side, and a triangle in the middle. Lines lead from each symbol type to a legend:

- O - corners: [ round post, L-shaped corner, short horizontal bar, short vertical bar, small square block, triangular wedge ]
- ☐ - walls: [ long vertical bar, round post, square block, dashed thin bar, partly dashed bar, thin bar, half-dashed bar ]
- △ - center:
  - square blocks of size 1/1, 1/2, 1/4, then a long thin cross, then a small thick cross
  - round blocks of size 1/1, 1/2, 1/4, then a short vertical bar, a long vertical bar, a small triangle

*(interpretation)* Each grid cell has nine support slots (4 corners, 4 wall midpoints, 1 center), each of which can hold a pillar of a different shape, material and thickness; dashed bars probably mean weaker/partial (damaged or light) supports.

## Scan Topverse Test Notes (10).jpg

Two pages in one scan: a full page of exterior/interior cell mapping diagrams, and below it the top of a second page with only two headings.

### Part 1: exterior to interior mapping

*Diagram (top left):* "Ext." a single cell with a dot (labelled "human" by a small square under it), arrow to "Int." a 3x3 grid with an x in each cell.

*Diagram (top right):* "Ext" a column of three cells (dots in the top and bottom cells), arrow to "Int." a 3-wide by 9-tall grid made of three stacked 3x3 blocks; the dots appear in the matching blocks; small arrows point down out of the bottom edge.

*Diagram (middle):* a 3x3 interior block with a dot in the center, compass labels N, W, E, S around it. Arrows point outward from each edge cell (three up, three down, three left, three right); the four outside diagonal corners are crossed out with X. A small square (*(interpretation)* the human/player marker) sits next to N.

> Interior wall exits (one way only)

*Diagram (bottom):* an arrow from S leads down to a plus-shaped arrangement: a center cell with a dot, and dashed cells N, W, E, S around it.

> Exterior exit landing zones NSWE (non-UG)

*(interpretation)* One exterior cell expands into a 3x3 interior; walking out of an interior wall is a one-way exit that drops you into the exterior cell adjacent on that side (N/S/W/E), never diagonally. "non-UG" means this applies above ground, not underground.

### Part 2: second page

Two column headings separated by a vertical line: **Exterior** | **Interior**. Nothing else is written. (Faint text visible on this part, such as "-30hp +10hp(%) (turret) (hull)", is show-through from scan 11 on the next sheet, not writing on this page.)

## Scan Topverse Test Notes (11).jpg

Single page, vehicle-layer damage sketches and exterior wall damage by unit type.

**Vehicle layer**

*Diagram (top):* two vehicles seen from above. The left vehicle (two turrets) is hit by a small aircraft/missile from the upper left: "(hull) -5hp". It fires its turrets at the right vehicle; the right vehicle shows "(hull) -100hp". The left vehicle itself shows damage at its rear: "-30hp + -10hp(%) (turret) (hull)". A soldier/jetpack figure at the bottom fires up at the right vehicle: "-20hp (hull)".

*(interpretation)* A hit on a turret damages the turret (-30hp) and passes a percentage (-10hp) on to the hull; small arms and small craft only chip the hull.

*Diagram (middle left):* three attackers labelled M (a mecha), H (a human), T (a tank) all fire arrows into a building outline labelled "Exterior", whose walls are drawn in segments, some hatched. Label: "(damage walls/supports segments)".

*Diagram (dashed box, right):*
- ground/UG/sea/space/UW
- air intercept

Inside the box, separated by dashed lines: a jetpack trooper and a helicopter each firing at an "Ext." building outline (air row), and below them a small ground vehicle and a walking mecha firing at another "Ext." outline (ground row).

*(interpretation)* The box lists the combat layers in which vehicles can attack an exterior (ground, underground, sea, space, underwater, plus air intercept), and shows air and ground units damaging the exterior wall segments the same way.

## Scan Topverse Test Notes (12).jpg

Single page, one list. Faint show-through from the other side of the sheet is visible (not part of this page).

**Vehicle Setup**

*Diagram:* a small horizontal rectangle with hatching and a dot inside (*(interpretation)* a vehicle with a person/crew marker).

Entrance:
- Superstructure.
- On foot/minor vehicle entrances/exits.
- walls, support solids, all destroyable.
- On foot defences (traps, turrets, troops)
- Vehicle weapons usable via commander or remote interface control. (anywhere in humansize room, hits arrive from above. May have min-range.

*(interpretation)* This is the first appearance of the MDRC "Entrance" face from the glossary: the vehicle's on-foot outer layer, whose weapons can be fired from inside the on-foot room and whose shots land "from above", like the interior hits described later.

## New terms

- **TTO**: Teenage Tacticool Operator(s), Reactorcore's own abbreviation.
- **AEG**: automatic electric gun (airsoft term).
- **AV**: most likely audio-visual (effects/sound cost of each fire source).
- **FireMan**: the global fire manager.
- **MMS style interaction system**: unclear; possibly a typo for MMO(S) or a reference to a specific game.
- **Ultima Protoss**: unclear reference beside the Super Warrior beam/sword (possibly StarCraft Protoss styling).
- **M / H / T**: mecha, human, tank (attacker labels on scan 11).
- **Ext. / Int.**: exterior / interior (precursors of the DRC Entrance / Interior faces).
- **Interior wall exits / exterior exit landing zones NSWE**: one-way exits from a 3x3 interior to the adjacent exterior cell.
- **Support pillar slots**: corners / walls / center, with shapes, sizes (1/1, 1/2, 1/4), material and thickness.
- **Grid cell sizes**: 64px base, 2X = 128px, 3X = 192px; regular human 32px, giant human 64px.

## Open questions

- Scan 1: whether "Operator" has a plural "s" added above it; the crossed-out letter before "torch"; whether "(fox/eagle)" belongs to "remove obstacles" or "repel pests".
- Scan 2: strokes above "Beasts" cut off by the scan edge.
- Scan 3: the boxed warning ends "1 floor inte..." and is cut off; the small word "has" squeezed into the 2F support note.
- Scan 5: the meaning of the unlabelled blocky sketch under the ALT box.
- Scan 7: the crossed-out word before "I always revert to"; what "MMS" stands for.
- Scan 8: "132px" vs "32px" for regular human (read as 32px).
- Scan 10, part 2: the "Exterior | Interior" page has no content in this scan; any content may be on a later scan.

## Cross-references

- Scan 1 (TTO), scan 2 (Miner vs Beasts), scan 6 (Super Warrior, EMTAG) and scan 7 (Civilian Animal Crossing: Decorator/Communicator/Facilitator, default mode) are the subgames already named in the text notes; scan 6 confirms the EMTAG expansion "electromagnetic thermo atomic graviton".
- Scan 7's "changing station and supply system" rule for taking other classes (police, firefighter, soldier, engineer) links the civilian default to the civil-service subgames.
- Scan 3's "stairs usable via E press" matches the room-network rule "Doors: press E to enter"; its "NOT FOR UNIGEN MEGA GAME, 1 floor interiors" warning limits multi-floor collapse in the universe game.
- Scan 3 and scan 9 (destructible walls/supports, pillar slots) feed the "destructible levels" part of the standard framework and the DRC "walls, support solids, all destroyable" in scan 12.
- Scan 10's one exterior cell → 3x3 interior mapping is the early form of the glossary rule "each entrance cell maps to a 3x3 interior cell" (DRC Entrance → Interior).
- Scan 11's hull vs turret damage and scan 12's "hits arrive from above" are the early form of the glossary's interior hit / hull hit rule; scan 12's "Entrance: Superstructure" is the first appearance of the DRC/MDRC Entrance face.
- Scan 11's layer list (ground/UG/sea/space/UW, air intercept) prefigures the vertical layers list.
