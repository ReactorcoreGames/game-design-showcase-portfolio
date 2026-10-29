# TopVerse: design digest

This folder is the text form of TopVerse's design, transcribed from 49 scanned notebook pages in `C:\08 Projects\Project_Topverse\2 !scans\` plus the project's text files and the Syndemic material it grew from. Read this instead of the scans. The process is in `workflow/scan-digest.md`. Digested 2026-10-23.

## Summary

TopVerse ("Top-view Universe") is a persistent, procedurally generated universe built from 30+ small top-down twin-stick games that share one standardised framework: one character with 10 item slots and auxiliary abilities, destructible levels, simple physics, a procedural level generator and a campaign generator. The subgames run from a microbe shooter (Syndemic, where it started) through human-scale civil-service jobs, a psychic fighter, real-time Pokemon-style monsters and a cozy "Civilian Animal Crossing" default mode, up to fleet combat, mecha and kaiju, hyperspace god machines, a city builder and a transport tycoon. They all happen in one universe: you make a decision on a region map (an Advance Wars-like grid), play it out on foot in a generated room network or in a vehicle arena or tunnel, and the result permanently changes the tile, the region and everything above it. The universe is an **equilibrium**: nothing bad comes to you unless you provoke it, so it can be as cozy or as violent as you choose. It scales from 10 m rooms to a universe of hundreds of millions of potential celestials, kept affordable by storing only data and generating everything else on demand. Buildings and vehicles share one model, the DRC/MDRC, which exists as an on-foot entrance and interior, a vehicle-layer facade, a map icon and a data node, so the same ship can be boarded, fought, flown and traded. Fleets of four pack into a flagship, travel by drive shaft through tunnels, and get shot at by anti-FTL reticles.

TopVerse, RoomSpace and Planet Warfare ("PW") are Reactorcore's three attempts at the same dream: a persistent play universe simulator. This design is self-contained.

## How the design evolved

1. **Syndemic** (2021): Reactorcore beta-tested Adjuvant's microbe shooter and wrote a long overhaul report (room networks, highways, a modular room generator, diseases as recipes, standardised tiers, collateral damage). Adjuvant gave up on the game. See [origin.md](origin.md).
2. **The hijack** (`4 Syndemic Hijack Project Aka Topverse.txt`): the same systems reframed as other games (Regime Eradicator, civil service, alien wars, mecha, kaiju, X-COM, Pokemon TCG, Hyperspace God Mecha), which Reactorcore then saw as pieces of one larger game.
3. **The text notes** (`1 TopverseNotesBU2_Cleaned.txt`, the core document, plus the layers, slot and defence txts): principles, the list of 33 games, Unigen scales, spheres of influence, game flow, characters, fleets.
4. **Test Notes 1–29 and the two BigScans**: the chaotic brainstorm (Reactorcore's word): subgame toolkits, buildings and vehicles, damage, exits and escapes, altitude, arenas, tunnels, a prototype star system, the Wilderness, cell contents.
5. **The Book** (2–16, sticky notes): the refinement. Layer systems, structure faces, rejected multi-floor buildings, ghosts, character sprites and portraits, the energy cycle, scrolls, celestial layer documentation, star system generation, drive shafts, arena doors, space movement, pack/unpack, anti-FTL reticles.

**Later sources supersede earlier ones where they conflict.** The topic files state the later version and note the earlier one.

## Files

| File | Covers |
|---|---|
| [origin.md](origin.md) | Syndemic, the overhaul report's systems that TopVerse inherited, the weapon slot system, the hijack |
| [subgames.md](subgames.md) | The shared frame and all 33 subgames by group, with every described toolkit and ruleset |
| [on-foot.md](on-foot.md) | On-foot zones, room networks, exits, emergency escapes, the shared inventory, crew kit, ghosts and vertical targeting, how characters are drawn, building collapse, fire |
| [vehicles-and-fleets.md](vehicles-and-fleets.md) | DRC/MDRC faces and rules, facade, damage and penetration, defences, size, altitude and falling, ejected crews, fleets, flagship pack/unpack, drive shafts, population control |
| [travel-and-combat-layers.md](travel-and-combat-layers.md) | Combat zones, vehicle arenas and doors, region travel, tunnels, star system movement, sublight/FTL/hyperspace, interdiction, the anti-FTL reticle, defence structures by scale |
| [universe.md](universe.md) | Scales, storage, spheres of influence, tile contents, vertical layers per celestial type, star system generation and grid effects, the Wilderness, the energy cycle, chaos system, scrolls |
| [metagame.md](metagame.md) | Purpose, modes, the region-view loop, equilibrium and persistence principles, characters, start/mid/endgame, resources, wildlife loyalty, growth and modding |
| [transcript/](transcript/) | Scan-by-scan transcripts in 5 chunks, with all text and diagrams described; the source for everything above |
| `TopVerse.txt` | Reactorcore's condensed overview, kept as is |

Each topic file ends with **Proposals**: Claude's suggestions for topics Reactorcore titled but never filled in, or left undecided. Reactorcore authorised this. They are clearly separated from the design itself. Elsewhere, *(interpretation)* marks Claude's reading of an unclear note.

## Scan codes

- **TN1–TN29**: `Topverse Test Notes (1).jpg` … `(29).jpg`, small grid notepad pages.
- **BS1–BS2**: `TopverseBigScans (1).jpg`, `(2).jpg`, two large loose sheets.
- **B1–B18**: `TopverseBook (1).jpg` … `(18).jpg`, a notebook of sticky-note spreads. B17 and B18 are rescans of BS1 and BS2.

Reactorcore's count was 50 scans; the folder holds 49.

## Glossary

- **TopVerse**: "Top-view Universe". **Multi Combo Mega Game / Nexus Game / super game**: Reactorcore's names for the whole.
- **Subgame**: one of the 30+ themed games on the shared framework. **Quick play**: a throwaway standalone run. **Persistent world**: the universe mode.
- **Region view**: the map where you make the next decision; time passes only on moves and actions; no end turn.
- **Area tile**: the persistent map cell (1–10 km²). The tile persists; its contents (room network, DRC zone) are random each visit. **Region** (10x10 to 25x20 tiles), **continent** (3x3 regions), **celestial** (1/2/4/6 continents wrapped into a sphere), **star system** (11x11 grid), **star sector** / **cloud** (5x5 or 7x7), galaxy, clusters, **universe**.
- **Unigen**: the universe generator. **Spheres of influence**: each scale shapes the ones below it and is changed by them in return.
- **Wilderness**: the universe's border, a chaos-ruled lost & found that recycles matter and energy (the **energy cycle**) and hosts oddities and user challenges.
- **Chaos system**: enforcer of performance and density quotas; **chaos storms** when quotas are exceeded.
- **Equilibrium universe**: nothing bad comes unprovoked. **Calamity**: a crisis the player triggers, which makes a permanent change unless stopped.
- **Hub**: a persistent, player-customised settlement district with a **nexus** screen, under a density quota.
- **Room network**: a generated chain of on-foot rooms (Syndemic-derived): **E** entry, **C** corridor, **L** location, **T** layer transit. **Highway room**, **toll gate**, **Main Insertion** in the Syndemic version.
- **DRC / MDRC**: (Mobile) District Room Complex: a building / vehicle or mobile base. **MV**: major vehicle. Faces: **entrance** (superstructure, foundation), **interior** (each entrance cell = a 3x3 interior cell), **facade** (vehicle layer), **map icon**, **far-layer data node**.
- **Vehicle Entity / Overlay Facade**: a vehicle's rectangular true collider / its optional freeform art on top.
- **Hull hit / interior (penetrating) hit**: damage to the superstructure / to one random interior cell "from above".
- **Separated-cell DRC**, **mobility coaster**, **phantom girders / bio struts**: non-adjacent MDRC cells, their propulsion visuals and their connecting frame.
- **Fleet**: up to 4 ships. **Flagship**, **docking gantry**, **pack / unpack**, **adjustable ring spawn**. **APC effect**: a destroyed flagship destroys what it carries.
- **Drive shaft**: an abstract component for fleet binding and long-range travel (gantry, fleet propulsion, interdiction defences, forward plasma lance), reached on foot through **drive shaft nodes**. **Subterrain boring drive shaft**: the drilling version.
- **Vehicle arena**: a tile's vehicle combat zone, with a central **parking space (P)** and requirement-driven edge **doors** (up to 4 per side). **Ghost mode**: the no-physics slide through a door.
- **Combat zones 1–3**: orbit/upper atmo; sky/surface/soil-sea; the far depths.
- **Tunnel**: a temporary scrolling corridor for travel and transit combat (in-region, FTL, hyperspace, any medium). **Cruise mode**, **interdiction**, **quick combat space**.
- **Anti-FTL reticle**: a random-scatter targeting circle used by **anti-FTL (direct)**, **potshot** and **chaser** gunners.
- **Sublight / FTL / hyperspace**: tile by tile; jump within a system and between stars; structure-based instant one-way catapult (**hypergate**).
- **Ghosts**: how entities on other vertical layers are drawn. **Pinpoint vertical targeting**.
- **Layer pictograms** (B10): surface/shallows/fog, underground/underwater/under fog, bedrock/depths/deep fog, plus orbit, high altitude, sky, crust, mantle, shell, core.
- **Micro BIO**: the microbe scale (Syndemic).
- **EMTAG**: "electromagnetic thermo atomic graviton" variable weapon (Super Warrior). **TTO**: Tacticool Teenage Operator. **PKMN**: the Pokemon-like monsters (Evolver Devourer); kaiju are their huge forms. **God machine**: an MDRC-sized superweapon mecha.
- **Synchronisation percentage / astral score**: the Astral Psychic Fighter's power level; awakening tiers Super to God.
- **Scrolls**: messages and user content attached to contexts, with clearance levels from Angel/0A to God/99.
- **MIA / KIA / lost & found list**: what happens to ejected crews.
- **Rebrand / Partners / Randoms**: the later character manager.
- **Fear/loyalty index**: regional wildlife attitude toward humans and factions.
- **Token Fleet Pack**: paper tokens for prototyping.
- Explained by Reactorcore after the digest (2026-10-23): **AFF** = *Angels Fall First: Planetstorm*, an indie game of walkable warship interiors (crew stations, repairs, launching fighters, boarding by dropships, FPS fights in the corridors), the namesake of the Planetstorm subgame. **MMS** = *Mutant Minx Successor*, an unrelated erotic visual novel idea of Reactorcore's; why it is mentioned in TopVerse is forgotten, so treat the two MMS mentions as noise. **FTL cups**: probably FTL traffic infrastructure that launches and catches starships, organising FTL travel at busy places like homeworlds and major colonies. **8089-style RPG** = *8089: The Next Action RPG* (Steam). **Ad Circus**: see [metagame.md](metagame.md).

## Main conflicts and how the digest reads them

| Topic | Earlier | Later / chosen reading |
|---|---|---|
| Fleet size | TN27–28: 8 vehicles per fleet, up to 4 fleets per arena | Notes Fleet Unpack-Pack, B14, B15: **max 4 ships**. B13's drive shaft "connects up to 8 vehicles for journey transit" stands beside it; see the proposal in [vehicles-and-fleets.md](vehicles-and-fleets.md) |
| Multi-floor buildings | TN3 explores collapse across floors (already flagged "not for Unigen") | B4: **one entrance, one floor plan** per (M)DRC |
| Space travel | B7: escape velocity, momentum drive, separate sub-FTL/FTL moves (crossed out) | The start-to-end tunnel ("S…E system"), tile doors, FTL jumps (B13, B15, B16) |
| Character face | TN5: head turned face-up to the camera | B8: three-sprite human (face-up is one head option) plus a hover portrait with emotion overlays |
| Characters | Notes: 9 slots (1–3 immortal, 4–6 saved, 7–9 random) | Notes, later "character manager": Rebrand + presets, Partners ("formerly slot 2–6"), Randoms ("formerly 7–9") |
| Universe grid | Notes draft: 8x8 50/50 universe, 2x2 superclusters, 4x4 galaxies, 8x8 zones | Notes tile listing: universe even grid + wilderness border, 3x3 galaxies/clusters (30/70), 5x5/7x7 sectors, 11x11 systems |
| Region size | Notes "Region map": 10x10 up to 50x50 tiles | Notes tile listing, TN26: **10x10 to 25x20** (max 500 tiles) |
| Area tile size | 1–10 km² (Notes 2.0, B5); B7 writes "9 km²"; the early draft used 10 km² city maps of 1 km² cells | Kept as 1–10 km²; B10 slices "a single 10 km² area tile". Proposal in [universe.md](universe.md) |
| Vehicle zone | layers txt: vehicle level 1 km, "no human" | TN28: vehicle arena is a "10 km² zone" (a whole tile) |
| DRCs per on-foot room | layers txt: up to 4 | B4: 2–4; B2 (city builder): 4 max, one per corner |
| Regions per continent | Notes: 3x3 | B5 drawing shows a continent with 6 numbered regions (read as continents per celestial; proposal in universe.md) |
| Vehicle play on the map | layers txt: cross-layer combat on the area layer as RPG-style turn attacks | B12: area grid becomes 4X-style strategy; battles happen in generated zones, fleet vs fleet |
| Penetrating hits | layers txt Alt1 (special weapons only), Alt2 (attacker chooses) | Both rejected in the same file; "New3": circumstances decide |

## Source table

| Scan | Title / content | Status | Fed |
|---|---|---|---|
| TN1 | Teenage Tacticool Operator (TTO) | core | subgames |
| TN2 | Miner vs Beasts / Demolition expert | core | subgames |
| TN3 | Building/Structure Collapse mechanics | core (later rejected by B4) | on-foot |
| TN4 | Fire Spreading System | core | on-foot |
| TN5 | Character Face on top-down view | core (refined by B8) | on-foot |
| TN6 | Super Warrior (EMTAG) | core | subgames |
| TN7 | Civilian Animal Crossing | core | subgames, metagame |
| TN8 | Grid cell and character pixel sizes | core | on-foot |
| TN9 | Support Pillars | core | on-foot |
| TN10 | Exterior → interior 3x3 mapping, wall exits; second page "Exterior / Interior" | core; second page **headings only** | vehicles-and-fleets |
| TN11 | Vehicle layer damage | core | vehicles-and-fleets |
| TN12 | Vehicle Setup (Entrance) | core | vehicles-and-fleets |
| TN13 | Vehicle Setup 2 (interior areas) | core | vehicles-and-fleets |
| TN14 | Interior cell supports, walls, doors, armour | core | vehicles-and-fleets |
| TN15 | Vehicle Level Setup (the Facade) | core | vehicles-and-fleets |
| TN16 | Vehicle Level Mechanics | core | vehicles-and-fleets |
| TN17 | Separated Cell DRCs | core | vehicles-and-fleets |
| TN18 | Vehicle/MDRC personnel class/role | core | on-foot |
| TN19 | Altitude Ranges | core | vehicles-and-fleets |
| TN20 | Room exits on foot | core | on-foot |
| TN21 | Universal cross-character item inventory | core | on-foot |
| TN22 | DRC/MDRC fleet exploration room network | core | on-foot |
| TN23 | Emergency escape | core | on-foot |
| TN24 | Regional Pokemon Fear/Loyalty Behaviour Index | core | metagame |
| TN25 | People ejected from vehicles | core | vehicles-and-fleets |
| TN26 | Region-to-region entry determination | core | travel |
| TN27 | "Tunnel" travel for vehicles/fleet | core | travel |
| TN28 | (Major/MDRC) Vehicle Arenas | core (fleet of 8 superseded) | travel |
| TN29 | Prototype Star System (grid-based) | core | universe |
| BS1 | Topverse Unigen: Wilderness | core | universe |
| BS2 | Cell contents → biome, area grid, layer column | core | universe |
| B1 | Notebook cover "Topverse" | **title only** | — |
| B2 | Token Fleet Pack; Multi Combo Mega Game; City Builder/World Terraformer | core | metagame, subgames |
| B3 | Vehicle/char categories, Crash Derby, Planetstorm, Evolver Devourer; Transport Network; EvolDevour ideas; Pokemon TCG monster defines | core | subgames |
| B4 | Vertical layer stack; scale chain; Struct–Vehicle faces; Build/Struct Collapse Advanced (rejected) | core | universe, vehicles-and-fleets, on-foot |
| B5 | On-foot room sublayers; Action mode ghosts and vertical targeting; Celestials ALT sizes | core | on-foot, universe |
| B6 | Topic list; Region combat/transit considerations; terrains and traversal; population control | core (mostly open topics) | travel, vehicles-and-fleets, metagame |
| B7 | Space travel idea (crossed out, replaced by S…E tunnel); topic list; Max MDRC size; Altitude/crash fall | core (part rejected; personal todos ignored) | travel, vehicles-and-fleets |
| B8 | "Humans" sprite styles; TopVerse Human; Checking faces; Syndemic-hijack project | core | on-foot, origin |
| B9 | Topverse Energy Cycle; User defined scrolls | core (partial spread) | universe |
| B10 | Celestial layer legend and DOC parts 1–4 (planets, stars, giants, sizes, remnants) | core | universe |
| B11 | Celestial movement/combat; space features; star system generator variables; stellar grid effects | core | universe, travel |
| B12 | Separating vehicle play from the area grid; area tile contents; space → orbit → layers; Planetstorm movement modes | core | travel, universe, subgames |
| B13 | Vehicle advanced travel; MDRC access vs size; Drive Shafts; Drive Shaft occurrence/model | core | travel, vehicles-and-fleets |
| B14 | Exiting a vehicle arena; region vehicle travel; 4-door exits; requirement-driven doors | core | travel |
| B15 | Space movement (star system); vehicle space travel; fleet pack-unpack; vehicle combat zones | core | travel, vehicles-and-fleets |
| B16 | Escape/Leave/Retreat (**headings only**: Arena, Tunnel); Cruise mode combat; anti-FTL reticle; tunnel chase HUD | core; one note **unfinished** | travel |
| B17 | Rescan of BS1 | **duplicate** | — |
| B18 | Rescan of BS2 | **duplicate** | — |

## Other sources

- `C:\08 Projects\Project_Topverse\0 Syndemic - loose inspiration to TopVerse\`: `2 RC's Syndemic Report V1.html` / `RAW WIP SyndemicReport.md` (Reactorcore's overhaul report for Syndemic v0.43, about 35% finished) with its images in `SyndemicReport.assets/`; `1 Adjuvant's Syndemic Indiegogo Page.doc`.
- `C:\08 Projects\Project_Topverse\1 !txts\`: `1 TopverseNotesBU2_Cleaned.txt` (the core notes), `2 Syndemic - enemies_hazards.txt`, `3 Syndemic design - weapons.txt`, `4 Syndemic Hijack Project Aka Topverse.txt`, `5 Topverse system layers n mechanics.txt`, `6 Topverse weapon slot system VARIANTS.txt`; `misc relevant/`: `Topverse Combat Defence Structures.txt`, `AAL civilization prompt artstyle.txt` (a prompt brief for a clean, prosperous, colour-coded future civilisation look, usable as an art direction reference), `Pokemon TCG types.pdf` (type reference, not read).
- `TopVerse.txt` (in this folder): the condensed overview.

Topics Reactorcore left open that no source answers (listed so nobody invents them silently): the "how to make Unigen not suck" section (title and concerns only), continent details ("???"), the star system section of the universe generation notes (empty), the Escape/Leave/Retreat note (B16), the TN10 "Exterior / Interior" page, the number of Partners, modding, the falling-out-of-a-DRC and digging-into-the-sea todos, B6's topic list and B7's character tracking/followers. Claude's proposals for most of them are in the topic files.
