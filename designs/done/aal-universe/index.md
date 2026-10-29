# AAL Universe: Perpetual Boundless Freedom — design digest

Formerly **Planet Warfare** ("PW"), renamed by Reactorcore on 2026-10-24 because the old name was "too war focused" for what the project became. This folder is the text form of the design, transcribed from 132 scanned notebook pages in `C:\08 Projects\Project_Planet Warfare\` plus the project's text, rtf, doc and docx files. Read this instead of the scans. The process is in `workflow/scan-digest.md`. Digested 2026-10-24.

## Summary

A persistent, endlessly playable universe simulator played as a 2D side-view action game. You are an ordinary, versatile person (or a small group you switch between) in one continuous universe with no levels or rooms. You walk on planets, dig and build, enter buildings, drive vehicles into bigger vehicles and walk around inside them, and fly between stars. Everything is made of materials and obeys equivalent exchange. Far-away places exist as data and are aged when you return. A Chaos System keeps performance in check as a visible law of nature, and a Wilderness at the universe's edge recycles whatever falls off it. When everyone you play as is lost, you are reborn elsewhere after a time skip, and the universe remembers your earlier lives.

It started in 2011 as a two-front war game (a Cortex Command-style side-view Planet Front, a Battleships Forever-style top-down Space Front, and a Risk-like turn-based overview), and over a decade grew into Reactorcore's "Super Game" vision. Its art system became PSRC and the 3M system. Its ideas were split into three later, simpler designs: RoomSpace (rooms), TopVerse (top-down subgames on a region map) and AAL Bunkerships (side-view tile stages without the universe). Reactorcore still wants this one as its own game.

**Reactorcore asked for a cohesive high-level design to return to later. That is [cohesive-design.md](cohesive-design.md), Claude's proposal; the other files record what the notes say.**

## Files

| File | Covers |
|---|---|
| [cohesive-design.md](cohesive-design.md) | **Claude's proposal**: the whole game as one coherent, feasible setup, what's kept, merged, cut, proposed numbers, build order, and the open decisions |
| [history.md](history.md) | How the design evolved: the 2011 fronts, Wave 1, the 2013–16 rtfs, Wave 2, PSRC/3M, the equilibrium rules, the NVC AI, the 2023 pitch, the descendants and the rename |
| [universe.md](universe.md) | The bowl universe and the Wilderness, equilibrium, the hierarchy and its generation, stars and light, the matter cycle, celestial structure, atmospheres, liquids, fields |
| [simulation.md](simulation.md) | Storage, zones by distance, passage of time, detail by significance, the Chaos System, far vision, travel levels and transitions, system layers |
| [matter-and-making.md](matter-and-making.md) | The molecular system, energy forms, phenomena and supply, crafting and research, frames for vehicles and buildings, mechanisms, terrain and digging, modding |
| [life-and-people.md](life-and-people.md) | The player and the two modes, death and rebirth, souls and psychic powers, the NVC-based NPC AI, bodies and clothing rules |
| [art-and-presentation.md](art-and-presentation.md) | PSRC and 3M as far as the game depends on them, the scale history, layers and look |
| [transcript/](transcript/) | Scan-by-scan transcripts in 7 chunks, with all text and diagrams described; the source for everything above |
| `Planet Warfare.txt` | Reactorcore's 2023 pitch (the long text), kept as is |

The text documents in the project folder were read directly; they are cited by file name. A copy of this folder is also kept in the project folder (`C:\08 Projects\Project_Planet Warfare\digest\`).

*(interpretation)* marks Claude's reading of an unclear note. Each topic file ends with open questions rather than invented answers; the proposals are all in cohesive-design.md.

## Scan codes

- **W1-1 … W1-35**: `1 FotoScan_Planet Warfare Misc\wave 1 PW docs (n).jpg`, the earliest notebook pages.
- **W2-1 … W2-38**: `1 FotoScan_Planet Warfare Misc\Wave 2 PW Docs (n).jpg`, the second notebook ("PSRC/PW 2").
- **PS-n**: `2 FotoScan_PSRC - needed an art system for PW\Image (n).jpg`, the notebook "PSRC / Megastructures / PW-Universe Engine Design / 3M/96px System Detailed" and PSRC production pages. The folder's numbering has gaps (no 24–26, 33, 36, 38, 40–43, 45, 48, 58–66, 68–73, 75–77). **PS-IMG-hhmmss**: `IMG_20191005_hhmmss.jpg`, phone photos of PSRC production pages.

Reactorcore's counts (59 PW, 73 PSRC) were swapped: the PW folder holds 73 scans and the PSRC folder 59.

## Glossary

- **PW**: Planet Warfare, the old name. **AAL**: Alteisen Arsenal Laboratories, the company that names Reactorcore's shared universe; the game is set in its "Exploration of the Universe" era.
- **Super Game**: Reactorcore's term for an endlessly playable, data-driven, persistent game that serves the player (`Planet Warfare.txt`).
- **Planet Front / Space Front / Tactical Overview**: the 2011 structure (side-view squads, top-down ships, turn-based strategic map).
- **RU / EN**: resource units / energy units.
- **Hyperverse / Emptiness**: the 2013 infinite canvas of universes and the space between them (later lore only).
- **Wilderness**: the curved edge of the universe that takes in matter and ejects it reshuffled. **Equivalent exchange**: matter is never created or destroyed.
- **Equilibrium universe**: everything tends to settle; forces still cause events.
- **Chaos System / Chaos Monitor / Density Monitor / Chaos Flux / light and heavy chaos**: the in-world anti-lag system, its monitors, its build-up rate and its response grades.
- **Anti Butterfly effect**: overwhelming events cancel the tiny ones they overpower, keeping only their mass.
- **Passage of time / Time Skip**: aging an area on return; forward-only time travel.
- **Clump, chunk, region, continent, celestial, entity**: the terrain hierarchy by size; an entity is a parentless piece. **Supercelestial**: the largest solid.
- **Shadow background / flank canvas**: the dark backdrop of surrounding mass seen when underground.
- **C0–C4**: universe, supercluster, local cluster, galaxy/void, cloud/void-2. **AGN / core**: a galaxy's active nucleus. **Wild sectors**: the 8 compass sectors of the Wilderness.
- **Atmo/geo cells**: the ring of cells around a planet; their density exchange is wind. **Liquid-Gas Canvas**: the separate system of liquid and gas bodies. **E-fields**: radiation, magnetism, heat and similar overlay fields. **Collections**: fields of asteroids or debris stored as material percentages. **Exclusion aura**: the bubble a digging machine carries.
- **Huge List / Active List**: the on-disk reference tree and the in-memory scene built from it. **Instant switch range**: where you can switch characters without loading.
- **Potency**: an object's far-view priority. **Far vision / farsight horizon / event horizon box / infinity star**: the background as a forward camera, where distant things appear, and its vanishing point. **Type 1 / Type 2**: realistic vs sector-based far view.
- **Travel levels 1–5**: surface, high velocity, FTL, beyond-FTL, interuniverse. **Entry Field**: the orbit-to-surface transition ring. **FTL Phase Field**: what makes only stellar bodies hittable at FTL.
- **Principle of significance / LOD 0–4 / Inspection Mode (LOD -1)**: detail by significance. **L0–L4** (3M): polygon budgets per level.
- **Aerodynamic / resting state**: physics vs static background form of an object.
- **Molecular system / MolSys**: objects defined by materials and amounts. **Phenomena**: material capabilities. **Composite objects / flattening the layers**: core + addons baked into one item. **Knowledge object**: an unlocked, shareable blueprint.
- **Energy forms**: solid, area, fall-off area, being.
- **Moving Frames / M-Frames / Movable Frames / Entity Framework**: the early frameworks for vehicles, buildings and creatures. **Main struct / sub struct**: big objects and the smaller ones that go inside them. **MEGAS**: megastructures.
- **Res tri / res ball / RU triangle**: resource pieces from broken terrain. **Exclusion meshes**: subtractive holes. **Interior tri**: interior space behind terrain triangles.
- **Privacy Facade**: hides an interior from outsiders. **Capability / functionality packs**: modules injected into a structure. **Invention canvas**: the node-editor lab.
- **Astral Plane / Astral Being ("Me") / Astral Barrier / Astral Influence field / connectivity**: the soul layer and how psychic power works.
- **Group mind / consensus of the faction**: controlling a group and switching into any member. **Sanctuary**: where you respawn while your group lives.
- **NVC**: Nonviolent Communication, the basis of the needs/feelings AI. **Paradigms**: higher causes that override needs. **Pods**: homes where NPCs go dormant.
- **PSRC**: Pixel Sprites ala Reactorcore. **3M system**: primitive shapes with tiled textures for anything over 3 m (96 px). **3Mera**: the planned 3M asset packs.
- **Shard System**: Red Faction-style local breaking of bunker modules (W1-4). **Security grid**: capturing a security room reveals a building's interior.
- Unexplained in the notes: **LVIS** (W2-30, W2-34), **RSH** (W2-32), **X-EFFECT** (W2-33), "overpowering effect" (W2-21), "Memory Aquizition" (W2-37).

## Main conflicts and how the digest reads them

Later sources state the later version and note the earlier one. The proposal's choices are in cohesive-design.md.

| Topic | Earlier | Later |
|---|---|---|
| Genre | 2011: war game, conquer a solar system or galaxy | 2023 pitch and foreword: an all-aspect life in a universe; war is one situation |
| Space view | 2011, W1-5, W1-15: top-down space, side view on planets and inside ships, 90° turn on landing | Foreword: one side-view universe with directional or zero gravity |
| Structure | 2011: turn-based overview + real-time fronts; W1-6 node map | Wave 2 onward: seamless real-time universe, overview views as in-world sensors (W2-9) |
| Universe shape | 2013, W2-14: infinite Hyperverse of universes | UniverseBounds 2014, EUR, AAL lore: one finite universe in a Wilderness bowl |
| Terrain | 2011: indestructible node/edge chunks; W1-4: shards | W2-28: destructible triangles; EUR: clumps/chunks/regions; PS-4: C/R/RC/T body types |
| Scale | 2011, MolSys: 30 px/m; W2-13, PS-57: 40 px/m; 2015: tiered 40/20/10 px/m | EUR, PSRC packs: **32 px/m**, human 60 px, screen 40 × 32 m |
| Screen | W2-13, PS-57: 1024×768 | EUR: 1280×1024 (5:4 on purpose) |
| Characters | 2011–2021: multi-part sprite ragdolls (up to 14 pieces) | Foreword: willing to use single box or circle colliders |
| Player | 2011: the faction's consensus, finite population; 2014: group mind | 2023 pitch: a reincarnating person, solo or group mode |
| Celestial motion | Wave 1–2: planets movable and collidable | EUR: no orbits or spin; stars pulse; things move only when pushed (both keep crashes possible) |
| Far view model | W2-15: Type 1, no distance limit | W2-16: Type 2, sector-based, 100 AU limit; undecided |
| Loaded range | PS-44: 25 m normal to 1 km loaded | 3M musing: 250 m at 100% zoom to 1 km at 25%; NVC musing: 1 km full AI |
| Galaxy/void cloud share | PS-12: 50% (30% written above it) | EUR: 40/60 clouded/clear; marked REDO |

## Source table

### Wave 1 (W1)

| Scan | Title / content | Status | Fed |
|---|---|---|---|
| W1-1 | Planet Warfare: ship roles, engineer view, navigator view | core | history |
| W1-2 | Menu flow; homeworld campaigns; naming planets | core | history |
| W1-3 | Information Warfare; Game Setup | core | history |
| W1-4 | Terrain & Bunkers | core | history, matter |
| W1-5 | Space Combat; ship modules | core | history |
| W1-6 | Node system strategic map | core | history |
| W1-7 | Map grid options (square, hex, triangle, free) | core | history |
| W1-8 | Ship cutaway with crew and docking dropship | core | history |
| W1-9 | Concept 01 | core | history |
| W1-10 | Star Fighter controls and composition | core | history, matter |
| W1-11 | Game Modes | core | history |
| W1-12 | Planetary Defence (drawing) | core | history |
| W1-13 | Element/raw material based content creation | core | matter |
| W1-14 | Moving Frames System V1 | core | matter |
| W1-15 | Seamless Space Transition part 1 | core | simulation |
| W1-16 | Seamless Space Transition part 2 | core | simulation |
| W1-17 | "Performance & Diskspace / Simulating a hyperverse" | **title only** | — |
| W1-18 | Entity Framework System | core | matter |
| W1-19 | Tile-grid ships, mechs, buildings; gravity | core | matter |
| W1-20 | Integrate content dev into core game; distribution models | core | matter |
| W1-21 | Elements sticky note | core (small) | universe |
| W1-22 | Screen-edge vision sketches | core (small) | simulation |
| W1-23 | Modular structures sketch | core (small) | matter |
| W1-24 | Debris: absorbing, merging, grouping | core | simulation |
| W1-25 | Notable physical properties of materials | core (small) | matter |
| W1-26 | Huge List | core | simulation |
| W1-27 | Huge List → Active List → Gameview | core | simulation |
| W1-28 | Events & influence from far zones; load ranges | core | simulation |
| W1-29 | Topic checklist (spirit plane, FTL, psychic...) | core | history, people |
| W1-30 | Energy graphic types / light types | core | matter |
| W1-31 | "For answer": disk space, wilderness, scatter, digging | core | simulation |
| W1-32 | "You are an android" variant pitch | core (variant) | history |
| W1-33 | Structures list | core (variant) | history, matter |
| W1-34 | Vehicles list; combat/builder modes; health | core (variant) | history |
| W1-35 | Alien Standard Alphabet | sidetrack | — |

### Wave 2 (W2)

| Scan | Title / content | Status | Fed |
|---|---|---|---|
| W2-1 | Notebook cover "PSRC/PW 2" with todo sticky note | core (small) | history |
| W2-2 | Planetary Transition; planetary features | core | simulation, universe |
| W2-3 | Anti Butterfly effect | core | simulation |
| W2-4 | Passage of time effect | core | simulation |
| W2-5 | Simulation level of detail | core | simulation |
| W2-6 | Travel Levels | core | simulation |
| W2-7 | Procedural generation from the larger picture | core | universe, simulation |
| W2-8 | Game Area Composition part 1 | core | simulation |
| W2-9 | Game Area Composition part 2 (sensor views) | core | simulation |
| W2-10 | Game Area Composition part 3 (FTL, space) | core | simulation, universe |
| W2-11 | Todo sticky notes; FTL continued | core | simulation |
| W2-12 | Using background as far-vision | core | simulation |
| W2-13 | Speed & Scale | core | simulation, art |
| W2-14 | Space elements | core | universe |
| W2-15 | Distant objects; Type 1 vs Type 2 | core | simulation |
| W2-16 | Type 1 vs Type 2 | core | simulation |
| W2-17 | Event horizons; BG to active | core | simulation |
| W2-18 | Loaded chunks | core (small) | simulation |
| W2-19 | System Layers | core | simulation |
| W2-20 | Xenobiology / Flora | core | universe |
| W2-21 | Scatter object issue / Chaos Flux | core | simulation |
| W2-22 | Range & objects | core | simulation |
| W2-23 | "Different farview issues: huge objects" | fragment | simulation |
| W2-24 | "Designed for grid?" | fragment | — |
| W2-25 | Shifting states | core | simulation |
| W2-26 | Time Skip | core | simulation |
| W2-27 | Celestial scale ladder; forces; stellar stuff | core | universe |
| W2-28 | Triangle terrain layers | core | matter |
| W2-29 | Digging process | core | matter |
| W2-30 | Inspection mode; principle of significance; functionality packs | core | simulation, matter |
| W2-31 | Primitive-shape art styles | core | art |
| W2-32 | Low poly; blueprints; exclusion meshes; texture stretching | core | art, matter |
| W2-33 | Object internal functionality canvas | core | matter |
| W2-34 | Modder content check; privacy facade; object layers | core | simulation, matter |
| W2-35 | Interior triangles | core | matter |
| W2-36 | Interior/terrain open questions | core | matter |
| W2-37 | Minerals, vitamins, memory, Astral Beings | core (partly faint) | people |
| W2-38 | Rescan of W1-31 | **duplicate** | — |

### PSRC universe-engine notebook (PS), transcribed

| Scan | Title / content | Status | Fed |
|---|---|---|---|
| PS-1 | Cover: PSRC / Megastructures / PW-Universe Engine Design / 3M/96px System Detailed | **title only** | — |
| PS-2 | Over 3m research & megastructures: factors, requirements | core | universe, art |
| PS-3 | More factors | core | universe |
| PS-4 | Tri-based chunks; scales; planets as wedges | core | universe |
| PS-5 | Layers and load order; Equilibrium Universe | core | simulation, universe |
| PS-6 | Celestials/continents; body types C, R | core | universe |
| PS-7 | Megastructure rules; PSRC 3M universe; loaded sphere | core | universe, simulation |
| PS-8 | PSRC todo; over-3m limits; mipmaps L1–L4 | core | art, simulation |
| PS-9 | Universe hierarchy C0–C4; cause & effect nature | core | universe |
| PS-10 | C0 universe, C1 supercluster, C2 local cluster | core | universe |
| PS-11 | Ideas 1–3; solar system generation | core | universe |
| PS-12 | Galaxy C3, Void C3 | core | universe |
| PS-13 | Cloud C4, Void C4 | **headings only** | universe |
| PS-14 | Celestial structure (planet, gas giant); planet partitions | core | universe |
| PS-15 | Celestial structure (star); evolution cycle; rings | core | universe |
| PS-16 | Quakes; overlap mechanics; solid chunk dynamics | core | universe |
| PS-17 | Waves/wind; atmospheres; atmosphere dynamics | core | universe |
| PS-18 | Buoyancy & gravity; liquid-gas canvas | core | universe |
| PS-19 | Force fields; digging; solid fields/collections | core | universe |
| PS-20 | 3M overview; 3M design guide | core | art |
| PS-21 | PSRC todo; human stages | core | art, people |
| PS-31 | Distance via sides into the horizon | core | simulation |
| PS-44 | Loaded ranges | core | simulation |
| PS-57 | Horizon distances on an Earth-size planet; size classes | core | simulation, art |

### PSRC production pages, not transcribed (sidetrack: sprite-pack production)

These are about making and selling PSRC sprite packs, which the info pack's text and guide images already cover: PS-22 (animation FX), PS-23 (effect lists), PS-27 (terrain/tile types), PS-28 (leg muscle shapes), PS-29 (arm muscle shapes), PS-30 (clothing categories, frosting shapes), PS-32 (todo, sheet alignment, product catalogue), PS-34 (generic graphics, visual BG types, clothes), PS-35 (key images, screenshot guidelines), PS-37 (measurement aid pack), PS-39 (art style names, surface textures, micro particles), PS-46 (Complete Spritepacks Workflow, printed), PS-47 (Mass Production), PS-49 (sprite scale comparison: 10, 20, 30, 40–48 and 80 px humans against Soldat, Clonk, Terraria, KAG, Cortex Command, Link-Dead), PS-50 (format), PS-51 (workflow, format 2), PS-52 (sprites to draw, themes), PS-53 (drawing styles, spritepack ideas), PS-54 (how to begin), PS-55 (lightness levels, sprite art style requirements), PS-56 (style part 2), PS-67 (pack checklist), PS-74 (effect sketches), PS-78 (physical animated phenomena), PS-79 (emission/tile frame counts), PS-IMG-141007 (human pixel measurements), -141016 (human sprite layers), -141153 (object decorative per-pixel layers), -141349 (align to clean sheet), -141429 (sheet types), -141502 (package criteria), -141530 (sprite product), -141600 (product naming), -141623 (complete spritepack workflow), -141832 (align method).

### Other material

- `3 later crude messy PW dev docs\`: all 21 files read (rtf and doc converted to text); cited by name in the topic files. The 13.6 MB `PW Design Terrain System.rtf` is mostly an embedded picture; its text equals v1.1.
- `4 scrappy visual sketches (just tests)\`: 9 throwaway images (bunker views, world system test, planetary, space, terrain system, a parallax GIF); not read, per the foreword ("pretty much throwaway ideas").
- `5 PSRC Condensed Info Pack\`: read: `!info Pixel Sprites ala Reactorcore.txt`, the 3M info, and the docx musings on the 3M origin, material types and the NVC AI. Not read (art production): `!info About, PSRC Human MK2, Ultimate Dev Pack.md`, the clothing and animation musings, `PSRC Original Human Mk2 Design Plan Musing.txt`, and the images. `6 misc txts\PSRC Human Redux Plan.txt` was skimmed for its gameplay rules.
- `6 misc txts\`: all five read (the Human Redux Plan skimmed, as above). `PW PSRC Equilibrium Universe Rules.txt` matches the info pack's musing copy and the AAL lore copy except for small edits.
