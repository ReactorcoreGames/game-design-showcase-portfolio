# AAL Universe: simulating a seamless universe

How a continuous universe with no rooms could run on one computer: what is loaded where, how time passes in unloaded places, how detail scales with distance and speed, how far vision works in side view, how travel moves between scales, and the Chaos System that keeps it all above the lag line. This is the part Reactorcore called "a purely technical challenge that I truly need help with". Sources: `Planet Warfare.txt`, `PerformanceSimulations.rtf`, `FarVision.rtf`, EUR (`PW PSRC Equilibrium Universe Rules.txt`), the NVC AI musing, the 3M origin musing, scans W1-15/16, W1-24, W1-26 to W1-28, W1-31, W2-2 to W2-13, W2-15 to W2-26, W2-30, W2-34, PS-5, PS-7, PS-8, PS-31, PS-44, PS-57.

## The goals (W2-8)

- **A seamless universe**: no loading except on a body switch or a teleport to a far area. Only FTL may trigger a loading screen, or a hybrid one where only the craft is simulated, as in Starbound (W2-11).
- **Ultra-high velocity with no "chunk not loaded" rubbish**, in any direction, with sudden changes.
- **Only what matters is stored**: terrain, structures, vehicles and live actors are kept; everything else is regenerated on demand from the area's general data, including the passage of time.
- **Gameplay on two levels**: human scale (destructible terrain, low-level interactions, accurate environment) and high velocity (less detail, more abstraction).

## Storage: the Huge List and the Active List

- `Planet Warfare.txt`: most of the universe sits on disk as a library of text files; far things are dormant data points, "nothing more than a set of coordinates and properties", made live when relevant.
- W1-26/27: a disk-limited **Huge List** holds references to every unique material, object and area, as a tree so area-specific lists load quickly. The **Active List** (an active core in a passive ring) takes from it to build the game view.
- W2-7: what you do in a small area changes its parent's properties (collect all of a nebula's gas and it shrinks; release it and it grows back). "Anything that is unique and not tied to the environment will be remembered, but all other content is procedurally reloaded and regenerated, with any new and old parameters introduced to that specific area."
- PS-19: fields and collections are stored only as material percentages and rolled into objects around the player.
- Tech & Dev rtf: crafted objects are flattened into a single saved entity, loaded and unloaded like world sectors.

## Zones by distance

Several versions of the same idea:

| Source | Zones |
|---|---|
| W1-28 | Active load around the player; an **instant switch range** (switch characters without loading); passive load; far zones that still send events and influence. |
| W2-22 | Visible zone with an active buffer (for zoom-outs and Soldat-style camera moves), active zone (maximum accuracy), passive zone (medium-high: tiny objects unloaded, simplified graphics), low accuracy (minimal physics, ultra-simple graphics), unloaded objects. |
| W2-17 | Event horizons per size class: small, medium, large, huge, moons, planets, stars, galaxies and super big objects each load at their own distance, out to a maximum spawn range. |
| PS-7 | A loaded sphere built in detail around the player, a vague ring beyond, far bodies run as simple L1/L2 objects. |
| PS-44 | Normal 25 m, nearby 75 m, minimum loaded 100 m, maximum visible load 400 m, 1 km loaded, abstract beyond. |
| 3M musing | 1 km radius of loaded elements at 25% zoom, 500 m at 50%, 250 m at 100%. |
| NVC AI | AI fully loaded under 1 km (heavyweight), simplified 1–10 km (mediumweight), abstract beyond 10 km (lightweight), shut down far away except for meta effects. |
| W2-18 | Outside the loaded chunks the world "does not exist". |

## Time in unloaded places

- **Passage of time** (W2-4, `Planet Warfare.txt`, EUR): the game records a global universe time. When you return to an area after a long absence, it is regenerated with a "time passed" variable and aged: overgrown, flooded by melted icecaps, decayed by radioactive waste, rusted, collapsed. Events may fire on return, from the area's contents plus the universe's "ambient pulse". Abandoned places decay; conquered ones host an opponent's base; eradicated ones are wastelands. Strip example: plasma left burning beside a flower takes the spot from +18 °C to +60 °C while you're away.
- **Background routine** (EUR density monitor): every 1–10 minutes a routine walks the universe zone by zone, recalculating, extrapolating consequences and executing events, so the universe "breathes its events" without the player.
- **Time Skip** (W2-26): forward-only time travel (stasis, cryostorage, time machines, chaos portals) using the same system. Risky, since things can decay or block the reappearance spot; Reactorcore flags that case as a "consistency fail".

## Detail scales with significance

- **Anti Butterfly effect** (W2-3): when an overwhelming event hits (a huge bomb on a planet's surface), the tiny events it overpowers (a chemical reaction, a plant spewing water) lose their function and visuals, leaving only their molecular mass, which becomes dust, imprints the terrain or is absorbed into the air. "No values are ever lost, only the computational method changes to a more broad one."
- **Simulation level of detail** (W2-5): automatic, on demand: when the player views a larger space, travels past a speed threshold, or a cataclysm happens. More powerful objects and forces get priority.
- **Principle of significance** (W2-30): LOD 0 (everything, with interior) → 1 (no decor) → 2 (silhouette) → 3 (box) → 4 (a single data point), by size, activity and significance. **Inspection Mode** (LOD -1) shows markings, writing, wear and grunge as in-game clues, one object at a time.
- **3M levels** (PS-8): L0 dot, L1 overall shape (max 4 polygons), L2 largest functional details (10–40), L3 normal view (10–100), L4 close-up (100–400); a maximum polygon density per area; hand-made mipmaps per object.
- **Load order** (PS-5): 0 terrain (with flank canvas and farsight horizon), 0.5 celestial mipmaps, 1 main structs, 2 sub structs, 3 characters and power armor, 4 items and addons, 5 effects; layer 5 unloads first.
- **Shifting states** (W2-25): an artificial object can switch from its physics "aerodynamic state" to a static "resting state" in the background (a tire becomes a flat slab, pants a crumpled heap), by direct player command only. Stacked background piles are fine; wobbly physics towers of junk are not.
- **Debris** (W1-24): loose trash falls by gravity, is absorbed into terrain (dig the node out to get it back), merges, groups by quad tree, is stored in frames, or dissolves into air. "More trash = more chaos levels." EUR's clumps (the smallest terrain unit) fuse back into surrounding terrain if left alone.

## The Chaos System

The universe's in-world anti-lag immune system, presented as a law of nature instead of hidden or apologised for (`Planet Warfare.txt`; AAL lore calls it the Chaos Management System, "Harmony System" being the more accurate name).

- **The spectrum** (EUR): full performance with room to spare → normal → "getting spicy" → (chaos procedures apply here) → lag start, which must never be reached → medium lag → severe lag.
- **Measures**: merging objects, teleporting material into clumps, slowing time, vanishing things into "the shadowrealm" or a far place where they run as data, simplifying or mutating objects, with chromatic aberration, arcs and black space-time tears (`Planet Warfare.txt`). **Chaos Flux** (W2-21): the build-up rate of load, answered in rings, far objects degraded first: immediate area (merging, grouping, overpowering effects, dropping tiny details, full interaction only for the player), **light chaos** (minimal physics, visibility off, fog, sleep), **heavy chaos** (physics shutdown, temporary unloads, outside events off).
- **Density Monitor** (EUR): counts celestials, entities, continents, regions, chunks, clumps and objects per radius at every level, actively near the player and passively everywhere, merging hot spots before they grow. Galaxy counts per cluster have hard maxima (chaos merges extras).
- **Content checks** (W2-34): the Chaos System checks modded content at startup for size, activity potential, significance and part count. EUR: mechanisms must be cheap (one door, not double doors; 3–4 joint tails, not 12); breaking the limits raises an object's culling priority.
- **AI under chaos** (NVC musing): the cleanest measure is to make AI react slower; an overwhelmed NPC is believably awestruck. AI already thinks on a delay (every ~30 frames), which also makes countless tireless AIs fair against one tiring player.
- **Wilderness link**: what the chaos devours isn't deleted; it is displaced, trapped or mutated and may reappear later, often from the Wilderness (AAL lore, UniverseBounds).

## Far vision: seeing ahead in side view

The core presentation problem: "Going fast in 2D sideview is a huge problem, as you cannot see what's in front of you" (W2-12).

- **The background as a pseudo-forward camera** (`FarVision.rtf`, W2-12, PS-31, EUR): distant things appear as desaturated dots in a central "event horizon box", grow and gain contrast as they come nearer, and move from the centre toward the screen edge they will appear from; everything at maximum distance converges on the **infinity star**. You see up, down, left and right, all 360°. Detection reaches up to 100 AU. Only ambient light is allowed in the background. Solid background walls and big near objects eclipse what's behind them.
- **Potency** (W2-15): an object loads into the sky only if its potency (size, brightness, significance against distance) is above a threshold; big objects get priority; light pollution from nearer objects reduces visibility. A "view from Earth" sketch puts an aurora (80 km), the moon (384k km), the sun (1 AU), the Milky Way and a distant supernova in one sky.
- **Two models** (W2-15/16): **Type 1**, realistic: no distance limit, one global potency-sorted list with a load cutoff, procedural starfield. **Type 2**, sector-based: a hard limit at 100 AU, per-sector object lists separated by sector separation space, nested by scale.
- **The LOD path to ground** (EUR): a celestial appears as a dot, then a circle gaining texture and saturation, then its continents as primitive shapes, then regions, then chunks of terrain, then main and sub structs as primitives, then their components (doors, antennas, weapons) by size, then full detail at the edge of the far view, then you arrive. Region **shadow backgrounds** stay visible at ground level and block the horizon when you dig underground.
- **Moving between layers** (W2-17): objects pass from the background (drawn desaturated, brighter or darker) into the real layer, mirrored across when they cross the horizon; an ICBM leaves the play layer, flies through the background and comes back down. The side-view play area is drawn as a window onto a whole planet.
- **Horizons on an Earth-size planet** (PS-57): from 2 m you see 5 km, from 20 m 16 km, from 12 km 400 km, from 500 km 2,600 km.

## Travel between scales

- **Travel levels** (W2-6): 1 planetary surfaces, low speed; 2 normal space and atmospheres, high velocity; 3 interstellar FTL (hyperspace); 4 intergalactic, beyond FTL; 5 between universes. Levels 1–2 are "real" play; 3–4 are UI- or sensor-based.
- **Sensor views** (W2-9): anything above the speed layer is a view through an in-world sensor, which a being needs a compatible optics interface to use. Stronger sensors give higher view levels; views can be infrared, radiation, pressure. Leaving a view is instant, and the playable stage is never unloaded.
- **Zoom** (W2-13, EUR): maximum zoom-in 600%; 50% on foot with binoculars or at high velocity; 25% through an interface for epic scale. EUR: non-mipmapped zoom 400% to 50%, lesser details unload at 25%.
- **FTL** (W2-10/11): an FTL Phase Field (graviton field distortion) means only stellar-class bodies can be hit at FTL; a crash turns the screen white (black if fatal) and the result is remembered. AAL lore adds that FTL slows to a crawl near large gravity sources and is useless below about a moon's high orbit, so ships use conventional thrust near planets.
- **Seamless space transition** (W1-15/16, after RayForce stage 3; W2-2): pick a point on the planet (mandatory); over 5–10 seconds the ship flies to it while the planet zooms in and rotates the entry point to the top; cancel, rotate and move stay possible; the view shifts 90° into side view through a short transit. W2-2: an **Entry Field** ring marks the switch; orbital strikes and choosing your own landing zone; ships in orbit and landed units can target each other.

## System layers (W2-19)

GUI; lighting; energy areas/entities (forces); foreground objects; solid active objects (characters, vehicles); background objects; background local atmosphere (an optical filter); Astral Plane; major vehicles and buildings (Movable Frames); terrain; loose materials and gibs; Chaos Monitor. EUR's render order: background < ethereal terrain (gas) < projectiles < liquid terrain < solid terrain < objects < characters < effects < HUD.

## Open questions

- Which far-view model (Type 1 or Type 2), and the hard detection limit.
- How the 2011 split (top-down space, side-view everywhere else) fits the later fully side-view universe; W1-15 still turns the view 90° on landing. See [cohesive-design.md](cohesive-design.md).
- The ranges above disagree (25 m to 1 km for "loaded"); they need one table tied to the final scale.
- "Overpowering effect" (W2-21) isn't explained.
