# Standalone: versions

Standalone was redesigned several times over thirteen years, and later material usually overrides earlier material. Reactorcore asked for the versions to stay findable as alternative variants rather than be flattened into one, so this file sets them out side by side. The project folder outside the repo (`C:\08 Projects\Project_Standalone\`) is now organised by these same version numbers.

**The current vision is V3** (the 2023 pitch document plus the 2024 weapon note), with **V2 supplying the detail**: the notebook pages and the 2013 Unity demo, which Reactorcore calls the project's "true vision" for flow and systems. Where V2 and V3 conflict, V3 wins. Everything earlier is a variant.

Dates come from file timestamps, a "(2012)" written on S24, and the notebook's own era markers ("AoY" headings, paper, pen). The notebook pages themselves were photographed on 2019-10-05, so that date says nothing about when they were written.

## Timeline

| When | What | Version |
|---|---|---|
| before 2011 (undated) | "SA concept #1", World 1 pitch, wheeled robot sketches, "Features of Standalone" (E1–E5, R35–R37) | V0 |
| 2011-05 | *Adventures of You* design document versions 1.0 and 2.0; Planetary/Space level mockups | V1 |
| 2011-05 to 2011-08 | AoY content lists: environments, effects, monsters (Robot Starships), player (spartan shield + arm rifle) | V2 |
| 2011-06 | AoY design document version 3.0: "a standalone, special forces military unit"; low-poly pixel-textured look | V2 |
| 2011 | "AoY"-headed notebook pages (R12, R13, A19–A21, A8, X2–X3) | V2 |
| 2011-10 | ReWaR developer log; mothership line sketch | V2 |
| 2011-08 to 2012-01 | Construction plan, master plan with marketing, intro spec, action component plan, construction todo | V2 |
| 2012 | The bulk of the notebook: systems, metagame, menus, damage, art, scale (S1–S54, A1–A18, R1–R11, R14–R34) | V2 |
| 2013-05 | The Unity click-through demo (18 screens) with ReWaR, mothership and enemy test models | V2 |
| 2013-12 | Skirmish mode setup screen mockup | V2 |
| undated, later notebook | Spinoffs: Standalone 2D editions, Standalone 2, Cyberspace Alternative, User Creative Tools (X1–X6) | spinoffs |
| 2023-12 | `Standalone.txt`, the pitch document, with its illustration set | V3 |
| 2024-05 | "Standalone multi weapon idea (new)": the full arsenal, Jager-gun modularity, supercores | V3 |

## V0: the piloted Standalone (before 2011)

"You pilot a Standalone, the greatest weapon ever designed. You fight against armies on your own." (E1)

- **You are a pilot**, not an AI. The Standalone is one machine with life support and a pilot (R35). No mothership; E5 gives the robot a **supply copter/dropship** instead.
- **The machine**: E4 sketches a stubby, egg-shaped **wheeled robot** with suspension legs, a 360° head, side and front boosters, a fold-out "leg support (parking or artillery)" strut and a back weapon holster. R35–R37 describe a humanoid with a **central super reactor**, two arm guns that each combine a close-range system and a variable energy rifle (infinite ammo, heat managed), and a **merged super rifle**: the whole SA becomes one big gun, an overcharge (OC) system on its back vents waste heat as collateral damage and forms an aura, the charge can be aborted, and firing leaves it immobile and unshielded for a recovery delay. The close-range system has four modes: solid long blade, wide energy ray, whip blade array, shield emitter (R37).
- **Structure**: a Scenario System (worlds, scripts, missions → "epic battles/challenges" and a "story campaign") plus moddable assets (E1, E3). "GunMetal style open environment" with boundaries and background terrain (E2).
- **World 1 pitch** (E5): open world action; barren worlds (desert, tundra, no organic life) occupied by robots, turrets, builders and bosses; "you and them are from same origin, but you are independent and your robot is unique"; attack and steal; blow up fortifications, robotic defenders and large super warmachines. Near-modern tech with emphasis on explosives, rockets, artillery. Low-poly, pixel-textured, believable; movement physics and momentum important.

**What survived:** the lone overpowered unit against armies, the momentum, the moddable scenario system, the low-poly pixel look, the blade/shield/rifle multi-mode weapon (it becomes the ReWaR's arm rifle), and the overcharged super shot (it becomes the Buster cannon). **What was dropped:** the human pilot, the dropship, wheels.

*S54 ("SA gameplay": third-person view, Mass Effect 2 Hammerhead hover movement, cockpit startup) talks of "piloting" a single SA and never mentions the mothership. It sits in the 2012 notebook and its camera notes match V2, so it is filed under V2, but it may be a V0 leftover.*

## V1: Adventures of You (May 2011)

The design document's versions 1.0 and 2.0 (`AoY design document v1 and v2 (2011-05).md` in the project folder).

- **You are an AI called "You"** aboard a long-range exploration ship, alone in deep space. You control the mothership and a humanoid **robot warrior** (no name yet).
- **Structure**: mission-based. A hand-made **campaign** of linear missions with objectives (destroy, escort, defend, infiltrate), unlocked one by one, "Star Fox 64 like ... with the exception of no rails", ending in an epic showdown; a **challenge mode** (a VR simulation aboard the ship) where you set up any fight with content unlocked in the campaign; mission times as a replay goal.
- **Enemy**: v1 "alien monsters", v2 **"The Army"**: massive unique monsters and warmachines led by "one very large evil entity".
- **Losing**: losing the mothership is game over (v1: losing either is). No persistent character.
- **Robot**: FPS-style controls; Variable Energy Rifle (machinegun / blast cannon / shield emitter), separate arm energy blade (one-handed blade use spoils the rifle's accuracy), missiles, remote thermonuclear bombs; deployed by linear catapult with a power-up system check, must dock at the end. On death it **splits into 5 pieces** the mothership must collect with a tractor beam before rebuilding.
- **Mothership**: auto-fires, takes support orders (artillery, covering fire, area denial), harvests resources (crystals, asteroids, gas) that pay for repairs, ammo and rebuilds; tactical command console with a full map.
- **Environments**: a square playfield inside a limitless flat area; no invisible walls, just a warning (the Planetary/Space level mockups of 2011-05 show this). Terrain fixed, scenery destructible.
- Modding (monsters and maps), co-op (shared mothership) and versus modes.

**What survived:** the AI in the mothership, the robot as a rebuildable proxy, resources gathered by the mothership, the tactics console, catapult launch, the challenge mode (as Quick Game / Skirmish). **What was dropped:** the authored linear campaign and story, The Army and its leader, the five-piece wreck recovery.

## V2: Standalone, 2011–2013 (the notebook and the Unity demo)

Starts with the design document's version 3.0 (June 2011), which first calls the unit "a standalone, special forces military unit", and runs through the 2012 notebook to the 2013 Unity demo. This is by far the most detailed version; the digest's topic files describe it in full.

- **The unit**: the **mothership (MS)** holding the AI core, and the **ReWaR** (Remote Warrior Robot), a transformable biped/jet mecha. Together: a **Standalone (SA) unit**. See [the-unit.md](the-unit.md).
- **Persistent character with permadeath**: one character per profile (core, ship and mech names and colours). Losing the mothership erases the character. No save/load, only autosave plus two hidden emergency backups.
- **Campaigns**: each is a randomly generated **local star system** (or planetary system, or starless space) shown as a metagame map; enemies pursue their own goals on it; the campaign ends when all threats are gone or the place becomes lethal. Death mid-campaign: the next character arrives later and the enemy has had bonus time. Galaxy-scale progress is deliberately never shown.
- **Enemies**: enemy groups that are never fully eliminated; the first is the **Robot Starships (RS)**, Homeworld-inspired self-replicating resource gatherers built from modular chassis and hardpoints.
- **Modes**: Campaign (persistent), Quick Game / Skirmish (sandbox, no stats, no permadeath), Training (VR lessons).
- **Database** filled by scanning; enemy designation codes and nicknames.
- **Look**: deliberately ultra-simple low-poly graphics with small pixel textures and anime-style effects; no music (the player brings their own).
- **Production**: Unity, a menu-first build order, an episodic/expansion-pack business plan, and a click-through demo of all 18 screens (2013-05).

## V3: the pitch (December 2023 – May 2024)

`Standalone.txt` (kept as is in this folder) and the 2024 multi-weapon note. Read the pitch in full; the main changes from V2:

- **Enemy**: the **Space Monsters**, not one faction but every loose group of rogue monsters, masterless robots, rabid animals and infected zombie fleets, usually from outside the Milky Way, often some lost civilisation's mistake. They seed nests, replicators and factories on planets, stars, gas giants, belts, nebulae and moons, corrupt the system and spread. Groups fight each other too. Individually weak, numerous; the real danger is logistics.
- **The unit** is "an all-environment self-sustainable deep-space von-neumann probe assault battleship superweapon" with a mecha bay and linear catapult. The player is the AI, split between the two; the mothership goes on autopilot when not controlled. Built by humanity as a last measure.
- **Campaign**: a generated, **tile-based star system map** "slightly reminiscent of Freelancer's star maps", zones for nebulae, debris fields, planets, moons and stars; enemies move and corrupt locations while you race to intercept.
- **Semi-permadeath**: you name the mecha before starting and are locked to that name. A destroyed unit is **enshrined in a permanent casualty list** and its name can never be reused. Death does not reset the campaign: a new unit takes over, usually facing worse odds. A system that becomes too corrupt must be **destroyed by detonating its sun**, which leaves a permanent mark of shame in the logs (like XCOM's memorial). The universe is persistent; star system campaigns are temporary.
- **Feel**: an empowerment game. Abundance, excess, overkill; infinite flight, extreme speed, nukes and beam cannons from the start; a flow-state game meant to be played to your own music (Beat Saber, Audiosurf, Beat Hazard as the feel references). Physics momentum: you keep your speed and must brake; slide, skate, glide and throw yourself around with thrusters; turn on a dime.
- **Format**: third-person shooter, 3D or 2D; the metagame works for either.
- **Mecha**: a mix of Wing Gundam Zero (transforms to a jet) and Freedom Gundam (multi-lock-on), more overpowered than both. Shield withstands a nuke; it can fire a nuclear warhead.
- **Mothership**: prints a new mecha (costs resources gathered by helper drones), repairs, refuels and rearms both, FTL, a main cannon that wipes a fleet in one shot.
- **Spectacle kills**: elemental properties and attack type decide how enemies break apart.
- **Potential**: endless monsters and locations added to the generator's pool, variant and modular mecha/motherships, co-op with two Standalone units.
- **2024 weapon note**: the full V2-derived arsenal listed in one place; every weapon multi-mode; customisation by "Jager gun" modular nozzles or swappable elements, or alternative non-humanoid frames (Zoids-like, Zeon mobile armour); **supercores** held by enemies. See [the-unit.md](the-unit.md).

**Unchanged from V2**: AI in a mothership plus rebuildable transformable mecha, generated star system campaigns, persistent universe and logs, permadeath of the mothership, resources and drones, catapult launch, momentum physics, the overpowered lone unit.

**Changed from V2**: Space Monsters replace the Robot Starships as the enemy concept; a casualty memorial and sun detonation replace the V2 "erase the character" bluntness; you name the mecha before the game; the game wants to be played to your own music (V2 also had no music of its own, so that is a reframing rather than a change); 2D is allowed.

## Spinoffs

Separate games branched from Standalone; not part of the main line. See [spinoffs.md](spinoffs.md).

- **Standalone 2D editions** (X1): a side-view version with looping vertical layers and 1 km chunks.
- **Cyberspace Alternative** (X2–X4): an AoY roguelite, Gungeon/Isaac-style linear runs.
- **Standalone 2** (X6): a modular mech with arm and leg system slots.
- **User Creative Tools** (X5): a camera actor, screenshot mode and replay recording; tooling more than a spinoff.
- **Double AI co-op** (R1): two players sharing one SA and swapping between mothership and ReWaR by mutual agreement; a V2 mode idea, filed with V2.
