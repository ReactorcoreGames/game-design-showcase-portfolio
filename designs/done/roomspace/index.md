# RoomSpace: design digest

This folder is the text form of RoomSpace's design, transcribed from 108 scanned notebook pages (`C:\08 Projects\Project_RoomSpace\Scan_RoomSpace\Image (174).jpg` to `Image (282).jpg`; there is no 198) plus the condensed overview and two text files. Read this instead of the scans. The process is in `workflow/scan-digest.md`. The sibling folder `Foto_RoomSpace/` (220 photos of the same pages) was not used.

## Summary

RoomSpace is a persistent 2D side-view universe made of thousands of terrarium-like rooms. Each room is a diorama with its own local climate (gravity, atmosphere, liquids, gases, temperature, radiation, materials), and neighbouring rooms influence each other. Everyone in it is a floppy physics ragdoll that can fly and resist gravity "like fish in an aquarium", grabbing, throwing and fighting with anything. Rooms connect through Metroid-style doors that characters fold up to pass through. Rooms add up to planets ("cup worlds" that descend to a core), space regions, galaxies and a universe, all generated top-down by heuristics from distributing matter, never from biome templates. Matter is conserved. Only the current room is simulated; the rest are dormant files that a background thread updates. Buildings, caves and ships are District Room Complexes, and ships and mobile bases (MDRCs) move node to node across the universe, the "mobile headquarters mothership" Reactorcore always wanted. On top of that sits an infinite campaign generator that tells a new story in the same persistent universe every time.

It started from Floppy Heroes (a small ragdoll gladiator game) and is planned to start small as a ragdoll combat game, with the framework laid out so it can grow.

## How the design evolved

The scans come from two notebooks titled "C2 DEV PROJECT" ("C2" is Construct 2, the engine Reactorcore first planned to use; no longer relevant. The game would now be a portable Windows installation whose content folders hold mods and save files in the same place), plus a small spiral notepad in between. **Later scans supersede earlier ones where they conflict.**

1. **Notebook 1** (scans 175–215): the ragdoll game. Controls, movement, limbs, grabbing, the damage model, items, AI, vehicles, visitor objects, the chaos system, terrain pieces and performance budgets. A room here is a level sized to the screen resolution.
2. **Notepad** (217–258): rooms and doors. Room sizes, door types, packing for door transits, the out-of-bounds protocol, the first atmo models, room types and the first cup world sketches.
3. **Notebook 2** (261–282): the universe. Nodes, the interior-versus-atmosphere model, materials, Terrain Material Containers, DRCs and MDRCs, the box-room background, generation heuristics. A room is now the "semi-symbolic" interior of a universe node, 3×3 to 10×10 units.

Where they conflict, the topic files state the later version and note the earlier one.

## Files

| File | Covers |
|---|---|
| [characters.md](characters.md) | The ragdoll body and limb types, movement (gravity drive, dash, grounded ragdolls, mirror turn), controls, grabbing/throwing/storing, emergency head, healing, clothing and armor, AI |
| [combat-and-items.md](combat-and-items.md) | Damage model (HP/IL/JS, CKP, impulse and pull stress, blades, temperature), item anatomy, ammo, fire modes, power and volatility, melee, radial menu, visitor objects, gibs, collisions, vehicles, chaos system, performance budget |
| [rooms.md](rooms.md) | Scale, room sizes, walls, level generation rules, doors and packing, how rooms connect, camera, the background system |
| [environment.md](environment.md) | Equivalent exchange, the three atmo models, liquids/gases/blobs, quakes and sound, materials, terrain objects and Terrain Material Containers |
| [universe.md](universe.md) | Nodes and the universe hierarchy, cup worlds and cores, generation heuristics (with the RTF notes), DRCs, MDRCs |
| [metagame.md](metagame.md) | Purpose, starting small, Spirit Mode, campaign/mode ideas, dialogue choices, business and community |
| [transcript/](transcript/) | Scan-by-scan transcripts in 8 chunks, with all text and diagrams described; the source for everything above |
| `RoomSpace.txt` | Reactorcore's condensed overview (the long pitch text), kept as is |

Each topic file ends with **Proposals**: Claude's suggestions for topics Reactorcore titled but never filled in, or left undecided. Reactorcore authorized this, for details that felt unimportant at the time or depended on the tech stack. They're clearly separated from the design itself.

## Glossary

- **Node**: one cell of the universe grid (about 100 km³), with one core room, its atmosphere and a matter reserve. Also a **district**.
- **Core room**: a node's playable room, 3×3 to 10×10 units, with 4 exits and one docked DRC.
- **Unit (u)**: 3 m = 120 px (1 m = 40 px). One wall segment, one atmo cell.
- **Room interior / room atmo**: the small playable room versus the vast atmosphere of its node; they exchange through walls (the **vent cycle**) unless insulated.
- **Cup world**: a planet in side view, a cup of rooms from orbit down to a core. **Aether**: an inverted, negative-mass cup world. **Pocket cup world**: a core sunk into space.
- **Core** (planet): the bottom of a cup world, with properties (polarity, mass, gravity) that shape the planet. **Core** (character): the torso, which runs the limbs and stores items.
- **DRC**: District Room Complex, a 16-room grid of subrooms in a node (buildings, caves, fortresses); the node's "spine". **MDRC**: Mobile DRC (ships, mobile bases). **MicV**: micro vehicle. **Rooted/unrooted**: subrooms tied to the node or converted for travel. **Spineless**: a node whose DRC launched.
- **Dock point**: one of 4 corner slots per core room for MDRCs; 5 at a node is a **blockade**. **Pips**: background markers of neighbours' MDRCs. **Entry buoy / tether**: connector from a room to an MDRC.
- **TMC**: Terrain Material Container, a chunk of mostly solid terrain (3×3 down to 1×1) that cuts along the grid or fractures into **blobs**. **Nugget**: notebook 1's ½ m loose terrain sphere.
- **Equivalent exchange**: conservation of matter.
- **Manipulator**: a hand, claw or grabber. **Sensor unit**: the head. **Mounted item**: a built-in weapon limb. **Vehicle interface**: a limb for piloting.
- **Gravity drive**: force on the core that lets characters fly. **Dash / Reckless Mode**: boost that weaponizes the body. **Mirror turn**: facing flip where limbs catch up.
- **HP / IL / JS**: hit points, impulse limit, joint strength (also written HP / IFT / JT).
- **CKP**: Charged Kinetic Pressure, intentional blunt damage on contact. **ISD**: Impulse Stress Damage. **Pull stress**: ripping/drag damage. **Gnarlyness**: the damage multiplier.
- **WS**: weaponized surface. **A/C/R + LM**: ammo, capacitor, reactor, launch mechanism. **Volatility**: stored, dangerous power in an item. **Safety rating**: containment that trades power for safety.
- **Visitor object**: anything temporarily spawned (projectiles, beams, fields, effects); **gibs** are reduced visitors.
- **Chaos (Intervention) system / Glitch-Chaos system**: the performance guard that simplifies, delays or erases things under load and resolves stuck or out-of-bounds objects. **Chaos Curse**: an item rating that makes heavy items glitch under load. **Border Glitch Anomaly**: what happens when a wall is overloaded.
- **Packing / packed**: folding a character and everything it holds into 3×3 m to pass a door. **APZ**: auto pack zone. **Commit line**: the point of no return in a door.
- **Reverse door**: a wall compartment that releases content into a room.
- **Nullware**: the top weapon tier, the only thing that can erase an MDRC. **Armageddon device**: a node-sized nullware weapon.
- **Spirit Mode**: possessing ragdoll bodies; **HoF**: its hall of fame.

## Main conflicts and how the digest reads them

- **Room size**: notebook 1 ties it to screen resolution (max 20×15 m at 800×600); notebook 2's core rooms 2.0 (3×3 to 10×10 units) supersede it.
- **Character size**: "max 3×3 m" is the packed size for doors; unpacked characters and their items can be bigger (5×5 class, 10 m with long items).
- **Atmo**: grid, single-cell and node models; notebook 2's node model (interior vs atmo, wall/BG/seep flows) is the latest.
- **Doors**: four door designs compared; the auto-packing door with APZ and commit line is the most developed. Warp key: "press E + direction" (225) over "Shift+W" (220).
- **Packed transit**: stats and collisions off at commit (222, 241); vulnerability during packing as a per-door option (223).
- **MDRC movement**: grid steps between neighbours (274) over free 8-direction movement (273).
- **Critical density**: transmutes and collapses into a star/black hole/singularity (277) over "breaks down and explodes" (275).
- **Universe size**: 131,072 rooms (265), decided by Reactorcore (2026-10-22) on Claude's proposal in `universe.md`; larger totals (268) stay possible later.
- Undecided in the notes: storing scheme, ammo refill, healing split, armor implementation. The topic files list the options and a proposal.

## Source table

| Scan | Title (as written) | Content | Goes into |
|---|---|---|---|
| 174 | — | Cover of notebook 1, "C2 DEV PROJECT" | — |
| 175 | Keys | Controls, wall-boost dash | characters |
| 176 | Hand/Torso Movement | Master topic list; gravity drive, manipulators | characters |
| 177 | Limb angle constraints / Camera Behaviour / One-handed flipping | Constraints, camera basics, item flips, multi-hand MW4 groups | characters, rooms |
| 178 | Player Camera & AI vision / Letting Go | Zoom/pan, AI vision; drop, toss, charged throw | characters, rooms |
| 179 | Grabbing | Slipperiness, ripping, crushing | characters |
| 180 | Non-Human Characters / Grounded ragdolls / Limb Types | Creature classes and perf scores, slumping, the six limb types | characters |
| 181 | Credits to music artists / Emotions/AI | Credits page; needs, feelings, actions | metagame, characters |
| 182 | Charged Kinetic Pressure | HP/IL/JS, damage types, CKP | combat-and-items |
| 183 | Anatomy of Items | Item components, object types, emission parameters | combat-and-items |
| 184 | Blades | Blade impact sequence, blade properties | combat-and-items |
| 185 | Character Components & Structure | Core/limbs, status, decap/gib, head = AI | characters |
| 186 | Mirror Turn | Facing flip | characters |
| 187 | Impulse Stress Damage | ISD | combat-and-items |
| 188 | Advanced Temperature / Object Properties | Temperature bands, properties, object shaders | combat-and-items |
| 189 | Storing objects in core | Storing rules and schemes, 3-set switching | characters |
| 190 | AI Flags / Threat assessment | Flags, opinions | characters |
| 191 | Body possession angry spirit metagame | Purpose/needs, Spirit Mode, 3 variants | metagame |
| 192 | Potential Metagame Ideas | Business notes, Strong Opinion Ragdolls, nemesis NPCs | metagame |
| 193 | Collision Layering | Layers, isCollisionsCleared | combat-and-items |
| 194 | No-manipulator combat & emergency head | Advanced AI, judgement, mouth as hand | characters |
| 195 | Crates / Sprite states for usable items | Storage objects, effects as visitors, "make memories", vehicle topics | combat-and-items, metagame |
| 196 | Ammo reserves / Health/Limb Repair | Ammo and refill, healing items | combat-and-items, characters |
| 197 | Observation Methods / Inflicting self-damage | Attack tags, broadcasting, recoil | characters, combat-and-items |
| 199 | Cannibal feature for healing self | Eating limbs, food reserve regen | characters |
| 200 | Clothing/Armor/Covering | Packages, 4 sectors, armor stats and implementation | characters |
| 201 | Naked combat/Damage reduction | Dash damage examples | combat-and-items |
| 202 | Visitor objects | Types, properties, damage modes, deployables | combat-and-items |
| 203 | Gib/Effect Types / Chaos Intervention System | Gibs, settling sketch, chaos functions, Chaos Curse | combat-and-items |
| 204 | More AI Logic Systems | Awareness, nav nodes, global lists, gib properties | characters, combat-and-items |
| 205 | More metagame ideas | Heat, trigger states; 14 campaign concepts | combat-and-items, metagame |
| 206 | Usable Item Anatomy/Systems | Fire modes, item taxonomy, packed/unpacked anatomy | combat-and-items |
| 207 | Usable Item Power, Recoil, Volatility, Safety | Power chain, volatility, A/C/R units | combat-and-items |
| 208 | Weaponized Surfaces | WS rules, melee catalogue, balancing, Gnarlyness | combat-and-items |
| 209 | Radial Context Menu | Use cases, radial menu, stats panel | combat-and-items |
| 210 | Vehicles/Mounts | Rules, use cases, entry types, stationary devices | combat-and-items |
| 211 | Terrain System Overview | Borders, glitch anomaly, terrain components | rooms, environment |
| 212 | Terrain Objects | Topic list, generic and decorative terrain objects | environment |
| 213 | Border Standardization | Grid, sizes, zoom, resolution-based room size | rooms |
| 214 | Perf-Budget | Visitor rates, budget, worst case | combat-and-items |
| 215 | Camera Screen Space / Game Content Pricing | Units, camera types, release tiers | rooms, metagame |
| 216 | — | Cover of the spiral notepad | — |
| 217 | Terrain System Basics | Door size, border types A/B, level gen factors | rooms |
| 218 | Type C / Data collection | Min/max room size tables | rooms |
| 219 | Fundamental Points | Level gen rules | rooms |
| 220 | Door/Exit Types | Four door types, obstructions | rooms |
| 221 | Object Transfer Between Rooms | Questions only | rooms |
| 222 | Object/Item/Loose Terrain Interactions w/ Doors | Door states, packed-only entry | rooms |
| 223 | Room Transition: Packing & Unpacking | 3×3 m packing | rooms |
| 224 | Touch-surface door / Mario BG Door | Transition steps | rooms |
| 225 | Player Room-to-Room Transitions | Metroid door, warp exit | rooms |
| 226 | Terrain/Objects/Items Limit/Budget | **Title only** | environment (proposal) |
| 227 | (Close) BG Pin Wall (atmo blocking, parallax blocker, view) | **Title only** | rooms |
| 228 | Terrain Destruction / Loose terrain properties/behaviour | **Title only** (later covered by TMC, 275–277) | environment |
| 229 | (Panning) Camera/Zoom Defaults/Limits | **Title only** (later covered on 281) | rooms |
| 230 | Tergen Process Heuristics | **Title only** | environment (proposal) |
| 231 | Role of the Far Background (far vision, parallax, mood setting) | **Title only** (later covered on 266, 280, 282) | rooms |
| 232 | Atmospheres/Air/Weather/Events | **Title only** | environment (proposal) |
| 233 | Blob System Questions / Gas/Liquid design factors | Questions and factors | environment |
| 234 | Liquids & Gases | **Title only** | environment (proposal) |
| 235 | Filtration of Rooms (Border Vents) | **Title only** | environment (proposal) |
| 236 | Equivalent Exchange (refill via doors, visible on far background vision) | **Title only** | environment |
| 237 | Accidental Out-of-Bounds Protocol | Four-step resolution | rooms |
| 238 | (door opening methods / types) | Opening methods, APZ, commit line | rooms |
| 239 | Metroid doors revisited | Door designs compared | rooms |
| 240 | Reverse Doors (Equivalent Exchange) | Spawner compartments | rooms |
| 241 | Long Object Metroid Door Transition | Autopack flow chart | rooms |
| 242 | (fast travel / Tetris vs Tunnels) | Topic list, layout styles | rooms, environment |
| 243 | Special Packing Details (related to pack/unpack) | **Title only** | rooms (proposal) |
| 244 | Planetary Mapping of Rooms / Single-Cell Room Atmo | Looping surface, gas balls | universe, environment |
| 245 | Grid-based Room Atmo System | Cell contents and factors | environment |
| 246 | Cell Atmo Dynamics & Visitor Interaction | Vents, diffusion, wall absorption | environment |
| 247 | Single-Cell Room Atmo/Global Atmo | Global atmo, micro/macro nodes | environment |
| 248 | Room Exit Consistency / Room Anatomy | Matching exits, wall setup | rooms |
| 249 | Room Based Overworld, Metadata | Descent path, room types | rooms, universe |
| 250 | (space contents / cup world topics) | Lists | universe |
| 251 | (cup world anatomy / core types) | Anatomy diagram, cores | universe |
| 252 | (planet node graph / cup world shapes) | Shapes, Earth/Aether | universe |
| 253 | (world shapes / Planetary Orientation, crossed out) | Pizza, cocoon, pocket worlds | universe |
| 254 | Spheres of enviro influence | Influence levels, planet layers | universe, environment |
| 255 | Lighting via walls/objects / Doors as vents/lamps/projectors | **Titles only** | rooms (proposals) |
| 256 | Player choices in narrative games | 8 choice types | metagame |
| 257 | Nothing = 3 options / to-do | Polite/indifferent/hostile; to-do list. Also a sidetrack note ("GRR") and two number strings, left out as possibly personal | metagame |
| 258 | Doom Projects / The Design Process | **Sidetrack**: other projects, a business note, a design-process sketch | — |
| 259 | — | **Duplicate**: a photo collage of the stickies on 261/262 | — |
| 260 | — | Cover of notebook 2, "C2 DEV PROJECT Part 2" | — |
| 261 | Universe Structure / Room load speed | Hierarchy sketch, main/wild, point of interest; load speed **title only** | universe, rooms |
| 262 | (task list / clamps / shockwaves / connection methods) | Corrupt chars, clamps, quakes, elevator/omit/BG tunnel | characters, environment, rooms |
| 263 | Material types / Material Attributes | Materials | environment |
| 264 | (buildings / HVAC / Quakes / district tiles) | Building list, ventilation model, quakes, district tiles | universe, environment |
| 265 | Universe, World Overall Structure | Hierarchy (131,072 rooms), adjacent atmo, interior vs atmo | universe, environment |
| 266 | Rooms are semi-symbolic / wall vent / BG layers | Semi-symbolic rooms, wall flow display, 3 BG layers | rooms, environment |
| 267 | (generation / exit directions / local space / Buildings) | Fixed entry and core, N/S/E/W only, building types | universe, rooms |
| 268 | (size math / Mobile District Tether / wrap) | Universe totals, tethers, no wrap. Also a sidetrack note (two unrelated game ideas) | universe |
| 269 | DRCs / core room states / Mobile DRC / Core Rooms 2.0 | DRC definition and cap, MDRC, core room size | universe, rooms |
| 270 | Tethers/Anchors / BG Opacity / Core Room size / Room-DRC-Node-Sector size | Buoys, opacity, scale ladder | universe, rooms |
| 271 | DRC (District Room Complex) | Definition, adjacent paths, entry placement, spine | universe |
| 272 | MDRC Launch Procedure / editing / destruction / Grade Mounted Superweapons | **Titles only** | universe (proposals) |
| 273 | (BG node status / MDRC movement / obstacles / connectors) | MDRC slots, movement options, blockades, cables and buoys | universe, rooms |
| 274 | (MDRC in BG / movement / access / Docking points) | Point-to-point movement, docks | universe |
| 275 | MDRC Propulsion / First Wave Materials / TMC / density | Propulsion, materials, TMC basics | universe, environment |
| 276 | TMC coverings / Room HVAC wall representation / TMC splitting | Frostings, wall flow display, splitting, performance | environment, rooms |
| 277 | TMC creation / merging / Critical Density / rooting | TMC lifecycle, rooting | environment, universe |
| 278 | Flow of atmo / Excavation / Control command systems / Nullware | Atmo channels, slit excavation, consoles, nullware | environment, universe |
| 279 | Damaging an MDRC / Core-to-MDRC weapons / parallax / side BG | Sterilization, SAM systems, parallax, box room | universe, rooms |
| 280 | Type A / Type B / BG layer stack / Room Gradient BG System | Background system | rooms |
| 281 | (cell sketch) / Camera options / Node atmo circulation / Sound | Camera, node exchange, sound | rooms, environment |
| 282 | Beyond Wall Zone / Universe Generation Heuristics / cup world CORE modifiers | Beyond-wall display, generation steps; core modifiers **title only** | rooms, universe |

## Other sources

- `RoomSpace.txt`: the condensed overview, in this folder.
- `C:\08 Projects\Project_RoomSpace\UniGenHeuristics.rtf`: universe generation notes by Reactorcore, digested into `universe.md` (Generation heuristics).
- `C:\08 Projects\Project_RoomSpace\FormationCreationOfUniverse.txt`: a transcribed third-party narration about the early universe, kept as inspiration; summarized in `universe.md`, not copied.
- `C:\08 Projects\Project_RoomSpace\RoomSpace Core\`: 2018 image mock-ups of the room background gradient system and 3×3 room tiles (120 px per 3 m); described in `rooms.md` (Backgrounds). Not copied into the repo.
- `Foto_RoomSpace\`: photos of the same notebook pages; not used.

Notes marked *(interpretation)* are Claude's reading of an unclear drawing, not Reactorcore's words. Sections headed **Proposal** are Claude's suggestions.
