# RoomSpace: atmosphere, materials and terrain

The stuff rooms are filled with: air, liquids and gases, the materials everything is made of, destructible terrain, and the rule that matter is conserved. Notebook 1 treats terrain as level pieces (211–214) and sketches atmo as a grid (233, 242–247); notebook 2 (263–281) defines materials, Terrain Material Containers and the node-level atmosphere model. Numbers in brackets are scan numbers; full wording in `transcript/`. *(interpretation)* marks Claude's reading; **Proposal** sections are Claude's suggestions.

## Equivalent exchange

The universe conserves matter: nothing is created or destroyed, only transformed (RoomSpace.txt). The notes apply it everywhere: all terrain breaks down into ½ m loose spheres rather than vanishing (213); reverse doors must take their contents from somewhere (240); out-of-bounds objects become a glitch blast rather than being deleted (237); 99% of each node's volume is a matter reserve held in the background (270); gibs and deployables can't exceed their parent's mass and energy (202). Title-only strips list "Equivalent Exchange (refill via doors) (visible on far background vision)" (236) as a topic to design.

## Atmosphere

Three models appear, in order:

**1. Grid atmo (notebook 1, 245–246).** A room is a grid of 3×3 m cells (e.g. 6×4 = 24; maybe up to 10×8 = 80). Cells are corner, wall or open types, and talk to their neighbours.

- **Contents**: water/liquid, air/void/dark matter, gas/plasma, mist/haze, aggregate, radioactive material, in varying densities or amounts per cell.
- **Affected by**: temperature, gravity vector, ambient radiation (α, β, EM, gamma: light, radio, X-ray), pressure (own and transferred from neighbours), electric charge, light, momentum, and the chaos system as a performance guard.
- A cell's state comes from its contents and these effects ("99% air, 1% water: humid air cell").
- Cells constantly pass contents to neighbours toward **equilibrium**, but only when a minimum threshold is met; small changes are ignored for performance. Update orders: alternating rows, whole grid at once, or cell by cell.
- **Visitor interaction**: gas balls released by a vent diffuse and fade; emissions diffuse into the atmo over time; walls absorb impacting projectiles (fully or partly), record the damage, and shed the heat and material back into the cell.
- **Input vents**: emit any combination of contents, with rate of fire, pulse size, batch interval, pause and emit length (GO / STOP / GO), and stop when the cell is full (maybe still applying pressure). Output vents suck.
- Cells can **solidify into 3 m terrain blocks** at enough density.

**2. Single-cell atmo (244, 247).** The whole room is one atmo cell with global settings. Contents are imagined as gas balls that collide, squash against walls, combine chemically (H + O → HO) and get absorbed. Nested: the room's micro (local node) atmo sits inside a macro (mega node) atmo.

**3. Node atmo, interior versus atmosphere (notebook 2, 265, 266, 278, 281).** This is the latest model.

- A room has a small **interior** (the playable room) sitting in a vast **room atmosphere**, the general setting of the node it's in.
- Every wall segment and door constantly **cycles** between interior and atmo. Insulation per segment can boost, reduce or stop the cycle; corners are inert. If all walls are fully insulated, the atmo won't cycle in, unless it's fierce enough to break the insulation.
- A room's goal is to saturate toward its node's atmo and reach equilibrium, through three channels (278, 281):
  - **Wall flow**: with the immediately adjacent room, through the walls (blocked with wall tech).
  - **BG flow**: with the node's ambient background atmo, up to a saturation level set by the node's density (blocked with BG panel tech).
  - **Adjacent node seep**: nodes exchange atmo and materials with their neighbour nodes, node to node, not room to room.
- **Adjacent room atmo effect** (265): all rooms in a local sector run a periodic pass that alters each other, reduced by room resistance and isolation and increased by greater-zone influence.
- Atmo also circulates through a DRC's chain of subrooms, starting from its entry room (278).
- A real-world HVAC loop (outdoor air, air handling unit, filters, heat recovery, air changes per hour) is sketched as reference (264), with the channels it moves: clean air, CO₂, heat, humidity, impurities/dust/bacteria/viruses.

**Spheres of environmental influence** (254): room → adjacent room → planet → universe; wall insulation ratings; equilibrium versus dynamics.

**Representation**: wall flow lines (see `rooms.md`, Walls). An untitled sketch (281) seems to show a single 3 m cell's contents as small symbols in a 1 m sub-square, with material draining in at the top and pouring out at the bottom *(interpretation; unwritten)*. Reactorcore doesn't remember it and calls it a throwaway sketch, safe to ignore.

## Liquids, gases and blobs

Questions for a **blob system** (233): splitting and merging, min/max size and density, layering and mixing elements, level generation, chaos-system management, interaction with characters, objects, visitors, vents and terrain, and blob-on-blob phenomena and weather. Design factors: performance (collision checks, entity count, update frequency) versus gameplay (granularity, dynamic and vast, usable in weather events, storing and releasing, phenomena, layering forces).

Two versions were proposed (242): a **grid** of 3×3 m cells for rooms, or **freeform blobs/squares** for an open world, and blobs that solidify into grid terrain. Notebook 2 uses both: cells carry the atmo, and blobs are loose matter from broken terrain (below).

Titled but empty: "Liquids & Gases" (234), "Atmospheres/Air/Weather/Events" (232), "Filtration of Rooms (Border Vents)" (235). Weather appears only in the worst-case room (rain, wind, geofire, gravity well, an incoming flood, 214).

## Shockwaves, quakes and sound

- **Quakes** (262, 264) are generated by a planet's core and propagate from the core room up to the surface, or along the cup world's outer walls inward. They can be local or from outside, and pass from room to room only through walls that conduct quakes.
- **Sound** (281): very loud sounds propagate from adjacent nodes, very slowly and distorted through vacuum, delayed through air, faster through liquid, fastest through solids; travel time depends on both nodes. A minimum threshold applies, and big sounds come with shockwaves and forces.

## Materials

**Classification** (263): origin (natural or engineered) → class (biological, mechanical, other/exotic) → state (solid, liquid, gas, plasma, supercritical). The RTF notes add mist/haze/dust, aggregate, triple point and void as matter types.

**Attributes** (263): temperature and pressure ranges (melting/boiling curves); stability (decay into radiation, magnetism, light); chemical volatility (reactivity, absorption, flammability); mass density and inertia; strength, brittleness, cohesion; conductivity; energy density and fuel potential; technical complexity score; embedded compounds (toxicity, resistances); insulation and rot; half-life and entropy; pH resistance; HP/gib and impulse limits; CKP/ISD charge speed; unreleased momentum.

**Derived attributes** (263): roughness, energy transfer, liquid surface tension, viscosity and buoyancy, loss of magnetism in heat, machinability, gas expansion, embodied cost, elasticity (only for objects under 3 m), durability, reflectivity, emission reluctance, thermochromism.

Open task (263): define which attributes are **core** and which are derived, and a standard way to calculate them. Resolved: material attributes from a wiki, rocks as fuel, where friction and inertia come from.

**First wave materials** (275): water (snow, ice), rock and sand (aggregate), mud, clay, soil, oxygen, and dirty, contaminated and oily water (separation and formation as questions).

## Terrain

**Terrain system parts** (211): border, pinned terrain objects, loose terrain objects and containers, items, characters and nav nodes, background and region influence, atmo/weather/forces/liquids/gases/fields, generation heuristics.

**Terrain objects, notebook 1** (212, 213). Generic blocks of 3 m, 2 m, 1 m and ½ m on a ½ m grid, in many shapes (wedges, steps, spires, ramps). **Pinned** to a wall, the background or a neighbouring pin; once the pin breaks they're loose. States: pinned → ripped or destroyed → split smaller → loose "nuggets" (½–1 m spheres) → vanish with gibs. Colliders are slightly smaller than sprites so pieces pile up nicely. **Decorative terrain** (212) tells a story, sets the mood and provides landmarks: sparing, broad, significant placement; less is more; edges emphasized, centre usually left open.

**Terrain Material Containers (TMC), notebook 2** (275–277), the later version:

- Chunks that are **over 50% solid**, sized 3×3, 2×3, 2×2, 1×3, 2×1 and 1×1 (plus a 1 m round one). Each has a composition that depends on temperature and pressure (e.g. 90% rock, 5% water, 5% methane) and an overall density.
- **Cut** damage splits them along the grid: 3×3 → 1×3 + 2×3; 2×3 → 2×1 + 2×2; 1×3 → 1×1 + 2×1; 2×2 → 2×1s; 2×1 → 1×1s.
- **Grind/fracture** damage shatters them into **blobs** (3×3 → 1–5 blobs, 2×2 → 1–3, 1×1 → 1), depending on granularity, density, stickiness and the damage, while their liquids and gases go into the local atmo cell.
- **Blobs** gradually give their liquids and gases to the cell atmo, shrinking to solids only. They merge easily when close, combining content and momentum.
- TMCs merge only by welding or by being forced together, into the bigger or denser one. Welding into a 3×3 (the maximum) siphons material from the small one into the big one.
- **Created** by a machine, extruded from the wall by the node atmo (over capacity, high pressure, emptiness), solidified in a cell from the room's materials, or warped and reassembled by the chaos system (anomalies, lag control, room repair/defence). Ideally in a clear cell; colliders switch on once the space is clear.
- **Density**: more density adds gravitational pull and inertia; a minimum is needed for cohesion; cramming more in takes progressively more force; past a point, gravity compresses new matter by itself.
- **Critical density**: past a threshold, a TMC burns mass away as radiation and heat, and its materials transmute to heavier elements. If the cramming outpaces that emission, it collapses: **any TMC can become a star, a black hole or a singularity** (277). An earlier note (275) had the overload converting everything to the most basic matter and exploding; 277 is later.
- **Performance** (276): a 10×10 room could hold 900 1×1 pieces. The chaos system monitors the count, blocks cutting under high load, merges blobs in a growing radius, absorbs blobs into the atmo faster, and converts small TMCs (and in extreme load 2×2 and 3×3) into blobs or atmo. Placement should be sparse, creation uncommon, larger pieces preferred.
- **Coverings/frostings** (276): inert shader layers on top (snow, moss, rust, soot and more; listed in `combat-and-items.md`).

The settling sketch on 203 (a circle that squashes into a square and spreads to a 1 m-thick layer) fits blobs or liquids *(interpretation)*.

## Proposals for open questions

Claude's suggestions, offered for topics Reactorcore titled but left empty or undecided.

- **Proposal, one atmo model.** Use the notebook 2 node model as the base and the grid only inside a room: the node holds one atmo record (composition, temperature, pressure, radiation, gravity); the room interior is a coarse grid of 3 m cells that drifts toward it through wall flow and BG flow. Dormant rooms store only their node record, which fits "only the current room is simulated". The single-cell model is the room's state when it's unloaded.
- **Proposal, liquids and gases** (title only, 234). Liquids and gases live as amounts in atmo cells, not as particles. Visible water is drawn per cell as a fill level with a surface line, flowing to lower and emptier neighbour cells under the room's gravity vector each update. Gases mix within cells and only show as tint, haze and the wall flow lines. Blobs are reserved for loose solids and sudden releases (a burst tank), and dissolve into cells. This is cheap, fits the 3 m grid, and handles floods between rooms through doors and walls.
- **Proposal, weather and events** (title only, 232). Weather is the node atmo changing over time plus a few room-level effects driven by it: rain and snow as visitor particles when a gas-heavy node passes a humidity threshold, wind as a force field from pressure differences between neighbouring nodes, storms and floods as universe events scheduled by the background thread. Players change weather by changing the atmo (venting, insulating, terraforming), which is how deserts turn to forests in the overview.
- **Proposal, filtration of rooms / border vents** (title only, 235). Wall segments can carry a filter instead of plain insulation: a filter passes chosen channels (e.g. let air through but block toxins, or let water out but keep oxygen). Filters are installable wall tech, so a player can build a breathable bubble inside a hostile node.
- **Proposal, terrain budget** (title only, 226). Count terrain against the same per-room object budget as items and visitors: about 40–50 physics-enabled TMCs per room (the worst-case figure on 214), each fracturing into at most 5 blobs, with the chaos system merging once blobs exceed about 150.
- **Proposal, terrain generation heuristics** (title only, 230; to-do on 257). Generate a room's terrain from its node record rather than from biome templates, as the overview demands: node density sets how much of the room is filled (solid nodes give excavated rooms, open nodes give a few floating TMCs); composition picks the TMC materials; gravity sets where they settle (floor ledges under gravity, floating clusters in zero-G); and the room's "remarkable point of interest" is placed first in the centre, with the decorative terrain rules (edges, sparse, centre open) after.
- **Proposal, core versus derived material attributes.** Core: density, state temperature and pressure curves, stability, chemical volatility, strength/cohesion, conductivity, energy density. Everything else derives from these plus the object's shape: brittleness from strength and density, flammability from volatility and energy density, machinability from strength and cohesion, HP and impulse limits from strength × size, CKP/ISD charge speed from density and strength.
- **Proposal, critical density.** Keep the later version (277) and merge the earlier one as its failure mode: a TMC that reaches critical density but can't keep up its emission explodes and scatters lighter elements (a nova), while one whose cramming outpaces emission collapses into a star, black hole or singularity. That gives both outcomes a place and ties into the universe-scale lifecycle in `universe.md`.
