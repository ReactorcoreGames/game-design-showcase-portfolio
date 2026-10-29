# AAL Universe: how the design evolved

How Planet Warfare grew from a two-front war game into a universe simulator, and how its ideas were later split into RoomSpace, TopVerse and AAL Bunkerships. Sources: Reactorcore's `!foreword.md` (in the project folder), the 2011 docs (`Planet warfare.doc`, `PW - Overview.doc`, `PW - PROJECT PLAN.doc`, `PW Design Overview V2.rtf`, `PW Design Gameplay Classes.rtf`, `PW Design Terrain System*.rtf`, `PW Design bunkers.rtf`, `GameProjectRequirements.rtf`), the 2013–2016 rtfs, scans W1 and W2 (codes in [index.md](index.md)), and `Planet Warfare.txt` (the 2023 pitch, kept in this folder).

## 1. The two-front war game (2011)

The first documents describe "an epic war game expanding through galaxies" that is "2 games in one": a **Planet Front**, a side-view squad shooter with bunkers "very like Cortex Command", and a **Space Front**, top-down ship combat "like Battleships Forever", tied together by a turn-based **Tactical Overview** of a solar system, "very similar to the board game Risk". Concept 01 (W1-9) names the shape: "3 games, 2 modes" (Conquest plays all three games, Scenario is a single custom battle).

- **You are the consensus of your faction.** You take direct control of any unit while the AI runs the rest, and give simple RTS orders (move, attack, defend, waypoints) in a command mode. Fighters fly like Asteroids; capital ships are multi-crew and take orders (W1-1 has engineer and navigator views: power split 60 shields / 30 weapons / 10 thrust, per-facing shields, doors and elevators).
- **Population is your lives.** About 100 people to start; they man ships (a fighter needs 1, a carrier or dreadnought 5–10), garrison bases and fight; cloning facilities add people slowly (example: 10 people in 5 days). When everyone is dead, you lose. This keeps armies small without arbitrary caps. ("Limited Population" is crossed out on W1-9, but it stays in all the 2011 docs.)
- **Resources are physical.** Resource Units (RU) come from mining machinery each turn, but exist as crates that must be loaded into cargo holds you can walk into, so they can be stolen, captured or jettisoned to a friendly ship.
- **Planets** are a web of base sites linked like Unreal Tournament 2004's Onslaught nodes (W1-6: "Locations of Control", links cost one day). You must build a chain of bases to reach the enemy's. Each site has its own terrain map. Space battles take priority over ground battles because ships in orbit affect the ground.
- **Bunkers** are modules with systems, connected directly or by tunnels, tubes, elevators and walkways. Terrain is indestructible (node-and-edge chunks with material properties); modules break locally into auto-defined shards after Red Faction (W1-4). Outside you see only a bunker's exterior; inside, only its interior; capturing its security room reveals the whole building (W1-3, W1-4).
- **Ship interiors are side view.** Switch to a crew member on a large ship and the game turns into a Planet Front level inside the ship: man a turret, repair, launch a fighter, or board an enemy through a breaching ship (W1-5, W1-8; `PW Design bunkers.rtf` adds airlocks, purging, magnets and spikes).
- **Naming is the prize.** Default systems are unnamed and unexplored; you name what you conquer, and the winner names the system or galaxy (W1-2).
- **Modes** (W1-11): Homeworld Defence (after Starfox 2), Assault Campaign (Starfox 64's metagame), Persistent Galaxy conquest (Imperium Galactica 1/2, Galactic Civilizations 2, Homeworld's tech progression), Skirmish. V2 adds a story Campaign with branching missions, Scenario with map rotation and gamemode scripts, and a Sandbox with a spawn menu.
- **Modding** was central from the first page: factions, units, ships, maps, missions, campaigns, scripts, "completely new games", usable everywhere, with an online mod database and forum.
- **Look:** 2D sprites, one sprite per object, multi-part objects animated by moving parts (parent-child), alpha, glows and lighting; "somewhat photorealistic but slightly simplified", "90% realistic, 10% just-because-we-can", with no teleports, hyperdrives or nanomachines as plot devices (V2).

## 2. Wave 1: the scope opens up (W1, early 2010s)

The first notebook keeps the Planet Warfare name but starts asking structural questions: standardised element-based content so modders can't invent "BS values" (W1-13, after Powder Toy); Moving Frames and the Entity Framework as one model for vehicles, mechs and buildings (W1-14, W1-18, W1-19); a seamless zoom from top-down space to the side-view surface, after RayForce stage 3 (W1-15, W1-16); content tools inside the game and three ways to distribute mods (W1-20); the "Huge List" of all unique things on disk and the "Active List" built from it (W1-26 to W1-28); and loose debris absorbed, merged or grouped, with "more trash = more chaos levels" (W1-24). A topic list (W1-29) adds a spirit plane, FTL, psychic aptitude, souls and reincarnation.

W1-32 to W1-34 is a separate variant pitch: **"You are an android"** fighting a parasitic alien lifeform, "Super Metroid + Terraria", with a persistent character across worlds, a galaxy map, suit-part upgrades, a Terraria inventory, an HQ cross-section (lab, med bay, hangar, containment), combat and builder modes, a Toxigun and its opposite the Fertigun, and two-stage health (100 regenerating over 1000 long-term).

## 3. The 2013–2016 rtfs: the universe takes over

- `WorldUniverseMetagame.rtf` (2013): the Hyperverse, universes and the Emptiness between them, the Astral Plane, Astral Beings and reincarnation, psychic powers. "EDIT: It turned into explaining the very fabric of existence and purpose of life. oops."
- `CraftingMolecules.rtf` (2013), `EnergyInVideoGames.rtf` (2014), `MolSys_SpriteArt_Objects_Energy.rtf` (2016), `PW Tech & Dev & Research.rtf` (2016): the molecular system, energy forms, phenomena and composite objects. See [matter-and-making.md](matter-and-making.md).
- `PerformanceSimulations.rtf`, `UniverseBounds.rtf` (2014): a seamless hyperverse with a "group mind", and the boundary question, answered with a Wilderness edge that pushes things back "like a bowl edge" ("GOOD +10").
- `FarVision.rtf` (2014): using the background to see what's ahead in a side-view game.
- `PW research idea.rtf` (2015): research by experiments that unlock shareable knowledge objects (copied from Eco).
- `PW Multiplayer Elements.rtf` (2016): optional social features rather than shared worlds.

## 4. Wave 2: the seamless universe engine (W2)

The second notebook ("PSRC/PW 2") works on how a seamless universe could run: the anti-butterfly effect, passage of time, simulation LOD, travel levels, game area composition, far vision and its two models, event horizons per size class, chaos flux, the system layers, shifting objects into the background, time skips, triangle terrain with resource triangles, the principle of significance, primitive-shape art, exclusion meshes, the invention canvas and privacy facades. Most of [simulation.md](simulation.md) and [universe.md](universe.md) comes from here.

## 5. PSRC and the 3M system (2015–2025)

Planet Warfare needed a standard art system that could show "a pie, a person and a planet", so PSRC (Pixel Sprites ala Reactorcore) was born, then the 3M system for anything over 3 m. The PSRC notebook ("PSRC / Megastructures / PW-Universe Engine Design / 3M/96px System Detailed", scans PS) is as much about the universe engine as about art: body types, megastructure rules, the C0–C4 universe hierarchy, celestial structure and evolution, atmospheres, liquids, quakes. The packs themselves became real products (several commercial packs and the released Human Mk2 Devkit). See [art-and-presentation.md](art-and-presentation.md).

## 6. Equilibrium Universe Rules (2020)

`PW PSRC Equilibrium Universe Rules.txt` is the most mature universe document: the chaos spectrum, clumps/chunks/regions/continents/celestials/entities with sizes, the LOD path from deep space to ground, megastructure stability, the density monitor, mechanisms, ropes, the universe jurisdictions with counts (partly marked "REDO"), the universal cycle of novas, solar spawn, and star light that pulses instead of planets orbiting. The same text, lightly edited, is in the AAL lore folder as `AAL Lore, Equilibrium Universe Rules.txt`.

## 7. The NVC AI musing

`PW_NVC Based AI System Musing.docx`: NPCs act only to meet needs, communicate through feelings, remember sources and routes, share memories, think with a deliberate delay, and go dormant in pods. See [life-and-people.md](life-and-people.md).

## 8. The pitch and the descendants (2023 onward)

`Planet Warfare.txt` restates the project as a **Super Game**: "a persistent open world universe" where you play "a reincarnating regular yet malleable person", with a solo mode and a group mode, an infinite overarching goal plus a generator of finite local goals, and the industry critique. It ends by calling the project dormant: the seamless universe is "a purely technical challenge that I truly need help with", so **RoomSpace** (rooms like Super Metroid, still ragdolls) and **TopVerse** (top-down, single-collider characters, subgames on a region map) were designed to deliver the same promise more simply. **AAL Bunkerships** later brought back the side-view Cortex Command core with tile-based stages and single-sprite characters, without the universe simulation.

## 9. The rename (2026-10-24)

Reactorcore renamed the project **AAL Universe: Perpetual Boundless Freedom**, because "Planet Warfare" is too war-focused for what it became. The foreword sets the current direction:

- one continuous universe with **no rooms, stages, walls or doors**, simulated by how far things are from the player;
- a 2D side-view platformer world with directional gravity or zero gravity;
- characters as physics objects; ragdoll paperdolls were the original intent, but Reactorcore is "willing to simplify all characters to just single box/circle colliders";
- walk on terrain, go inside buildings, ride vehicles, drive small vehicles into large ones and walk around inside them, fly them between stars;
- everything interactable, destroyable and creatable with equivalent exchange and simplified, "arcady-but-not-too-arcady" rules of nature;
- modding tied to standards: "a player can determine an object's size, density and materials, but they cannot define the weight of that object or how much hitpoints it has";
- newer concepts from Reactorcore's later designs may replace the older, more primitive ones.

The AAL timeline (`reference/lore/aal-universe/AAL Lore, The Complete AAL timeline.txt`) already places the game in the **Exploration of the Universe** era, followed by Exploration of the Wilderness and To Infinity and Beyond.
