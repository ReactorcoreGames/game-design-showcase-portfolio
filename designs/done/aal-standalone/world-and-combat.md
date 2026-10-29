# Standalone: world, entities, damage and enemies

How a battle's space is built, the rules every object obeys, how damage looks and works, and who the enemies are. Mostly V2 (2011–2013); V1 and V3 differences are marked. Sources: S7–S16, S18–S21, S26–S27, A4, A8–A9, A17–A21, M1, the AoY content lists and the demo's world construction images.

## The two world types (S9, S7–S8, A19–A21)

Every battle happens in one of two "core types of worlds". Each is a large open area; the play happens in a band or region of it, and nothing is walled in.

**Planetary**

- A large flat area that **loops around** at its edges ("if possible, it should curve to simulate planet roundness").
- Entry and exit **only from the top**; a variable exit altitude leads to space.
- Gravity has a direction (height). A variable "play field" altitude marks where "shit happens".
- Solid surface and/or liquid surface (at least one). With no solid surface there must be a **killzone at depth** (pressure, gradual, with warnings).
- On a planet the tactics map is the planet's entire surface.

**Space**

- A large area with boundaries; **no looping**, exit at any border; play area always in the middle.
- An optional gravity source. Certain directions can grow progressively lethal as you approach (sun, anomaly, black hole).
- Space level v2 (S8): a play area spiralling round a central body, with hatched fields and a large body at the edge.

**V1** had the same two types, simpler: "the only difference is gravity and whether there is a terrain or not", a square playfield inside a limitless flat area, a warning but no punishment for leaving (2011-05 level mockups). **V0** sketched a "GunMetal style open environment" with boundaries and inaccessible background terrain (E2).

## World components (S7–S8, M1, demo images)

- **Solid objects**: collidable scenery following the "universal entity standard". Can carry emitters. Can be set non-solid (collision still registers but you pass through).
- **Solid surface**: collidable planetary surface, semi-indestructible (only planet-killer weapons affect it), loops at edges, can have material properties.
- **Liquid surface**: semi-collidable. Entering and exiting trigger splash events; below the surface is a progressively stronger "effect area", and at a variable depth (by planet and liquid type) it becomes fatal.
- **Effect areas**: "Freelancer based system". Built from multiple parts, seen from afar as a generic cloud; inside they may hold randomly dispersed solid and non-solid objects, screen effects, particles and entity effects (damage). Effect areas have **priorities**, so one can override another: a field within a field.
- **Weather layers/zones**: a min–max height band (planetary) or distance band from centre (space) where weather happens; seen up close and from afar like effect areas.
- **Exclusion areas** (A9): inverted spheres with normals pointing inward.

The 2013 demo's world construction images show the stacks:

- **Planetary type**: Terrain Layer → Scenery Object Layer 1 (rocks) → Water Area Layer → Water Surface Layer → the player → Scenery Object Layer 2 (clouds) → Effect Area Layer (gas atmosphere layer).
- **Space type**: a spherical area boundary containing Scenery Object Layer 1 (asteroids), Layer 2 (large gas clouds) and Layer 3 (small gas clouds), each spread from the centre outward.
- **Skybox layout**: "each side shows distant objects based on the metagame map": the six faces show what lies in that direction on the star system map (asteroid field, sun, nebula, empty).

Render layers (M1): GUI, FG filter, game, in-game "clouds", BG filter, actual background (skybox).

## Environments (AoY lists 2011, A19–A21)

| Planetary | Space |
|---|---|
| Crater Desert | Asteroid Field |
| Coal Mountains (possibly lava) | Ice Field (fog between slabs) |
| Sea World | Gas Nebula |
| Gas Geysers (acid pockets of fog/smoke) | Planetary Ring |
| Cloud World (no terrain, almost zero-g, gas giant; "very similar to space") | Dusty Planetoid (zero gravity) |
| Crystal Valley (giant crystals, barren rocky terrain) | Solar Corona |
| Ice Mountains (water or snow; icebergs) | Empty Space |
| Dusty Rocks (moon, Mars: craters, dust, rocks) | Giant Gas Bubbles (notebook only) |
| Flying Islands | |
| Bubble World ("POP!", notebook only) | |

World features (A19): planets have destructible ground scenery, liquid areas (water, lava, acid, other; surface level or depth), weather (rain, snow, lightning, meteors, tornadoes), fog and clouds. Space has large non-interactive scenery, floating destructible scenery, special-effect areas (gas, magnetic, radiation fields), active phenomena (solar flares, meteor storms, wormholes) and nebula fog. "Gravity" and "No gravity" are both crossed out on that page.

Planetary scenery ideas (A4): rock pillars, hills, trees, stumps, geysers, bushes, crystals, explosive gas bubble trees, spikes, arches, floating islands, fog blobs, clouds, mist patches, huge domes, gas puffs, static tornadoes and whirlpools, liquid puddles, cracks, craters, alien flora and huge bean stalks, Red Alert-style cliffs, Tiberium-like gems, underwater cacti, surface anomalies, energy pylons, lightning obelisks, vertical plasma beams, buoys.

The demo's tactics screen shows an environment readout in use: condition 70%, occupied 5%, surface type solid, biome "Mossy Moon", fog heavy, features (rock formations, acidic clouds, mossy stones, surface mist), weather lightning, warnings ("Meteor Storm Approaching! Duration 40 seconds, danger level 7, ETA 1:20"; "Reinforcements incoming! Enemy Group 3 (Unknown), 14 objects, ETA 0:50").

## Scale (A17–A18)

The pages are filed as "too small scale oops", so this scale was later judged too small (*interpretation from the filename; the replacement scale is not on paper*).

- 1 Blender unit = 1 m in Unity. Max stable Unity world about **90 km** (7-digit float precision); Earth's circumference 40,000 km for comparison.
- Mothership 16 m long, 6–8 m wide, 3.4 m high; two main defence turrets, a "sideways positron cannon".
- ReWaR 1.2 × 2 × 0.5 m. Rifle 0.6 m, shield 1.1 × 0.5 m, fusion bomb 0.4 m, CM bomblet 1 cm.
- Speeds: human 5–10 m/s; 360 m/s is supersonic and crosses 90 km in about 4 minutes.
- Action field box on the sensor page (S13): 100 × 100 × 100.

V2's environments were to be "very large, details semi-low": the player has extreme speed and sustained flight, so the world must feel limitless and have no upper limit (S54).

## Universal entity standard (S10, S16)

Everything (player, enemies, scenery) follows the same rules: "Same dimension as player character in terms of universal game rules. Maximum consistency is must." "No bullshit allowed."

Universal entity properties: **mass**, **scan integrity** (multiplier 1–5×), **pin strength** (mostly for planetary scenery), **gravity scalar**, damage system, **material system** (what it is made of), **gibs**, collision effects (scaled by impact power), **IsSolid** toggle.

Rules all enemies follow too: ammunition limits on non-energy weapons; heat generation (vent and pause firing); environmental hazards and gravity affect them; universal damage types.

## Damage (S11–S12, S14–S16)

**Health**: every active entity has one hidden HP number ("NOT shown to player at any cost!"). No hit zones or weak points. On top of HP, definable thresholds:

| Threshold | Effect |
|---|---|
| EMP threshold (recharges) | minor effects below it, stun if breached |
| Armor strength | deflects or reduces each shot that is not armour-piercing enough (per shot) |
| Heat resistance | absorbs a cumulative amount until breached |
| Radiation protection | damage once over the max value; the amount is set by the source |
| Kinetic force threshold | not damage: force it can shrug off, else it gets pushed |
| Cryo resistance | like heat resistance |

Example block (S12): HP 1000/1000, EMP 100/100, armor 100, heat resist 10, rad limit 10, kinetic resist 100, cryo resist 100.

Damage types: radiation, fire/heat, EMP, kinetic, cryo.

**Cryo and freezing**: cryo slows the target (increasing delay before each action), makes it weaker to other damage except heat, and eventually freezes it solid. Heat reverses cryo effects (not damage). Freezing only stuns, never kills; it melts away over time depending on the entity and environment. Cryo deals small damage on contact only.

**Destruction**: normal death leaves a **flaming corpse** (corpses have HP). **Overkill** vaporises the entity according to damage type: continuous minor damage breaks it into exploding debris and smoke; major kinetic gives a violent explosion into shreds; major heat melts it into nothing; a major radiation burst makes it light up and dissolve slowly.

**Damage visuals** (S14): normal texture; an opacity-controlled damage texture (0–80% while alive, jumping to 100% at death); impact decals; one internal damage emitter for severe damage (fire, sparks, leaks), or alternatively particles spawning across the whole surface; a death explosion burst.

**Hit effects** (S15–S16) are Direct/Contact (projectiles, beams, bolts) or Area/Ambient (explosions, areas, rays), each Resisted or Unresisted:

| Source | Resisted | Unresisted |
|---|---|---|
| Kinetic (D) | shockwave, shrapnel, debris sparks, small fireball, smoke | bigger flames and fire burst, more shrapnel |
| Heat (D) | localised glow, small heat particles, light flames, minor smoke | plus fire that sticks and burns a few seconds |
| Heat (A) | surface glows orange/red by intensity | surface actually on fire, saturated and reddish |
| Radiation (D/A) | like heat but yellow, slower; surface seems to vibrate | entity seems to slowly vaporise, matter coming off as particles; brighter, desaturated |
| EMP (D) | bright spherical flash, small local arcs, sparks | large arcs spreading across the surface, lingering, blue glow |
| EMP (A) | blue surface glow, random small arcs | many more arcs |
| Cryo (D/A) | cyan glow, white puffs | texture turns progressively whiter |

A variable limits gradual damage when the source is weak enough.

**V1** was simpler: one HP pool, smoke/fire/sparks as damage grows, the robot exploding into five recoverable pieces. **V2's player robot** has a passive barrier plus armor integrity (see [the-unit.md](the-unit.md)).

## Sensors (S13)

- **Galaxy** → **local space**: long-range sensors cover the entire local space. All targets visible as blobs; rough type ID possible in open space; highlighting shows details if known.
- **Action field**: all visible, but lock-on needs closer range.
- **Tactics screen**: top-down map with altitude readouts per group.
- Environment type affects sensor efficiency (slower lock-on, shorter range, slower ID scan).

## Enemies

### Enemy groups (V2, S18–S21, S25)

Enemy groups are factions that threaten mankind directly or indirectly. Some want something (resources, human samples, tech); others exterminate everything. "Anything from savage animals to intelligent, but mad beings". They cannot be reasoned with or beaten by a deus ex machina (no virus, no off switch). **No enemy group is ever fully eliminated**; the game is infinite.

On the metagame, factions are not static: each has its own motives and objectives and pursues them as the player does. Some actively destroy or convert the system.

### Robot Starships, RS (V2: AoY Monsters list 2011-08, S10, S20–S21)

- Origin: a project by an organic civilisation (perhaps humans) that went out of hand; the robots became self-aware, saw their makers as slavers, and turned on them. Self-replicating robot starships that expand across the galaxy consuming resources to build more of themselves.
- Look and feel: inspired by the **Homeworld** ships. Large, heavily armed and armoured, numerous; technology near the player's and familiar (railguns, lasers, missiles).
- Not directly hostile to others, but take any resources they find, so people retaliate. Whoever retaliates is identified as a **threat**, and that identification spreads to every RS unit in the same star system (not beyond). They remember you, attack on detection and hunt you while they can see you.
- **Gatherers** harvest resources and fight only under direct attack (then to the death); **defenders** are pure combat units guarding the gatherers and attack any identified enemy.
- Uniform chassis types and manufacturing standards; simple, straightforward tactics.

**Modular enemy structure** (S10, Monsters list): a **chassis** gives a base AI behaviour and special features (cloak, shield, overcharge…), thrusters, and **hardpoints** that mount weapons, tools or utilities. The 2011 list splits hardpoints into small, large and special:

| Small | Large | Special |
|---|---|---|
| rapid fire, cannon, homing missiles, charge laser, rocket/torpedo, shotgun, tractor beam, EMP cannon | the same plus death ray, nuclear cannon | turning speed, advanced sensors, mine layer, hunter-seeker launcher, drone bay |

The 2012 page simplifies this: "a single HP can mount any system". Size categories: Normal and Large ("heavy-duty"). **Scaling enemy size** (A8): chassis scaled 0.5–3.0×, with hardpoints, thrusters and abilities scaling with it ("Bigger chassis → bigger guns → bigger power"); "excellent for biological type constructs". The modular system was built with the skirmish mode in mind: players can pick chassis and loadouts and set up any battle.

The demo's test models (m1–m7) include green-and-black RS-style ships of several sizes, a large black carrier, a hexagonal pod and a triple-barrel turret.

### V1: The Army

Massive unique monsters and warmachines, organic or machine, built as killing machines by one large evil leader; some so big only one appears at a time, smaller ones in groups.

### V3: Space Monsters

See [versions.md](versions.md). Many unrelated groups instead of factions with motives; from outside the galaxy; nest, replicate, corrupt; individually weak and numerous, may infight; spectacle deaths by element and attack type.
