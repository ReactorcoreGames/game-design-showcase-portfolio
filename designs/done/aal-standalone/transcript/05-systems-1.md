# Standalone notebook transcript: Menus, briefing, demo plan, world system, enemies and damage

This chunk covers the first 18 scans of the "menus maps metagames systems" folder, in order: the character edit (create) screen layout and colour options (S1); the briefing screen and how you choose your entry point in space and on a planet (S2); the in-action "tutorial refresher" overlay (S3); unique IDs for persistent units and the option to fight ReWaR-only without the mothership (S4); the click-through demo plan (S5); the tactics screen layout and the numbered screen order with HSV values (S6); the world components (solid objects, solid and liquid surfaces, effect areas, weather layers) and a "Space level v2" sketch (S7–S8); the World System with its two core world types, planetary and space (S9); enemy types, structure and common rules (S10); cryo resistance and freezing (S11); the general damage system with thresholds and destruction/overkill (S12); sensor ranges across galaxy, local space, action field and tactics screen (S13); damage effects on targets (S14); damage hit effects by source, including the resisted/unresisted table (S15–S16) and universal entity properties (S16); the Prototype 1 todo list (S17); and the start of the Enemy Groups text (S18, continued on a later page).

## S1 — Character edit / create screen (`IMG_20191005_134541.jpg`)

Grid paper, blue pen, portrait; page has a fold crease across the upper right corner. No sticky notes.

**Sketch (top left):** a UI screen mockup titled **CHAR EDIT**, with **CREATE** written underneath the frame (the screen's name or the action it leads to *(interpretation)*). Inside the frame:

- Left column: three rows, each a text field with squiggle "text" and a small numbered square button at its right end (**1**, **2**, **3**). Below them three empty square boxes side by side labelled **CORE SHIP MECH**, and below that a button **RANDOM**.
- A vertical divider line, with a dot/arrow pointing from the left rows into the right side.
- Right column: a text bar at the top (with a "1" under it), then a framed box holding a drawing of a figure / mecha and ship *(interpretation)*, with numbers **1**, **2**, **3** at the box's edges (the three textures/name previews).
- Bottom: a wide **DONE** button.

A label **"Preview"** in quotes points at the right column box, with the note: Multiple textures, affected by color choices.

A long curved line runs from the left of the mockup down to the "Color Options" heading.

**Color Options**

1. Core/Energy color (Avatar color, shield/propulsion/weapon color)
2. Ship color
3. Mech color

Right of the heading: a small sketch of a tall rectangle with a circle (an eye/lens) in it, labelled **HAL9000 style avatar**.

**L-side** — (enforced) [written above, with a small arrow pointing down to "max char"]

- 3 txt labels (name, max char)
- 3 img labels
- 3 textfields [double underline below]
- 3 repeat buttons (color pickers)
- 3 txt labels
- 1 button ("random")

**R-side**

- 1 txt label [underlined]
- 1 box
- 3 textures (AI, Ship, Mech)
- 3 txt labels (name previews)

## S2 — SA-Briefing Screen & Action Intro (`IMG_20191005_135120.jpg`)

Grid paper, blue pen, portrait, spiral-bound edge on the left.

**SA-Briefing Screen & Action Intro**

During briefing, you are presented with a map and information of the situation on it. On the map, you can select your entry point.

**Selection:** [arrow-shaped heading box]

Two map sketches side by side.

**Space** (left): a square map with a large circle drawn inside it. The circle's rim is a hatched band labelled **Playable play area** (pointer from the left margin). Inside the circle are a few smaller circles; a cluster of circles at the top is labelled **enemy forces** (shared label between both maps). On the rim at lower right, a dot with an arrow pointing inward (the entry point facing the centre) and a curved arrow along the rim (sliding the entry point around the edge *(interpretation)*).

Text under it: Select ~~from~~ ^entry^ from edge, entry height is always 0. Face center always. Spawn in motion (forward) at X distance from secondary border.

*(Reading note: "entry" is written small above "from", as an insertion: "Select entry from edge".)*

**Planet** (right): a square map divided into a grid (about 7 × 7 squares), with faint circles at the upper left (enemy forces) and a black dot in the middle (the chosen entry point). A label **Entire planet surface** at upper right, with lines pointing to the map. To the right of the map, a small control column:

- **0 → 360°**, with a small box **15°** below it *(interpretation: angle step)*
- **Angle**: a box showing a side view of a craft diving nose-down at an angle, with an arrow **F →** (forward)
- **Preview**
- **Rotation**: a box showing a top-down view of the craft, with an arrow **↑ F**

Text under it: Select anywhere on planet surface & set angle of entry (any, no limit). Spawn in motion downwards ~~at~~ desired angle X distance from secondary border, near top of the map at position indicated ~~at~~ briefing in XY coordinates.

**Entering action:** [arrow-shaped heading box]

1. Fade from black into ingame.
2. When clear, begin countdown (2-3sec) to gain control.
3. Ready to play.

Transition from Action to Action via metagame is automatic. (Autopilot) [an arrow from "Autopilot" points up toward "gain control" in line 2]

## S3 — SA-tutorials refresher course (`IMG_20191005_135159.jpg`)

Grid paper, blue pen, portrait, cropped photo.

**SA-tutorials refresher course**

The "tutorial refresher" gives a simple toggleable overlay UI that reminds you what button does what.

**Sketch:** a screen frame with four columns of text, each with a squiggle heading. The left column lists keys down its edge: **A, D, W, S, X, E[?], C[?], ctrl, shift** with dashes after each (the binding descriptions). In the middle, drawn over the columns, is a mecha figure seen from the front. The right column has a second heading lower down with a few more entries. Bottom left: **PRESS X to toggle**.

Besides just keybinding with categories, you also get basic hints. It also reminds you ~~[?]~~ about the operation manual in the "Database". And how to access it.

The overlay also describes what each UI element is.

Small example sketches in a row: a horizontal bar partly hatched, labelled **Health bar:**; an ammo icon with **015**, labelled **Ammo**; a radar ellipse with blips, labelled **Radar**.

The overlay DOES NOT pause the game. It's only a quick on-demand reference.

## S4 — SA-Unique IDs / ReWaR-only battles (`IMG_20191005_135410.jpg`)

Grid paper, **pencil** (grey), portrait. Two separate notes divided by a horizontal line.

**SA-Unique IDs for persistent units**

Instead of restricting using a same name for a unit, a unique identifier is used with each new SA unit.

---

**SA-Allowing choosing to go ReWaR-only during battles.**

**Sketch:** a briefing screen frame titled **Briefing...**. On its left a map area with vertical stripes, a small circle/face and an **X** marked, labelled **select** (pointer from outside left). On its right a panel with text lines at the top, then a checkbox labelled **☒ MOTHERSHIP** above a small picture of the mothership. A note to the right: Check box to indicate if mothership joins the battle.

**If no MS:**

- No repairs/respawns/rearms for ReWaR
- No resource gather
- No fire support or superweapons
- No MS direct control (out of range)

## S5 — Demo setup (`IMG_20191005_140012.jpg`)

Grid paper, black pen, portrait; top right corner folded over.

**Demo setup:**

Step by step experience of the game, roughly in a screen from screen mock up using menus and buttons, but no actual function behind them yet.

- Going from Intro to gameplay (very simplistic) and game exit in a one way slideshow-like fashion.

**Sketch:** a screen frame with a small **Next** button in the top left corner, squiggle title, three little boxes, the word **Content** in the middle, and a row of controls at the bottom. Labels: **Button: "Next" for next screen/scene** (pointing to the Next button); **GUI Controls: Example of final result, no real function** (pointing to the screen).

Profiles → Main Menu → Campaign Entry Screen →

→ Skirmish Screen → Briefing → Action Demo (with pause menu)

→ Debriefing → Exit

This demo should be uploaded as a webplayer for ease of access.

## S6 — Tactics Screen and screen order (`IMG_20191005_140037.jpg`)

Grid paper, black pen, portrait, cropped photo.

**Tactics Screen**

**Sketch:** a screen layout of four panels: a narrow left panel with list lines, labelled ~~[?]~~ **World** ~~Player~~ **Status** (the left label has been rewritten: "World" written over a crossed word, "Player" crossed out); a large central panel with a grid, labelled **Battlefield overview**; a right panel headed with a squiggle and list lines, labelled ~~World~~ **Status / Selection**; and a wide bottom bar across under the three, labelled **player status**.

**Order** (a numbered list with a vertical line to its left; numbers were renumbered, old numbers overwritten/crossed):

| # | Screen | Side branches |
|---|---|---|
| 1 | PreIntro | |
| 2 | Intro | |
| 3 | Profiles | |
| 4 | Main | |
| 5 | Options | |
| 6 | Start Game | |
| 7 | Tutorial | |
| 8 | Campaign | |
| ~~10~~ | Metagame | ← 9 Character Edit |
| 12 (was ~~13~~) | Skirmish | ← ~~11~~ Tactics, ← ~~11~~ Pause *(the two branches point at Skirmish/Metagame; their numbers are overwritten and unclear)* |
| 13 (was ~~14~~) | Briefing | |
| 14 (was ~~15~~) | Action | ← 15 Tactics (a long curved arrow from the upper Tactics/Pause pair down to Action) |
| 16 (was ~~18~~) | Debriefing | |
| ~~19~~ [?] | Quit confirm | ← 17 Database |

*(Interpretation: the new numbering puts Character Edit at 9, the Metagame-level Tactics/Pause at 10–11, and the in-action Tactics at 15; the overwritten digits are hard to read.)*

**HSV** (left margin, three values, old values crossed out):

- ~~219~~ [?] → 220
- ~~103~~ [?] → 100
- ~~59~~ [?] → 60

## S7 — World Components (`IMG_20191005_143220.jpg`)

Grid paper, blue pen, portrait.

**World Components**

- **Solid objects.** (Can attach emitters to these) Collidable scenery. Follow rules of "universal entity standard". May also be set as non-solid. Collision still happens, but can pass trough them.
- **Solid surface** Collidable planetary surface. Semi-indestructable (only planetkiller weapons/devices have effect). Loops at edges. If possible, it should curve to simulate planet roundness. Can have material properties.
- **Liquid surface** Semi-collidable planetary surface. Entity may pass through, but upon entering a collision event happens for splash effects and such. Same when exiting liquid. Below the surface is a progressively stronger "effect area". Depending on planet and liquid type, there is always a fatal area at a variable depth.
- **Effect area** Freelancer based system. Areas are made out of multiple parts. They are seen from a distance as a generic cloud, but upon entry they may contain randomly dispersed solid- and nonsolid object, screen-effects, particles, entity effects (damage system). Effect areas have priorities. One effect area can override another by having a higher priority. This means you can have field within a field.

## S8 — Weather layers/zones and Space level v2 (`IMG_20191005_143226.jpg`)

Grid paper, blue pen, portrait, top right corner folded. Large parts of this page are blurred out by the owner (a band at the top, and a big block in the middle).

[blurred area at the top]

- **Weather layers/zones** Variable min-max height (planetary) or distance from centre (space) where weather effects occur/take place. Works similar to Effect areas in how they appear up close and from afar. [a further word follows, crossed out and cut off by the blur]

[blurred area in the middle of the page]

**Space level v2**

**Sketch:** on the left, a large spiral of concentric circles/ellipses with a small circle at the centre and radial arrows pointing outward from it (a sun or gravity source with the play area around it *(interpretation)*), labelled **Play area** (pointer). Three heavily hatched blobs sit in a row along the top (asteroid fields or effect areas *(interpretation)*). Below left, a tiny figure (a person, for scale) next to a long ship-like outline with a circle near its front end (the mothership *(interpretation)*). On the right, a large irregular outline with diagonal hatching runs down the right side of the page (a planet edge, nebula or large body *(interpretation)*), with a smaller hatched irregular shape at its lower left edge.

## S9 — World System (`IMG_20191005_143302.jpg`)

Grid paper, blue pen, portrait, spiral edge on the right.

**World System**

There are 2 core types of worlds:

**Planetary** (left sketch): a trapezoid / cone shape seen side-on: a flat base line marked **3.** and slanted sides with arrows, numbered **1** on the left side, **2.** and **3.** on a vertical arrow rising from the middle, and an arrow on the right side. Faint lines and small shapes are drawn inside (entry paths into the planet's play area *(interpretation)*).

**Space** (right sketch): a large ellipse with a small circle (sun/solar object) at its centre and concentric rings around it. Labels: **solar object area** and **area border** (top right, pointing to the outer ellipse); **neutral** (a hatched section at the top left of the rim); **solar object** (an X just outside the ellipse at the right); **weather area** (lower left). X marks sit just outside the rim at top, left, right and bottom (exit points *(interpretation)*). Below right, a separate small circle with an X in a ring (another solar object).

**Difference:**

Left, under "Planetary": a side-on cross-section. From top down: a hatched zigzag band (sky/space limit); an arrow up labelled **space ↑**; a line labelled **Play field** (with a small marker); a line labelled **surface** with heavy hatched lines below it; a label **core ↓** above a band of crossed X marks at the bottom. A vertical arrow on the right side is a **Height** axis with ticks marked **+1m**, **0m**, **-1m**. Beside the axis, a small grid box and a circle labelled **weather area**. Label at the bottom: **(planet)**.

Right, under "Space": a perspective drawing of a flat grid plane with lines through it in several directions and small circles on it, labelled **Play area**.

Planetary:

- Large flat area, loops around
- Entry/Exit only top
- Gravity Direction (Height)
- Variable "play field" altitude (eg. where "shit happens")
- Variable surface (and liquid surface) [OPTIONAL] (However atleast one must be present.)
- If no solid surface, a killzone must be at a certain depth (pressure, gradual. Get warnings)
- Variable exit altitude (Space)

Space:

- Large Area w/ boundaries
- No looping
- Exit at any border
- Gravity Source (OPTIONAL)
- Play area always at middle
- Certain directions can be made progressively lethal the closer the player comes to it (sun, anomaly, blackhole)

## S10 — Enemy Types (`IMG_20191005_145029.jpg`)

Grid paper, blue pen, portrait.

**Enemy Types**

**Structure**

**Sketch:** a top-down ship outline (a house/pentagon shape with a pointed front), with a central square holding a circle/target symbol, two long rectangles mounted on the left and right sides, a row of small squares near the nose, and two small angled boxes at the rear corners. Labels:

- **CHASSIS SPECIAL FEATURES** (cloak, shield, overcharge...) — pointing at the row of small squares
- **CHASSIS BASED AI BEHAVIOUR** — pointing at the central core symbol
- **HARD POINTS** — pointing at the side rectangles
- **CHASSIS** — the hull
- **THRUSTERS** — the rear boxes

A line runs from HARD POINTS to a circled list:

**Hard points:**

- Weapons
- Tools
- Utilities

Side note: A single HP can mount any system

**Common Rules ^ALL^ Enemies Follow**

- Ammunition limit (non-energy weps).
- Heat Generation on (will vent heat and be unable to fire for a short delay).
- Enviro-hazards affect enemy too.
- Damage is universal (later adv) maybe ← [note "(later adv) maybe" written into the line; "adv" possibly "advanced" *(interpretation)*]
  - Radiation
  - Fire/Burning
  - EMP
  - Kinetic ~~damage~~ impacts
  - Cryo
- Gravity affects enemies too.
- No bullshit allowed.
- Same dimension as player character in terms of universal game rules. Maximum consistency is must.

**Size Categories**

- Normal
- Large (Heavy-fucking-duty)

## S11 — Cryo resistance and freezing (`IMG_20191005_145204.jpg`)

Grid paper, blue pen, portrait, cropped photo; continues a list from a previous page (starts with a dash item).

- **cryo resistance** (Same as heat resistance in ^terms of^ mechanics.) Enough cryo-exposure will slow down the target, make it ^weaker to^ other damage types (except heat, which reverses any effects (except damage) done by cryo attacks) and eventually completely freezes the target.

**Freezing:**

Cryo-effects "melt away" constantly, depending on entity properties and environmental conditions either slower or faster. Even if a target is 100% frozen, it only becomes stunned, not dead. Either by itself and/or help from environment or ally, an entity will always recover from freezing. cryo-attacks deal small damage on contact, but not during.

Also "slowing down" means increasing delay to action of an entity, making it react slower as it gets more frozen, up until its completely frozen, where it stops reacting all together.

## S12 — Damage System: Overall (General) (`IMG_20191005_145213.jpg`)

Grid paper, blue pen, portrait, spiral edge on the left.

**Damage System: Overall (General)**

- Every active entity has a predefined amount of health (a number, NOT shown to player at any cost!)
- Entity takes damage universally, there is only a universal HP amount total. No segmented hitzones or weakpoints.
- An entity has several definable threshold values besides the universal integrity.
  - EMP threshold (Minor effects if minor, stun if breached.)
  - Armor strenght (Deflect or reduce effect if not [?] AP enough.) (PER SHOT.)
  - Heat resistance (Can reduce X amount of damage until breached. Cumulative.)
  - Radiation protection threshold (recieve damage if crossed over max value. Amount of damage dictated by source, none is reduced or blocked.)
  - Kinetic Force threshold. — **NOT DAMAGE** (amount of physical force an entity may shrug off. If breached, entity will be pushed by the overwhelming force.)

*(Reading note: in the Armor line the word "not" may be partly struck through; AP likely means armour-piercing.)*

**Sketch (left):** the same pentagon-topped entity shape as on S14, with a line down to an example stat block:

| Value | Stat |
|---|---|
| 1000/1000 | HP |
| 100/100 | EMP (recharges) |
| 100 | armor |
| 10 | heat resist |
| -10- | rad limit |
| 100 | kinetic resist |
| 100 | cryo resist |

**Destruction**

**Normal** - Entity turns into flaming corpse.

**Overkill** - Entity will completely vaporize. Effect based on damage type. Corpses have a certain amount of HP.

- \* If depleted by continuous minor damage - break into exploding debris and smoke.
- \* If major kinetic damage - violent explosion into shreds
- \* If major heat - melt and disintegrate into nothing
- \* If major radiation burst - light up and dissolve slowly.

## S13 — Sensor ranges: galaxy to tactics screen (`IMG_20191005_145332.jpg`)

Grid paper, blue pen, landscape photo of a portrait page with the spiral on the right. All sketch, with labels.

**GALAXY** (top left): a spiral galaxy sketch with a tiny square marked on its edge. A line runs down from the square to the local space map.

Label between galaxy and local space: (entire local space) **LR sensor effectiveness** ("LR" = long range *(interpretation)*).

**LOCAL SPACE**: a circle containing a square map with scattered dots, small clusters and a triangle marker (the player) at the top left. Under it:

- ALL TARGETS VISIBLE AS BLOBS
- ROUGH TYPE ID POSSIBLE (IF IN OPEN SPACE)
- Highlighting can bring up details if known

A line runs from a point on the local space map to the action field box.

**ACTION FIELD**: a 3D box drawn in perspective with a horizontal mid-plane, dimensions **100** (height, double arrow), **100** (depth) and **100** (width). Under it:

- ALL VISIBLE BUT LOCKON REQUIRES CLOSER RANGE

A line runs from the action field to the tactics screen.

**TACTICS SCREEN**: a square top-down map with groups of small unit icons inside circles, scattered dots, a sun symbol at the top edge and a spiral (black hole/anomaly) below the bottom edge. Labels around it:

- ▭ 0m (top, beside the sun) *(interpretation: altitude/height readouts)*
- ▽ 80m (pointing at the top right group)
- △ 125m (pointing at the lower right group)
- ▭ 0m (left)
- △ 576m (by the spiral at the bottom)

Below: **envirotype affects sensor efficiency** (reduce lock on speed/range and slower ID scan)

**Crossed-out sketch** (top right, a large X drawn through it): a cylinder with a sphere inside containing a small ship, with a vertical double arrow beside it, a scribbled-out number next to the arrow, and an arrow cross at the top. Label ~~Sensor effectiveness~~.

## S14 — Damage Effects: Targets (`IMG_20191005_145357.jpg`)

Grid paper, blue pen, portrait, spiral edge on the left.

**Damage Effects: Targets**

**Top right diagram:** **ALIVE 0-80% → DEAD 100%** above a bracket labelled **O P A C I T Y**, running from **HP 100%** at the left end to **0%** at the right end; a mark near the right end is labelled **1HP LEFT D.T. at 80%** ("D.T." = damage texture *(interpretation)*). A line runs from the bracket down to the "Opacity Controlled 'damage' texture" bullet.

**Left column sketches** (the pentagon-topped entity shape in four states, labelled down the margin):

- **ENTITY / ALIVE**: clean outline.
- **DAMAGE (80%)**: the same shape with dark marks, flames, sparks and smoke puffs rising off it; several lines connect it to the bullets on the right.
- **DEAD**: the shape fully blackened with holes/circles.
- **OVER KILL**: the shape inside a burst of jagged flame and debris.

**Damage Components**

- Normal Texture
- Opacity Controlled "damage" texture
- Decals/Black-impact-draw texture
- Internal Damage Emitter (SEVERE DAMAGE) (Fire, sparks, leaks...) 1x only
  - \* (Located in middle of entity.) (or surface)
- Death explosion burst (Transition from alive to dead.) — a four-step mini sequence: **1.** clean shape, **2.** marked shape, **3.** shape in an explosion burst, **4.** blackened shape; under it **80% → 100% OPACITY JUMP**
- → Alt. Instead of single or multiple point emitters on entity, the entity itself is the emitter with particles spawning accross its surface. [a curved arrow leads from the "Located in middle of entity" line down to this alternative]

## S15 — Damage Effects: Sources (`IMG_20191005_145511.jpg`)

Grid paper, blue pen, portrait, spiral edge on the left. Continues onto S16.

**Damage Effects: Sources**

**Hit Effects are divided into 2 types:**

Sketch: **Direct/Contact** — an entity shape with an arrow hitting it at one point. **Area/Ambient** — a large circle containing a small burst/sun and an entity shape inside the area.

- \* D: Projectiles, beams, bolts
- \* A: Explosions, Areas, rays

There needs to be a variable to limit gradual damage when source is weak enough.

**Both types have 2 states:**

Sketch: two blocks. **Resisted**: a block with a small D arrow hit and a small A plume on top, minor effect. **Unresisted**: the same block with a much bigger burst of debris and flames at the D and A hits. Note with arrow: **More damage / Defences breached**.

**Hit effects by source**

| ✕ | Resisted | Un-Resisted |
|---|---|---|
| Kinetic D | Shockwave, shrapnel, debris sparks, tiny fireball, smoke | same, but more significant flames, bigger fire burst and more shrapnel. |
| Heat D | Localized spherical glow effect accompanied by tiny heat particles and light flames and minor smoke | same, but added fire that sticks and burns at the impact location for a few seconds |
| Heat A | The surface of the entity glows with heat. Intensity of glow controls how strong the glow effect is. Also tiny particles and minor smoke. Glow is orange/red. | Glow not so intense now, but the surface of the entity is actually on fire, with the entity being bright from the heat. (Saturation++ and reddish color). |
| Radiation DA | Almost same as heat, except in yellow color and not as fast/less vivid. If possible, creates an visual effect that makes it look like the surface of an entity is shaking/vibrating. | Same, but now it also looks like the entity is slowly vaporising as matter comes off the surface of an entity in the form of particles. If possible, the texture of entity gains brightness and lowers saturation to add to the effect. |

(table continues on S16)

## S16 — Hit effects by source (cont.) and Universal Entity Properties (`IMG_20191005_145651.jpg`)

Grid paper, blue pen, portrait, spiral edge on the right. Top: continuation of the S15 table; the empty remaining rows of the table are struck through with diagonal hatching.

| ✕ | Resisted | Un-Resisted |
|---|---|---|
| EMP D | A bright spherical glow flash. Minor electric arcs that do not spread beyond impact point. ~~Tiny blue particles burst out.~~ Sparks. | Same, but much more larger electrical arc that wide accross the surface of the entity spread. Arcs linger for a second. Blue glow. |
| EMP A | Blue surface glow, minor electric arcs randomly appearing. | Much more electric arcs. Otherwise pretty much the same. |
| Cryo DA | Cyan glow on impact/surface. White puffs bounce off. | Same, but entity's texture becomes progressively whiter. |

Written in the hatched empty area of the table, small capitals: **KATSUYA EGUCHI** [?the "Y" could read as "J"] (an unrelated note *(interpretation)*).

**Universal Entity Properties**

- Mass
- Scan Integrity (Multiplier 1-5.0x) [written to the right, above the next line]
- Pin Strenght - (Planetary Scenery mostly use this)
- Gravity Scalar
- +Damage System + Material system (what is it made out of.)
- Gibs
- Collision Effects (self only, scalable with impact power)
- IsSolid (Toggle between a solid and nonsolid)

## S17 — Prototype 1 todo - Designs (`IMG_20191005_145659.jpg`)

Grid paper, blue pen, portrait, cropped photo. Many items carry tick marks (✓).

**Prototype 1 todo - Designs**

- Enemy group 1 (robot ships) standards ✓
- World framework system & standards ✓
  - \+ General enemy behaviour (initial status, etc.) ✓
- Metagame basics (Overworld, Campaign, Progression) [a single slash mark beside it]
- Basic game logic (Menu, Profiles, Options) - 1 ✓
  - (Start, Game, End, Features) - 2 ✓
- Prototype controls for mothership (Both automatic and manual) ✓ — "automatic" is underlined, with **Priority** written next to it

**Note: Code with modularity in mind!** ("modularity" double underlined)

- The Database (Ufopedia of sorts) + Scanning mechanic ✓ — side notes: **Part of user manual** (with an arrow to the tick); **Enemy type/size**; **scan time**; **cumulative - Per[?centage]** (underlined)
- Marketing plan (Episodic releases!) ✓
- Intro sequence ✓
- Tactics Screen ✓

Prototype 1 release aims to create a playable, but barebones release featuring only the Mothership with basic capabilities. Main focus will be to set up the basic framework of the game, notably the world- and entity-systems. Major focus will be on modular code design, as it is likely to replace with more complex components as development goes on.

## S18 — Enemy Groups (`IMG_20191005_145740.jpg`)

Grid paper, blue pen, portrait, cropped photo. Text only; continues on a later page ("CONT →").

**Enemy Groups**

Enemy groups are factions that threaten mankind directly or indirectly. Some groups seek to get something (RUs, Human Samples, Tech...), while others are simply exterminating anything they find.

They might be anything from savage animals to intelligent, but mad beings. Point is, they cannot be reasoned with or beaten with a deus ex machina (Virus, On/off button etc...).

The game focuses on the finesse and adrenalin of combat with some slight survival and tactics to keep the game continuously interesting.

While the main game is played in campaigns with a definite goal (Defeat enemy in star systems), the game is essentially infinite. There is progression in the game to keep motivation up during a single campaign and stats recorded with the persistent character, but no enemy group is fully eliminated ever. CONT →

## Glossary additions

- **CHAR EDIT / Character Edit**: the character creation screen (names, three colour pickers for Core/Energy, Ship and Mech, Random button, preview with three textures).
- **Core/Energy color**: the AI's colour, used for the avatar, shields, propulsion and weapon effects.
- **HAL9000 style avatar**: the AI ("You") shown as a lens/eye in a panel.
- **Entry point / secondary border**: where you spawn into action, picked on the briefing map; space maps: on the edge facing centre at height 0; planet maps: anywhere on the grid with an entry angle. The "secondary border" is the distance reference for spawning.
- **Tutorial refresher**: toggleable, non-pausing overlay of key bindings, hints and UI element names.
- **Unique ID**: identifier given to each new SA unit so names can repeat.
- **ReWaR-only battle**: a battle where the mothership box is unchecked; no repairs, respawns, rearms, resource gathering, fire support, superweapons or MS control.
- **Solid objects / Solid surface / Liquid surface / Effect area / Weather layers**: the world components. Effect areas are Freelancer-style clouds with priorities (a field within a field).
- **Universal entity standard / Universal Entity Properties**: shared rules for every entity: Mass, Scan Integrity (multiplier 1–5.0x), Pin Strength, Gravity Scalar, Damage System, Material system, Gibs, Collision Effects, IsSolid.
- **Planetary vs Space worlds**: the two core world types. Planetary: flat looping area, entry/exit only at the top, gravity direction, play field altitude, killzone at depth. Space: bounded, no looping, exit at any border, optional gravity source, play area in the middle, lethal directions (sun, anomaly, black hole).
- **Play field / Play area**: the band or region where the action happens.
- **Hard points (HP)**: enemy chassis mounts for weapons, tools or utilities; any HP can mount any system. (Note: "HP" also means health points on S12.)
- **Chassis special features**: cloak, shield, overcharge, etc. **Chassis based AI behaviour**.
- **Size categories**: Normal, Large.
- **Damage types**: Radiation, Fire/Burning (heat), EMP, Kinetic impacts, Cryo.
- **Thresholds**: EMP threshold, armor strength (per shot, vs AP), heat resistance (cumulative), radiation protection threshold, kinetic force threshold (not damage, causes pushback), cryo resistance.
- **AP**: probably armour-piercing (S12).
- **Overkill**: destruction mode where the entity vaporizes in a way that depends on damage type.
- **D.T.**: probably damage texture, the opacity-controlled overlay (S14).
- **D / A hits**: Direct/Contact (projectiles, beams, bolts) and Area/Ambient (explosions, areas, rays) hit effects; each has Resisted and Unresisted states.
- **LR sensor**: long-range sensor (S13). **Action field**: a 100 × 100 × 100 box of play. **Envirotype**: environment type that affects sensor efficiency.
- **Ufopedia**: the Database is described as "Ufopedia of sorts" (the X-COM encyclopedia).
- **Prototype 1**: a barebones playable release with only the mothership, focused on the world and entity systems and modular code.
- **Enemy groups**: factions that threaten mankind and are never fully eliminated; some seek RUs, human samples or tech.

## Open questions

- S1: Is "CREATE" under the CHAR EDIT mockup the screen's other name or the button/action that leads there? What does "(enforced)" above "max char" mean exactly, an enforced character limit?
- S2: What is the "secondary border" (in both space and planet maps)? Does the "15°" box under "0 → 360°" mean the angle step?
- S3: Two of the key letters in the overlay sketch (after X) are unreadable (E? C?).
- S6: The renumbered screen order has overwritten digits; which numbers do the Metagame-level Tactics and Pause get (10 and 11?), and what was the old number of Quit confirm? What are the HSV values 220 / 100 / 60 for (a UI theme colour?)
- S8: What do the hatched blobs and the large hatched shape on the right of "Space level v2" stand for? What was under the blurred areas (if it matters)?
- S9: What do the numbers 1, 2, 3 on the Planetary trapezoid sketch mean (entry paths? layers?)
- S10: What does "(later adv) maybe" mean on "Damage is universal": advanced damage types added later?
- S12: In "Deflect or reduce effect if not AP enough", is "not" struck out? Is "AP" armour-piercing?
- S13: What do the 0m / 80m / 125m / 576m labels on the tactics screen measure (altitude, distance)? What was the crossed-out cylinder sketch meant to show?
- S16: What is the "KATSUYA EGUCHI" note about (a reference or reminder unrelated to the table)?
- S17: The side note under "scan time" reads "cumulative - Per…"; percentage?
- S18: Where is the "CONT →" continuation of Enemy Groups (presumably a later scan in this folder)?
