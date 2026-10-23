# RoomSpace: universe, worlds, generation and districts

The big structure: how rooms add up to planets, sectors and a universe, how cup worlds are shaped, how it's all generated, and the District Room Complexes (DRCs) and their mobile versions (MDRCs), which are the buildings, ships and mobile bases. Mostly notebook 2 (261–282) plus the cup world stickies from notebook 1's end (244, 249–254) and the two text files beside the scans. Numbers in brackets are scan numbers; full wording in `transcript/`. *(interpretation)* marks Claude's reading; **Proposal** sections are Claude's suggestions.

## Structure and scale

**Nodes.** The universe is a grid of **nodes**. A node is a cell of a planet or of a space region, about 100 km³ (270). Each node has one **core room**, the playable interior (3×3 to 10×10 units, see `rooms.md`), sitting in the node's atmosphere. 99% of the node's volume is a **matter reserve** stored as background (270). Each node/cell is also a **district** with its own terrain mix (264). Scale ladder (270): room ≈ 100 m² symbolically (30 m actually), DRC 10 km², node 100 km³, sector 10,000 km³.

**Hierarchy** (265): room → planet, station or ship, or a local sector in space (32) → star cluster quadrant (16) → galaxy quadrant (16) → universe quadrant (16) = **131,072 rooms**. Scan 261 writes "1024×1024, 4×4", and scan 268 works out other totals without choosing: 64⁴ ≈ 16.7 million, 128⁴ ≈ 268 million, 256⁴ ≈ 4.3 billion. Decided (Reactorcore, 2026-10-22): the 131,072-room hierarchy, as in the proposal below.

**Simulation** (RoomSpace.txt). Only the room the player is in is simulated. Every other room is a semi-dormant node, a file that changes only when invoked. A background universe-events thread updates nearby and far rooms as needed and generates events for the player's region or room from the properties of the rooms and regions. Entering a room may apply changes accumulated while it was dormant; leaving saves the room's state into the universe simulation.

**Space** is a top-down grid of regions branching into star systems, galaxies and superclusters (RoomSpace.txt). Its contents (250): suns, pulsars, black holes, supernovae; gas and dust nebulae; hulks, asteroids and stations; artificial spaces (outposts, buildings, zones); transit (wormholes, time); living world / universe events.

**Local space** (267): a region whose four entry points are fixed and whose interior rooms and connections are randomized.

## Cup worlds

Planets are "cup worlds": in side view, a vertical cup of rooms descending to a core at the bottom (RoomSpace.txt). Stars, gas giants and moons follow the same concept with different interiors.

**Anatomy** (251, 254, 261):

- **Orbit** at the top, linked to space; a "safe dimensional transition shaft" drops into the cup.
- A layer sequence downward: orbit/re-entry exit → low atmosphere/stratosphere → cloud → surface → underground/underwater → mantle → core (254; RoomSpace.txt).
- The surface row **loops around**: room 9 wraps to room 1, or four compass sectors N/E/S/W wrap (244, 252). Descent shafts branch down from the surface and converge on the **core room**, which has a door on each side (252).
- **"Main" and "wild"** (261): a main central band flanked by wild margins.
- **Remarkable locations** (251): notable points of interest, some guaranteed (252).
- Width and height adjust with the core (251). A planet has a **facing direction** (254). Edge wrapping at the cup's sides was considered and rejected ("Nah", 268). A "planetary orientation rotation process" was drafted and crossed out (253): two sectors linked by in-between nodes whose number depends on their "meta distance".
- Each room carries metadata that affects and is affected by its neighbours (244).

**Generation** (267): the **entry** room and the **core** room are fixed ("solid"); everything between is randomized by heuristics into regions, rooms and connections.

**Cores** (251): attractive or repulsive (like magnets, for materials and elements); positive or negative mass; inverted polarity; gravity up, down or neutral; cup/pocket field modifiers (background and foreground "hairs"); wall properties (light, collision, emissions); core and cup size. **Quakes** come from the core (264). Topics listed for later (250): core properties, cup shapes and scales, single or multiple cores, field/wall, lifecycle (creation, overload, destruction), generation heuristics, layers and "remarkables", digging between nodes, adding/editing/deleting nodes, entry and exit.

**Shapes** (252, 253): narrow cups, wide bowls, multi-lobed cups (one lobe per core), shallow dishes, capsules with cores at both ends, clover shapes. **Earth** is a positive-mass cup that opens upward; **Aether** is a negative-mass cup inverted, opening downward with its core at the top. Also a **pizza world** (a wedge slice) and a **cocoon world**, and the **pocket cup world**: a core that sinks into the fabric of space and makes a dent, like a weight on a rubber sheet. "Research cupworld formation" is noted as a to-do.

**Mapping** (249): a sample overworld path through room types: asteroid → asteroid exit → space → atmosphere exit → atmosphere → surface/underground exit → underground → underground exit → underground water reservoir → its exit → undersea → sea exit.

## Generation heuristics

The generator adds materials and conditions and lets each room's climate and biome follow from them, rather than placing biome templates (RoomSpace.txt). It works top-down, each level leaving an "imprint" the next reads, "just a matter of IF statements with a logical chain of order".

**Steps** (282, latest):

1. Distribute all matter into the universe via big bangs (random, several).
2. Designate zones from the result, with attributes (rules A).
3. Coalesce matter into cores and conglomerations (rules B–E): universe A → galaxies B → systems C → sectors D → pocket planets Ea / local space Eb.
4. Render core node rooms and natural DRCs at the macro level (size, status, location, surroundings) from the A–E imprints.
5. Render rooms and subrooms at the micro level (rules F).

**From `UniGenHeuristics.rtf`** (Reactorcore's text doc beside the scans, an earlier version of the same steps; its rule sets run A universe → B superclusters → C local galactic groups → D galaxies/star clusters → E star zones → F celestial bodies/local space → G rooms → H subrooms (DRC/MDRC)):

- **Goals**: big enough for the full range of places, macro and micro; interesting, varied, vast and logical, with a clear reason why each place is the way it is; able to cover a universe sector's whole lifetime, from a big bang spread to the critical-mass big crunch, with **multiple bangs and crunches as normal lifecycle events** rather than a single one; comparable to the real universe but adapted to the room-node world and its "2.2D" flatness.
- **Layers**: 0 baseline (universe filament as noise-distributed matter/energy) → 1–2 "unsoupification" (superclusters, local galactic groups) → 3 concrete locations (galaxies or star clusters) → 4 subregions (star zones, sectors, solar systems) → 5 local neighbourhoods (celestial bodies / pocket worlds, or local space; only selected active nodes) → 6 the final room pass (3 m / 120 px units; rooms 3×3 to 10×10, DRC subrooms 1×1 to 10×10). Each layer is an N×N grid.
- **Forces and attributes**: temperature, pressure, radiation, light, gravity/antigravity, salinity, humidity, macro- and microbiological life, object properties, friction, stickiness, AI psychology, chaos/glitch, sharpness, density, anomalies, astral/mind powers, civilization and tech, constructions and ruins, electric and mechanical charge, magnetism, planet size, number and placement of cores, weather, quakes, dust, erosion, entropy and time, lifecycles, ecosystems.
- **Matter types**: gas, liquid, solid, plasma, supercritical, triple point, aggregate, mist/haze/dust, void.
- **Materials to solve**: list all materials, compounds and alloys (not atoms); standards for complexity, cost, attributes, the conditions they form under and the resulting rarity and placement; state ranges by temperature and pressure; everything a material can have, emit or absorb.
- **Space elements** (headed "PW", likely shared with the Planet Warfare design *(interpretation)*): planets, stars, galaxies, globular clusters, gas giants, rings, black holes, quasars, nebulae, asteroids and fields, comets, solar winds, gamma-ray bursts, moons, supernovae and remnants, interstellar medium, Hawking radiation, clouds, voids, dark matter, dark energy, dark flow, pulsar planets, dust.
- **Reference lists**: tile concepts (fire, gas, liquids, girders, pipes, windows, vines, webs, ladders, vents, light/sound/emission sources), tile shading styles (flat, bevel, rounded matte/glossy/metal, glass), special tiles (one-way, affectors such as radiation, ice, goo, EMP; boosters; selective colliders; fields), tile sizes (1×1 to 3×3), a long animated-effects list (fire, smoke, liquids, shockwaves, muzzle flashes, gibs, portals, bubbles and many more), and environment templates (planetary: crater desert, coal mountains, sea world, gas geysers, cloud world, crystal valley, ice cliffs, flying islands, bubble world; space: solar corona, void, gas bubbles, asteroid field, ice field, nebula, planetary ring, zero-G dusty planetoid).

**`FormationCreationOfUniverse.txt`**, also beside the scans, is a short transcribed narration about the early universe (cooling, the first atoms, galaxies forming along filaments, stars seeding heavier elements: "we are their progeny"). It's third-party text kept as mood and inspiration, so it isn't copied here; the ideas it carries (filaments, stellar lifecycles, element seeding) are the ones the heuristics use.

## Districts: DRCs

**District Room Complex (DRC)** (269, 271): a wireframe of subrooms immersed in a node, either **embedded** (stationary: a cave, building, fortress) or **mobile** (an MDRC that has entered the node: a freighter, starship, floating fortress, mobile building). DRCs are like sponges that soak up and release the materials and properties of the node they sit in.

- **Grid**: 16 rooms as 4×4, 8×2 or 16×1 (271), each up to 10×10 units (267: "16 × (10×10) rooms, any config"). Subrooms sit on a rigid grid.
- **Entry room**: the DRC room connected to the node's core room, placed by a bias (centre, corner, wall + centre, corner + centre, corner + wall) with a severity slider 0–100% (271).
- **Adjacent DRC paths** (271): two DRCs in neighbouring nodes can link a room in each into a path, wherever those rooms are in their grids, if both sides consent.
- **Spine** (271): the DRC is the "bone structure framework" of a node; without it no subrooms can be built there. Launching it as an MDRC leaves the node **spineless** until any MDRC lands and docks there. Converting an MDRC back into a DRC isn't necessary but yields materials. Open: a visual indicator for spine status, and what instability a spineless node suffers.
- **Core room states** (269): normal (untouched), docked (a district exists), undocked (the district left; remnants hint that a DRC exists somewhere). Max DRCs = total core rooms in the universe, linked one to one (the example on the note is ambiguous).
- **Buildings** (264, 267): type 1 reinforces a room node with insulation; type 2 is an entrance into a DRC, a grid-based subregion rather than node-based. Building questions: limits (max rooms, configuration), construction and deconstruction, collapse, backgrounds and insulation, anchoring, tree structure, and free placement of the root room in grid space reserved for that district, "XCOM base style".
- **Control command systems** (278): installed or portable consoles in core rooms and designated DRC subrooms. In core rooms they remotely activate, excavate, fill, refill, deactivate or modify adjacent core nodes and their rooms, resize the home room, and show sensor data. In DRCs they control installed functions; in MDRCs also movement.

## Districts on the move: MDRCs

**Mobile DRCs** are the "mobile headquarters mothership" of the overview: starships, mobile bases, moving fortresses. Smaller **micro vehicles** (MicV) use the same tether system (269, 270).

- **Mobility** (269, 277): every room of an MDRC needs installed mobility pipes/framework. A DRC's subrooms are **rooted** to the core node; all must be unrooted (converted) before it can launch. Rooms built aboard an airborne MDRC are unrooted automatically; rooms built while landed at a vacant node are rooted (marked "?"). Rooting converts a whole room at once, with time depending on size. Insulation is optional, but without it the local node's atmo floods in.
- **Propulsion** (275): needed to push an MDRC out of its node and to launch a DRC as an MDRC. Types by medium: vacuum, air/gas, liquid; each works well, differently or not at all in each medium. They vary in style, quality, efficiency, tech, price, ability and material needs, are installed as systems in subrooms, and can be combined. Launching can be reversed to "mothball" a docked MDRC at a core. A DRC with propulsion but still rooted can't move.
- **Movement** (273, 274): MDRCs move **point to point** on the core node grid, one step between N/S/E/W neighbours at a time, travelling straight (even diagonally) to a **pre-reserved** dock point in the next node. Both points stay reserved until the move ends. MDRCs can't collide with each other; passing over an inactive node doesn't activate it, disembarking does. An MDRC stays accessible throughout: at node 1 until it crosses the border, then at node 2. (An 8-direction free-movement option was rejected.)
- **Docking** (273, 274): every core room has **4 dock points** at its corners plus the central DRC point, standard across the universe (positions can shuffle in larger rooms). Dock states: free (green), reserved (yellow, "incoming"), occupied (red). Each is 3 m / 120 px. 5 at a node (4 foreign MDRCs + 1 local) = **blockade**; MDRCs pile up in traffic jams.
- **Where they can go** (273, 278): through vacuum, gas or liquid nodes; solid nodes must be excavated or converted first. **Excavation** isn't a layer-by-layer dig: a slit widens in stages and only becomes passable when fully open, after which all MDRCs fit at once.
- **Connecting to rooms** (270, 273): through **tunnel cables** or **anchor buoys with tethers**: an entry buoy in the room links by a transfer wire to the MDRC or vehicle. Connectors must allow constant traffic (no elevators, shuttles or trams), are themed as natural extensions of the DRC "spine" of the universe, can be upgraded with tech, and are visible in the background with their MDRC.
- **In the background** (273, 274): an MDRC is shown as a blob/circle, a box, or a miniature replica. The back wall shows this node's docked MDRCs and status; side panels show neighbours' MDRCs as pips (see `rooms.md`).
- **Damage** (279): apart from nullware and the chaos system, MDRCs and their subrooms **can't be destroyed, only sterilized**: a nuke inside could strip all insulation, vaporize every object, character and system, and leave the bare framework. No collapse mechanics: losing an in-between subroom only cuts access through it.
- **Core-room weapons against MDRCs** (279): SAM-like systems installed in a core room target MDRCs in the background of the local and adjacent nodes, along with invasive alternative transit, remote modification and cargo transfer.
- **Nullware** (278): the tier above antimatter, based on glitch destabilization and nullifying the universe's construct. Enormous energy, tech, material and complexity costs. The only weapon that can erase an MDRC entirely or modify its subrooms remotely. The biggest weapon in the game dedicates a whole core node to one **armageddon device** that nullifies an entire local sector (10,000 km³ wiped and reset).

Titled only (272): MDRC launch procedure; MDRC editing (shrink/grow/modify); MDRC destruction/damage (answered on 279); MDRC grade-mounted superweapons. Also titled only: "List of pocket/cup world CORE modifiers/attributes/abilities/features" (282), the last note in the notebooks. Unexplained words on 262: "begin invasion", "release virus", "electro".

## Proposals for open questions

Claude's suggestions, offered for topics Reactorcore titled but left empty or undecided.

- **Proposal, universe size.** Ship with the 131,072-room hierarchy of scan 265 (32 × 16 × 16 × 16), but generate only to layer 5 at start and render rooms lazily on first visit. Since dormant rooms are only files, the larger totals from scan 268 remain possible later by adding quadrants, without changing the room format.
- **Proposal, MDRC launch procedure** (272). A launch is a short checklist the control command console walks through, each step visible in the room: 1. all subrooms unrooted (rooms flash as they convert, time by size); 2. propulsion matching the node's medium installed and fuelled; 3. a free dock point reserved in the target neighbour node (yellow); 4. tethers and buoys retracted (anyone outside is warned); 5. the node goes spineless and the core room switches to "undocked". Then the first step. Launch can be aborted until step 5.
- **Proposal, MDRC editing** (272). Growing an MDRC means building new subrooms on its 16-room grid from materials carried aboard (rooms built while airborne are already unrooted); shrinking means dismantling a subroom, which returns its materials to storage and cuts access through it. Modification (reassigning a subroom's function) is done at the control console and takes time per room. All of it costs matter, under equivalent exchange.
- **Proposal, grade-mounted superweapons** (272). Superweapons are subroom installations graded by how much of the MDRC they occupy: grade 1 (one subroom: SAM-like batteries targeting neighbouring nodes), grade 2 (a 2×2 block: area weapons such as atmo-poisoning or quake drivers that act on a whole adjacent node), grade 3 (a quarter of the grid: antimatter-class). Nullware stays node-scale only, as scan 278 says, so no MDRC can carry an armageddon device.
- **Proposal, cup world core modifiers** (282). A starting list built from scan 251's core types: polarity (attract/repel materials), mass sign (positive = cup, negative = inverted Aether), gravity direction and strength, heat output (drives the temperature gradient from core to surface), quake frequency, magnetic field strength (shields the surface from radiation), emission type (radiation, light, exotic particles), core count and placement (shapes the lobes), lifecycle stage (young, stable, overloading, dying), and wall properties for the cup edge (insulation, light, collision). Each is a number the generator reads, so planets differ by their cores rather than by templates.
- **Proposal, spineless nodes.** A spineless node can't host subrooms, its core room shows exposed docking struts in the background, and its atmo drifts more easily toward its neighbours (no rigid framework holding it). Docking any MDRC restores it. That makes leaving with a mothership a visible, meaningful act in the world.
- **Proposal, DRC cap.** Read it as "at most one DRC per core room, universe-wide": every core room either has its district (docked), had one (undocked) or never had one (normal). Then the number of MDRCs flying around plus docked DRCs never exceeds the number of core rooms, and undocked rooms are clues to where a ship came from.
- **Proposal, invasion and viruses** (262). Treat "begin invasion", "release virus" and "electro" as universe events the background thread can fire on a region: an invasion sends hostile MDRCs toward a node; a virus spreads through atmo seep from node to node; an electrical storm disables powered items in a node for a while.
