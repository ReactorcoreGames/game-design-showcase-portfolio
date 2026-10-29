# AAL Universe: matter, energy, objects and making things

How everything is built from materials, how energy and forces are represented, how vehicles and buildings are put together, how crafting, research and digging work, and how modding stays consistent. Sources: `CraftingMolecules.rtf` (2013), `EnergyInVideoGames.rtf` (2014), `MolSys_SpriteArt_Objects_Energy.rtf` (2016), `PW Tech & Dev & Research.rtf` (2016), `PW research idea.rtf`, `PSRC Material Types Musing.docx`, EUR (mechanisms, ropes), `PW Design Terrain System*.rtf`, `PW Design bunkers.rtf`, scans W1-4, W1-10, W1-13, W1-14, W1-18 to W1-20, W1-25, W1-30, W1-33, W1-34, W2-27 to W2-36, PS-19.

## The molecular system

"Without being able to define an object by any standards, the content of the game can never be considered properly consistent" (`CraftingMolecules.rtf`). Everything (items, vehicles, worlds, characters) is built from **molecules** of a **material**, and the material decides:

- mass (summed from the materials), cost to produce (the ingredients), what can be salvaged;
- integrity: how much force it takes before breaking;
- behaviour: density, friction, inertia, flammability, elasticity, what forces affect it;
- what it can do: which inventions are possible with it;
- manufacturing complexity: more and rarer materials make an item harder to build.

New materials can be defined by players, "basically inventing new elements into the periodic table", and are instantly part of every system ("Elerium 115"). W1-25 lists the notable properties: pressure, temperature, mass, radioactivity, electrical conductivity, emission (hardness crossed out). The material musing adds surfaces (paper to astral) and six visual axes (hard–soft, meshy–granular, solid–loose, strong–weak, edgy–fuzzy, cohesive–erratic) with four reactions (collide, pierce, absorb, deflect).

**Derived values** (`MolSys` 2016): density comes from the sprite's non-transparent pixels times the material amount. You can make a 10 m boulder from 1 kg of cardboard, but it will burn, and a one-metre fall will crush it. A sand ball crumbles, a water chair becomes a puddle. Standard: 1 px ≈ 4–5 cm. The foreword's rule is the same: players set size, density and materials, never weight or hit points.

**Container attribute**: storing a substance needs hollow space in the object's design, and the container's material must suit it ("a container made of wood won't hold lava too well").

**Equivalent exchange**: matter is never created or destroyed, only changed (UniverseBounds, EUR, `Planet Warfare.txt`).

## Energy and forces

"Every developer/modder has their own interpretation of how fire, water or anything else non-solid works", but only one kind of fire can exist in a universe (`EnergyInVideoGames.rtf`). Energy means anything not solid that changes form: electricity, fire, plasma, liquids, gas, radiation, pressure, wind, sound, light, ethereal beings, PSI, gravitons, exotic particles. Four forms:

- **Solid form**: projectiles, beams, bolts, orbs, arcs, shells. Active and expensive; large shapeshifting energy (lightning) is chopped into segments; extra-large instances may use richer methods.
- **Area form**: values spread over world tiles (30/40 px blocks, air included) that affect what's inside and spread to neighbours (gas, liquid, fire).
- **Fall-off area form**: a radius effect weakening with distance, in circle, triangle or rectangle shapes with source, direction, size and falloff; for exhausts and blast radii.
- **Being form**: creatures made of slime, gas or energy; they lose matter instead of taking decals and dissolve past a threshold.

Also: opacity versus per-pixel alpha (only materials that allow it may go invisible), glows by particle density, sound that travels through a medium and is muffled by walls and distance, and vision modes (optical, colour-blind, night, thermal, sonar, x-ray, PSI physical, PSI life, radiation/EM, AI thought-reading, pressure). The force list: substances (liquid, energy, mass, object count, gas, potential energy), contact forces (tension, torque, linear force, friction), field forces (magnetism, heat, pressure, graviton, electricity, light, radio, radiation, sound, data, PSI). W1-30 sketches the light types: line laser, 15° spotlight, 360° point light, animatable image-based light, ambient directional light, polygon light.

## Phenomena, supplies and connections (`PW Tech & Dev & Research.rtf`)

- Materials carry **phenomena** (light emission, magnetism, thermal radiation, propulsion...). A template object can use a phenomenon as an ability if its materials allow it; the crafting station sets how efficient it is.
- Most phenomena need **supply**: a lamp needs energy, a gun bullets, a reactor rods, a tree sunlight. Objects need inputs (inlet, slot, capacitor) and suppliers need compatible outputs. "Tossing actual lightning at a plug isn't going to power a device as well as a proper modulated socket."
- **Transfer media** (pipe, wire, conveyor, beam, tunnel) must suit what they carry: no electricity through a wooden pipe, no lava through copper wire.
- **Material interchangeability** (experimental): recipes list requirements (solid/liquid/gas, whole/granular, hard/soft...) instead of exact materials, so substitutes work and pass on their properties: a real basis for "Rusty Sword, Heavy Sword".

## Making things

- **Three requirements** to create anything: raw materials, a creation environment (bench, machine, embryo, pool, robot) and the memory or blueprint. Time too, shortened by a better environment. Anything can be made, even terrain, planets and stars.
- **Composite objects / flattening the layers**: generic greyscale templates (cores and addons) live in an eternal blueprint library; a manufactured object pastes addons onto a core, gains their abilities and mass, gets painted and wears, and is flattened into one saved entity.
- **Research** (`PW research idea.rtf`, from Eco): research by performing experiments in special buildings, which consume resources; enough experiments unlock a **knowledge object**, owned by whoever did the research and shareable for a price or freely. The NVC AI musing adds that knowledge is memory that can be lost, so libraries, vaults and data storage matter.
- **Invention canvas** (W2-33): a node-editor lab where inventions, filters and utilities, all derived from natural phenomena and forces, are wired into any object (things, characters, buildings, vehicles); the workspace's size, zoom, tools and automation limit what can be built.
- **Element-based items** (W1-13, after Powder Toy): an item is a sprite plus device functions (create particles, generate force, trigger, timer, remote receiver), each with a cost: a bomb spawns 20 metal particles (1 RU each), radial force and radial heat (100 EN each). The aim is to stop modders inventing "BS values".
- **Blueprint flow** (W2-32): blueprint → construction zone → final.
- **Capability packs** (W2-30, W2-34): functionality modules injected into a structure (house + pack = working house), and a **Privacy Facade** module that hides a building's interior from outsiders (astral powers see through it), toggled by key.

## Vehicles, buildings and characters as one framework

- **Moving Frames V1** (W1-14): functional, layers, visual; from back to front: internal background decoration, M-Frame slots (functional slots/space), internal components (attached inside or next to a frame), external components (visible over the foreground decoration), foreground external decoration; wiring is normally invisible. "Similar system used for static structures/buildings."
- **Entity Framework** (W1-18): an **entity core** holds the requirements of operation, base functions, limb pivot slots, control system and UI; **locomotional limbs** give movement or propulsion; **active function units** add functions and UI "drivers". Cells hold framewalls, solid M-frames, foreground and background items.
- **Tile-grid hulls** (W1-19): ships, mechs and buildings drawn as tile grids, with destroyed tiles breaking off and falling under gravity, and a smooth-hull "hybrid system?".
- **Ship composition** (W1-10): chassis + Device objects (base, optional turret, fire spawn points) + Thruster objects (base, thrust spawn points), all with configurable variables.
- **Bunker modules** (2011, W1-4): modules with systems, connected directly or by tunnels, tubes, elevators, ladders and walkways; front layer turns transparent when inside; grid-snapped placement in allowed zones.
- **Main and sub structs** (EUR): subs can go inside mains (a utility vehicle inside a cargo carrier). Objects built from components max out at 10 m; bigger things use chunks, regions and continents.
- **Mechanisms** (EUR): doors, hatches, cranes, elevators, pistons, wheels, drills, conveyors (a rectangle that applies force, never real belts), catapults; organic jaws, claws, tails, tentacles. Two primitives: an object moving along a line in a parent, and an object rotating around a point on a parent. Keep it cheap: one door not two, 3–4 joints not 12. No wings or aerodynamics: lift is an attribute of the shape, modified by material and size.
- **Lines** (EUR): ropes, cables and wires as 1 px vector lines in the material's colour; free lines up to 20 m with both ends loaded; rails up to a region long; bending ropes after Clonk Rage (5–10 bend points, then break).

## Terrain, digging and destruction

- **2011**: node-and-edge terrain chunks with material edges (sound, debris, friction, one-way platforms), indestructible; dynamic chunks only for barricades.
- **W2-28**: triangle terrain. Draw layers: background override tris (interiors), background items, resource materials, people/vehicles, terrain. Solid material breaks into a **resource triangle** with a full collider; loose material into a **resource ball**. At 50% damage a piece degrades; at 0% it becomes a raw blob that falls and buries things. Planets are subdividing sectors.
- **Digging** (W2-29): Type A breaks a piece into resource units instantly at 0% structural HP; Type B, a harvester drains it gradually (0 → 40 → 95 → 100%) and stores it.
- **Exclusion meshes** (W2-32): subtractive meshes cut holes, tunnels and damage; over 80% excluded and the solid and its cut-outs are deleted.
- **Interiors** (W2-35/36): one interior triangle per terrain triangle; merged shapes give more (square 2, pentagon 3, hexagon 4); interiors grow from a start point or installed doorway. W2-36 is a list of open questions: merging rules, minimum triangle size (too small becomes resources or is absorbed), collisions, energy/gas/liquid triangles, limits on doors and windows.
- **EUR clumps and chunks**: digging past the minimum chunk size breaks terrain into 0.5–1 m clumps (balls, squares, triangles) coloured by composition; clumps fuse back into surrounding terrain or air if left alone.

## Modding

- **Standards first.** The 2011 plan already wanted factions, units, maps and scripts usable everywhere. Later documents add the reason: standards keep shared content from breaking the universe (`CraftingMolecules.rtf`, `MolSys`).
- **Tools in the game** (W1-20): a graphics editor (Paint Shop Pro 9 style), animation/bone/pivot editor, import/export, composite viewer, database search.
- **Distribution** (W1-20): A, every user mod automatically in your game (needs heavily enforced standards); B, browse a database and pick, anything goes; C, a hybrid: content that meets the standards loads automatically, the rest by choice.
- **Startup check** (W2-34): the Chaos System checks modded content for size, activity, significance and part count.
- **Consoles** (`Planet Warfare.txt`): no in-game modding; authors can apply to have content bought outright for official console updates.
- **Multiplayer**: single-player at heart and too griefable for public servers ("crash entire planets into a sun"); at most drop-in co-op or asynchronous social features (chat, sharing blueprints, photos, stories, meeting spaces) (`Planet Warfare.txt`, `PW Multiplayer Elements.rtf`).

## Open questions

- Terrain representation: node edges (2011), shards (W1), tile grids (W1-19), triangles (W2), clumps/chunks (EUR). No version is final; see [cohesive-design.md](cohesive-design.md).
- How many materials, and whether recipes use exact materials or requirement lists.
- LVIS (W2-30, W2-34) and RSH (W2-32) are never expanded.
