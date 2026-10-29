# Standalone: interface, menus and the 2013 Unity demo

The program's screens, how they connect, and the click-through Unity demo that Reactorcore built to show the flow. Sources: S1–S6, S28, S32, S34, S36, S38, S40, S44–S53; the AoY intro spec and construction todo; the 18 demo screens and the loose demo images.

## The 2013 Unity demo

A semi-interactive slideshow built in an old Unity with its basic GUI (May 2013). Each screen has a **"Next scene"** button on the left that names the next screen; no gameplay. The table follows that chain, which is also the numbering of the renamed files in `6 Unity demo (2013-05)\1 demo screens\` (the original crops were numbered differently: the tactics screen, crop 15, actually comes right after the star system map, matching the screen order on S6). It follows the demo plan on S5 ("step by step experience of the game ... using menus and buttons, but no actual function behind them yet ... uploaded as a webplayer for ease of access"). All screens share a dark slate-blue background, dark panels, and a vertical STANDALONE logo on the right edge (white letters, the A drawn as a red chevron). Most screens carry "Hint: Use right-click for tool tips over buttons." at the bottom left.

| # | Screen | What it shows |
|---|---|---|
| 1 | Important notice | Warning triangle. "This game features permadeath in the campaign mode. If you die, your character will be erased." / "The campaign mode is virtually infinite, which is broken down into individual, long, finite sessions." / "The focus of this game is action, so don't expect a scripted storyline to follow." / "The game uses an automatic save system with three back up layers to keep your progress safe." / "Have fun!" Continue; "Do not show this message in the future" checkbox. |
| 2 | Intro slideshow | "Press ESC to skip the intro." A black-and-white image: the mothership seen from behind, engines blazing, against a spiral galaxy, with the STANDALONE logo. |
| 3 | Select profile | Player profiles list (xXxL33tSnipaxXx, Spaceman5, New Player, UserX), Add, Delete, Enter, Exit Game. |
| 4 | Main menu | Start Game, Profiles, Options; "New player? Click Here" top left; "Profile: UserX / Access Database" top right; Quit Game. |
| 5 | Options | Tabs Video, Audio, Controls, Misc; "Category specific buttons, sliders and toggles." |
| 6 | Select game mode | Skirmish (a planet icon), Campaign (a galaxy), Tutorial (the mothership), each on a green-gridded thumbnail. |
| 7 | Tutorial | Story (View Intro); Training Scenarios (Movement, Sensors, Weapons, Systems, Tactics); What's next (Skirmish, Campaign). |
| 8 | Campaign mode | Current campaign status (duration, mothership condition 3305/10000, 56 enemy units remaining, star system 2/3 bodies, 2/2 solars, 5/5 fields, enemy hostile, resources 6000/10000); a "Galaxy Map" panel; Continue Campaign; Character Editor. |
| 9 | Edit character | Core Name, Ship Name, Mech Name fields; Core, Ship and Mech colour pickers; a character preview of the mothership (top and side views) and the ReWaR; Done. |
| 10 | Campaign: local star system | "System: Omicron Alpha 5" map with nebula zones, planets, suns, asteroid fields, red enemy groups and the green "You"; panels General Status Info / Warnings, Mothership Sensors, Mothership Weapons, Mothership FTL Drive, Selection Info, Objects/Groups List; "Your Turn – Action Points Left: 5", End Turn; Status; "Need help? Click Here". |
| 11 | Sensors – Tactics | Sector A4: an environment status panel (condition, occupied, surface, biome Mossy Moon, fog, features, weather, warnings of a meteor storm and incoming reinforcements); a top-down map with WARNING and INCOMING markers; Standalone status (mothership 89500/100000, ReWaR 2400/5000, resources 800/10000 RU, time elapsed, mothership ammo "MSSL 43, RAILG 220, MAING 40% charge", ReWaR ammo "FSB 2/6, EMIIM 37/90, CAP 1/1"); Ship Orders: Avoid Enemy; Mech Orders: Attack; Selection Status. |
| 12 | Pause menu | Resume, Database, Options, Exit to Main Menu, Quit to Desktop. |
| 13 | Skirmish battle | Three columns, each with Randomize and Hide/Show: Player (starting health %, starting resources, Mothership ON, Mech OFF), Enemy (list of enemy groups and enemies, Add/Remove), World (world type Planet, terrain Solid, sky colour picker, terrain surface list, scenery objects). Start Skirmish. "NOTE: Campaign is unaffected by skirmish play. Characters are not deleted upon death." |
| 14 | Mission briefing | Select Entry Position (a map with Enemy Groups 1–3 and an entry point); Select Entry Angle (the mothership's silhouette inside rotation arrows); re-entry parameters (position, angle, velocity 220 m/s, gravity 1.5 G, enemy count 230 objects, weather stormy); mission text; Launch. |
| 15 | Action | The mothership from behind, twin engines lit, flying toward a huge enemy fleet silhouetted against a blazing sun. |
| 16 | Mission debriefing | "Victory!/Defeat!"; Summary, Details and Statistics, Combatant Status Listing; Retry, Next. |
| 17 | Database | Tabs Player, Enemies, Environment, Statistics; list of objects and description panel. |
| 18 | Quit confirm | "Are you sure you want to quit the game? (This dialog is also displayed if alt+f4 is pressed.)" Yes/No. "Shutdown Demo". |

The ammo abbreviations on the tactics screen are not explained anywhere. *(Interpretation)*: MSSL = missiles, RAILG = railguns, MAING = main gun (charge-based), FSB = fusion bombs, EMIIM = EM/IM missiles (cf. "EM|IM" on A18), CAP = probably a capacitor-style special charge (cf. the Buster/overcharge ideas).

### Other demo material (2013-05)

- **ReWaR prototype renders** (e0–e10, MechFront): a blocky grey-white humanoid with round red sensor ports, a big hexagonal shield with a glowing cyan rim on the left arm, a long arm-mounted rifle on the right; shown on a red-brown planet surface. A rifle model in close-up (e8–e10). "ReWaR Prototype" composite (`misc/21.jpg`, re-exported 2023).
- **Mothership renders** (r1–r5): a long, flat, boxy grey carrier with a white launch deck along the top, a red-and-white bow, hazard stripes, swept fins with red tips, and twin rear engines; r5 looks down its catapult deck with the STANDALONE logo painted on it and the ReWaR standing at the end.
- **Asset lineups** (m1–m7): mothership, ReWaR, enemy ships (green-and-black, several sizes), a large black enemy carrier, a triple-barrel turret, a hexagonal pod, rock pillars and a mushroom tree, on test grounds. Work3: the texture sheet (mothership, ReWaR, shield, weapons, enemies, terrain).
- **Action mockup** (e11): a low run over red ground toward black enemy craft, cyan beams crossing, sunset sky.
- **World construction** diagrams (planetary layer stack, space layer sphere, skybox layout): see [world-and-combat.md](world-and-combat.md).
- **Screen art**: briefing map, galaxy map, star system map, tactics map, intro image, title logo.

### Earlier and later mockups

- **2011-05 Planetary Level / Space Level** (V1): a square play area drawn on a hazy ground or in starfield space, with arrows pointing outward past its edges (you can leave; no walls).
- **2011-10 Mothership sketch**: line art on magenta: side, top, front and rear views of a long gun-like carrier with a big multi-barrel nose cannon, an internal compartment labelled "STOMACH", fins and pods.
- **2013-12 Skirmish Mode setup screen**: a cleaner layout of World / Opponents / Player panels, each with four icons (show/hide "Surprise! :D", randomize, lock from Randomize All, clear), misc settings and a big BEGIN; see [campaign-and-modes.md](campaign-and-modes.md).

## Screen flow (S6, S45, S53, construction todo)

The full program flowchart (S45):

- Start → **pre-intro warning** → **intro slides** (both can be disabled) → **Profiles / start screen** ↔ **Main Menu**. Exit from either; Alt+F4 anywhere asks for confirmation.
- Main Menu ↔ **Start Game** (tabs Campaign / Quick / Training) and ↔ **Options** (tabs Video, Audio, Game, Misc, Controls). **Player char edit/create** as a popup. **The Database** reached through the profile link.
- **Campaign** ↔ Galaxy ↔ Local Space (metagame) ↔ Briefing. Quick and Training go straight to Briefing.
- Briefing → **Action** ↔ **Map/Tactics**, Action ↔ **Pause Menu** (↔ Tactics, ↔ Database) → **Debriefing** → back to Local Space (campaign) or Briefing (quick and training, "retry").
- Campaign → Continue, or New (erase existing progress and stats). A character can also be reset to change its name.

Unity scene setup (construction todo, S53): **Start** (pre-intro, intro); **Main Menu** (profile select, main menu, about); **Game Prep** (campaign brief/debrief, galaxy/local space); **Action** (action, tactics, pause); and "standalone components" usable in any scene (options, database, brief/debrief for quick/training, character edit, Alt+F4 confirm). Four scenes total.

## Screens in detail

**Menu requirements** (S44): fast and clear, organised, easy to learn, never forces the tutorial or intro. Right-click anything for context help. "Important: Consistent and streamlined." Start/profile screen modelled on Soldat's.

**Main menu concepts** (S48): buttons scaled by importance (Campaign 1.3, Quick 1.1, Options 1.0, Exit); a profile tab linking to the Database; tabs coloured red (Campaign), yellow (Quick), green (Training). A "New?" helper button pulses yellow when there are no profiles or characters.

**"New?" popup** (S49): 1. create a profile (mandatory), 2. create a character, 3. play training, 4. customise options, 5. play quick or campaign. Its links don't jump; they run a **guided autopilot** that shows the way.

**Character edit** (S1, S50, demo): name (permanent once created, greyed when editing), nicknames for mothership and ReWaR, colour pickers for **core/energy colour** (the AI's colour, also used for shields, propulsion and weapon effects), ship and mech, a Random button, a preview of both units. The AI is shown as a **HAL 9000-style avatar** (a lens in a panel). Options considered: separate colours per unit.

**Options** (S51): tabs Gameplay (maybe unnecessary), Video, Audio, Controls, Misc. Saved automatically on leaving, with a brief note telling the player so. Controls: action/key table with Default.

**Briefing** (S46): mission objectives; location and environment (hazards, resources, environment type); enemy amount and types (the number is always known, types may be unknown, e.g. in clouds); player status (condition, resources); threat level; points of interest; a picture of the location. Units listed hierarchically with icons and condition if known.

**Debriefing** (S40): player status (condition, resources, images of MS and ReWaR, database entries uncovered), enemy status (destroyed, escaped, damaged), statistics (time, targets destroyed, identified), world status (was the area destroyed?), a victory message and an X-COM-style **compliment image** of your unit in a badass pose. **No score**: "Score numbers are bad." Retry only in quick and training.

**Tactics screen** (S6, S28; demo 15): the overall battle situation. Does **not** pause the game (maybe slows it). Contents: a rough map of the area (grid, symbols), player unit status, detected enemies with condition if known, environment and hazards, available resources and stockpiles (ammo, drones), time elapsed, the PC clock, warnings (incoming disasters), **production controls** (make ammo, make a ReWaR), objective info, and **orders** to the mothership and ReWaR as automated tasks: move to, fire A at B, use X on Y, be aggressive/defensive, dock the ReWaR to repair/resupply, retreat, repair self, harvest here. The map is a flat 2D view of the horizontal plane with a faint cloud/debris overlay, targets as blobs with **height indicators**, significant bodies (sun corona, planet) at the edges; planet maps wrap, space maps have retreat boundaries.

**Pause menu** (S32): from Action or Tactics; Resume, Options, Database, Retry (quick and training only), Quit to Main Menu, Quit Program (both save). Shows the profile and the PC clock.

**Tutorial refresher** (S3): a toggleable overlay (doesn't pause) listing key bindings by category, basic hints, what each UI element is, and how to open the manual in the Database.

**HUD and camera** (S54, AoY Player list, A18): third-person view that moves with the player and pulls back with speed; optional first-person view during mech startup/shutdown; vapour trails in atmosphere. The 2011 design aims with a rectangular lock-on reticle in third person (nearest-centre priority, the arm aims itself) and switches to first person with a pinpoint crosshair for manual aim. The V2 look for the interface is "a green, jet fighter display in a serious mindset" (design doc v3), with targeting brackets as name labels (S50). UI theme colour noted as HSV 220/100/60 (S6, *interpretation*).
