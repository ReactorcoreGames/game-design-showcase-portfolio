# Project Manifest

The definitive list of showcase projects: which design files feed which page, what each page and its images are called, and where each project stands. A design file is not the same thing as a project. One file can hold several games, and several files can feed one game. This table is where that gets decided.

**Slug** is the page file name (`site/projects/<slug>.html`) and the image prefix (`site/projects/images/<slug>_1_title.jpg` …). Slugs for new projects are lowercase kebab-case. Published pages keep their old file names and image prefixes, even untidy ones, because their URLs have already been shared.

**Status values:** `standby` (no page yet) · `released` (a shipped game; its page links to it) · `page` (page written, images pending) · `published` (page and images live) · `revisit` (published by the old Sonnet 3 workflow, due for an Opus rewrite) · `revisited` (rewrite done).

## Published pages (37)

All 37 are `revisit`. Images are kept as they are unless a rewrite changes what a picture needs to show.

| Page file | Image prefix | Title | Source design(s) in `designs/done/` | Notes |
|---|---|---|---|---|
| `AAL-Stealth-Sector.html` | `stealth_sector` | AAL Stealth Sector: Covert Battleship Wars | `Battleships clone on steroids.txt` | |
| `AAL-Bunkerships.html` | `aalsw` | AAL Bunkerships: Tacticool Physics Squads | `AALSW CC summary of final design.md`, plus the wider Bunkerships docs outside the repo (`C:\08 Projects\Project_Bunkerships`) | **Pilot rewrite, `revisited`.** Image 3 regenerated on Nano Banana; ten SDXL mini images in `site/projects/mini/aalsw/`. Renamed from `AALSW.html` ("Tactical Arsenal Command" was a Sonnet-era misname); `AALSW.html` is now a redirect stub, keep it. The image prefix stays `aalsw`. |
| `AALSuperweapon.html` | `AALSuperweapon` | AAL Superweapon: Physics Combat Devastation | `AAL Superweapon.txt` | |
| `ChainReactionDemolitionPunch.html` | `chainreaction` | Chain Reaction Demolition Punch | `falling-sand-pack/Chain Reaction Demolition Punch.md` | |
| `City Buster.html` | `citybuster` | Orbital City Buster: Sand Breaker Ball | `City Buster game.md` | |
| `Collidotron.html` | `collidotron` | Collidotron: Cascade Physics Processor | `Collidotron game.md` | |
| `Custom Dismount.html` | `cathartic` | Cathartic Dismount: Ragdoll Destruction Game | `Custom Dismount with Toribash Ragdoll Finisher Game.txt` | No story image yet |
| `EradicationWars.html` | `EradicationWars` | AAL Eradication Wars: Apocalyptic Mecha Warfare | `AAL Eradication Wars game.md` | Thumbnail is `EradicationWars 2_vignette_thumb.jpg` (space, not underscore) |
| `Halberd_Suit_Wars.html` | `stellarconflict` | Halberd Suit Wars: Ragdoll Mecha Combat | `floppy-variants/floppy mecha gundam uc extra design info.txt` + `Floppy Heroes Clone Remix.txt` | |
| `HazardMissionTeam (2).html` | `hazardteam` | Hazard Mission Team: Settlement Crisis Response | `Hazard Mission Team.txt` | |
| `Justice Will Glass Them.html` | `justice` | Justice Will Glass Them: Orbital Vengeance Obliteration | `falling-sand-pack/Justice Will Glass Them.md` | |
| `Mafia_Takedown.html` | `mafiatakedown` | Mafia Takedown: Dismemberment Ragdoll Vigilante | `Floppy Heroes Clone Remix.txt` (variant 2) | |
| `Megalodon.html` | `megalodon` | Megalodon Firefighter: Tactical Crisis Response | `falling-sand-pack/Fire Extinguisher Megalodon.md` | |
| `Mosh_Pit_Mayhem.html` | `moshpit` | Mosh Pit Mayhem: Heavy Metal Brawler | `floppy-variants/Variant 5 moshpit *.txt` (2 files) | No story image yet |
| `MutantLoveQuest.html` | `mutantlove` | Mutant Love Quest: Morphing Ragdoll Romance | `floppy-variants/Variant 6 mutant love design info.txt` | No story image yet |
| `Planetary Ring Miner.html` | `ringminer` | Planetary Ring Miner: Breakout X Falling Sand | `Falling Sand Asteroid Miner game.md` | |
| `Poo Storm Janitor Powersuit.html` | `poostorm` | Poo Storm Janitor Powersuit | `falling-sand-pack/Poo Storm Janitor Powersuit.md` | |
| `RussiBiomonster.html` | `russibio` | Russki Biomonster Neighbourhood: Apartment Ragdoll Rumble | `floppy-variants/Variant 7 flesh monster in russia design info.txt` | No story image yet |
| `Skullhead.html` | `skullhead` | Skullhead: Death Journal Vengeance | `floppy-variants/floppy variant 3 skullhead extra design info.txt` | |
| `StardustAssault.html` | `stardust` | Stardust Assault: Twin-Stick Mecha Shooter | `falling-sand-pack/R-Type, Missile Command and Space Invaders.md` | |
| `Underground Brawl.html` | `underground` | Underground Brawl: Ragdoll Combat | `Floppy Heroes Clone Remix.txt` (a variant) | |
| `Zero Space Robo Derby.html` | `zerobotderby` | Zero Space Robo Derby: Cellular Automata Celebrations | `falling-sand-pack/Zero Space Robo Derby.md` | |
| `abyssal_caretaker.html` | `abyssal` | Abyssal Caretaker: Environmental Survival Action | none | Designed in chat; **the page itself is the design doc**. Revise it in place, don't rebuild it from scratch. |
| `admiralwars.html` | `admiralwars` | Admiral Wars Beyond: Strategic Warfare Evolution | `2 extra context Admiral Wars Beyond.txt` | |
| `antigrav_deconstruction.html` | `antigrav` | Antigrav Deconstruction: Therapeutic Brick Breaker | `falling-sand-pack/Station Deconstruction Brick Breaker.md` | |
| `astro_industry.html` | `astro_industry` | Astro Industry Freelancer | `Astro Industry Freelancer.txt` | |
| `bunkership.html` | `bunkership` | Bunkership Exhaust Port Breaker: Tactical Demolition Action | `Bunkership Exhaust Port Breaker game.md` | |
| `colossal_devastators.html` | `colossal` | Colossal Devastators: Rampage Fighting Combat | `Fighting game but it's Kaiju rampage.md` | |
| `cyberdungeon.html` | `cyberdungeon` | Cyberdungeon Rider: Megacorp Agent Motocross | `Elasto Rider Game Idea.txt` | |
| `greensteelcommander.html` | `greensteelcommander` | Green Steel Commander: Turn-Based RTS Hybrid | `1 main AWB but as a TB-RTS hybrid.md` | |
| `kickblade.html` | `kickblade` | Kick Blade: Vigilante Action Game | `Elevator Train Kick Blade micro game.md` + `kickblade wip character fashion style.txt` | |
| `spacelancer.html` | `spacelancer` | Spacelancer: Open World Explorer | `Freelancer X Start sector space wanzer combat.md` | |
| `starforge-legion.html` | `starforge` | Starforge Legion: Mecha Space Combat | `jet fighter 3d game idea AI made.md` (V1 or V2) | No story image yet. The doc holds two games; which page is V1 and which is V2 is unconfirmed. |
| `thunderstrike-justice.html` | `thunderstrike` | Thunderstrike Justice: Fighter Jet Mech Combat | `jet fighter 3d game idea AI made.md` (V1 or V2) | See above |
| `tile-mechs.html` | `tilemechs` | AAL: Tile Mechs – Tactical Grid Combat | `Grid-based realtime mech cave of cards style game.md` | |
| `unhinged_lander_heist_scifi.html` | `unhinged_heist` | Unhinged Lander Heist: Anomalous Materials Hooligan | `falling-sand-pack/Unhinged Anomalous Materials Heist.md` | |
| `vectorthunder.html` | `vectorthunder` | Vector Thunder: Transformable Pursuit Combat | `KITT Hawk Thunder game premise.txt` | |

`falling-sand-pack/!MST Falling Sand themed game projects build via AI.txt` is the original mega-doc the falling-sand pages were split out of. It's useful shared context for all of them.

## New pages

| Page file | Image prefix | Title | Source design(s) in `designs/done/` | Notes |
|---|---|---|---|---|
| `graviton-mayhem.html` | `graviton-mayhem` | Graviton Singularity Mecha: Physics Missile Mayhem | `Momentum Missile Mayhem 2 Redux.md` | **Pilot 2, status `page`** (on `dev` until reviewed). Klein images plus ten SDXL minis in `site/projects/mini/graviton-mayhem/`. AAL in spirit only, so no prefix. The enemy is "the Masterless Legion" (the doc's "Death Force" is M.D. Geist's name). |

## Released game: needs a page, no image generation

| Slug | Title | Sources | Notes |
|---|---|---|---|
| `turbo-minesweeper` | Ukrainian Turbo Minesweeper | The game's own repo `C:\14 Repos\Ukrainian Turbo Minesweeper` (`readme.md`, `guide.md`, `CLAUDE.md`, `promo.md`). `designs/done/Minesender Maximum.txt` is the original, now obsolete, spec. | Already released: https://reactorcore.itch.io/ukrainian-turbo-minesweeper. The page presents its design like any other showcase page, adds a prominent "Play it" link, and calls itself a released game, not a concept. Images come from that repo's `promo/` folder (cover, gameplay shots, cutscenes, trophy room): copy and crop them to the five slots, no BAIG. That repo is outside this one, so read its files from a local session. |

## Standby projects

Proposed slugs. They are open to change until the page is built, then frozen. Files are in `designs/standby/`.

**Naming rule.** Where the design doc names a project, use that name. A project gets the `AAL` prefix only if its design already has one; many games are set in the AAL universe in spirit only (side stories) and go without it. AAL Bunkerships was the one exception. Where it doesn't, the planning step proposes a title that fits the game's mood, and an AAL one if the game belongs in that universe. Projects built on someone else's IP or trademark (BLAME!, UNO, LEGO) credit their inspiration on the page, but the title and every in-game name are original stand-ins.

| # | Proposed slug | Working title | Source file(s) | Notes |
|---|---|---|---|---|
| 2 | `wobble-royale` | (ragdoll battle royale, singleplayer) | `PUBG battle royale better singleplayer.md` | Title TBD |
| 3 | `planet-warfare` | Planet Warfare | `Planet Warfare.txt` | Biggest doc (50 KB). `designs/done/ALREADY DONE Pixel Sprites ala ReactorCore.txt` is its art-system companion. |
| 4 | `roomspace` | RoomSpace | `RoomSpace.txt` | |
| 5 | `shape-smasher` | Shape Smasher | `Shape Smasher.txt` | |
| 6 | `net-terminal` | "Do you have the Net Terminal Gene?" | `Small BLAME game with marching squares dest terrain.md` | Strongly inspired by BLAME!, but set in its own universe. The page credits the inspiration, and the protagonist, weapon (the doc's "GBE") and catchphrase all get original names. |
| 7 | `smash-droids` | AAL Smash Droids: Vibranium Knockout Arena | `Smash Bros Arena with Jager Guns.md` | |
| 8 | `smash-room` | (closed-room stress-relief smasher) | `rosebud gdev smash bros idea.md` | Separate game from #7. Title TBD. |
| 9 | `soldat-doom` | Soldat Doom Infinite | `Soldat Doom Infinite FPS.txt` | Small doc (3 KB), so the bible will have to do the heavy lifting |
| 10 | `space-chunks` | (Space Chunks 2–inspired arcade blast-em-up) | `Space Chunks 2 inspired Arcade BlastEmUp Game.txt` | Title TBD |
| 11 | `aal-standalone` | AAL Standalone | `Standalone.txt` | The Terrene games are set after this one |
| 12 | `metroid-forever` | (Super Metroid Forever) | `Super Metroid Forever concept.txt` | Needs an original title |
| 13 | `aal-collector` | AAL Collector: Reach, Capture/Cute, Recover | `TerreneV3 AAL Collector.txt` | Terrene V3 trio, see the note below |
| 14 | `aal-exterminator` | AAL Exterminator | `TerreneV3 AAL Exterminator.txt` + `terrene aal inspector.md` | Terrene V3 trio |
| 15 | `aal-voyager` | AAL Voyager: Robinson Survival Challenge | `TerreneV3 AAL Voyager.txt` | Terrene V3 trio |
| 16 | `aal-inspector` | AAL Inspector: Planetary Explorer | `Terrene Subnautica Halo Doom inspired AAL Inspector.txt` | Possibly a 4th game, possibly only the V2 the trio grew from. See the note below. |
| 17 | `topverse` | TopVerse | `TopVerse.txt` | |
| 18 | `trash-miner` | AAL Trash Miner: Landfill Recycling Bonanza | `Trash Miner Web Game.md` | |
| 19 | `temporal-shift` | Temporal Shift (RTS) | `Two RTS Ideas - TemporalShift - Type X Mecha.txt` (first half) | One file, two games |
| 20 | `type-x-mecha` | Type 1-X Mecha (RTS) | `Two RTS Ideas - TemporalShift - Type X Mecha.txt` (second half) | |
| 21 | `punk-orphans` | Titanium Punk Orphans | `Worms 2 Clone, Titanium Punk Orphans.txt` | |
| 22 | `metsanelaimet` | Metsanelaimet | `liero ja metsanelaimet Claude clone.md` | |
| 23 | `auto-chess` | (self-playing chess) | `random auto chess.md` | Small and tech-focused. If it's too thin for a full page, fold it into another page. |
| 24 | `bazooka-bomber` | (Bomberman with launched bombs) | `simpler Bomberman Bazooka crusader idea.md` | Title TBD |
| 25 | `party-crasher` | (simplified Party Hard, 16x16 sprites) | `simplified party hard with 16x16 sprites.md` | Close relative of #30. Decide at planning whether it is its own page or one of the games on the anthology page. |
| 26 | `telekinetic-eradicator` | Telekinetic Eradicator | `theme idea, Telekinetic Eradicator.txt` | The doc's villain list names real-world groups and nationalities. The page uses fictional stand-ins (archetypes of cruelty, not real groups). |
| 27 | TBD | (UNO-inspired card game family) | `UNO/` folder: `uno card game web app singleplayer.md` (main "SuperUNO" design), `Uno poke energy card spinoff addon.txt` (elemental spinoff), `uno bizarro idea.md` (reverse rules, "ONU"), `txt based uno card game setup.md` (text-only presentation idea) | Probably 1–3 games. Decide the split at planning. Credit UNO as the inspiration, with an original title and no UNO naming in-game. |
| 28 | TBD | Epic Toy Cool Combat (ETCC) family | `ETCC/` folder: `v1 Casual Lego Combat - Quick ruleset.txt`, the `v2 ETCC - *.txt` set (Introduction, Game Rules, Unit Designer, Weapon Designer; AI Control and Campaign Maker are empty stubs), `KMF Kinetic Minifig Fights - Proto ETCC physics driven simple.txt`, `vX Simplified Minifig Only ETCC.txt`, `Lego Combat inspirations.md` | Reactorcore counts about 3 separate games here: v1 casual quick play, v2 full ETCC with unit and weapon designers, and KMF physics-driven minifig fights. Confirm at planning. Credit the toy-brick inspiration, but no LEGO naming. |
| 29 | `vigilant-pursuit` | (vehicular pursuit racing) | `vigilant terminator pursuit.md` | Title TBD |
| 30 | `kenney-jam` | (unhinged stress-relief webgame series) | `KenneyJam Easy Game Idea.txt` | **One page presenting the whole series** of small absurd-comedy webgames meant for itch.io. Each game has a Party Hard–style metagame: a campaign of levels with a few randomized bits per playthrough and a cheeky ending cutscene. Built with Kenney asset packs. The doc's tech notes (GDevelop etc.) are obsolete; don't present them. |
| 31 | `human-apex` | Human Apex: Overreacting Justice Against Animal Kingdom | `VAGUE IDEA Overreaction hunt animals with military lol.md` | Raw but good idea |
| 32 | TBD | (Motherlode × Tasty Planet) | `VAGUE Motherlode X Tasty Planet idea doc 9x variants.md` | 9 variants. **Pick the best few**, not all nine. Propose the picks and whether they share a page at planning. |
| 33 | TBD | (pinball / Nanaca Crash / breakout mixes) | `VAGUE Pinball Game Idea.md` | Raw. The doc floats several mixes, so pick the strongest. |

**The Terrene family (#13–16).** Based on the file dates and contents: `Terrene Subnautica Halo Doom inspired AAL Inspector.txt` (2024-10-19) builds on the original Terrene and has its own "V2" section, which makes it the forerunner. The three `TerreneV3 …` remixes (Collector, Exterminator, Voyager) followed on 2024-10-28/29. `terrene aal inspector.md` (also 2024-10-29) describes the same Agent / Jet-Mech / Carrier cast as Exterminator, so it is read as Exterminator's extended notes. Reactorcore doesn't remember whether Inspector is a 4th game or only the V2 the trio grew from. Plan the trio first, then judge whether Inspector still has enough distinct identity for its own page. If it doesn't, fold its best ideas into the trio's pages.

Roughly 35–40 new pages at 5 images each is about 175–200 images, which is 3 days of the Klein allowance (70/day).

## Retired designs

These stay in `designs/done/` and get no page of their own:

- `Minesender Maximum.txt`: superseded by the released Ukrainian Turbo Minesweeper (see above)
- `ALREADY DONE Pixel Sprites ala ReactorCore.txt`: an art-asset system, not a game (companion to Planet Warfare)
