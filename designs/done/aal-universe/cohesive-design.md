# AAL Universe: Perpetual Boundless Freedom — a cohesive high-level design

**Status: Claude's proposal (2026-10-24), not Reactorcore's design.** Reactorcore asked for "a high level cohesive design... not going too deep into detail, just enough to make the basic setup sensible, possible and feasible", as a starting point to refine later. It is built from this digest (the other files in this folder record what the notes actually say) and from the newer designs the foreword says may replace older ideas: TopVerse, RoomSpace and AAL Bunkerships. Every decision here can be overturned. Each one names the source it builds on, so it's clear what was kept, merged or replaced. The open decisions are listed at the end.

## The game in one paragraph

You are one person, and the head of a small household, in an endless, living universe drawn as one continuous 2D side-view world. You walk on planets whose surfaces wrap all the way round, dig into them, build on them, drive a rover up a ramp into a dropship, walk to its cockpit, fly it into orbit and dock in your carrier's hangar. Then you climb out, go to the bridge and take the carrier to another star. Nothing is a level, a room or a loading door. Everything near you is simulated; everything far away is kept as data and catches up when you return, so places you left are overgrown, rebuilt or ruined when you come back. Every object is made of materials, so mass, strength and cost follow from what it's made of, and nothing is created from nothing. The universe tends toward calm. Danger exists but rarely comes looking for you, and you choose each session whether to garden a valley, explore a nebula, help a colony through a crisis or go to war on a frontier. When your whole household is lost, you are reborn somewhere else years later, and the universe remembers what you did.

## What stays from Planet Warfare (the non-negotiables)

These run through every version from 2011 to the foreword, so the proposal keeps all of them:

1. **One continuous universe, no rooms or stages**; what's simulated depends on distance from the player.
2. **Side view**, with directional gravity near masses and zero gravity in space.
3. **A versatile human** whose abilities come from what they wear, hold and operate (WASD, mouse, Q inventory, E context).
4. **Vehicles inside vehicles**, walkable interiors, any scale from rover to capital ship.
5. **Everything interactable, destroyable and creatable**, under equivalent exchange.
6. **Material-derived values**: players and modders set size, shape and materials, and the game derives weight, toughness and cost.
7. **The Chaos System** as a visible law of nature that keeps the game above the lag line.
8. **Persistence with aging**: the universe keeps going without you, and places change while you're away.
9. **A Wilderness edge** that takes things in and gives them back reshuffled.
10. **Rebirth after total loss**, with your past lives kept in the universe's history.
11. **An infinite goal you choose, plus endless finite local goals.**
12. **Single-player, data-driven, mod-friendly, timeless pixel-art look** (PSRC + 3M).

## Part 1: the framework

### 1. One plane, side view everywhere

**Decision:** there is no top-down space view. Space is the same side-view plane with zero gravity.

The 2011 split (top-down Space Front, side-view Planet Front) existed because ships had to turn 360° and still be walkable inside. That's solved if each ship carries its own gravity and the camera follows whatever you are inside (decision 2). A ship can roll freely in space while its crew still has a floor. This removes the 90° view switch of W1-15 and keeps one simulation, one renderer and one control scheme. *(Builds on: foreword "side-view platformer world/galaxy"; EUR's omnidirectional 5:4 screen.)*

### 2. Bodies and frames: everything nests

**Decision:** the world is a tree of **bodies**. A celestial is a body. A ship, station or building is a **frame** (Moving Frames / Entity Framework / DRC-MDRC, renamed once). Frames sit inside other bodies, and characters and loose objects sit inside a body or frame.

- Every body has its own local coordinates and its own **gravity rule**: radial toward a celestial's core, a fixed "floor" direction inside a frame (artificial gravity, switchable), or none.
- Things inside a frame are simulated in the frame's own space, so a character keeps standing on the deck of a carrier that is accelerating and rolling. Things inside a moving body are safe from outside forces but keep its momentum (PS-7).
- **The camera rotates to the local "down"** of whatever you stand in, so the floor is always the bottom of the screen near a surface. In free space with no gravity, it stays aligned with your ship.
- Nesting depth: **celestial → frame → frame → character** (for example planet → carrier → dropship → pilot). Two frame levels is enough for every fantasy in the notes and keeps the physics tractable.

*(Builds on: Moving Frames W1-14, Entity Framework W1-18, main/sub structs EUR, TopVerse DRC/MDRC, Bunkerships bunkerships.)*

### 3. Celestials are discs you can walk around

**Decision:** in side view a celestial is a **cross-section disc**. Its surface is a ring you can walk, drive or fly all the way around, and it goes down through strata (surface, crust, mantle, core) toward a centre that "down" points to.

- This is the PSRC notebook's planet-as-wedges model (PS-4d) and planet partitions (PS-14): the disc is cut into **sectors** (wedges), and each sector streams in on its own.
- **Atmosphere** is the ring of atmo cells around the disc (PS-17: 8 rects split into up to 128 cells), whose density exchange is the wind. **Orbit** is the band above the atmosphere where gravity still pulls but there's no air.
- **Compressed scale**, as W2-10 asks ("more compact than realistic, but still huge"). Proposed surface circumferences: asteroid 1–4 km, moon 8–20 km, planet 32–128 km. At walking speed a planet takes hours to circle, by rover tens of minutes, by aircraft a few minutes. Gas giants and stars have no walkable surface and need special vehicles to dive their layers (TopVerse).
- **Celestials don't orbit or spin** (EUR); stars pulse bright and dim instead, which gives day and night. This keeps systems stable and cheap and avoids moving targets for docking.
- **Far-off celestials** use 3M: dot → circle → textured circle → continents as primitive shapes → regions → terrain (EUR LOD path).

### 4. Terrain: tiles up close, shapes far away

**Decision:** at human scale, terrain is a **tile grid of materials**, half a metre per tile (16 px at 32 px/m). Above that, the same terrain is drawn as 3M shapes (regions, continents) and simulated as data.

- Every version before this (indestructible node edges, shards, triangles, overlapping clumps) stalled on digging, merging and interiors (W2-36 is a page of open questions). Tiles are the proven answer (Terraria, Bunkerships), and they make the hard parts trivial: digging removes a tile, building adds one, interiors are empty tiles behind a frame's facade.
- **Equivalent exchange becomes counting.** Every tile is a quantity of one material. Digging yields material piles (KAG-style, as in Bunkerships) that you carry, store or feed to machines; building consumes them. Nothing appears from nowhere.
- **Background wall tiles** carry the "shadow background" (EUR): when you tunnel into a region you see its dark mass behind you, not the far horizon.
- **Loose rubble** becomes clumps that settle and slowly fuse back into terrain if left alone (EUR clumps), so debris never accumulates forever.
- **Big events go coarse** (anti-butterfly effect, W2-3): a huge blast removes whole tile blocks and turns them into rubble and dust totals, instead of simulating every tile's fall.

### 5. Characters: one collider, a paper doll on top

**Decision:** every character is **a single capsule collider** for physics and gameplay, drawn as a PSRC paper doll animated procedurally (rotating parts, no frame animation). Ragdolls happen only visually, on death or a heavy knockdown.

- This is the foreword's concession ("single box/circle colliders") and Bunkerships' rule, and it is what makes crowds, vehicles and interiors affordable.
- **Body slots per limb** (head, torso, arms, legs, back, hands) hold clothing and gear flattened into the limb, as the Human Redux Plan describes. Protection is per limb, and categories 1–4 of clothing (vanity, everyday, extreme, specialist) set what environments you survive.
- **Abilities come from equipment**: magboots for hulls, jetpacks for zero-g, scuba gear, climbing hooks, suits for vacuum, heat or radiation. Duck and prone are collider changes (Bunkerships).
- **Controls**: WASD, mouse aim, Q inventory, E context, a few hotkeys (`Planet Warfare.txt`). Mouse aim pushes the camera, Soldat-style (W2-22's buffer zone).

### 6. Frames: vehicles, buildings and stations are one thing

**Decision:** a frame is a **tile grid with its own gravity**, a hull, modules and an optional facade. A rover, a house, a dropship, a carrier and a space station are all frames; they differ in size, anchoring and what modules they carry.

- **Modules** are the functional parts placed on the grid: cockpit/bridge, engines and thrusters, reactor, gravity generator, turrets, hangar, cargo hold, crew quarters, med bay, lab, workshop, airlock, doors and elevators (W1-5, W1-33, the 2011 bunker modules). Each needs supply (power, fuel, crew) through connections (`PW Tech & Dev & Research.rtf`).
- **Anchored or free**: a building is a frame anchored to terrain; a vehicle is free. Anchoring can be undone (a base that lifts off is the "mobile headquarters mothership" fantasy from RoomSpace and Gundam).
- **Facade** (2011 bunkers, W2-34 Privacy Facade, TopVerse): from outside you see the hull; step inside and the hull fades to show the interior; outsiders don't see in. Capturing a security room reveals the whole interior (W1-3).
- **Size classes:**

| Class | Size | Examples | Notes |
|---|---|---|---|
| Object | up to 3 m | tools, crates, bikes, turrets | PSRC sprites, one sprite each |
| Small frame | 3–20 m | rovers, mechs, fighters, dropships, houses | 3M hull, interior if crewed |
| Medium frame | 20–200 m | gunships, freighters, bunkers, towers | fully walkable interior |
| Large frame | 200 m–2 km | carriers, stations, arcologies | walkable decks, hangars for small and medium frames |
| Megastructure | over 2 km | ring stations, planet fortresses, Dyson parts | built as a body, like a celestial, from regions; only parts are walkable |

- **Docking and hangars**: a frame flies into a hangar module of a bigger frame and becomes its child (TopVerse pack/unpack; RoomSpace dock points). An APC rule applies: destroy a carrier, and what it carries is in danger (TopVerse).
- **Megastructures** follow EUR's stability rules: monolithic is stable, finely split is fragile, and overloading a place with mass can collapse it into something new.
- **Damage**: tiles of the hull break off, modules stop working when their tiles are destroyed, and boarding happens through breaches, airlocks or open hangar doors (2011 bunkers). Mechanisms stay cheap: doors, hatches, elevators, cranes, pistons, rotators along a line or around a point (EUR).

### 7. Matter and making

**Decision:** a small fixed set of **material groups** with derived stats, plus a three-part making rule. The full molecular ambition (players inventing new elements) is kept for modders, not the base game.

- **Material groups** (from TopVerse's bundles, extended with the notes): light metals, heavy metals, rock and minerals, hard organics (wood, chitin), soft biomass, ice and water, volatile chemicals, inert chemicals, exotics (degenerate matter from black dwarfs, anomalous matter from the Wilderness). Each has density, toughness, conductivity, heat tolerance, flammability and **phenomena** (light, magnetism, radiation...).
- **Derived values**: an object's mass, hit points, cost and salvage come from its shape and materials. Make a 10 m boulder out of cardboard and it will be light, flammable and fragile (`MolSys`).
- **Making anything takes** materials, a creation environment (a bench, a fabricator, a shipyard) and knowledge (a blueprint), plus time, which better environments shorten (`PW Tech & Dev & Research.rtf`).
- **Knowledge objects** (from Eco): experiments in labs unlock blueprints, which are data: copyable, tradeable, shareable, and losable if every copy is destroyed (NVC musing: libraries and vaults matter). No experience levels; power comes from what you know, own and can build.
- **Supply chains** are physical but light: things need inputs (power, fuel, ammunition, food) through matching connections (sockets, pipes, wires, conveyors that are force rectangles, not real belts).
- **Energy** uses the four forms (`EnergyInVideoGames.rtf`): projectiles and beams (solid form), tile-cell fields such as heat, gas and radiation (area form), blasts and exhausts (fall-off form), and gas or slime creatures (being form). Liquids and gases are tile-cell fluids inside the live bubble and atmo or canvas cells beyond it (PS-17, PS-18).

### 8. The simulation: one live bubble, a ledger for everything else

**Decision:** three tiers, plus seeds and deltas for storage.

| Tier | Range (proposed) | What runs |
|---|---|---|
| **Live** | about 1 km around the player, and around the frame you're in | full physics, tiles, fluids, NVC AI, combat |
| **Near** | 1–10 km | coarse movement, simplified AI, no fluids; frames and NPCs as moving tokens |
| **Ledger** | everything else | data only: faction holdings, populations, settlements, fleets, celestial state; updated by a background routine every few minutes (EUR density monitor) |

- **Storage = seeds + deltas.** The generator recreates any untouched place from its seed and its parent's properties (W2-7). The save keeps only what changed: dug and built tiles, frames, named places, persistent NPCs, faction state. Natural content is regenerated; unique artificial content is remembered. This is what keeps a whole universe on a hard drive and answers the "out of disk space" worry (W1-31).
- **Persistence quotas** (TopVerse persistence tiers): your sanctuary and owned frames are truly persistent; places you've claimed are semi-persistent; everywhere else is seed plus aging. Over the quota, the Chaos System merges or forgets the least significant.
- **Coming back** (passage of time, W2-4): a place leaving the ledger gets the elapsed time and the events that touched it applied before it loads: overgrowth, decay, rebuilt or conquered settlements, flooding, ruins.
- **Seamless streaming**: celestial sectors stream in around the live bubble; the far view (decision 10) covers the gap visually, so there is never a "chunk not loaded" edge.
- **Instant switch range**: you can switch to a household member who is inside the live or near tier without loading (W1-28).

### 9. Speed bands and travel

**Decision:** travel is continuous up to sublight, and FTL is a sensor-view journey with real interruptions.

| Band | Where | View | How |
|---|---|---|---|
| Foot | surfaces, interiors | 100%, zoom 50–600% | walking, climbing, jetpack |
| Ground and air | surfaces, atmosphere | zoom out to 50% | rovers, mechs, aircraft; live bubble stretches ahead in the direction of travel |
| Orbit and sublight | between celestials in one system | 25% "epic scale", then the far view | ship flight in zero-g; simplification by speed (W2-5) |
| FTL | between star systems | sensor view (a system/galaxy map drawn by your ship's sensors) | a jump with a duration; can be interdicted into a real encounter (TopVerse tunnels and reticles) |
| Deep FTL | between galaxies, toward the Wilderness | sensor view | long journeys needing better drives |

- **Proposed travel times** instead of real distances: crossing a system at cruise takes 2–10 minutes; an FTL jump to a neighbouring star 30–90 seconds of sensor travel; crossing a galaxy is an expedition of many jumps.
- **FTL follows AAL lore**: it slows to a crawl near big gravity and is useless below about a moon's high orbit, so descent and launch are always flown. That makes the seamless space-to-surface transition (W1-15, RayForce) a real flight through the entry field instead of a cutscene.
- **Sensor views are devices** (W2-9): better sensors show more, in different spectra (thermal, radiation, pressure), and leaving the view is instant.

### 10. Seeing ahead: the far view

**Decision:** the background is a **live far view** using the **sector-based model** (W2-16 Type 2) with a fixed detection limit.

- Distant bodies appear in the centre as desaturated dots, grow and drift toward the screen edge they'll arrive from (W2-12, `FarVision.rtf`); you can see up, down, left and right. Only ambient light reaches the background.
- **What appears** is chosen by potency (size and brightness against distance, W2-15), within your current sector and its neighbours. Type 2 is chosen over the realistic Type 1 because it caps the list and fits the ledger's sectors.
- **Underground**, the region's shadow background replaces the horizon (EUR).
- Objects can cross between the background and the play layer (a missile arcing out of view and back, W2-17).

### 11. The Chaos System, with real budgets

**Decision:** keep the Chaos System as lore and law, and give it **explicit numeric budgets** per live bubble (objects, active physics bodies, AI agents, fluid cells, particles, mechanisms) that are part of the content standard.

- **Graded response** (EUR spectrum, W2-21 chaos flux): first invisible (merge rubble, sleep distant bodies, lengthen AI delays), then visible (space-time shimmer, objects folded into clumps or "absorbed" into rifts), then severe (local storms that displace things into the Wilderness). Never let the frame rate reach the lag line.
- **It's diegetic and predictable**: crowded places feel stormy, so players learn to build sensibly. Excess never just vanishes; it goes to the Wilderness pool and can come back (AAL lore).
- **Content checks at startup** (W2-34): mods that exceed part counts or mechanism limits get a higher culling priority, or a warning.

## Part 2: people

### 12. You and your household

**Decision:** one model, the **household**. Solo play is a household of one.

- A household is **you plus up to 8 members** (nine in total, the TopVerse formation): family, crew, partners. You switch freely to any member in range (`Planet Warfare.txt` group mode); the others follow simple orders (follow, guard, work, go there) and live by the NPC needs model when you're not controlling them.
- **The sanctuary** is your household's home: a settlement, a building or a frame, with a **revival facility**. In the Exploration era the Homo Mugen have digital immortality (AAL timeline), so a dead member is restored at the sanctuary after some in-game time, and you continue as someone else at once.
- **Extinction**: if every member is dead, or the sanctuary falls with no one left to restore, your soul returns to the astral pool. You are **reborn elsewhere** in the universe into a new family after a long time skip. The old sanctuary becomes ruins that others, or you, may find (`Planet Warfare.txt`, TopVerse).
- **Rebrand** (TopVerse character manager): change your own look and name any time, so you never need to reset a universe to feel new.
- **No grind** on rebirth: the new family's situation decides your start (spaceport nearby or stone tools), and everything you knew is still out there to reclaim.

### 13. NPCs: needs, feelings, memory, delay

**Decision:** keep the NVC model's shape, with a deliberately small first version.

- **Eight needs** (subsistence, safety, freedom, growth, fun, meaning, respect, care), each a number. An NPC picks the most urgent and uses a short list of default strategies per species (eat at home, go to work, flee danger, seek company).
- **Feelings** are shown with emotes and speech bubbles ("please" / "thank you" phrasing), so the player can read why someone acts.
- **Memory**: a few records per NPC (people and places marked safe, dangerous or unknown; which strategy worked), with forgetting. NPCs share memories by talking, so word of what you did spreads.
- **Delay**: NPCs decide every half second or so, longer under chaos (they're awestruck), which is both cheap and fair.
- **Pods and homes** let NPCs go dormant inside buildings; break the building and they come out (NVC musing).
- **Paradigms** (sustainability, equality) come later, as a second layer for factions and leaders.

### 14. Factions and civilisation

The Exploration era's civilisation is a "soft utopia" (AAL lore), so most of the settled universe is peaceful. **Factions** (colony governments, companies, research groups, guilds, nomad fleets, and on the frontier, outcasts, warlord remnants, rogue machines and space monsters) live mostly in the ledger: holdings, attitudes and needs, updated on the background tick. Their attitudes toward you change with what you do, per region (TopVerse karma proposal, the fear/loyalty index). War is one situation among many, mostly on frontiers.

## Part 3: why you play (the metagame)

### 15. Equilibrium and calamities

**Decision:** adopt TopVerse's rule. **Nothing bad comes to you unless you provoke it or go where it lives.** Natural cycles (star flares, quakes, storms, floods) are real but **telegraphed** with warning signs, so living somewhere is a choice, not a trap.

- Poking a dangerous place (a monster nest, a derelict reactor, a warlord's border) can start a **calamity**: a growing crisis over an area that makes a permanent change unless you stop it. Calamities can chain but never end the universe; at worst you relocate.
- **Disasters scale with empire** (TopVerse): a small household is threatened by small things; a big civilisation is stable but can be hit by bigger events.
- This keeps the cozy-or-intense choice in the player's hands, which the foreword's complaint list ("Simon Says", "something that ruined it") asks for.

### 16. Callings and situations

The structure `Planet Warfare.txt` asks for: an infinite goal plus endless finite ones.

- **Callings** (choose one or several, change any time): **Guardian** (seek out what threatens the universe and stop it), **Gardener** (cultivate places into well-kept, beautiful worlds), **Pathfinder** (reach and understand the edge: the Wilderness), **Founder** (raise your household into a civilisation that can take on anything), **Free spirit** (no calling; just live). A calling changes which situations are highlighted, not what's allowed.
- **Situations** are finite goals generated from the **real state of the world**, never scripted: a better place to settle, a crossing you can't make on foot, a nest growing, materials your settlement needs, a stranger needing help, a cave with ruins, an anomaly on the horizon, a city to explore, a hostile border, an incoming storm, an unreachable place that needs research, a factory to build (the list in `Planet Warfare.txt`). They reach you through sensors, comms and people, and through the **situation board** in your sanctuary.
- **Session flow**: boot up, see "clearly highlighted routes" (situations near you and for your callings), pick one or ignore them all, and play. Every session ends at a safe point; the game saves continuously (Super Game "convenient exit points").

### 17. Naming, records and mementos

- **You name what you find or claim**: planets, systems, settlements, ships (2011's prize, kept).
- **The Chronicle**: the universe's history of your lives (places named, calamities stopped or caused, households lost and reborn), readable in the sanctuary, and the source of the "deja vu" when you return somewhere.
- **The Wilderness pool** keeps unique things lost to chaos or the edge, so a ship you lost may drift back one day.

### 18. Endgame

There isn't one; the AAL timeline's last eras are the shape of it. **Exploration of the Universe** (the main game), **Exploration of the Wilderness** (understanding and using the edge: "throw bad stuff in, get bad stuff out"), and **To Infinity and Beyond**: once settled, the universe keeps decaying, reshuffling and surprising, so there's always somewhere wild, something to rebuild, and someone in need. At the very top end, a civilisation can move celestials, build megastructures, and even trigger or defuse a nova or a big bang (EUR universal cycle).

## Part 4: setting

Set in the AAL **Exploration of the Universe** era: after the space monster wars, humanity (Homo Mugen) and allied aliens colonise beyond the Milky Way, and the edges of the universe are coming into view. This fits everything the notes want:

- **Peace by default**, with frontier danger: remnant space monsters, rogue machines, anomalies, dimensional fallout from old superweapons, groups that refused the galactic community.
- **Digital immortality** explains respawning; the **astral realm** explains total-loss rebirth and the rare psychic powers.
- **FTL limited by gravity** keeps planets and descents physical.
- **The bowl universe and the Wilderness** are already AAL canon (`AAL Lore, Universe Basics.txt`).
- **Every other AAL game** happened in this universe's past, so its ruins, wrecks, relics and superweapon sites can be found: the first source of "ancient ruins" content.

## Part 5: what's cut or deferred, and why

| Idea | Status | Why |
|---|---|---|
| Physics ragdoll characters | visual only | the foreword's own concession; crowds, vehicles and interiors need cheap characters |
| Top-down space front | cut | one side-view plane with frame gravity does the same job (decision 1) |
| Turn-based tactical overview | replaced | by the ledger, sensor views and situations; the universe never stops for turns |
| Node-edge, triangle and clump terrain | replaced by tiles | tiles make digging, building and interiors simple; shapes stay for far LOD |
| Hyperverse, other universes | lore only | the later docs describe one universe with a Wilderness edge |
| Orbits and spinning planets | cut (EUR) | pulsing stars give day and night; static celestials stay stable and dockable |
| Players inventing elements | modding only | the base game uses fixed material groups |
| Psychic powers | later layer | needs its own presentation (the musing says so); fits as a rare late capability |
| Full NVC paradigms | later layer | the needs/feelings/memory core comes first |
| Public multiplayer | cut | "an apocalyptic griefing nightmare"; asynchronous sharing and visits instead |
| Console modding | later | the vetted-purchase idea from `Planet Warfare.txt` stays as the plan |

## Part 6: proposed numbers (all to be tuned)

| Thing | Value | Source |
|---|---|---|
| Pixel scale | 32 px = 1 m, human 60 px | EUR, PSRC |
| Tile | 0.5 m = 16 px | proposal |
| Screen at 100% | 40 × 32 m | EUR |
| Zoom | 600% in, 50% on foot or with binoculars, 25% in vehicles via interface | W2-13, EUR |
| Object limit (sprite-built) | 3 m pixel art; components up to 10 m | 3M, EUR |
| Live bubble | about 1 km | PS-44, NVC musing |
| Near tier | 1–10 km | NVC musing |
| Ledger tick | every 1–10 minutes, zone by zone | EUR |
| Household | you + up to 8 | TopVerse |
| Frame nesting | 2 levels inside a celestial | proposal |
| Planet circumference | 32–128 km; moon 8–20 km; asteroid 1–4 km | proposal |
| Universe | 7 superclusters × 7 local clusters × galaxies and voids, about 64 systems per galaxy, about 8 celestials per system | EUR (marked REDO there) |
| Detection limit for far view | sector plus neighbours (EUR's 100 AU in real terms) | W2-16 |

## Part 7: build order — five playable milestones

Each milestone is a game someone could play and enjoy, so the project ships something early and never depends on finishing everything:

1. **One strip**: a few kilometres of one planet's surface. Tiles of materials, one character, digging and building with piles, a workbench, one rover frame you can drive and walk into, simple day and night. (Close to AAL Bunkerships' sandbox; proves tiles, materials, frames.)
2. **One world**: the whole planet as a disc you can circle, sector streaming, the live/near/ledger tiers, passage of time on return, far view, atmosphere flight, orbit, a ship frame with a hangar holding the rover (nesting), the Chaos System's first budgets.
3. **One system**: several celestials, sublight flight between them, descent and launch through entry fields, settlements with needs-driven NPCs and pods, the household and sanctuary with revival and rebirth, situations and callings.
4. **One galaxy**: FTL sensor travel and interdiction, galaxy generation (C3–C4), factions in the ledger, calamities, knowledge objects and labs, ruins of earlier AAL eras.
5. **The universe**: the full C0–C2 generator, the Wilderness and its pool, megastructures and moving celestials, the visible chaos events at their most dramatic, mod tools and the standards check.

## Part 8: decisions for Reactorcore

Open choices this proposal makes provisionally; each changes the design if decided differently:

1. **Single collider characters with visual ragdolls only?** Or keep a simplified 6-limb physics ragdoll for the player only (the Human Redux Plan allows this for one character)?
2. **One side-view plane** for space too, or a top-down space mode after all?
3. **Celestials as walkable discs** at compressed scale: are 32–128 km planets the right feel, or should they be smaller (faster to circle) or bigger?
4. **Tiles** for terrain at human scale, and is 0.5 m the right size?
5. **Household size** (9), and are members recruited or born into your family?
6. **Equilibrium rule** (nothing comes unprovoked) versus the `Planet Warfare.txt` example of a natural disaster striking a settlement: is "telegraphed natural cycles" the right middle?
7. **Callings**: the right set, or should the infinite goal come from the universe (the edge, the space monster remnants) instead?
8. **Which earlier AAL eras' remains** should be findable (superweapon sites, Standalone probes, Bunkerships wrecks)?
9. **Psychic powers**: in or out of the base game?
10. **Resource groups**: the nine proposed, or TopVerse's seven?
11. **The title on the site**: the site's AAL lore page is also called "AAL Universe", so a future showcase page needs a slug and a short title that don't clash (for example `aal-perpetual-boundless-freedom`, titled by its subtitle).
