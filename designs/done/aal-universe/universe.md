# AAL Universe: the universe

What the universe is, how it is laid out and generated, how matter cycles through it, and how celestials, atmospheres, liquids and fields are built. Sources: `PW PSRC Equilibrium Universe Rules.txt` (EUR), `WorldUniverseMetagame.rtf`, `UniverseBounds.rtf`, `Planet Warfare.txt`, scans W1-21, W1-31, W2-2, W2-7, W2-10, W2-14, W2-20, W2-27, PS-2 to PS-19. *(interpretation)* marks Claude's reading; later sources win where they conflict.

## Shape: a finite universe in an infinite bowl

- **Earlier (2013, `WorldUniverseMetagame.rtf`, W2-14):** an infinite **Hyperverse** holding infinite universes, separated by the **Emptiness**, where rift storms siphon matter from old universes until a big bang births a new one. Travel between universes is possible but vast (W2-6 travel level 5, "interuniverse ∞ FTL"). W2-14: "the universe is Hyperverse", "no bounds, no core, infinite"; "the big bang is only a tiny part of a bigger picture."
- **Later (UniverseBounds 2014, EUR, AAL lore):** **one universe, finite in matter, with an infinite edge.** The universe proper is a flat, stable middle; around it the **Wilderness** curves up like a bowl or a skate ramp. Things that go over the edge are reshuffled, combined, purified or corrupted, and pushed back in, or swallowed by anomalies and spat out later in a starved void ("termination shock... like constant ocean waves on a beach"). Unique artificial objects that go in are kept in a recallable pool; generic matter is reduced to raw material and reused. The universe keeps a target total of matter and energy; when it drops, the edge throws stuff back in.
- **Rejected options** (UniverseBounds): loop-around ("MEH"), and a temporary generated Wilderness that vanishes when you leave ("BAD").
- **Never created, never ending.** No heat death, no endless expansion. A big bang is "an 'a' event, not 'the' event": an extreme local event you can cause, survive, escape or defuse.

## Equilibrium

"Everything within the universe has the goal of becoming stable / dormant / idle / settled. However forces within the universe still cause things to generate events" (EUR). Gravity clumps things; weather, life, anomalies and chemistry erode, grow and reshape. Celestials slow down and settle; the universe disperses regions, continents and celestials toward less dense, less split configurations, sometimes through a build-up and burst (quake, tsunami, eruption, anomaly). "In celestials, the parts make up the whole, but the whole influences the parts." The Wilderness is the one exception: it ejects.

The PSRC notebook states the same rules (PS-5): driven toward stability, makes all matter more uniform, randomized but consistent, celestials settle into better configurations over time. Its sketch puts the stable universe at origin 0,0 inside a wilderness band of randomly shifting ejected material.

TopVerse later sharpened this into a player-facing rule ("nothing bad comes unless provoked"); see [cohesive-design.md](cohesive-design.md).

## Hierarchy

Three versions, from rough to most detailed:

- `Planet Warfare.txt`: superclusters, galaxies/voids, galactic sectors, star systems, celestials, continents, regions, areas, local coordinates (the screen you arrive at).
- **PS-9** (C-levels): C0 universe → C1 superclusters → C2 local groups/clusters (collections of galaxies and voids) → C3 galaxy/void → C4 cloud (nebula)/void, or a quasar/galactic nucleus → solar system/void → celestials/entities → contents.
- **EUR "Jurisdictions"** with sizes: universe 1000 Mly; supercluster 100 Mly–1 Bly; local cluster 10 Mly; galaxy/cloud/star cluster 100 ly–10 Mly; quasar or star system 1–10 ly; celestial up to 0.0001 ly (1000 M km).

Generation layouts (EUR and PS-10 to PS-12; EUR marks the galaxy and star system steps "REDO"):

| Level | Layout |
|---|---|
| Universe (C0) | Wilderness edge in 8 compass "wild sectors"; in the centre 7 superclusters of equal size, one in the middle and six around it, with pure dark voids between them. PS-10: uniform density. |
| Supercluster (C1) | 7 local clusters, the centre one densest. |
| Local cluster (C2) | Galaxies and voids, at least 50/50 (EUR: 4:5 galaxy to void; PS-10: 4 galaxies, 5 voids). Matter budget from the cluster plus the universe's surplus; galaxies get priority; voids grow or shrink to compensate. Too many galaxies → chaos merges them. |
| Galaxy / void (C3) | 3×3 cells (PS-12). A galaxy needs 1–9 active cores (AGN) and is moved by moving its core; usually over 50% cloud. A void ("galactic anti-space") has no active core, usually under 50% cloud. EUR: 8–128 points (avg 64), half star systems and half small voids; galaxies bias points to the centre with a quasar core (denser, more life, richer, "hot power, active fusion"); voids bias them to the edges (derelicts, anomalies, rogue celestials, "cold power, ambient higgs-boson"). |
| Cloud / void-2 (C4) | Symmetric fractal patterns marking clouded and clear areas, 40/60; spiral arms of 1–16 circles. PS-13 is headings only. |
| Star system | EUR: 2–32 points, avg 8 celestials. A star is always at the core. PS-11: 0–6 stars in a ring, then 0–16 celestials placed along one line from centre to edge, each given a random 0–360° angle. |

EUR's running count is 225,792 potential celestials in the universe (from its 7 × 7 × 9 × 64 × 8 chain).

**Generation by heuristics, not biome templates** (`Planet Warfare.txt`): matter is dispersed with noise, superclusters shape galaxies, which shape sectors, systems, celestials, continents, regions and areas. A location is defined by conditions (humidity, materials, temperature, life, hazards, weather, soil) and its biome emerges from them, so biomes mix and new ones appear unplanned. Every step has a wildcard chance of anomalies (the mountain with a hole punched through by a meteor).

**Early chaos** (PS-11, Ideas 2): at creation, random celestials are flung across space and overlaps are allowed, so the early chaos settles into bizarre places worth visiting. Relics too old or too new need a "technology understanding cypher" to use. Homeless rogue celestials belong to the universe level, slowing weakly in voids and strongly in nebulae.

## Stars, light and motion (EUR)

The universe is "optimized for 2D, doing things on 2D's terms instead of pretending to be 3D":

- **Celestials don't spin or orbit.** They don't move unless pushed; inside galaxies they drift and slowly stop.
- **Stars pulse** between hot/bright and cold/dim phases instead of shining in one direction. A planet in a star's luminant zone is lit all over during the bright phase, even its far side. The dim phase still gives starry nights and warmth. Cycle length varies per star, from month-long days to 2-minute days.
- **Multiple stars**: a much bigger star takes the centre; similar stars form a pair or ring within 10% of the system's radius, and over time either merge or equalise.
- **Stars age** like real ones when no new material arrives (red giant, white dwarf, black dwarf, neutron star, black hole, remnant). PS-15: a black dwarf is degenerated matter, a source of exotic rare resources.
- An idea to tie the game clock to real time is noted and rejected as unhealthy for real life.

## The matter cycle

- **EUR universal cycle** (descending scale): big bang (spreads matter over a supercluster; the hardest event in the game), hypernova (local group), giganova (galaxy), meganova (galactic sector), supernova (star system), nova (a star; the most likely, which defuses the bigger ones). Then cool-down; gas and dust clump into nebulae and asteroid fields; dwarfs, giants, planetoids, comets, belts; stars, planets; neutron stars, pulsars, "plamoons"; quasars, black holes; stabilisation; then life, civilisations, ruins, artifacts, catastrophes. After this the player can accelerate or slow cosmic processes, start new ones, defuse others, or deliberately trigger a nova to restart an area.
- **PS-15 Evolution Cycle:** nova → gas/dust cloud → condensing → pockets/clumps → chunks/regions → continents/celestials → star systems/quasars → galaxies → overload or fizzle out → repeat.
- **W2-27 scale ladder:** dust → clumps → asteroid/comet → planetoid → moon → planet → gas giant → star (I–V) → neutron star → black hole, then at "CRITICAL" back to dust. Stellar stuff is rock, metal, ice, organics and gas.
- **Too dense collapses** (EUR): pile enough into one place and a moon or megastructure becomes a gas giant, a star, a black hole or a big bang. Dark regions of the universe may siphon matter harder to fight pile-ups.
- **Moving celestials** is allowed: crash a planet into another, push one into a sun (W2-2, EUR). Terraforming, gaining or losing mass and changing type happen "at a critical scale" (W2-2).

## Celestial structure

- **Terrain hierarchy** (EUR): clumps and objects 0.2–10 m; chunks 4–100 m (square, circle or triangle, overlapping ones fuse); regions 4 m–10 km (collections of chunks that cast a **shadow background**); continents 1 km and up; a **celestial** is a container of two or more continents with global properties (gravity, magnetism, radiation, heat, emissions). A chunk, region or continent with no parent becomes an **entity**: it acts on its own but doesn't shape stellar-scale gravity. Megastructures, battleships, kaiju and mega flora are all built with the same system above 10 m: "anything larger than that should be utilizing the chunk system itself."
- **Body construction types** (PS-4, PS-6): C (overlapping circles, nested celestial → continent → region → chunks, with a centre of gravity), R (rects, ordered and tilemap-friendly, or disordered), RC (both), T (triangle pie sectors). Tri-based chunks have a solid shell and hollow interior triangle, at least 10 m pieces; circle-rect suits the mega class.
- **Planets as wedges** (PS-4d): a planet is wedge sectors cut into strata (core, mantle, crust, surface); at L4 they split 10×10 down to 10 m² pieces; max density per sector 1,000–10,000 km². Digging in shows the background **flank canvas** of surrounding mass.
- **Planet partitions** (PS-14): core, mantle, crust and surface ringed by 8 rectangular **atmo/geo cells**; cells can be culled or added at the corners so a planet shrinks or grows. Topics listed: regeneration, collisions, flooding, too much mass → gas giant or star.
- **Overlap and quakes** (PS-16): overlapping solids store pressure by depth and size and normally drift apart slowly; a severe overlap causes a quake (wave motion or vibration) that can shatter a body into orphan pieces, which are absorbed by others or settle on their own. "Macro can command micro."
- **Rings** (PS-15) form in 5 steps as a newborn core's gravity clears an exclusion zone in a dust collection.
- **Megastructure rules** (PS-7, EUR): megas can't overlap; they live in the background but can be "activated" to affect the normal layer (deliberately as a weapon, naturally as an erratic cascade). Things inside a moving mega are safe from outside forces but keep its momentum. Big monolithic chunks and regions resist decay and collapse; a megastructure made of many small splits is unstable (EUR "Megastructure stabilized structure designs").

## Atmospheres, liquids, gases and fields

- **Atmospheres** (PS-17): layer 1 is a circle, layer 2 eight rects, layer 3 each rect split into 1–128 cells by celestial size. Each cell has a total composition and mass and tries to equalise density with its neighbours; that exchange **is** the wind. Cells can generate weather. An atmosphere can be removed for good, one cell temporarily.
- **Liquid-Gas Canvas** (PS-17, PS-18): liquids and gases use overlapping circular chunks and regions on their own canvas, reaching up to galactic clouds (solids top out at "supercelestials"). Liquids never collide as rigid bodies, only as trigger areas. Waves and wind pass force to what floats in them; buoyancy points to the centre in space and to the core on planets. Gas comes as global ambient gas plus local pockets that exclude, replace or mix with it (Freelancer-style).
- **Force fields / E-fields** (PS-19): radiation, electricity, bacteria, magnetism, pressure, heat; either celestial-wide or local projections (circle, ray, beam, rect, line, point). Digging machines carry an **exclusion aura** of normal conditions; stop digging and heat, pressure or lava can crush you.
- **Collections** (PS-19): asteroid and debris fields stored only as material percentages and spawned by random rolls around the player; sensors point to rare elements; collections condense into celestials over time.
- **Space** (W2-10): space between starzones is never permanent unless something is built there; it is generated from the properties of the "general sector" it lies in, mostly empty with rare passing objects. "The scale of the universe is more compact than realistic", but planets and distances are still huge.
- **Life** (W2-20): an area stores only an abstract species list and stats, shaped by area, time, materials, environment and events; actual flora is generated when the zone is visited. Four plant sizes: small, medium, large, oversize.
- **Orbital traffic** (`forum log Orbital Atmo Traffic in AAL worlds.txt`): homeworlds with millions of landings a year use orbital rings, elevators, vacuum corridors with cargo railguns and "skyways", and may need traffic quotas and cooling towers, because mass re-entry heats an atmosphere.

## Open questions

- EUR's galaxy and star system steps are marked "REDO"; the 30%/50% cloud figures on PS-12 look revised.
- How celestials are shown at human scale in side view (the wedge/partition model is the closest answer); see [cohesive-design.md](cohesive-design.md).
- Whether the Hyperverse and other universes exist in the game at all, or only as lore. The later documents only describe one universe and its Wilderness.
- "Winds, tsunamis, quakes" propagation and "Energy/modifier fields" are TODO headings in EUR.
