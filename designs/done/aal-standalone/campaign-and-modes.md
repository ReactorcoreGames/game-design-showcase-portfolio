# Standalone: campaign, persistence and game modes

The game around the battles: the campaign metagame, the persistent character and permadeath, saving, the three modes, and the Database. Mostly V2 (the 2012 notebook and the 2013 demo); V3 changes are marked. Sources: S2, S4, S17–S19, S22–S25, S27, S29–S31, S33–S43, S47, S49, S52; the AoY intro spec and master plan; the demo screens; `Standalone.txt`.

## The point of it all (S18–S19, S22–S25, intro spec)

- "The game focuses on the finesse and adrenalin of combat with some slight survival and tactics." "The ultimate purpose of the game is entertainment, stress relief and adrenaline. Not the story."
- **No mystery story.** The premise is told plainly up front; there is "no storyline or narrative or anything mysterious that the player would explore (besides the content)". The intro is a short slideshow of silhouettes that hint at the content without revealing it.
- **Infinite, but never shown as a count.** You are on an almost endless quest to make the galaxy safe for mankind, one star system at a time. But the game must never show higher progress than a single campaign: no galaxy map of cleared systems, no total. "A minor mention about it can make certain players see it as a challenge" and chase it instead of playing. So: **"show the galaxy, but not the progress."** Rewards are subtle; this governs which menus, win/lose screens and statistics exist.
- **Warn the player up front** (S24, 2012): explain the infinite nature and the mindset to play it in, because the game industry "may have embedded certain habits into users through their (bad) game design". This became the demo's opening notice.
- **No music**: only sounds and ambient soundtracks; the player is encouraged to play their own music or radio (intro spec). V3 builds on this: the pitch wants a Beat Saber / Audiosurf flow state to your own music.

## The campaign (V2: S25, S27, S29–S31, S33, S38, S45, S52; demo)

**One campaign = one generated local space**: a star system, planetary system or starless space. The galaxy screen above it shows a picture of the galaxy and "Next Campaign", but no location and no cleared areas.

**Generation variables** (S29): size of area and number of celestial objects (at least one); number of stars (0 to 9); whether the whole area sits inside a cloud or field; enemy amount and number of groups (dispersal); enemy progress (already occupied, in progress, or yet to arrive); chance of events and disasters. "Some might be relatively easy, while others far more serious."

**The metagame map** (S25–S27): a flat rectangle or square (perhaps a circle or ellipse) with random celestial bodies: planets, nebulae, stars, fields and other regular and irregular bodies. Reference styles sketched: Advance Wars, Freelancer (flat and spherical), Star Wars Battlefront II's galactic conquest, Star Fox 64's route map, Space Pirates and Zombies. The map is **static for the whole campaign** (nothing moves) but **destructible**: every body has structural integrity that only disasters and superweapons affect, up to the whole system going supernova. New objects can appear (minefields, artificial fields and clouds, excessive debris). The player has no such weapons; their goal is to remove threats and minimise damage, i.e. to protect and preserve.

**Flow** (S30, S38, S52):

1. Campaign status screen (warning about permadeath and the persistent world, campaign status, Continue, a well-isolated **Master Reset** that wipes campaign progress and stats).
2. Galaxy screen ↔ the **metagame screen (local space)**. Autosave between them.
3. On a new campaign you see the generated map and a short briefing (area, foes, what's going on, warnings), which you can recall any time. You choose where to **enter the zone at any edge** of the map.
4. The campaign runs in **semi-realtime, like Star Fox 2**: you and the enemies act on the map; the enemy pursues its own plans.
5. Moving onto a target leads to Briefing → Action → Debriefing (even on failure or death) → back to the metagame. Autosave on entering a briefing.

**The 2013 demo's version** is closer to turn-based: the local star system map ("System: Omicron Alpha 5") has panels for General Status Info / Warnings, Mothership Sensors, Mothership Weapons, Mothership FTL Drive, Selection Info and an Objects/Groups List, and "Your Turn: Action Points Left: 5" with an End Turn button. The map shows coloured nebula zones, planets, suns, asteroid fields, a cluster of red **Enemy Groups** and the green "You". The campaign status screen reads: Duration 00:20:30; Mothership Condition 3305/10000 (30%); Enemies Remaining 56 units; Star System Status 2/3 Bodies, 2/2 Solars, 5/5 Fields; Enemy Hostile: Yes; Current Resources 6000/10000.

**Entering a battle** (S2, demo): the briefing shows the map; you pick an **entry point**. In space you enter from the edge, facing the centre, at height 0, already moving. On a planet you pick any point on the surface plus an **entry angle and rotation**, and spawn moving downward (re-entry). The demo's mission briefing has "Select Entry Position" and "Select Entry Angle" panels and a Re-entry Parameters readout (position 43x 122y, angle 0°, velocity 220 m/s, gravity 1.5 G, enemy count 230 objects, weather stormy). Entering action: fade in, a 2–3 second countdown, then control. Travel from battle to battle via the metagame is automatic (autopilot).

**ReWaR-only battles** (S4): a checkbox lets you leave the mothership out. Without it: no repairs, respawns or rearming for the ReWaR, no resource gathering, no fire support or superweapons, no direct mothership control.

**End of a campaign** (S31, S33): it continues until all threats are removed (or have retreated), or the entire place "explodes", or (joke) the user uninstalls the game. "Everything explodes" means local space becomes lethal (a supernova, a matter-disintegrating cloud), not merely that every body is gone; if only the bodies are gone, the fight carries on in empty space. Good or bad, you get a short debriefing and statistics, and the only option is a new campaign.

### V1: authored campaign

A hand-made linear campaign of missions with objectives, unlocked one at a time, with a story against The Army; mission times as a replay target; each mission unlocks its enemies and environments for the challenge mode.

### V3: the star system campaign

A generated, tile-based star system map with clearly defined zones (Freelancer star map feel). Enemies move, spread and try to corrupt locations; you race to intercept. When the system is clear it is safe for future colonisation and for building more Standalone units. A system that becomes too corrupt must be destroyed by **detonating its sun**, a permanent mark of shame in the logs.

## Persistence and death

**V2** (S30–S31, S33, S47, S49; demo notice):

- One **player character** per profile at a time: a core (the AI), a ship and a mech, each with a name and colour.
- **Dying means the mothership is destroyed.** The character is erased for good ("precious and relatively easy to fuck up"). The campaign keeps going: no progress is lost, the enemy gets plenty of bonus time, and the next character arrives on the scene.
- **No save/load.** "The lack of an active save-system prevents the player from going back in time and undoing mistakes, which forces players to learn to move on and live with their consequences." Everything autosaves, so you can quit any time.
- **Two hidden backup saves** for emergencies only (one between battles on the metagame, one between campaigns), forceable only through a third-party config described in the technical manual's troubleshooting section. The demo notice: "an automatic save system with three back up layers".
- **Unique IDs** (S4): instead of forbidding a reused name, each new SA unit gets a unique identifier.
- The universe and the character both generate persistent statistics.

**V3**: you name the mecha before the game and are locked to it. A lost unit and its names go onto a **permanent list of casualties**, and that name can never be used again. The universe is persistent and never reset; your victories and failures form a history worth reading back.

**V1**: no persistence; losing the mothership is a mission failure.

## Game modes

**Campaign**: the persistent mode above, with permadeath.

**Quick Game / Skirmish** (S35–S36, demo, 2013 mockup): "another, non-persistent and non-serious gamemode", in-fiction a VR simulation or a spinoff fight not taken seriously. Generate a random scenario or build one (saveable prefabs or not). No statistics, and dying does not erase your character ("Campaign is unaffected by skirmish play"). Setup:

- **World**: location and environmental parameters with unlimited variation, disasters too. Demo panel: world type (planet), terrain type (solid), sky colour, terrain surface, scenery objects. 2013 mockup: area size, hazards and density (asteroids, nebula), outposts and sensor arrays, a preview with "Generate Again".
- **Enemies / Opponents**: add groups to a list, then entities under each group (specific, random or unknown); tweak conditions in an advanced menu. Mockup: "How do they behave? Aggressive? Defensive? What is their goal?"
- **Player**: condition, resources, MS and/or ReWaR (demo: starting health %, starting resources, Mothership ON/OFF, Mech ON/OFF). Mockup: "What is the objective? What are the winning and losing conditions?"
- Per category: **randomize**, **lock** from Randomize All, **hide** (for a surprise), **clear**, and an **OLD/NEW flag** marking categories changed recently (useful when randomising hidden ones). Misc settings: Randomize All, disable mods, developer menu (cheats/modding aid), balance teams, clear all, save/load. Then Begin.
- Debriefing offers Retry (quick and training only).

**Training** (S34, S37, S44, S53): renamed from "Tutorial". A series of lessons and challenges in a VR simulation:

1. Slideshow: what you are and your mission; your unit's composition and capabilities; introduce the always-available **user manual** (it pauses time); repeat the opening warning.
2. Action with guidance, no danger and no rush: movement, aiming, shooting, basic commands (challenges 2.1, 2.2, 2.3…).
3. Slideshow: the game modes; remind of the warning and the manual.

Impatient players can skip straight to a predefined quick game ("let the player figure it out"), which doubles as a refresher; the manual opens first. The menus never force the tutorial or intro. The demo's Tutorial screen has Story (View Intro), Training Scenarios (Movement, Sensors, Weapons, Systems, Tactics) and What's Next (Skirmish, Campaign). Training provides a "trainer player char".

**V1** had Campaign and a Challenge mode (the VR simulation), with challenge content unlocked through the campaign; also co-op (2–8 players with their own robots sharing a mothership) and versus. **V3** mentions co-op with two Standalone units. The V2 "Double AI" idea (R1) puts two players in one SA, swapping places by mutual agreement.

## The Database and scanning (S17, S39, S41–S43, S46; demo)

- A static encyclopedia ("Ufopedia of sorts") of the game's content, part of the user manual. Opening it pauses the game. Tabs: **Player, Enemies, World, Statistics**.
- **Player** is fully revealed from the start (overall, mothership, robot, details). **Enemies** (faction → entity → equipment) and **World** (world types) start empty.
- **Scanning**: keep the larger missile box-crosshair on a target. Each enemy has a **scan integrity** that sets how long it takes. One target at a time; starting a new scan cancels the old one. Scans are **cumulative**, so short bursts work, but the data is lost if the target dies before the scan completes. A known type carrying different equipment can be scanned again for that equipment, faster.
- A successful scan adds the entity and each of its modules as entries. Scanning enough of a faction reveals the faction's overall description. Entries give backstory and useful information; purely optional depth.
- **Designations**: a first-seen enemy is "unknown". Destroying it gives an incomplete entry (image + designation code). The code format is **RS-1**: faction code + nth type encountered. You can rename it at any time, and add a **nickname** shown as a subtitle (e.g. "RS-5 / Bogey"). Saved in the overall save file.
- Worlds get an incomplete entry when you pass near them and a full one when you enter.
- Statistics: per character and overall.

## Profiles (S47, S49)

Because a character is so fragile, and a computer may be shared ("friend comes over"), there are **user profiles**. A profile holds: one player character (name not modifiable), its own campaign world, database progress (entries, stats, log), control bindings, one automatic save plus two emergency saves, the profile name, and an optional password with a recovery email. One person can keep several profiles; several people can share a machine without interfering.
