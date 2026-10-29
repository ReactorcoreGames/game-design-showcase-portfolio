# AAL Standalone: design digest

This folder is the text form of Standalone's design. It was digested on 2026-10-29 from 127 scanned notebook pages, 16 RTF documents (2011–2012), the 18-screen Unity demo of 2013 and its renders, and the later pitch document. Read this instead of the scans; the process is in `workflow/scan-digest.md`. The project folder outside the repo is `C:\08 Projects\Project_Standalone\`. It was reorganised in the same session into version folders, with every scan renamed after its code below, and it holds a copy of this digest in `5 digest\`.

## Summary

You are an AI, split between a **mothership** and a transformable **mecha** it can rebuild, a lone tandem superweapon called a **Standalone** that humanity sent out to clear star systems of threats it cannot reason with. Each campaign is a generated star system shown as a map: the enemy pursues its own plans on it while you pick your fights. A fight is a fast third-person battle on a planet or in space, with momentum physics, infinite flight, beam rifles, shields that shrug off nukes, guided fusion bombs, and the mothership's railgun turrets and main cannon in support. The mothership harvests resources with drones, repairs and rearms both machines, and prints a new mecha when you lose one, so you can be reckless with the mecha. Lose the mothership, though, and that unit is gone for good: its name joins a permanent casualty list and a new unit inherits a worse situation. The game is about the pure empowerment of an overpowered machine, played in a flow state to your own music; it has no story to uncover and never counts how much of the galaxy you've cleared.

Standalone is one of Reactorcore's oldest projects (started before 2011; *Adventures of You* in 2011; a full design and a click-through Unity demo in 2012–2013; a pitch in 2023). The AAL Terrene games (Collector, Exterminator, Voyager) are set after it. The AAL Inspector design (`designs/done/AAL Terrene Clones/`) opens "after events of 'AAL Standalone'": human scouts visit the star systems the Standalones secured, and clear out dormant, weakened Space Monsters the Standalones missed. The Standalones also left behind outpost factories and automated bots that keep the peace. AAL Exterminator's smart bomb is modelled on "Standalone's versatile fusion missile/grenade hybrid".

## Versions

Later material overrides earlier. **V3 (the 2023 pitch and the 2024 weapon note) is the current vision; V2 (the 2012 notebook and the 2013 demo) supplies the detail.** V0 and V1 are kept as variants. Full comparison in [versions.md](versions.md).

| Version | When | In short |
|---|---|---|
| V0 | before 2011 | You *pilot* a Standalone, one machine with a supply dropship; wheeled-robot sketches; merged super rifle |
| V1 | 2011-05 | *Adventures of You*: the AI "You", mothership plus robot warrior, authored mission campaign and challenge mode, "The Army" |
| V2 | 2011–2013 | Standalone: MS + ReWaR, persistent character with permadeath, generated star system campaigns, Robot Starships, Database, Unity demo |
| V3 | 2023–2024 | The pitch: Space Monsters, casualty memorial, sun detonation, flow-state empowerment, 2D or 3D, full arsenal, supercores |

## Files

| File | Covers |
|---|---|
| [versions.md](versions.md) | Timeline and every version side by side, what survived and what was dropped |
| [the-unit.md](the-unit.md) | The mothership and the ReWaR: systems, flight, thrusters, sensors, weapons, the rifle's modes, shield, fusion bomb, controls, the V3 arsenal, Jager-gun modularity, supercores |
| [world-and-combat.md](world-and-combat.md) | Planetary and space worlds, world components and layers, environments, scale, the universal entity standard, damage and its effects, sensors, enemy groups, Robot Starships, The Army, Space Monsters |
| [campaign-and-modes.md](campaign-and-modes.md) | The design's intent, the campaign metagame, entering battles, permadeath and saving, Quick Game/Skirmish, Training, Database and scanning, profiles |
| [interface-and-demo.md](interface-and-demo.md) | The 2013 Unity demo screen by screen, the demo renders, the screen flow, every menu and screen, HUD and camera |
| [art-and-production.md](art-and-production.md) | Art direction, Ultra Simple Graphics Style, effects, textures, asset standards, sound, production and business plans |
| [spinoffs.md](spinoffs.md) | Standalone 2D editions, Cyberspace Alternative roguelite, Standalone 2, User Creative Tools, Double AI co-op |
| [transcript/](transcript/) | Scan-by-scan transcripts in 7 chunks, all text and diagrams described; the source for everything above. They cite scans by their original filenames (listed in the table below) |
| `Standalone.txt` | The 2023 pitch document, kept as is (V3) |

*(interpretation)* marks Claude's reading of an unclear note. Open questions are listed at the end of each transcript chunk and collected below.

## Sources outside the scans

In the project folder, converted to markdown in the same session (the RTF originals are in `9 archive - original RTF documents\`):

- `1 V1…\AoY design document v1 and v2 (2011-05).md`
- `2 V2…\1 docs\`: `AoY design document v3 (2011-06).md`, `AoY content lists (2011-06 to 2011-08).md` (player, monsters, environments, effects), `AoY ReWaR requirements and intro sequence (2011-10, 2012-01).md`, `AoY production and marketing plans (2011-08 to 2012-01).md`
- `3 V3…\Standalone pitch document (2023-12).md` (this folder's `Standalone.txt`), `Standalone multi weapon idea (2024-05).md`, `pitch images (2023-12)\`
- `2 V2…\6 Unity demo (2013-05)\` and `7 other mockups\`, read directly for this digest (no transcript; described in [interface-and-demo.md](interface-and-demo.md))

Duplicates dropped in the cleanup: `AdventuresOfYou.rtf` (an earlier save of the design document), `AoY_EnviroContentList.rtf` and `AoY_EnviroList.rtf` (identical, both inside `AoY_Content_Enviro.rtf`), `AoY_GenericEffectsContentList.rtf` (identical to `AoY_Content_Generic.rtf`), `AoY_Content_Player.rtf` (the stub at the end of `Player2`), and `STANDALONE demo\Image (28).jpg` (byte-identical to the X1 scan). The RTFs are kept in the archive folder; only the image was deleted. The JPEGs in `pitch images (2023-12)\` are 2023 re-exports of demo material made for the pitch, kept as that set.

## Glossary

- **Standalone / SA**: the tandem combat unit (mothership + mecha), and the game. Each unit has a unique ID (e.g. "SA-56"). **AoY**: *Adventures of You*, the 2011 working title; the AI you play was called "You".
- **MS**: the mothership (carrier). Holds the AI core; its loss is permanent death. **ReWaR / RWR**: Remote Warrior Robot, the transformable biped/jet mecha the AI remote-controls; rebuildable.
- **Core**: the AI itself; has its own name and colour (core/energy colour tints shields, thrusters and weapon effects). Shown as a HAL 9000-style lens.
- **Arm rifle / Variable Energy Rifle / temgrav rifle**: the ReWaR's multi-mode particle weapon (rapid fire, charge cannon, spread, blade, tractor; Buster mode). **Buster**: the ultimate overcharged rifle or sword configuration.
- **Fusion bomb / megabomb / FSB**: compact guided thermonuclear-type bomb, stuck, placed, thrown or launched. **CM**: countermeasures (bomblets, flare guns). **EM/IM missiles**: the ReWaR's small missiles (EM missile / micromissile, *interpretation*).
- **RV / RU**: resource values/units, harvested by drones from rocks, crystals, asteroids and gas; pay for repairs, ammo, drones and new ReWaRs.
- **LAB**: the mothership's fabricator (drones, ammo, ReWaR). **PD**: point defence. **RCS**: reaction control thrusters. **ATR / IFF**: automatic target recognition / friend-or-foe.
- **Metagame / local space**: the generated star system map of a campaign. **Galaxy screen**: the level above it, deliberately without progress. **Entry point / entry angle**: where and how you drop into a battle.
- **Action / action field**: the real-time battle. **Tactics screen**: the non-pausing battle map for orders and production.
- **Quick Game / Skirmish**: sandbox battles, no permadeath. **Training**: VR lessons. **Challenge mode**: V1's skirmish.
- **Database / Db**: the in-game encyclopedia ("Ufopedia of sorts"), filled by **scanning**; enemy **designations** like RS-1, plus player **nicknames**.
- **Enemy groups**: factions never fully eliminated. **RS**: Robot Starships, the first group. **Gatherers / defenders**: RS roles. **Chassis / hardpoints**: the modular enemy build. **The Army**: V1's enemy. **Space Monsters**: V3's enemy.
- **Effect area**: a Freelancer-style cloud zone with contents and priority. **Weather layer**, **exclusion area**, **killzone**.
- **Universal entity standard**: shared rules (mass, scan integrity, pin strength, gravity scalar, materials, damage, gibs, IsSolid) for every object. **Overkill**: destruction that vaporises by damage type.
- **Supercore**: an enemy-held power object you can steal (2024 note; see `reference/supercores.md`).
- **Jager guns**: the 2024 idea of modular gun "nozzles" strapped to a modular mech in place of its standard systems.
- **Ultra Simple Graphics Style**: the deliberately minimal low-poly, flat-colour and pixel-texture look.

## Open questions for Reactorcore

Collected from the transcripts; none blocks a page.

1. **V0**: was the piloted Standalone (E1, E5, R35–R37, and possibly S54's hover-legged "SA gameplay") the original concept before the AI and mothership? Is E4's wheeled egg-shaped robot the first form of the mecha?
2. **Scale**: the A17–A18 scale pages were filed as "too small scale oops". What scale replaced the 16 m mothership and 2 m ReWaR?
3. **Mothership guns**: R10 gives the general turrets variable energy weapons; R8 makes the main turrets railguns using resource-made ammo. Which is later? (V3's 2024 list has railgun multigun turrets, so probably railguns.)
4. **Campaign time**: S30 says the campaign runs "semi-realtime, similar to Star Fox 2", while the 2013 demo's map has action points and End Turn. Which was the intent?
5. **Demo abbreviations**: MSSL, RAILG, MAING, FSB, EMIIM, CAP on the tactics screen. Guesses are in [interface-and-demo.md](interface-and-demo.md).
6. **Cyberspace Alternative**: the second game name after "Gungeon/" (Isaac?), and the word in "R?force Campaign" (X4).
7. **Unclear labels**: "GRS1 style laser system" and "FM" (R8); L2–L5 on the thrusters (R9); "D/E" buttons (S34, S36); "KATSUYA EGUCHI" on S16.
8. **Head style** (R16): which of the sketched eye styles (Gundam, Votoms, Armored Core, Iron Giant…) was the chosen one? The 2013 model has a square head with a round red sensor.

## Scan table

Codes are Claude's, assigned for this digest; in the project folder each scan is now named `<code> <title>.jpg` (codes zero-padded, e.g. `S07`). "Era" is the version folder it went into. Chunks: 01 = `transcript/01-earliest-spinoffs-misc.md`, 02 = `02-art-scale-world.md`, 03 = `03-mothership-rewar-1.md`, 04 = `04-rewar-weapons-controls.md`, 05 = `05-systems-1.md`, 06 = `06-systems-2.md`, 07 = `07-systems-3.md`. No scan was title-only or unreadable; all were transcribed in full.

| Code | Original file (`FotoScan_Standalone\`) | Title | Era | Chunk |
|---|---|---|---|---|
| E1 | `earliest/1 earliest raw ideas (1).jpg` | SA concept 1 mind map | V0 | 01 |
| E2 | `earliest/1 earliest raw ideas (2).jpg` | GunMetal style environment | V0 | 01 |
| E3 | `earliest/1 earliest raw ideas (3).jpg` | mod friendly scenarios note | V0 | 01 |
| E4 | `earliest/1 earliest raw ideas (4).jpg` | wheeled robot and weapon sketches | V0 | 01 |
| E5 | `earliest/1 earliest raw ideas (5).jpg` | World 1 and art direction | V0 | 01 |
| X1 | `x other/2D sideview spinoff.jpg` | Standalone 2D editions | spinoff | 01 |
| X2 | `x other/linear gauntlet campaign spinoff (1).jpg` | Cyberspace Alternative roguelite | spinoff | 01 |
| X3 | `x other/linear gauntlet campaign spinoff (2).jpg` | Cyberspace Alternative randomizable content | spinoff | 01 |
| X4 | `x other/linear gauntlet campaign spinoff (3).jpg` | Cyberspace Alternative campaign shapes | spinoff | 01 |
| X5 | `x other/user creative tools.jpg` | User Creative Tools | spinoff | 01 |
| X6 | `x other/x offshoot idea.jpg` | Standalone 2 | spinoff | 01 |
| M1 | `misc/IMG_20191005_143328.jpg` | render layer stack | V2 | 01 |
| M2 | `misc/x loose assets lists (1).jpg` | AoY generic effects printout with notes | V2 | 01 |
| M3 | `misc/x loose assets lists (2).jpg` | AoY environment assets printout with notes | V2 | 01 |
| M4 | `misc/xstandalone mesh colorer exploder.jpg` | mesh colorer exploder baker sticky note | V2 | 01 |
| A1 | `art related/1 deliberate low poly artstyle (1).jpg` | Ultra Simple Graphics Style part 1 | V2 | 02 |
| A2 | `art related/1 deliberate low poly artstyle (2).jpg` | Ultra Simple Graphics Style part 2 | V2 | 02 |
| A3 | `art related/1 deliberate low poly artstyle (3).jpg` | microart style scenery | V2 | 02 |
| A4 | `art related/1 deliberate low poly artstyle (4).jpg` | terrain and planetary scenery ideas | V2 | 02 |
| A5 | `art related/1 deliberate low poly artstyle (5).jpg` | naming conventions and asset list | V2 | 02 |
| A6 | `art related/1 deliberate low poly artstyle (6).jpg` | pixel art scenery pack | V2 | 02 |
| A7 | `art related/1 deliberate low poly artstyle (7).jpg` | models graphics stages | V2 | 02 |
| A8 | `art related/2 misc gfx ideas (1).jpg` | scaling enemy size | V2 | 02 |
| A9 | `art related/2 misc gfx ideas (2).jpg` | exclusion areas | V2 | 02 |
| A10 | `art related/2 misc gfx ideas (3).jpg` | Great Fox booster effect | V2 | 02 |
| A11 | `art related/2 misc gfx ideas (4).jpg` | expanding water splash | V2 | 02 |
| A12 | `art related/2 misc gfx ideas (5).jpg` | Star Fox 64 destruction effects | V2 | 02 |
| A13 | `art related/i already built this too (1).jpg` | effect textures sticky note | V2 | 02 |
| A14 | `art related/i already built this too (2).jpg` | texture thumbnails substances energy | V2 | 02 |
| A15 | `art related/i already built this too (3).jpg` | texture creation guidelines | V2 | 02 |
| A16 | `art related/i already built this.jpg` | Basic Primitives Mega Pack | V2 | 02 |
| A17 | `art related/too small scale oops (1).jpg` | mothership scale and world size | V2 | 02 |
| A18 | `art related/too small scale oops (2).jpg` | scale speeds ReWaR and weapon sizes | V2 | 02 |
| A19 | `art related/world features (1).jpg` | AoY world features | V2 | 02 |
| A20 | `art related/world features (2).jpg` | AoY enviro listing 1 | V2 | 02 |
| A21 | `art related/world features (3).jpg` | AoY enviro listing 2 | V2 | 02 |
| R1 | `rewar mech or mothership/IMG_20191005_134905.jpg` | double AI coop idea | V2 | 03 |
| R2 | `rewar mech or mothership/IMG_20191005_142134.jpg` | mothership sketches and interior system | V2 | 03 |
| R3 | `rewar mech or mothership/IMG_20191005_142141.jpg` | ReWaR sketches with shield and rifle | V2 | 03 |
| R4 | `rewar mech or mothership/IMG_20191005_142209.jpg` | mothership sensors and electronics | V2 | 03 |
| R5 | `rewar mech or mothership/IMG_20191005_142218.jpg` | mothership ecosystem | V2 | 03 |
| R6 | `rewar mech or mothership/IMG_20191005_142240.jpg` | hull and jet sketches | V2 | 03 |
| R7 | `rewar mech or mothership/IMG_20191005_142245.jpg` | robot body sketch | V2 | 03 |
| R8 | `rewar mech or mothership/IMG_20191005_142300.jpg` | mothership main and PD turrets | V2 | 03 |
| R9 | `rewar mech or mothership/IMG_20191005_142306.jpg` | mothership flight systems | V2 | 03 |
| R10 | `rewar mech or mothership/IMG_20191005_142332.jpg` | mothership armaments | V2 | 03 |
| R11 | `rewar mech or mothership/IMG_20191005_142337.jpg` | megabomb CM gun targeting optics | V2 | 03 |
| R12 | `rewar mech or mothership/IMG_20191005_143602.jpg` | AoY robot features | V2 | 03 |
| R13 | `rewar mech or mothership/IMG_20191005_143613.jpg` | AoY mothership features | V2 | 03 |
| R14 | `rewar mech or mothership/IMG_20191005_143810.jpg` | ReWaR torso and shoulder mechanics | V2 | 03 |
| R15 | `rewar mech or mothership/IMG_20191005_143822.jpg` | ReWaR thrusters by body part | V2 | 03 |
| R16 | `rewar mech or mothership/IMG_20191005_143903.jpg` | ReWaR head features and styles | V2 | 03 |
| R17 | `rewar mech or mothership/IMG_20191005_143914.jpg` | ReWaR limb R&D | V2 | 03 |
| R18 | `rewar mech or mothership/IMG_20191005_143925.jpg` | ReWaR body and thruster sketches | V2 | 04 |
| R19 | `rewar mech or mothership/IMG_20191005_143933.jpg` | ReWaR torso features | V2 | 04 |
| R20 | `rewar mech or mothership/IMG_20191005_143951.jpg` | ReWaR arms | V2 | 04 |
| R21 | `rewar mech or mothership/IMG_20191005_144009.jpg` | AoY ReWaR rifle | V2 | 04 |
| R22 | `rewar mech or mothership/IMG_20191005_144102.jpg` | rifle ranged modes | V2 | 04 |
| R23 | `rewar mech or mothership/IMG_20191005_144234.jpg` | ReWaR head and lockon sketches | V2 | 04 |
| R24 | `rewar mech or mothership/IMG_20191005_144327.jpg` | rifle melee and buster modes | V2 | 04 |
| R25 | `rewar mech or mothership/IMG_20191005_144335.jpg` | rifle firing sequence | V2 | 04 |
| R26 | `rewar mech or mothership/IMG_20191005_144536.jpg` | particle beam appearance | V2 | 04 |
| R27 | `rewar mech or mothership/IMG_20191005_144543.jpg` | additional rifle components | V2 | 04 |
| R28 | `rewar mech or mothership/IMG_20191005_144700.jpg` | rifle and mount sketches | V2 | 04 |
| R29 | `rewar mech or mothership/IMG_20191005_144707.jpg` | weapon module and bomb sketches | V2 | 04 |
| R30 | `rewar mech or mothership/IMG_20191005_144721.jpg` | fusion bomb and biped-jet shifting sketches | V2 | 04 |
| R31 | `rewar mech or mothership/IMG_20191005_144907.jpg` | ReWaR shield | V2 | 04 |
| R32 | `rewar mech or mothership/IMG_20191005_144943.jpg` | ReWaR remote guided fusion bomb | V2 | 04 |
| R33 | `rewar mech or mothership/IMG_20191005_144955.jpg` | fusion bomb impact cap and attachers | V2 | 04 |
| R34 | `rewar mech or mothership/IMG_20191005_145502.jpg` | mothership controls | V2 | 04 |
| R35 | `rewar mech or mothership/Image (149).jpg` | Features of Standalone - super reactor and merged super rifle | V0 | 01 |
| R36 | `rewar mech or mothership/Image (150).jpg` | Features of Standalone - super rifle recovery | V0 | 01 |
| R37 | `rewar mech or mothership/Image (151).jpg` | close range weapon modes | V0 | 01 |
| S1 | `menus maps metagames systems/IMG_20191005_134541.jpg` | character edit screen | V2 | 05 |
| S2 | `menus maps metagames systems/IMG_20191005_135120.jpg` | briefing screen and entry point | V2 | 05 |
| S3 | `menus maps metagames systems/IMG_20191005_135159.jpg` | tutorial refresher overlay | V2 | 05 |
| S4 | `menus maps metagames systems/IMG_20191005_135410.jpg` | unique IDs and ReWaR-only battles | V2 | 05 |
| S5 | `menus maps metagames systems/IMG_20191005_140012.jpg` | demo setup plan | V2 | 05 |
| S6 | `menus maps metagames systems/IMG_20191005_140037.jpg` | tactics screen and screen order | V2 | 05 |
| S7 | `menus maps metagames systems/IMG_20191005_143220.jpg` | world components | V2 | 05 |
| S8 | `menus maps metagames systems/IMG_20191005_143226.jpg` | weather layers and space level v2 | V2 | 05 |
| S9 | `menus maps metagames systems/IMG_20191005_143302.jpg` | world system planetary vs space | V2 | 05 |
| S10 | `menus maps metagames systems/IMG_20191005_145029.jpg` | enemy types and common rules | V2 | 05 |
| S11 | `menus maps metagames systems/IMG_20191005_145204.jpg` | cryo and freezing | V2 | 05 |
| S12 | `menus maps metagames systems/IMG_20191005_145213.jpg` | damage system overall | V2 | 05 |
| S13 | `menus maps metagames systems/IMG_20191005_145332.jpg` | sensor ranges galaxy to tactics | V2 | 05 |
| S14 | `menus maps metagames systems/IMG_20191005_145357.jpg` | damage effects targets | V2 | 05 |
| S15 | `menus maps metagames systems/IMG_20191005_145511.jpg` | damage effects sources | V2 | 05 |
| S16 | `menus maps metagames systems/IMG_20191005_145651.jpg` | hit effects and universal entity properties | V2 | 05 |
| S17 | `menus maps metagames systems/IMG_20191005_145659.jpg` | prototype 1 todo | V2 | 05 |
| S18 | `menus maps metagames systems/IMG_20191005_145740.jpg` | enemy groups | V2 | 05 |
| S19 | `menus maps metagames systems/IMG_20191005_145816.jpg` | focus on action not story | V2 | 06 |
| S20 | `menus maps metagames systems/IMG_20191005_145843.jpg` | enemy group Robot Starships | V2 | 06 |
| S21 | `menus maps metagames systems/IMG_20191005_145911.jpg` | RS gatherers and defenders | V2 | 06 |
| S22 | `menus maps metagames systems/IMG_20191005_145928.jpg` | metagame basics | V2 | 06 |
| S23 | `menus maps metagames systems/IMG_20191005_145948.jpg` | metagame basics - show the galaxy not the progress | V2 | 06 |
| S24 | `menus maps metagames systems/IMG_20191005_150003.jpg` | NOTE warn players (2012) | V2 | 06 |
| S25 | `menus maps metagames systems/IMG_20191005_150013.jpg` | enemy role in the metagame | V2 | 06 |
| S26 | `menus maps metagames systems/IMG_20191005_150022.jpg` | metagame map style sketches | V2 | 06 |
| S27 | `menus maps metagames systems/IMG_20191005_150031.jpg` | metagame map random static destroyable | V2 | 06 |
| S28 | `menus maps metagames systems/IMG_20191005_150227.jpg` | tactics screen | V2 | 06 |
| S29 | `menus maps metagames systems/IMG_20191005_150235.jpg` | metagame beginning | V2 | 06 |
| S30 | `menus maps metagames systems/IMG_20191005_150342.jpg` | campaign start flow and death | V2 | 06 |
| S31 | `menus maps metagames systems/IMG_20191005_150354.jpg` | campaign end conditions and saving | V2 | 06 |
| S32 | `menus maps metagames systems/IMG_20191005_150406.jpg` | pause menu | V2 | 06 |
| S33 | `menus maps metagames systems/IMG_20191005_150413.jpg` | backup saves and everything explodes | V2 | 06 |
| S34 | `menus maps metagames systems/IMG_20191005_150511.jpg` | training menu flow | V2 | 06 |
| S35 | `menus maps metagames systems/IMG_20191005_150518.jpg` | quick game | V2 | 06 |
| S36 | `menus maps metagames systems/IMG_20191005_150536.jpg` | quick game setup and flow | V2 | 06 |
| S37 | `menus maps metagames systems/IMG_20191005_150542.jpg` | tutorial | V2 | 07 |
| S38 | `menus maps metagames systems/IMG_20191005_150609.jpg` | campaign screen flow | V2 | 07 |
| S39 | `menus maps metagames systems/IMG_20191005_150617.jpg` | database and scanning system | V2 | 07 |
| S40 | `menus maps metagames systems/IMG_20191005_150740.jpg` | debriefing screen | V2 | 07 |
| S41 | `menus maps metagames systems/IMG_20191005_150745.jpg` | database hierarchy and designations | V2 | 07 |
| S42 | `menus maps metagames systems/IMG_20191005_150805.jpg` | nicknames and world entries | V2 | 07 |
| S43 | `menus maps metagames systems/IMG_20191005_150813.jpg` | scanning enemies | V2 | 07 |
| S44 | `menus maps metagames systems/IMG_20191005_150825.jpg` | menu flow brainstorm | V2 | 07 |
| S45 | `menus maps metagames systems/IMG_20191005_150837.jpg` | menu flowchart | V2 | 07 |
| S46 | `menus maps metagames systems/IMG_20191005_151048.jpg` | database popup and briefing | V2 | 07 |
| S47 | `menus maps metagames systems/IMG_20191005_151055.jpg` | user profiles | V2 | 07 |
| S48 | `menus maps metagames systems/IMG_20191005_151116.jpg` | main menu concepts | V2 | 07 |
| S49 | `menus maps metagames systems/IMG_20191005_151125.jpg` | profile data and New popup | V2 | 07 |
| S50 | `menus maps metagames systems/IMG_20191005_151154.jpg` | start game screens and char edit | V2 | 07 |
| S51 | `menus maps metagames systems/IMG_20191005_151200.jpg` | options screens | V2 | 07 |
| S52 | `menus maps metagames systems/IMG_20191005_151344.jpg` | campaign requirements | V2 | 07 |
| S53 | `menus maps metagames systems/IMG_20191005_151351.jpg` | game flow logic and scenes | V2 | 07 |
| S54 | `menus maps metagames systems/IMG_20191005_152459.jpg` | SA gameplay camera and scale | V2 | 07 |
