# TopVerse: the universe and Unigen

The scales of the universe, how **Unigen** (the universe generator) builds and stores it, the spheres of influence, the vertical layers of every kind of celestial, star systems, the Wilderness and the energy cycle, and scrolls. Sources: `1 TopverseNotesBU2_Cleaned.txt` (universe generation, tile type listing, spheres of influence, unigen concerns), `5 Topverse system layers n mechanics.txt`, scans TN29, BS1, BS2, B4, B5, B9–B12. Scan codes are explained in [index.md](index.md).

## Scales

From small to large (B4 zoom chain, layers txt, Notes):

| Scale | Size | What it is |
|---|---|---|
| Micro BIO | microscopic | Syndemic's scale, below the human room (B4) |
| On-foot zone | 10–100 m | room networks and DRC parking areas; see [on-foot.md](on-foot.md) |
| Vehicle zone | about 1 km | humans not shown; minor vehicles |
| **Area tile** | 1–10 km² | the persistent map tile; "city/area" grid; a vehicle arena is one tile's content |
| **Region** | grid of 10x10 to 25x20 tiles (≈100 km) | real-time vehicle combat happens on this layer's tiles; a node |
| **Continent** | 3x3 regions (≈1000 km) | a node |
| **Celestial** | 1, 2, 4 or 6 continents (≈10,000 km) | planet, moon, asteroid; stars and giants have no continents |
| **Star system** | grid 11x11 (min 9x9, max 15x15) | square only |
| **Star sector** | grid 5x5 (sparse outskirts) or 7x7 (galactic cores, dense clouds) | a "cloud" or "void" |
| Galaxy, local cluster, supercluster | 3x3 grids each | 30/70 material distribution for cloud vs void |
| **Universe** | even grid (4x4, 6x6, 8x8) + a 1-tile wilderness border | e.g. 10x10 with the border |

**Area tile, "new 2.0"** (Notes). A tile is a variable area of roughly 1–10 km². It includes an MDRC/DRC slot and a sector area (room network). The tile itself is persistent, but everything inside it is not: both the DRC zone and the room network are always random. City structures on a tile are separate from the DRC. One tile holds a whole installation, city district, course, farm, mine or factory: a single building is too small, a town too large, so cities span several tiles and a region is either a collection of small towns or one regional capital.

**Region map** (Notes). A versatile tile map, rectangular, wide or long; natural regions are generated from the seed, artificial areas are persistent. Later notes cap it at 25x20 (500 tiles), as small as 15x10 or 10x10. Transit tunnels, tunnel-end blockade sectors and impromptu combat zones are the same as a region map but throwaway.

**Continent and celestial** (Notes). A continent is 3x3 regions; its north/central/south and left/middle/right sectors mean nothing by themselves, since its climate comes from the star system (moons, stars, planets, giants, fields, nebulae). A celestial is 1, 2, 4 or 6 continents: 6 for an Earth-like planet, 4 for large moons and small planets, 2 for small moons, 1 for the largest asteroids. They are planes wrapped into a sphere: going up eventually brings you in from the bottom, going left wraps to the right. Stars and giants are too large and chaotic for permanent map data: they get a wild, on-demand scrolling region map for their whole surface, mainly to give coordinates to fleets and installations there. High atmo, orbit, space approach and mantle are shared by the whole celestial.

An earlier draft in the same notes started from an 8x8 universe of 50/50 light and dark tiles (supercluster or "tera void"), with 2x2 superclusters, 4x4 galaxies, 8x8 galactic zones, a 10,000 km² celestial map, a 1000 km² continental map, a 100 km² region map and a 10 km² city area map (8x8 cells of 1 km²). The later 2.0 and tile-listing sections replace it. BS1 keeps the "50/50 dark/light distribution" for the main universe.

## Size and storage (Notes)

Each tile stores hard data for its tangible contents, never maps: maps are generated when needed, random-ish from the same seed, with changed contents influencing the result. A full Earth-like planet is at most 500 tiles x 4 layers x 9 regions x 6 continents = 108,000 data points, each a database entry with slots of contents (so 10–100 times more), queried only when needed and edited locally only while in use; disk space is the main cost. A 10x10 universe has about 432 million potential celestial locations (about 86 million actual celestials at 20%), with smaller universe options worked out down to a single star sector (53,361). A star system averages 10 or fewer natural celestials plus 10 artificial ones. Everything is generated only when the player enters or interacts with it, and only as far as needed (entering a new continent creates only the region you stepped into); data is read and written from disk as needed and unloaded on exit. Save files will be several megabytes. A universe-wide quota of truly persistent DRCs/MDRCs exists because "the game already has an entire universe worth of data to remember".

## Spheres of influence (Notes)

"Each layer of the world is affected by those above it, while those below it, if changed, can influence those above it." A terraformed or devastated area tile causes proportional short- or long-term change in its region.

- **Universe**: basic physics, laws of nature, the chaos system.
- **Supercluster/void**: whether the zone is rich or poor in material.
- **Galaxy/void**: the galactic core's wind bubble gives subtle large-scale space weather.
- **Star sector/void**: local galactic weather and phenomena; may be covered by nebula or be a void.
- **Star system/void**: local gas/solid/liquid/plasma fields and stars or giants that affect planets, stations, moons, colonies, their contents and loose vehicles; planetary atmospheres can resist some of it.
- **Celestial**: total atmosphere (sky, high atmo) and main structure (crust, mantle, core); orbit is shaped by both the celestial and the star system, space approach by the star system. A celestial's core may have special effects reaching up to orbit. It allocates the total materials for its continents.
- **Continent**: its own climate, set by its position relative to the stars (emulating rotation without spinning); distributes its share of materials to its 9 regions.
- **Region**: its own sub-climate, set by its position on the continent; distributes materials to its tiles.
- **Area tile + major vehicle action zone**: the culmination of everything above, with its own detail, a little randomisation and a low chance of chaotic mutation, within what the region allocated. A vehicle arena is one tile's content; a tunnel draws from several tiles.
- **On-foot zone**: a randomised subsection of a tile; whatever mutations a room network has, it stays within the tile's frame.

## What a tile is made of

"Remember: no specific biomes" (Notes). A tile's look comes from its properties, not from a biome template.

- **Contents** (Notes): humid/dry; acid/neutral/base (with liquids); organic level and type (flora); population and type (fauna); specific structures; geological features (holes, walls, cliffs, ravines); weathering features (wind, lake, river, pond); local materials (what the solids, liquids and gases are). Regionally: hot/cold, weather, temperature and atmosphere. A celestial too small for regions uses space's local "climate" (vacuum, nebula, solar wind, anomalies).
- **Cell contents → biome** (BS2): materials (terrain: surface, underground, deep, mantle, core; orbital gas, asteroids, debris), structural elements (natural: flora, geo features; artificial: buildings, installations, platforms, supports, foundations), weather/climate/atmosphere, and an **occupant**: one DRC/MDRC or one major vehicle, either mobile or parked.
- **Area tile data** (B12): ID/coordinate = seed; the materials present and assigned to this tile (special, unique things, not general regional or celestial properties); structures; personnel; biodiversity (flora and fauna); saved characters (persistent uniques).
- Appearance is generic and comes from the most prominent element, in three layers drawn on top of each other: base, rivers/add-ons, structures (Notes). Heuristics turn the cumulative properties into desert, forest, mountain, shallow sea, a city district or any mix.

## Vertical layers

The Notes' tile listing gives the area layers: space approach, orbit, high atmosphere, sky, surface (with contents), shallow, soil, underwater, underground, bedrock, depths. B4 draws them as stacked planes: space/orbit, sky (low and high), surface/sea, light under/submarine, heavy under/depths, bedrock/mantle/ocean floor, then the **mantle as a side-scrolling view** down to the core shell and the core(s). BS2 adds rough figures: clouds at 1–10 km and 100–1000 km, lithosphere soil (or sea) 1–10 km, crust/bedrock (or super-deep sea) 10–100 km, mantle 100–1000 km and more, then the planetary core(s).

**The layer pictogram system** (B10, "DOC parts 1–4"): every celestial is described as a vertical slice through one area tile.

- Air: orbit (clear, nebula, debris or both, in sizes s/m/l, with radiation or wind weather), high altitude (or void), sky (or void).
- A solid/liquid/gas grid for the rest:

| | Solid | Liquid | Gas |
|---|---|---|---|
| top | surface | shallows | fog |
| under | underground (soil) | underwater (sea) | under fog |
| deep | bedrock | depths | deep fog |

- Then crust/mantle/core (various solid, liquid or gas layers, different for planets and stars).
- **Planet types**: Terran (surface, soil, bedrock), Oceanic (shallows, sea, depths), Europa (an ice surface over sea and depths), Venus (void high altitude, shallows, sea, bedrock), Shallow (void, no sky, shallows, soil, depths).
- **Gas giant**: clouds, fog, under fog, deep fog, metallic hydrogen, an ice-rock core. **Ice giant**: the same with an ice layer and an ice-ammonia layer over an ice-rock core.
- **Stars**: yellow/red stars have corona, chromosphere, photosphere, a convective then a radiative zone, and a helium core; blue stars swap the convective and radiative order and have an iron core.
- **Remnants**: a white dwarf (hydrogen burn, helium burn, a carbon-oxygen core), a neutron star (a neutron jet over the corona, neutron/electron superfluid, proton superconducting fluid, electron-degenerate matter), a black hole (event horizon and Hawking radiation jet, an electron burn shell, hyper-charged neutron superfluid, neutronium, positronium/protonium "energised hyper solid", and a core of "critical effect matter" with four question marks).

**Size decides layers** (B5, B10 part 3): "Continent or larger have mantle." An area-tile-sized celestial (10 km²) has only orbit, a surface, one ground layer and a core; a region-grid celestial adds void, soil and bedrock; a continent-sized one has the full set. Below 1 km² (stations and the like) an object isn't a celestial but an entity instance inside an area tile. Fewer layers means shorter transition times between them (B5).

## Star systems

**Prototype** (TN29): a grid with the star's corona in the centre and concentric bands around it (hot like Venus and Mercury, the habitable zone, cool like Mars and the asteroid belt), holding planets, moons, a ringed giant, asteroid fields and debris, a mini nebula, gas fields, an anomaly, two jump gates, two wormholes, a hyperspace hub, a megastructure, a trade lane (a "sub-celestial structure") and a fleet ("not celestial").

**Generator variables** (B11): star count (1–4 stars, a nebula/protostar, or a void); core placement (centre, corner, random, side/border); formations for multiple stars or objects (+ x − | / □ ⊏ L H); spacing (e.g. two cells between); star size/type (small, medium, giant, supergiant, white dwarf, neutron star, black hole, anomaly); others (planets, giants, moons, fields/clouds/debris, anomalies, megastructures, derelicts) with parameters (amount, proximity, placement, field width, sub-celestial elements, structures, orbitals). "Template-driven star system gen."

**Grid effects** (B11): each star projects a row of effect cells into the system grid: C corona, H hot, M medium/habitable, L low/cold, R radiation, G gravity.

| Star | Cells outward |
|---|---|
| protostar | C |
| dwarf | C L |
| main sequence | C H M L |
| giant | C C H H M L |
| supergiant | C C C H H M L |
| white dwarf | C H H M L |
| neutron star | C H M L R R, with radiation beams vertical, horizontal or both |
| black hole | G G C H M L ("event horizon gravity overkill") |
| anomaly | G C H M L R at a range of 1–3 (1x1, 3x3 or 5x5) |

B11 also lists the star system's features: trade lanes, jump gates and wormholes; orbital facilities (orbital elevators and launch assists, stations and satellites, a continent-based orbital grid for placing them); space, land and orbital defences; massive events (celestial collisions, superweapons, nukes, orbital bombardment); hyperspace infrastructure; and space travel with tunnels, strandings, fleet interceptions, chases, long-range superweapons and anomalies.

## The Wilderness and the energy cycle

**Wilderness** (BS1, Notes): the universe's outer border, "sort of a Lost & Found shuffle area: garbage collection, ejecting, mutate, recombine, chaos ruled". A wilderness chunk has bands going outward: 0 an entry boundary (bow shock barrier), 1 light, 2 deep, 3 core, 4 extreme, X the event horizon. Nothing bad ever pours out of it, but it holds oddities, monsters and mutations, reachable through the universe's borders or through the darkest spots, chaos wounds and chaos wormholes. It's the place to inject user-made content as friendly "other player challenges" to duel (Notes endgame).

**Energy cycle** (B9): civilisation uses matter and energy, which is lost from anywhere as heat and Hawking radiation, unrecoverably. It flows to the Wilderness, which collects, mixes, builds up and finally ejects or erupts it. The darkest sectors reach critical depletion and become light sectors through a big bang or a constant stream, producing new material and energy for use. This closes the universe's loop. Matter "should never get stuck": natural jump holes form where a system lacks FTL resources (Notes).

## Chaos system

The universe's enforcer of performance and density (Notes, B6): hidden and overt systems that act in an emergency when performance is at risk. It limits settlements and truly persistent DRCs/MDRCs per region, celestial and universe (chaos storms grow until order is restored), teleports intersecting colliders apart, and can be "evoked" by a high-level astral (merge, delete, relocate, eject, nullify, freeze entities). Exceeding the density of permanent parking rooms makes it "kick into action unless appeased in some way".

## Scrolls

Messages attached to places, events, groups and things (Notes "universe generation", B9). Kinds: welcome, hostile, warning, obituary, message, trap, hail, request, demand, declaration, manual, recipe, song, art, musings, research, blueprints, schematics, beacon, buoy, marker, lighthouse, sign, symbols, invitation, claim, surrender, ransom, threat. Content comes in tablets/trays by depth: surface/public, beginner/common, intermediate/classified, master/full access. Access uses security clearance levels named after angelic ranks: Angel/0A, Archangel/1B, Principal/2C, Power/3D, Virtue/4E, Dominion/5F, Throne/6G, Cherubic/7H, Seraphic/8X, God (?)/99.

**User-defined scrolls** (B9): player-made contexts, events, situations, locations or groups with a scroll attached, containing specific text in one or several files, with unlock, discovery and trigger mechanisms. Images, voice or in-game text-to-speech can replace text, under heavy, strict guidelines. Besides the message, a scroll carries metadata saying *what* to generate, not *how*. The universe's growth list (Notes) adds new scrolls, new procedural "autoscroll" rules, and new Unigen patterns, mixing rules, detailing steps, encounter types, events, calamities, discoveries and variants.

## Proposals

Claude's suggestions for topics Reactorcore titled but didn't fill, or left open. Not Reactorcore's design.

- **Proposal, "How to make Unigen not suck"** (Notes: a title and three concerns: meaningful variation without the "1000 cups of corn" problem; not boring, tame or restricted; cohesive and standardised yet wide-ranging). Answer it with the design's own pieces: (1) variation comes from *contents*, never from biome templates, so two deserts differ because their materials, structures, fauna and history differ; (2) the spheres of influence give cohesion, since every tile inherits from its region, continent and star; (3) the chaos mutation chance and the Wilderness give surprise within limits; (4) history gives meaning: every tile's data records what happened there (wrecks, MIA lists, KIA materials, scrolls, calamities), and the generator must use that history when building the tile's next room network or arena. A tile you fought over should look fought over.
- **Proposal, continent details** (Notes: "pixel grid maps or biome/climate/material zones with limited settlement tokens, with minimum distances...???"). A continent is a 3x3 grid of region nodes whose climate comes from its position relative to the stars; it holds a fixed number of settlement tokens (for example 3–6), with at least one empty region between two settlements, which is also where the persistent-hub quota lives.
- **Proposal, the continent drawing with 6 regions** (B5) versus 3x3 regions (Notes): keep 3x3 regions per continent and read the B5 drawing's six as a celestial's six continents.
- **Proposal, area tile size.** Fix the area tile at 10 km² (about 3x3 km) for generation and data, which matches the later sources (B10, the region-map scale) and still fits B7's MDRC size rule (10% of a tile, about 1 km²); "1–10 km²" then describes how much of a tile a given room network or arena actually uses.
