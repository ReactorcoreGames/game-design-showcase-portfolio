# TopVerse: buildings, vehicles and fleets

The DRC/MDRC model that lets one structure exist at every zoom level, how vehicles are built and damaged, ejected crews, and fleets with their flagship and drive shaft. Sources: `5 Topverse system layers n mechanics.txt`, `1 TopverseNotesBU2_Cleaned.txt` (fleet command, Fleet Unpack-Pack), scans TN10–TN17, TN25, B4, B6, B7, B13, B14, B15. Scan codes are explained in [index.md](index.md).

## DRC and MDRC

**DRC** = District Room Complex, a building or installation. **MDRC** = Mobile DRC, a vehicle, ship or mobile base. Every major structure is one, and so is a **major vehicle (MV)**. Minor vehicles (cars, tanks, fighters) are smaller and can ride inside.

One structure has several faces, one per zoom level (layers txt; B4 "Struct – Vehicle (MDRC system)"):

| Face | Level | What it is |
|---|---|---|
| **Entrance** ("superstructure", "foundation", "entrance hub") | on foot | the outer cells you walk around and into: max 20x20 cells of 2 m, with a 4 m buffer (two cells) around it |
| **Interior** ("inside spaces") | on foot | the inside, derived from the entrance footprint: each entrance cell corresponds to a 3x3 interior cell |
| **Facade** | vehicle layer | the zoomed-out look in vehicle combat (see below) |
| **Map icon entity** | map layer | an icon on the region map |
| **Data node** | far layer | pure data |

Rules (TN10, TN13, TN14, B4):

- A building or vehicle can't be larger than its entrance cells allow ("2 entrance cells = 2 x 3x3 interior cells"). One entrance, one floor plan (B4; multi-floor collapse was rejected).
- Exits between entrance and exterior correspond cell to cell; inside, an exit can be anywhere in its 3x3 interior cell.
- Breaking a boundary wall lets you leave the interior through it, dropping "from above" into the matching entrance cell's outside, never diagonally: a one-way exit (TN10 "interior wall exits, one way only", landing zones N/S/W/E above ground).
- Busting a new hole between interior and exterior is possible, but each interior/exterior pair has only one active entrance at a time.
- Minor vehicles may be on board; a vehicle bay shows the largest minor vehicle that fits an entrance cell (TN13).
- **Interior contents**: subsystems, weapons, interfaces, controls, furniture; internal defences (traps, troops, turrets); propulsion, drive, tanks, reserves, storage. Subsystems come in sizes S/M/L (TN13).
- **Interior walls, supports and armour** (TN14) do two jobs: sacrificial armour that protects the occupants of an interior cell from penetrating hits, and walls, cover and pillars that organise traffic and access inside. Materials, thickness and density set their HP. Border wall segments come whole per cell side ("full border segment: yeah; individual segment: nah"). Border walls keep out the outside (vacuum in space, flooding underwater, dust in a desert storm) and block the one-way exit; a missing border wall only affects its own cell. Door types: shift (sliding, the common one) and swing doors.
- An entrance can be several separate cells (TN17, **separated-cell DRC**): only the occupied cells are built. For a DRC nothing else happens. For an MDRC each cell gets a **mobility coaster** underneath (drawn under the floor, above the terrain: wheels, hover skirt, wings, thrusters, sea hull, underwater propeller, underground crawler, tank treads) and a rectangular support frame above connects all cells, rendered above the floors and casting a shadow: **phantom girders** (mechanical, various materials and techs) or **bio struts** (biological: bone, growth, strand).

## The facade and vehicle play (TN15, TN16)

- The interior modules (thrusters for air/space, wheels for ground, a missile battery, a cockpit, turrets, an exit) define a simple rectangular **Vehicle Entity**: the true shape and collider.
- Weapon firing offsets are set on the box (front/middle/back x left/centre/right) and weapons are pre-grouped, or the usual weapon/attack system is used.
- An optional freeform **Overlay Facade** is drawn on top to make the building or vehicle look like anything; ideally it fully covers the box. Weapons and systems can render above or below it.
- "Vehicle is like a character. Plays like one." It gets controls, mobility, abilities, weapons and traits from the modules installed in its interior.

## Damage (layers txt, TN11, TN16)

- A vehicle takes damage as **universal HP**: no locational damage, no advanced targeting; extra "armour HP" can come from modules.
- Superstructure strength comes from size (number of 2x2 m cells), material (cardboard, wood, steel...) and the amount and density of that material. Entrance HP = vehicle HP. If the superstructure is broken (all entrance supports and walls), the whole DRC collapses into rubble where it stood, and everything inside and on the facade is ejected into the scrap pile.
- **Hull hits** damage the vehicle and are dealt randomly to superstructure components (entrance struts and walls) as long as any remain. Turret hits damage the turret and pass a share on to the hull (TN11).
- **Penetrating hits.** Every hit is evaluated for payload size, type and penetration against material, armour thickness and size. A penetrating hit pays a tiny hull tax (0.1%) and deals the rest to one random 3x3 interior cell, "from above" (the interior is a perpendicular plane to the entrance, so hits arrive from above and land on one cell, never plough end to end). Within that cell, entities take the damage in random order, large mounted and heavy things first, with dedicated **interior absorption armour** taking priority; if nothing is there, the hit diffuses or passes out. Interior hits can never collapse a building; they ruin its contents.
- Three penetration outcomes: stop at the hull; go inside and stop (tactical-class weapons, basic AP); go through hull and interior and out the other side on the original or altered trajectory, possibly hitting another target (annihilation class, maximum collateral). This also works on foot with a strong enough weapon.
- Rejected alternatives: interior hits only from special weapons (it would stop collateral weapons overkilling through a DRC), or the attacker choosing hull or penetration (not every hit is chosen). Accepted ("New3"): the hull protects the interior as best it can, and some forces, by circumstance, simply penetrate.
- On foot, a DRC's own vehicle weapons can be fired by its commander or a remote interface anywhere in the human-size room, arriving from above, perhaps with a minimum range (TN12).

## Defences (layers txt)

- **Entrance**: interior-mounted heavy guns firing down anywhere in the on-foot room on command; armour plates, doors, traps, heavy external and light internal turrets, hazards, blockages, guards; numerous, strong, thick pillars and walls; minor vehicles and troops pouring out of doors or one-way wall drops; lethal rocket exhaust roasting the area at take-off or idle; locked floor doors, and superstructure too strong to cut new entrances into.
- **Interior**: troops, minor vehicles, traps, anti-personnel turrets, anti-intruder systems; doors and corridors that force intruders into kill zones; flushing loose contents through an airlock (or flooding cells underwater); cutting oxygen, life support, heating or cooling.
- **Vehicle**: mobility to dodge, or relocating to a layer the attacker can't reach (sky, underground, underwater); interior weapons usable against DRCs, MDRCs and minor vehicles.

## Size and access (B7, B13)

- Max MDRC/DRC/MV size: 10% of the max area tile size. Size can bar access to some tiles.
- Size classes like Starsector's: frigate, destroyer, cruiser, battleship; fighters are minor vehicles. B14 also uses t/s/m/l/xl.
- Below a certain size, an MDRC can enter a city or building tile; too large, and it can only use open spaces and collides with city tiles. City structures can be used as pass-through cover for MDRCs (B6), and a DRC can hide inside city structures and an MDRC can leave them behind (Notes, area tile 2.0); structures absorb damage for the DRC unless the attack is overpowering or precision-penetrating.

## Altitude and falling (B7, TN19)

- Each layer is a band of height (for example 0–1000 m). Two things at 4 m and 530 m are on the same level and can shoot each other directly.
- Jumping doesn't change altitude; it only switches a character's mobility to hover/fly briefly. Altitude only rises with propulsion that lifts a vehicle to the next layer; without thrust and with gravity, it falls, and a fast touchdown deals damage based on mass.
- TN19's overlapping thresholds keep units from flickering between layers in combat: from the surface, climb to +500 m to go high (sky), descend below +250 m to return; dive to –100 m to reach soil/sea, rise to –50 m to return; go to –1 km to go deeper, rise to –500 m to leave the deep; 5 km is a drop from high atmo, 10 km is escaping upward; the crust starts around –10 km. A HUD **altimeter** shows altitude and vertical speed with a falling/rising visual effect (also in the Notes todo).

## Ejected crews (TN25)

A vehicle or MDRC has subsystems that auto-equip passengers and pilots with vehicle-specific ejection survival kits (some kits can even be useless): parachutes, dinghies, dive coffins, stasis pods, rubber bubbles, escape pods/shuttles, airbags/balloons, tents/boxes, goo cradles. People ejected from a vehicle:

- become a **rescuable pickup**, or deliberately travel elsewhere in an escape vehicle;
- go **MIA**: added to a lost & found list, assigned to a tile/node/zone, and placed as a discoverable character in a room network on later on-foot missions there;
- or are **KIA** (destroyed, for things): scrapped, their materials added to the local tile's mass; remains and loot can be found on later on-foot missions.

## Fleets

**Fleet command** (Notes): drive shafts, flagships/motherships, team member ships (the vehicle equivalent of team characters); stranded ships (back to base, MIA, KIA, rendezvous); switching control during combat, including temporary direct control of an NPC ship as a side mission to resolve a stranded escape; enemies use the same flagship system; on-foot exploration of a flagship-bound fleet via catwalks; packing members to protect them and to prepare an emergency combat exit.

**Fleet size: 4 ships** (Notes Fleet Unpack-Pack, B14, B15), any size. The on-foot room configuration of a packed fleet is a plus shape: the gantry connection nexus in the middle, the four docked vehicles around it, and the four corners empty, where invaders, infiltrators or rescuers can spawn to raid a packed fleet. *(Earlier notes say 8 per fleet and B13 says a drive shaft binds up to 8; see the conflicts table in [index.md](index.md).)*

**Flagship.** Any ship with a docking gantry can be the flagship; whichever fleet ship the player is aboard (with a gantry) is the flagship, but the official change happens only while parked without disturbance, or after the flagship is destroyed. Any size of ship can carry any size of ship, "even if it's comically larger", but a small flagship is easy to destroy and the **APC effect** applies: if it blows up, everything packed in it is destroyed. Reasons to pack (Notes): the flagship can cross terrain the others can't (a boat across a desert, a plane underwater, a ground car in space); protecting a vulnerable vehicle in combat; long-range travel (FTL, high atmo/orbit, sublight, core-mantle diving, sleeper ships); and narrow tile-to-tile transitions where fewer than four doors are open on a layer.

**Pack** (Notes, B15). Requirements: one active flagship, a docking gantry, max 4 ships. Command a ship to auto-dock, or pilot it over the flagship's docking trigger collider and press E. It slides swiftly under the flagship, turning darkened, translucent and desaturated, with collisions off: it exists only as a node. (Its mass could slow or even paralyse the flagship; an optional realism rule.)

**Unpack.** Press or hold 2, 3 or 4 (the slot), aim with the mouse where the ship should appear and rotate it; an outline the size of the ship shows green when the spot is clear of solids, colliders and vehicles (projectiles don't count). Confirm, and it slips into place in under a second. Spawn positions lie on an **adjustable ring** around the flagship whose radius comes from the flagship's and the ship's dimensions, so it always clears the flagship's collider but stays within max distance (no teleporting across a mountain). Alternatively, command the flagship to release a ship on its own (the AI does this too). The slide-out has no delay (a delay risks spawning into another physics object); a cooldown on dock/undock commands stops the cheap trick of popping armour-brick ships in front of incoming fire. Spawn logic checks a frame for obstacles, then confirms on the next frame before spawning; if an intersection still happens, the chaos system teleports one party elsewhere.

**Enemies use it too.** An enemy fleet arriving packed in one flagship can be destroyed before it unpacks, killing up to four ships at once. A retreating enemy fleet can be chased (see [travel-and-combat-layers.md](travel-and-combat-layers.md)).

## Drive shafts (Notes, B13)

A component installed in a vehicle that enables **fleet binding** and **long-distance travel**: "connect up to 8 vehicles for journey transit" (B13). It has four parts:

- **(A) Connector gantry**, including a catwalk access network.
- **(B) Special fleet propulsion**: FTL, sublight, orbit/atmo, underground/underwater, core/mantle.
- **(C) Travel interdiction defensive weapons**: point defence, countermeasures, active weapons, attack nullifiers against drones. Mostly powered by the drive shaft's FTL field, so dormant outside it ("like the SR-71's ramjets", Combat Defence Structures txt).
- **(D) Forward plasma lance/shield**: clears dust, debris, asteroids, gas and incoming attacks on the path. It only works outside celestials, which interfere with it naturally and absolutely, so it can't be a superweapon (Combat Defence Structures txt).

Two forms are drawn: the FTL/sub-FTL drive shaft (a rocket-like spine) and the **subterrain boring drive shaft** (a drill-headed shaft for underground, mantle and core travel). The drive shaft itself is an abstract, invisible component "in the middle", between entrance and interior; on foot it is reached through **drive shaft nodes** in interior cells. One node is enough; more add redundancy and security. Losing every node destroys the drive shaft, which makes the nodes a boarding target. Using a drive shaft leaves clues at both ends of a trip (see travel).

## Population control (B6)

Vehicle/DRC/MDRC population is policed by the chaos system: the universe, each celestial and each region have quotas (labelled 1, 2, 3 on the note); exceed them and **chaos storms** begin and grow until order is restored. Beyond the quotas, any number of vehicles can exist, since they are data points and procedurally generated; only the player's flagship(s) are persistent while in use or registered. See [metagame.md](metagame.md) for the persistence tiers.

## Proposals

Claude's suggestions, not Reactorcore's design.

- **Proposal, fleet 4 vs 8.** Keep **4 ships per fleet** as the combat and packing unit (the latest and most repeated number), and read B13's "up to 8" as a drive shaft's **journey capacity**: one drive shaft can carry two bound fleets (or one fleet plus allies) through a tunnel transit, but they unpack and fight as fleets of four.
- **Proposal, quota numbers.** Persistent player-owned MDRCs: 3 per region, 12 per celestial, 48 universe-wide, as a starting point that the save-file budget can tune. Exceeding a region quota starts a slowly growing chaos storm in that region only, which telegraphs the problem without punishing the whole universe.
- **Proposal, falling out of a DRC midair** (Notes todo, unanswered). A character who drops out of a flying MDRC's interior (a broken wall, an airlock flush) gets that vehicle's ejection kit if equipped (parachute, balloon) and lands in the area tile below as a rescuable pickup; without one, they take fall damage scaled by the altitude band and, if they die, go KIA under the TN25 rules.
