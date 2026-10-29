# TopVerse: travel and combat layers

How vehicles and fleets move through the universe and fight there: vertical combat zones, vehicle arenas and their doors, region travel, tunnels, star system movement, FTL and hyperspace, interdiction and the anti-FTL reticle. Sources: `1 TopverseNotesBU2_Cleaned.txt` (todo list, game flow, Hyperspace God Mecha, Fleet Unpack-Pack), `misc relevant/Topverse Combat Defence Structures.txt`, `5 Topverse system layers n mechanics.txt`, scans TN19, TN26–TN28, B6, B7, B11–B16. Scan codes are explained in [index.md](index.md).

## Vertical layers and combat zones

Every place has a stack of vertical layers (the full set per celestial type is in [universe.md](universe.md)). For vehicle combat they are grouped into three **zones** (B15):

| Zone | Layers | Role |
|---|---|---|
| 1 | orbit, upper atmosphere | re-entry; space exit upward |
| 2 | sky, surface, soil/sea | the combat area |
| 3 | bedrock/deep sea, crust, mantle, shell, core | the far depths |

A vehicle arena simulates only the zone 2 layers; leaving upward (high atmo/orbit) or downward (deeps, mantle, core) is an exit (TN28). Cross-layer movement uses the altitude thresholds in [vehicles-and-fleets.md](vehicles-and-fleets.md). Underground and underwater are equivalents: you can travel through soil to adjacent tiles, but digging is slow; diggers and submarines are slower than surface and air fleets, so they should resurface to travel with a land-air fleet (Notes todo). Bedrock can't be crossed to another tile. Fleets on several layers travel together until a layer can't continue; the more a fleet sticks to one layer (amphibious surface fleets, or permanently airborne ones), the easier group travel is. Mantle travel turns the view sideways into a side-scroller (layers txt, B4). Cross-layer combat between icons on the area map plays out as RPG-style active turn attacks (layers txt).

B12 sets the scale of vehicle play: separating it from the area grid, which becomes 4X-style strategy. **Vehicle combat is fleet against fleet, not individual MDRCs**, and battles happen in a generated zone based on the tile, or on a tunnel's start or end, never on the grid map itself. Fleet members exist on any layer of a tile but move together only on the same level: units far away or stuck/lost in deep layers split off; active ones on adjacent layers move as one.

On-foot humans in vehicle mode are ants: generic visuals, no details (Notes todo).

## Vehicle arenas (TN28, B14)

- A **vehicle arena** is a zoomed-out zone of an area tile (TN28 says "10 km² zone"), tall, wide or square. Up to 4 fleets fight at once (TN28 also says 8 vehicles per fleet; see conflicts in [index.md](index.md)).
- Each arena has a designated, customisable **parking space (P)** in the centre, where the local fleet launches from and where vehicles spawn on arrival. Other fleets enter from the sides. Park at the centre to access on-foot missions or perform regional actions (long-range fire, scans).
- Exits are **directional doors** to the adjacent tile: no diagonal travel, a clear path required. Up to **4 doors per side** ("traversal"); terrain decides the minimum and maximum door count, each door can be biome-specific, and each door or slot takes one vehicle of max size. With fewer than 4 doors open, some ships must pack into the flagship to move to the next room as one fleet. A used door is occupied until its vehicle moves on at the other side.
- Doors are **requirement-driven**, like on-foot doors: a door may need a specific propulsion (ground, air, water...), and each layer has its own doors with their own requirements. A ground car that drives into the ocean sinks on the spot (Notes).
- **Leaving through a door**: move onto it and press E. If the vehicle's momentum points within the door's 90° acceptance angle, it keeps that momentum and slides through the border wall; if not, the door denies entry or the autopilot slows, turns and accelerates toward the wall. The passage is a "ghost mode" (path locked, no physics, auto-acceleration), but the vehicle can still be shot until it's gone. Existing speed lets you leave faster and less exposed. Retreat timing scales with momentum and size: slower and heavier means a longer exit delay (TN28).
- Why doors at all (Notes): spawning entities into a room without overlapping colliders, and giving vehicle rooms natural, varied entries where some vehicles don't fit or can't traverse.

## Region travel

- **On the ground or below it**: room by room, through a chain of vehicle arena rooms (B14).
- **In the air or above** (sky, high atmo, orbit): tile by tile on the region map, entering an arena or tunnel only when the situation demands it (B14). Interregional travel is a launch tile arena, a mid-transit tunnel and an endpoint tile arena; direct-control travel only happens when an obstacle forces an event (Notes).
- **Region-to-region entry** (TN26): regions differ in size (10x10 to 25x20 tiles), so an exit tile's position along its edge is turned into a percentage (tile 18 of a 20-tile edge = 90%), and you enter on the opposite edge of the neighbouring region at the tile with the same or nearest percentage.
- **No man's land** (Notes, "tentative idea"): regions are about 20 km apart (two area tiles). Dropping out of a tunnel between regions puts you on one of two temporary in-between tiles, provided by the continent and reflecting the region they face; you can go on or turn back, not sideways.
- Entering a new region, continent or celestial is always an event: its border tile is always accessible, but stepping on it wakes that place into active behaviour (Notes).
- Time passes only when moving between tiles or when acting while parked, waiting included (Notes). Actions on the region layer are "sort of turn-based": there is no end turn; the world reacts after each player action or wait. Reactions can have cooldowns, failure chances, limits or fatigue (an AA launcher against an air fleet wears down).

B6 lists region combat and transit topics still to design: region invader defences, stealthy entry, sensors and guards (borders, mainland), dodging past quickly, fleet transit interdiction, region-to-region travel (airway, tunnel, route), in-region travel, intercontinental transit, space travel, space locations, armed force pools.

## Tunnels

The tunnel is the shared answer to long-distance movement (Notes Hyperspace God Mecha; TN27; B7; B13).

- **What it is**: a temporary scrolling corridor from A to B, with controlled acceleration and some lateral movement, horizontal or vertical only. It exists only while in use. Solo travellers, groups and convoys can open one; enemies can discover it and enter at the start, middle or end to intercept. There's no time limit and no rush inside.
- **In-region tunnels** (TN27): a faster way for a fleet to cross a region, and a long corridor-like combat zone for races, interception, chases and mass-logistics puzzles ("get all vehicles from A to B"). Each segment is one region tile on the route and generates that tile's own terrain; side exits drop you into the adjacent tile; the far end exits to the adjacent region. Region-to-region travel is by single tile, not tunnel. Tunnels can be condensed compared to arenas; if long ones aren't viable, split them (e.g. 20 tiles = 4 sections of max 5 tiles with loading screens).
- **Leaving a tunnel early** deposits you on the grid by distance and thresholds (start, end, or somewhere between); a failed transit drops you near the start or the end depending on distance covered (B13).
- **The same tunnel** serves water, ground, rail, space, underwater, underground and sky routes (Notes): a transit scene in motion, "like Hill Climb Racing but top-down", that switches to on-foot-level play mid-trip without cancelling it.
- B7 replaced an earlier idea (escape velocity, an "88 mph" exit launch, momentum drive energy, separate sub-FTL and FTL movement) with this "S…E" start-to-end corridor; the earlier idea is crossed out.

**Advanced travel with a drive shaft** (B13): reaching high atmo needs a drive shaft (or equivalent). With one you can warp to any tile in the region, or jump to any tile of an adjacent region, through a tunnel transit sequence. The drive shaft leaves clues of the transit at both ends, which lets others start an interception or a chase of the fleet mid-flight. A lone vehicle counts as a fleet for chases.

## Space and the star system

**Star system movement** (B15). A star system is a grid (standard 11x11). Each space tile is an arena, "outside":

- edge doors to adjacent tiles: a minor timeskip at sublight, near-instant with an FTL drive; flying off the edge without FTL costs a timeskip;
- a centre "parking" equivalent, from which you make an FTL jump or go "inside" the tile;
- the arena's medium: void, gas or debris.

"Inside" a tile with a celestial is its orbit, with doors down to the celestial's area/region tiles and a way back out to open space. "Inside" an empty tile is a deeper spot of local space where star system infrastructure sits (no doors except the centre). Orbit is shown as the celestial's own grid, zooming to an area tile and into its layers (B12).

**Ways to travel** (B15, Notes game flow, Combat Defence Structures txt):

- **Sublight**: tile by tile in the star system. Interstellar is possible but with a hefty timeskip; not recommended, doable with stasis equipment. Sublight fleets can't be targeted by anti-FTL guns (no Z-axis jump), which makes them effectively stealthy; they meet regular arena artillery or fleets instead.
- **FTL**: jump anywhere in the star system except where blocked (an alternative note: horizontal or vertical lines only). You can't leave within a 1x1/3x3/5x5 radius of celestials, or enter onto tiles blocked by natural or artificial anti-FTL fields. FTL is instant star to star within a "cloud" (star sector) and tile by tile between clouds; "entire universe is now accessible". On the star sector grid it moves like chess: one tile, or any length horizontally or vertically up to the sector border; crossing to another sector happens from an edge tile, like region-to-region travel.
- **Hyperspace**: use a structure (a hypergate, "better than FTL; think warpgates", Stars in Shadow; B11 also cites "FTL cups", which Reactorcore reads as FTL traffic infrastructure that launches and catches starships at busy places like homeworlds and major colonies) to jump anywhere in the universe instantly, a one-way catapult; maybe a special drive shaft too. Required to enter hyperspace, not to exit it.
- **Infrastructure** (Notes, Combat Defence Structures txt): trade lanes (sublight, in-system), jump gates (in-system, and between adjacent systems of a star sector), natural jump holes (form where a system lacks FTL resources, an emergency exit so matter can't get stuck), galactic catapult/relay (intra-/inter-galactic), chaos quantum warps (one- or two-way anomalies anywhere, including the wilderness), hypergates, orbital elevators, space catapults, parachute-gliders and reusable landers (surface to orbit), trams, trains and hyperrails (surface and subsurface).
- Interstellar travel can meet space weather, monsters, miracles, anomalies and trapped derelicts.

## Interdiction and the anti-FTL reticle

**Cruise mode** (B16) is travel in high atmo, space and hyperspace tunnels. It can be interdicted: disrupting momentum, cruise speed or energy forces both sides into a small, temporary quick-combat space used only after a successful interdiction; from there they can enter a proper arena battle, start a new chase, or settle it on the spot.

**Chaser interdiction** (Combat Defence Structures txt, Notes Fleet Unpack-Pack): when one side escapes an arena in space, high atmo/orbit or FTL (not a hyperjump), the remaining side can fire special anti-escapee weapons at it: damage, kill, disrupt, pull back. It can't pursue directly, because the tunnel is marked in use; only after the escapee arrives can it follow, one tile behind. Interdiction uses a reticle aimed freely on screen to hit the target "from below/above" (the Z axis) with on-board weapons (limited ammo, fired together or toggled on a hotbar). Chaser fire starts accurate, fast and with little delay, and worsens as the escapee gets farther.

**Anti-FTL gun arrays** (Combat Defence Structures txt, B16) defend star systems against FTL travellers, whether the player is the traveller or the defender:

- The **reticle** starts large; each shot rolls a random angle (0–360°) and a random distance (min–max) from the crosshair. Moving the crosshair grows the reticle temporarily; holding still shrinks it to a minimum set by distance. Size also depends on weapon type, distance, fast movement, recoil, and jamming or weather. Each weapon has its own radius limits, effects and impact delay. Non-beam shots appear in the background first and grow in size and sharpness as they near the impact point, so the gunner peppers where the traveller will be, and the traveller dodges a gauntlet.
- Three types (B16): **anti-FTL (direct)** against an invader flying straight at you (accuracy, delay and rate of fire improve as it approaches); **potshot** against a traveller crossing elsewhere in the system (a bad-mediocre-bad curve); **chaser** against an escapee from behind. All available arrays share one reticle; weapons can be disabled per type, and out-of-range ones can't fire. Up to a "triple reticle threat" at once.
- Arrays can **overheat** (no override; it would just blow up), and longer range lowers rate of fire because shots must be launched harder.
- **The traveller's side** (Combat Defence Structures txt, B16): WASD moves within a maneuvering box; accelerate/slow down (speed changes throw off aim, bigger changes juke more); a Star Fox 64-style flip turn (a strong juke that costs distance); countermeasures; point defence against interdiction drones, missiles and warheads; anti-target lance weapons. There is a minimum speed, so no stalling out. The drive shaft's Wipeout-style defensive weapons (wave blast, shield, homing point defence, mines, flares, remote walls) work only in the FTL field.
- **The HUD** (B16): velocity, distance, ETA, current location on a start-to-end track divided into four range bands (the anti-FTL gun's bands counting from the destination, the chaser's from the start), and the FTL medium conditions.
- **The medium** matters: asteroid/solid fields block or weaken shots, hamper tracking, crash drones and missiles, favour energy weapons and lower travellers' max speed; gas fields reduce visibility and accuracy, weaken some weapons (energy bad, ballistic good, unless the gas powers them), make FTL easier to detect, but feed the traveller's plasma lance as an extra buffer. Cataclysms can create or remove fields and flip the advantage. Weather: storms, wind, bursts.
- **Detection** is separate: sensor arrays at every scale (galaxy to local tile) report an incoming FTL traveller; accuracy is the guns' problem. **High-atmo/orbital defences** are a cheaper, regional, lower-tech family (anti-satellite weapons, lasers, railguns, hypersonic missiles) doing the same job locally.

## Defence structures by scale (Combat Defence Structures txt)

| Scale | Structures |
|---|---|
| Galaxy | Galactic core gun |
| Star sector | Nicoll-Dyson beam, tachyon cannon, hyper EM railgun |
| Star system | Major railgun, super laser, IPBM, space fleets/doom star, celestial drop/ram (colony, large asteroid), anti-FTL cannon (orbital or ground) |
| Celestial | ICBM, orbital laser |
| Continental | Cruise missiles, minor railguns |
| Region | Artillery, rockets |
| Area/on foot/vehicle | Direct weapons, mortars |

Some can hit targets in high atmo, orbit, the star system or FTL, and also strike structures far away as indirect, artillery-like attacks, even in another star system. Celestials themselves can move to dodge, ram other celestials, or be converted (a tile, region, continent or whole celestial) into a weapon, system or device (B11).

## Proposals

Claude's suggestions for parts Reactorcore titled but left empty or undecided. Not Reactorcore's design.

- **Proposal, Escape/Leave/Retreat (B16, headings only: "Arena" and "Tunnel").** *Arena:* retreat is leaving through any door you qualify for, with the TN28/B14 rules (momentum, 90° angle, exit delay by size, shootable until gone); a packed fleet retreats as one unit through one door; the winner keeps the arena's tile, and the loser's MIA crews go to the lost & found list. *Tunnel:* retreat is dropping out sideways through a side exit (in-region) or turning back with a flip turn; a retreating party that started the tunnel can collapse it behind them only if its drive shaft is intact, otherwise pursuers may enter at the near end. Either way, a successful retreat starts a chaser interdiction window for the side that stayed.
- **Proposal, diagonal tunnels.** Take Reactorcore's own fallback from the Notes: below a 45° angle the tunnel is horizontal, above it vertical, and the exit side breaks ties, so a diagonal trip is one tunnel that ends near, not at, the diagonal target, plus a short tile move.
- **Proposal, digging from soil into a sea tile** (Notes todo, unanswered). Breaking through flooding is local and bounded: the dug tunnel's own cells flood to the sea's level, vehicles without underwater propulsion in those cells are paralysed (as with a car driving into the ocean), and the tile's layer data changes from soil to flooded soil, so the change persists and later room networks there are partly underwater.
