# RoomSpace: rooms, doors, camera and backgrounds

The single room as a play space: its scale and size, walls, how characters and objects pass between rooms, how rooms connect, the camera, and how the background shows the world outside. Notebook 1 (scans 211–241) designs the room as a level; notebook 2 (261–282) redefines it as the "interior" of a universe node and settles the background system. Numbers in brackets are scan numbers; full wording in `transcript/`. *(interpretation)* marks Claude's reading; **Proposal** sections are Claude's suggestions.

## Scale

- **1 m = 40 px; 3 m = 120 px** (213, 215, 274). A **unit** (u) is 3 m, the size of one wall segment and one atmo cell.
- Placement grid inside a room: ½ m (213). Terrain objects run 3 m, 2 m, 1 m and ½ m.
- Zoom: 25% (ultra min) to 600% (max), 100% default; a compact option is 50–400% (213, 215, 281).
- Supported aspect ratios 4:3, 5:4, 16:9. Phones get a 2–5× smaller arena relative to their resolution, with a closer default zoom (213).

## Room size

**Notebook 1: rooms as arenas.** Minimum size depends on how many characters must fit and how big they are; maximum size depends on the device resolution (213, 218, 219).

Minimum room per character count (218), in metres:

| Characters | Humans (1×2 m) | Max-size chars (3×3 m) | "Longbig wielders" (5×5) |
|---|---|---|---|
| 2 | 3×3 | 3×9 | 12×6 |
| 4 | 3×6 | 6×9 | 12×12 |
| 8 | – | 12×9 or 15×6 | 12×24 |
| 12 | 6×6 | 15×9 | – |
| 16 | 6×9 | 15×12 | 24×24 |

Maximum room by resolution (213, 214, 218), with one cell lost to the border: 800×600 → 20×15 m, 640×480 → 16×12 m, 320×240 → 8×6 m, 1024×768 → 25.6×19.2 m. The smallest room is 3×3 m (fits 2 people).

**Notebook 2: core rooms 2.0** (269, 270). A core room is **3×3 to 10×10 units** (9×9 m to 30×30 m) and must fit **4 exits** (one per side) and **one docked DRC** (shown in the background on decorative, non-interactable struts). Its size and shape come from the node: dense surrounding matter makes it small, open space makes it big, and vertical or horizontal pressure makes it tall or wide (270). A room is "100 m² symbolically, 30 m² actually" (270): it stands for a much larger place (see `universe.md`). Control command systems can resize the home room (278). This version supersedes the resolution-based limits.

## Walls

**Border types** (211, 217, 218):

- **Type A**: walls of 3 m segments with corner caps; Metroid-style doors are 3 m segments that can be combined.
- **Type B**: an inner wall of 1×1 tiles inside a single solid outer frame (seamless texture), with vents and dispensers built into the tiles.
- **Type C**: a single collider border with exclusion zones.
- Room shapes: rectangles (regular, long, tall, large, shaft, thin, tunnel), freely sized within min/max. Advanced: irregular polygons, no angles under 45°, diagonal walls may be trouble. Wall thickness from thin (outdoors) to thick (indoors), drawn as tiled segments or one stretched piece with corner caps and L/T welds, using a tiling texture plus tint mask.

**Wall anatomy, notebook 2** (248, 265, 266). Walls are 3 m panels with inert corner caps. Each segment is separate and unique, and its type, colour, texture, venting and doors depend on what lies in that direction. Every wall segment and door constantly cycles air between the room interior and the surrounding atmo; insulation per segment can boost, reduce or stop it (details in `environment.md`). The flow is shown on the wall as overlaid lines whose count, thickness, opacity, colour and pattern show the amount, type and state of matter (solid straight, liquid wavy, gas zigzag, plasma broken) (266, 276).

**Damage reactivity** (211). A wall hit hard glows brightly; cumulative damage desaturates and darkens it. Past its limit (e.g. 1001/1000) a **Border Glitch Anomaly** breaks out: data errors, mutations, destruction and creation, random forces, spawned items, characters or terrain, kills, heals, resurrections. Then the wall self-seals and returns to a stable but weaker state. Room walls and doors themselves are indestructible (RoomSpace.txt); the anomaly is the consequence instead.

## Level generation rules (notebook 1)

"Fundamental points" (217, 219), for generating a room as a level:

- 2 to 16 characters per room; characters 1×1 m to 3×3 m.
- The biggest character's longest side is the minimum passage width, between doors and between every character. Opponents must be at least 1 m apart, with an open path (direct or curved; gravity is fine).
- Door size is limited by the room's shortest side; wider openings use double or composite doors.
- Characters count as free movement space. Everything aligns to the grid; nothing overlaps (except items). Characters are placed first; terrain, items and objects only after, in leftover non-passage space.
- Backgrounds, gravity, environment, lighting and terrain must fit the room's place in the greater world.
- The metagame may override any of these (room limits, door types, passage widths, distances, terrain frequency).

## Doors and transitions

**Door and exit types** (220, 224, 225):

- **Metroid door**: shoot or open it, walk in. Time freezes during transit; the transition is instant, a fade, a Metroid-style tween, a loading screen with hints, or a world map / location card. You come out in front of the door with the same pose, the door already closing, then time resumes.
- **Space Chunks warp exit**: when the room is "condition green", pick an available direction and press E + direction to warp; arrive at the new room's entry point, destroying obstructions ("POOF"). Type A is player-controlled (a "freelancer cruise engine"), type B only when the room allows. Open variables: keep momentum, charge time, warp leaving a shockwave in the old room. An alternative: a MechWarrior 3 style exit.
- **Mario background door**: a door in the background; press E to open (type B, always usable) or an automatic proximity portal (type A).
- **Touch-surface door**: grab the door and press E, press E again to confirm. Variables: the door might launch you or apply effects.

**Ways to open a door** (238): button or keycard, a trigger in the background, a grab handle (hold E), break it (e.g. with a rocket), hack or force it, a condition sensor.

**Clear passage** (220). Exits and entries must stay free of obstructions; level generation weighs room size, passage size, player strength, terrain placement and destructibility, and events like earthquakes so doors can't clog.

**Packing** (222, 223, 241). Doors only admit **packed** characters. To standardize transits, every character with all its equipment must fit in **3×3 m**. Packing folds the character in a fraction of a second (2–4 frames, or instantly): items and hands on top, feet and inventory below, centred and tight. Loose objects, items and terrain can't pass through a door on their own; they only travel carried by a packed character. A closed door is a solid wall (with locked, barred, welded or filled sub-states). Characters always start packed in a newly loaded room.

**Auto Pack Zone and commit line** (238, 239, 241). Each door has an auto pack zone (APZ): touching it (with any body part or held item) packs the character automatically. Inside the zone is a **commit line**: once the character's centre of mass crosses it, they're committed. Before that, the player can back off and unpack. After it, the character is auto-moved through, desaturated and invulnerable, with collisions and stats off and rotation preserved; on arrival collisions and stats switch back on ("ALL GREEN"). Door colliders come in wall, corner and universal variants.

**Door designs compared** (239):

| Design | For | Against |
|---|---|---|
| 1× Metroid door | effortless entry | loses momentum, awkward state fiddling |
| 1× contact surface door | simple, no state fiddling | loses momentum, needs hold + E, must stop, awkward invulnerable tween |
| Auto-packing door | no object interference, 1× walls possible, 3×3 characters enter easily, keeps momentum and rotation | needs packing |
| 3× "fat" Metroid door | keeps momentum room to room; zone 1 packs (can back out), zone 2 admits only packed characters | walls must be 3× thick |

Per-door options (223): packing automatic or player-activated; whether body parts stay vulnerable and poking-out items stay shootable during the pack; all attacks, including dash, disabled while packed. (222 says stats and collisions go off at commit; 223 makes vulnerability a per-door option.) Inventory items are unshootable (262).

**Reverse doors** (240). Non-exit compartments in the walls or ceiling that push content into the room: items, objects, liquids and gases, loose terrain, or characters (a ceiling hatch dropping spiders). Because of equivalent exchange, the matter has to come from somewhere, and the room has to reserve free space for it.

**Object transfer between rooms** (221), for open-world metagames where rooms persist. A room, object, item, character or event might offer to send things that aren't held or carried to another room. Only questions were written: volume and size limits, queues, one- or two-way links, sending to a full room, speed, charge-up, fuel cost by size, equivalent exchange (swap something back?), forcing characters into transfer, choosing the destination.

**Out-of-bounds protocol** (237), run by the Glitch-Chaos system for anything that ends up outside a wall: 1. push it back; 2. teleport it to a free spot; 3. shove things aside to make room, then teleport it; 4. delete it and turn its matter into a glitch blast (area damage) at the target spot, so the matter isn't lost. The same system resolves anything stuck in a door (222).

## How rooms connect

**Directions** (267). Rooms connect only north, south, east and west; diagonals are crossed out. A long room can have its west entry and north exit far apart.

**Exit consistency** (248). The cell you leave from and the cell you arrive in must match: air to air, water to water. A water room can't open onto dry ground on the other side.

**Room types** (249): **area proper** (one biome), **transition exits** (up to 4 biomes, the "exit" rooms between biomes such as atmosphere exit, underground exit, sea exit), **multi-transit**, **stand-alones** (buildings, connectable to other stand-alones), and **transition airlock rooms**. A sample descent: asteroid → space → atmosphere → surface → underground → underground water reservoir → undersea.

**Layout styles** (242): **Tetris** (rooms of different sizes packed edge to edge) or **Tunnels** (separate rooms joined by door links). Notebook 2's node grid follows the tunnels idea: each room sits in its own node.

**Linking distant rooms** (262): a separate elevator room that shuttles between two places; omitting the rooms in between so A's door leads straight to B; or a **background tunnel** (any room of at least 3×3, no rooms omitted), a portal in the background leading to a matching one far away.

**Rooms are semi-symbolic** (266). A room interior is a small point of interest, the remarkable core of an area, inside a vast room atmosphere. Doors between rooms are airlocked, and the "true" distance between two rooms may be huge, so interiors don't bleed into each other; their atmospheres do (see `environment.md`). Each room centres on a "remarkable point of interest", with exit wormhole gates or a void glitch border around it (261).

## Camera

From the notes (177, 178, 215, 281):

- **Centred on the character** (stable) or **centred toward the cursor** (vision); the cursor has a maximum range from the character.
- Pan with RMB held: 50% or 100% toward the screen edge; without RMB the camera stays centred. A deadzone scheme was tested: inner circle no pan, middle slow, outer fast.
- Zoom with the wheel, 25–600% (or 50–400%); the cursor keeps its relative screen position while zooming.
- With no character present, the camera moves freely inside the room walls.
- Pause (ESC) freezes the camera and turns the crosshair into a pointer, leaving a ghost cursor so you don't misaim on resume.
- Clamping options: none, clamped to walls, to a deadzone, or to the character's view range.
- **Screen space** (215): type A, the room floats on a free canvas filled with black, a theme, ornaments or the node's dominant material texture; type B, the room fills the screen with letterbox or pillarbox bars in the same fill.

The three early pan descriptions (175, 177, 178) differ slightly; scan 281's option list is the latest.

## Backgrounds

**Three layers** (266): the **foreground** (the active room); the **near background**, tiled at 3 m, 1 m or as one piece, onto which terrain can be pinned (the "BG pin wall", which also blocks atmo and parallax, 212); and the **far background**, a gradient vertex-coloured from the four neighbouring nodes (north, west, east, south).

**The box room** (273, 279, 280, 282, the final version). The background is drawn as the inside of a box seen in perspective: the **back wall** is the node's own background ("core's BG"), and the four sloping **side panels** show the atmosphere of the four adjacent nodes ("side BG"). The bigger the room, the more side BG shows; in a small room the core's BG is kept first. The back wall carries the node's MDRC dock slots and its status; the side panels show **pips** for the MDRCs docked in neighbouring nodes. Two styles were drafted: A, a repeating texture on the side panels with a pulsing screen edge; B, gradients on the side panels (coloured by the neighbouring nodes) and texture on the back wall.

**Layer stack** (280): gradient + seamless repeating texture + ambient light + parallax fronts and objects.

- **Gradient system**: dark-to-light toward the centre for open areas, light-to-dark for excavated areas. Values stay within **40–60%** of the range. Built with shaders. Room size affects the inner tone.
- **Texture**: seamless, tinted, with a narrow saturation range.
- **Ambient light**: tints and raises contrast and saturation (20–80%), affecting everything in the room including filters.
- **Parallax** (279): static fronts (clouds, rock fronts, cliff faces) and free-moving entities, shaped by gravity, used sparingly, never hiding MDRCs or pips; garish perspectives and warp distortion allowed.

**Background opacity** (270) depends on what the node is filled with: vacuum 100% visible, gas or liquid 0–99%, solid and plasma/magma 0%. It also sets the horizon view distance, and thick backgrounds can hide a docked DRC/MDRC.

**Beyond the wall** (282). The same display in core rooms and DRC subrooms. Outside the room's walls, the camera sees a zone split into N/S/W/E segments that extends without end, filled with the node's dominant atmo/material texture (hinting at whether it's solid or excavated). At the edges of the deadzone, the neighbouring nodes' atmospheres wash in "like beach shoreline waves" with variable opacity, colour and pattern, and the DRC/MDRC pips sit there too.

The 2018 mock-ups in `C:\08 Projects\Project_RoomSpace\RoomSpace Core\` (not in the repo) show this gradient system: a 40–60% value gradient under a tinted repeating texture on a 3×3 grid of 120 px tiles, with the gradient stretching for wide rooms while the texture scale stays fixed.

## Proposals for open questions

Claude's suggestions, offered for topics Reactorcore titled but left empty or undecided.

- **Proposal, door choice.** Make the auto-packing door (APZ + commit line, 1× walls) the universal standard, since it solved every con of the others and is the one the flow chart (241) develops. Keep the warp exit and background door as special room functions (fast travel, buildings), and the touch-surface door for locked or story doors.
- **Proposal, special packing details** (title-only strip, 243). Packing keeps an "unpack pose" snapshot so the character unfolds exactly as it went in; held items that can't fit the 3×3 box (a 10 m beam) are carried as a separate packed bundle that follows the character through the door and counts against the room's object budget on arrival; characters carrying something larger than one door's width need a double door or must cut the object first.
- **Proposal, object transfer.** Make transfers a room function bought with matter: a "transfer hatch" (a reverse door in reverse) accepts objects up to 3×3 m, consumes energy proportional to mass, and only sends to rooms already connected through doors. The receiving room must have reserved free space (as with reverse doors); if it doesn't, the item waits in a queue in the sending room. This keeps equivalent exchange and avoids instant teleport-inventories.
- **Proposal, fast travel.** Use the existing pieces rather than a menu: background tunnels between discovered rooms, MDRC transit for long distances (your mobile base is the fast travel), and warp exits as rare room features. Each costs time or fuel, which preserves the sense of a real universe.
- **Proposal, lighting via walls and objects** (title only, 255). Every room has an ambient light value from its node (bright in open sky, dark underground); walls and terrain can carry emissive coverings (glowing moss, lava seams, rad glow) that add local light; and light-emitting items or visitors cast simple radial lights. Light level then feeds the background's contrast/saturation as scan 280 describes.
- **Proposal, doors as vents, lamps and projectors** (title only, 255). Since every door already cycles atmo, a door could double as a vent (push or pull atmo when open, or when set to venting while closed), a lamp (its frame lights the room in the colour of the neighbouring node's atmo, telling the player what's beyond) and a projector (it shows a live thumbnail of the room behind it). The lamp version doubles as navigation information.
- **Proposal, room load speed / preloading** (title only, 261). Only the current room is simulated; preload the four neighbours' saved state (not their simulation) in the background, so door transits stay inside the 2–4 frame pack time. The door transit animation and the frozen time already hide any remaining load.
