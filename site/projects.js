/*
  The nexus catalog. One entry per showcase page; index.html renders the cards from this list,
  and tools/sitemap.py reads it to rebuild sitemap.xml.

  Fields
    page      file name in site/projects/ (frozen once published)
    prefix    image prefix; the card uses projects/thumbnails/<prefix>_2_vignette_thumb.jpg
    thumb     optional, only for a thumbnail that breaks the naming rule
    title     the game's name
    subtitle  the three-word game type (the part after the colon on the page)
    icon      the project's ID badge: a game-icons name from assets/icons/ (without .png);
              copy it into the site with `python tools/brand.py icons <name>`
    tint      the badge and subtitle colour: cyan, blue, green, yellow, orange, red or magenta
    blurb     one or two sentences, shown in full on the tile
    genres    ids from GENRES below (kept for later use; the nexus doesn't filter on them)
    tags      a few free lowercase words (likewise not shown)
    universe  "aal" for games set in the AAL Universe (Alteisen Arsenal Laboratories), otherwise omit;
              aal/ lists them, the nexus doesn't
    status    "concept" or "released"
    play      released games only: where to play it
    added     YYYY-MM-DD the page went live

  The nexus always shows the list A–Z by title, so the order here doesn't matter.
*/

window.GENRES = [
  { id: "strategy", label: "Strategy" },
  { id: "action", label: "Action" },
  { id: "physics", label: "Physics & Destruction" },
  { id: "falling-sand", label: "Falling Sand" },
  { id: "ragdoll", label: "Ragdoll" },
  { id: "mecha", label: "Mecha" },
  { id: "arcade", label: "Arcade" },
  { id: "vehicles", label: "Vehicles" },
  { id: "sandbox", label: "Sandbox & Sim" },
  { id: "puzzle", label: "Puzzle" }
];

window.PROJECTS = [
  {
    page: "graviton-mayhem.html", prefix: "graviton-mayhem",
    title: "Graviton Singularity Mecha", subtitle: "Physics Missile Mayhem",
    icon: "black-hole-bolas-lorc", tint: "magenta",
    blurb: "Fling gravity orbs and let a clumsy robot tank army crash itself to pieces. Bank shots, chain-reaction pile-ups and a frontier planet that never runs out of campaigns.",
    genres: ["arcade", "physics", "mecha", "action"], tags: ["tower defense", "bank shots", "chain reactions", "procedural campaigns"],
    status: "concept", added: "2026-10-21"
  },
  {
    page: "admiralwars.html", prefix: "admiralwars",
    title: "Admiral Wars Beyond", subtitle: "Four-Layer Grid Tactics",
    icon: "captain-hat-profile-delapouite", tint: "blue",
    blurb: "Advance Wars-style turn-based tactics on up to four stacked map layers at once: orbit, air, surface and underground. Every mission is generated from a persistent universe that remembers every battle.",
    genres: ["strategy"], tags: ["turn-based", "multi-layer", "procedural campaigns", "space"],
    status: "concept", added: "2025-10-04"
  },
  {
    page: "abyssal_caretaker.html", prefix: "abyssal",
    title: "Abyssal Caretaker", subtitle: "Ocean Cleanup Ascent",
    icon: "frog-lorc", tint: "cyan",
    blurb: "A reverse Subnautica: an ancient frogman wakes in the abyss and climbs toward a port, adapting his suit to each depth from salvaged containers and cleaning up what the ships dropped.",
    genres: ["sandbox", "action"], tags: ["underwater", "survival crafting", "cleanup", "side view"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "kickblade.html", prefix: "kickblade",
    title: "Kick Blade", subtitle: "Vigilante Action Game",
    icon: "high-kick-delapouite", tint: "magenta",
    blurb: "Ultra-accessible arcade action: a cutecore heroine takes on corrupt CEOs with kicks and a utility knife. Physics-driven combat, playable with one hand.",
    genres: ["action", "physics"], tags: ["vigilante", "accessibility", "one-handed", "melee"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "AAL-Bunkerships.html", prefix: "aalsw",
    title: "AAL Bunkerships", subtitle: "Tacticool Physics Squads",
    icon: "crosshair-delapouite", tint: "red",
    blurb: "Clumsy physics squads and mobile fortresses, commanded across a turn-based galaxy map. Every system on a ship is a module you can shoot, and nothing you build is ever thrown away.",
    genres: ["strategy", "action", "physics"], tags: ["squad tactics", "bunkerships", "destructible terrain", "infinite campaign"],
    universe: "aal", status: "concept", added: "2025-10-04"
  },
  {
    page: "antigrav_deconstruction.html", prefix: "antigrav",
    title: "Antigrav Deconstruction", subtitle: "Therapeutic Brick Breaker",
    icon: "wrecking-ball-lorc", tint: "orange",
    blurb: "A calm brick breaker with a ball you can't lose. Derelict stations crumble into falling-sand dust, liquids and gases that mix and react, and each one becomes a new generated starship.",
    genres: ["arcade", "falling-sand"], tags: ["brick breaker", "relaxing", "chemistry", "space"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "colossal_devastators.html", prefix: "colossal",
    title: "Colossal Devastators", subtitle: "Kaiju Rampage Brawler",
    icon: "battle-mech-delapouite", tint: "red",
    blurb: "Be the alien monster of the week: a 2D Rampage-meets-Smash brawler where you wreck cities and fight their prototype super robots, with a builder that balances any 20-meter titan you can dream up.",
    genres: ["action", "mecha", "physics"], tags: ["kaiju", "platform fighter", "character builder", "transforming"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "astro_industry.html", prefix: "astro_industry",
    title: "Astro Industry Freelancer", subtitle: "Interstellar Construction Jobs",
    icon: "bucket-wheel-excavator-caro-asercion", tint: "yellow",
    blurb: "A Bob the Builder simulator in space: a robot engineer takes jobs across an endless peaceful universe, driving heavy machines as simple as toys, with everything available from the start and no end game.",
    genres: ["sandbox", "vehicles"], tags: ["engineering", "automation", "procedural jobs", "space"],
    status: "concept", added: "2025-10-04"
  },
  {
    page: "cyberdungeon.html", prefix: "cyberdungeon",
    title: "Cyberdungeon Rider", subtitle: "Megacorp Agent Motocross",
    icon: "aero-bike-delapouite", tint: "magenta",
    blurb: "Elastomania-style bike physics meets corporate sabotage. A transforming android agent rides, flips and fights through procedural facilities to destroy their reactors.",
    genres: ["vehicles", "physics", "action"], tags: ["motocross", "transforming", "cyberpunk"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "Zero Space Robo Derby.html", prefix: "zerobotderby",
    title: "Zero Space Robo Derby", subtitle: "Firework Arena Shooter",
    icon: "firework-rocket-lorc", tint: "magenta",
    blurb: "A laid-back zero-gravity blaster derby flown with the mouse alone. Drift, charge your shot, hide behind splitting asteroids, and every knockout bursts into a falling-sand firework.",
    genres: ["arcade", "falling-sand", "action"], tags: ["arena", "zero gravity", "fireworks", "one-handed"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "EradicationWars.html", prefix: "EradicationWars", thumb: "EradicationWars 2_vignette_thumb.jpg",
    title: "AAL Eradication Wars", subtitle: "Apocalyptic Mecha Warfare",
    icon: "missile-mech-lorc", tint: "red",
    blurb: "A Soldat-style side-scrolling mecha shooter played solo against human-like bots: momentum movement, transforming mecha, Arms Forts on rails and a year-long war between two identical nations.",
    genres: ["mecha", "action"], tags: ["2d shooter", "transforming", "token battles", "war campaign"],
    universe: "aal", status: "concept", added: "2025-10-08"
  },
  {
    page: "Poo Storm Janitor Powersuit.html", prefix: "poostorm",
    title: "Poo Storm Janitor Powersuit", subtitle: "Office Cleanup Platformer",
    icon: "vacuum-cleaner-delapouite", tint: "green",
    blurb: "An office after a literal shitstorm, and a janitor in a sealed powersuit. Vacuum, mop and punch the falling-sand muck loose, put it all in the flower pots, and water the office back to green.",
    genres: ["falling-sand", "action", "arcade"], tags: ["cleanup", "comedy", "platformer", "relaxing"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "greensteelcommander.html", prefix: "greensteelcommander",
    title: "Green Steel Commander", subtitle: "Turn-Based RTS Hybrid",
    icon: "battle-tank-lorc", tint: "green",
    blurb: "Command & Conquer meets Advance Wars: RTS-style controls and base building with turn-based execution, set in a terraformed industrial 2060.",
    genres: ["strategy"], tags: ["rts", "turn-based", "military"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "Halberd_Suit_Wars.html", prefix: "stellarconflict",
    title: "Halberd Suit Wars", subtitle: "Ragdoll Mecha Combat",
    icon: "halberd-lorc", tint: "green",
    blurb: "Zero-gravity mecha slugfests in the spirit of early Gundam: armor per limb, limbs that don't come back, pilots scarcer than machines, and retreat as a real choice.",
    genres: ["mecha", "ragdoll", "action"], tags: ["squad tactics", "ejection", "zero gravity", "war campaign"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "City Buster.html", prefix: "citybuster",
    title: "City Buster", subtitle: "Orbital Brick Breaker",
    icon: "meteor-impact-lorc", tint: "green",
    blurb: "Breakout turned upside down: slap energy orbs from an orbiting paddle ship into a falling-sand world that shatters, burns and melts, and dodge everything it throws back.",
    genres: ["arcade", "falling-sand", "physics"], tags: ["breakout", "orbital", "demolition", "procedural campaigns"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "spacelancer.html", prefix: "spacelancer",
    title: "Spacelancer", subtitle: "Open World Explorer",
    icon: "spaceship-delapouite", tint: "cyan",
    blurb: "A freelancer career in a living universe: modular ships, shifting factions, several paths to victory, and a ship that switches between flight and shipmech modes.",
    genres: ["sandbox", "vehicles", "action"], tags: ["open world", "space", "ship customization", "factions"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "Custom Dismount.html", prefix: "cathartic",
    title: "Cathartic Dismount", subtitle: "Precognition Ragdoll Finisher",
    icon: "falling-sbed", tint: "red",
    blurb: "Rehearse a terrible person's fall down stairs, into traffic or a fan in a precognition vision, make one real, then land a single slow-motion finisher.",
    genres: ["ragdoll", "physics"], tags: ["catharsis", "precognition", "slow motion", "procedural"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "tile-mechs.html", prefix: "tilemechs",
    title: "AAL Tile Mechs", subtitle: "Tactical Grid Combat",
    icon: "empty-chessboard-delapouite", tint: "cyan",
    blurb: "Real-time combat on a grid with Type-3 Mechas: turn-based precision at real-time speed, with destructible environments and moral consequences.",
    genres: ["strategy", "mecha"], tags: ["grid tactics", "real-time", "destructible terrain"],
    universe: "aal", status: "concept", added: "2025-10-08"
  },
  {
    page: "Megalodon.html", prefix: "megalodon",
    title: "Megalodon Firefighter", subtitle: "Light-Gun Fire Rescue",
    icon: "helicopter-delapouite", tint: "blue",
    blurb: "A light-gun game where the scene is in danger, not you: aim a time-lost mecha-helicopter's water cannon at a falling-sand city fire, and shoot down the meteors still coming.",
    genres: ["falling-sand", "arcade", "vehicles"], tags: ["firefighting", "light gun", "time travel", "cellular automata"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "Skullhead.html", prefix: "skullhead",
    title: "Skullhead", subtitle: "Death Journal Vengeance",
    icon: "burning-skull-skoll", tint: "red",
    blurb: "An uncensored ragdoll revenge game in the spirit of the old violent Flash games. A man who sold his soul works through a fictional early-1990s town place by place, marking each one off in his Death Journal.",
    genres: ["action", "ragdoll"], tags: ["side-scroller", "catharsis", "dismemberment", "flash games"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "AAL-Stealth-Sector.html", prefix: "stealth_sector",
    title: "AAL Stealth Sector", subtitle: "Covert Battleship Wars",
    icon: "battleship-cathelineau", tint: "cyan",
    blurb: "Battleship as a duel of deduction: eight hidden warships a side, each firing its own salvo shape in turn, with probes, mines and smoke inside a sensor-blind nebula.",
    genres: ["strategy", "puzzle"], tags: ["battleship", "turn-based", "deduction", "electronic warfare"],
    universe: "aal", status: "concept", added: "2025-10-04"
  },
  {
    page: "StardustAssault.html", prefix: "stardust",
    title: "Stardust Assault", subtitle: "Twin-Stick Mecha Shooter",
    icon: "interceptor-ship-delapouite", tint: "cyan",
    blurb: "R-Type meets Missile Command and Space Invaders. A starmecha aims anywhere against swarms that never ramp up, every invader bursts into falling dust, and each run leaves a painting of its explosions.",
    genres: ["arcade", "falling-sand", "mecha", "action"], tags: ["twin-stick", "shmup", "particles", "artwork"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "HazardMissionTeam (2).html", prefix: "hazardteam",
    title: "Hazard Mission Team", subtitle: "Settlement Crisis Response",
    icon: "gas-mask-lorc", tint: "yellow",
    blurb: "A Clonk-style settlement game as a service: dig, build and haul through generated missions for clients, and watch the world map grow with every finished job.",
    genres: ["sandbox", "strategy", "action"], tags: ["digging", "logistics", "service", "procedural missions"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "vectorthunder.html", prefix: "vectorthunder",
    title: "Vector Thunder", subtitle: "Transformable Pursuit Combat",
    icon: "full-motorcycle-helmet-delapouite", tint: "orange",
    blurb: "80s-flavored vehicle combat with car, motorcycle and helicopter transformations, dynamic enemy waves, and Supercores that let you steal enemy abilities.",
    genres: ["vehicles", "action"], tags: ["pursuit", "80s", "transforming"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "AALSuperweapon.html", prefix: "AALSuperweapon",
    title: "AAL Superweapon", subtitle: "Physics Combat Devastation",
    icon: "ray-gun-lorc", tint: "red",
    blurb: "A real power fantasy: an overpowered agent quad-wields modular guns through a planet-wide alien lab, in a hand-made campaign whose levels, enemies and finds reshuffle every playthrough.",
    genres: ["action", "physics"], tags: ["platformer", "power fantasy", "physics shooter", "shuffled campaign"],
    universe: "aal", status: "concept", added: "2025-10-04"
  },
  {
    page: "Mosh_Pit_Mayhem.html", prefix: "moshpit",
    title: "Mosh Pit Mayhem", subtitle: "Heavy Metal Brawler",
    icon: "guitar-lorc", tint: "magenta",
    blurb: "A mouse-only human demolition derby in front of a metal stage. Momentum decides who gets hurt, limbs fly, medics sew everyone back together between songs, and the floor becomes a painting of the night.",
    genres: ["ragdoll", "action"], tags: ["brawler", "heavy metal", "momentum", "mouse only"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "bunkership.html", prefix: "bunkership",
    title: "Bunkership Exhaust Port Breaker", subtitle: "Warship Brick Breaker",
    icon: "brick-wall-delapouite", tint: "magenta",
    blurb: "A brick breaker where every wall of bricks is a generated warship of moon rock and machinery. Bounce an energy orb through the exhaust port and let the ship's own fuel tanks finish the job, clan fleet after clan fleet.",
    genres: ["arcade", "physics", "action"], tags: ["brick breaker", "procedural ships", "no lives", "space"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "MutantLoveQuest.html", prefix: "mutantlove",
    title: "Mutant Love Quest", subtitle: "Morphing Ragdoll Romance",
    icon: "tentacle-heart-lorc", tint: "magenta",
    blurb: "A goofy wasteland slapfest: knock every gatekeeper out of the arena on the way to your date, with a random body you can re-roll one part at a time mid-fight.",
    genres: ["ragdoll", "action"], tags: ["romance", "comedy", "mutation", "platform fighter"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "Planetary Ring Miner.html", prefix: "ringminer",
    title: "Planetary Ring Miner", subtitle: "Falling Sand Mining",
    icon: "ringed-planet-lorc", tint: "cyan",
    blurb: "A brick breaker with the ball taken out: blast falling-sand asteroids from below, catch what falls, and grow a star sector's network of stations and trade lanes from your hauls.",
    genres: ["arcade", "falling-sand"], tags: ["brick breaker", "mining", "space", "living map"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "starforge-legion.html", prefix: "starforge",
    title: "Starforge Legion", subtitle: "Mecha Space Combat",
    icon: "robot-helmet-delapouite", tint: "blue",
    blurb: "Elite contractor pilots fly transformable mecha through 22nd-century space, in tactical combat across very different environments.",
    genres: ["mecha", "action", "vehicles"], tags: ["space combat", "transforming", "contractors"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "Justice Will Glass Them.html", prefix: "justice",
    title: "Justice Will Glass Them", subtitle: "Orbital Bunker Buster",
    icon: "police-badge-andymeneely", tint: "magenta",
    blurb: "A space police warship burns down through a buried dictator's layered fortress with a charge beam, shooting down the missiles that come back up, in falling-sand physics.",
    genres: ["falling-sand", "arcade", "physics"], tags: ["destructible terrain", "space police", "point defense"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "Mafia_Takedown.html", prefix: "mafiatakedown",
    title: "Mafia Takedown", subtitle: "Dismemberment Ragdoll Vigilante",
    icon: "fedora-lorc", tint: "red",
    blurb: "One ordinary person takes a whole gang apart, room by room, in slow ragdoll fights with armor on every limb. When a vigilante falls, someone close to them takes up the mask.",
    genres: ["ragdoll", "action", "physics"], tags: ["vigilante", "dismemberment", "soft death", "succession"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "thunderstrike-justice.html", prefix: "thunderstrike",
    title: "Thunderstrike Justice", subtitle: "Fighter Jet Mech Combat",
    icon: "jet-fighter-delapouite", tint: "yellow",
    blurb: "A transformable fighter jet and mech hybrid strikes at corrupt regimes, switching instantly between jet and mech modes mid-mission.",
    genres: ["mecha", "vehicles", "action"], tags: ["jet fighter", "transforming", "anti-corruption"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "ChainReactionDemolitionPunch.html", prefix: "chainreaction",
    title: "Chain Reaction Demolition Punch", subtitle: "Falling Sand Demolition",
    icon: "fulguro-punch-lorc", tint: "orange",
    blurb: "A cyclops superhero punches generated buildings, and the hot shrapnel melts the stone into ash in a cascading chain reaction. One punch, then watch it go.",
    genres: ["physics", "falling-sand", "puzzle"], tags: ["demolition", "superhero", "chain reactions", "stress relief"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "Underground Brawl.html", prefix: "underground",
    title: "Underground Brawl", subtitle: "Floppy Ragdoll Fight Night",
    icon: "boxing-glove-lorc", tint: "yellow",
    blurb: "Floppy ragdoll fist fights in basements and parking lots after dark. Scrap armor on every limb, pipes and sandwiches thrown in by the crowd, and each club's night ends with its giant champion.",
    genres: ["ragdoll", "action", "physics"], tags: ["brawler", "collision combat", "armor", "gauntlet"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "Collidotron.html", prefix: "collidotron",
    title: "Collidotron", subtitle: "Cascade Physics Processor",
    icon: "crystal-cluster-lorc", tint: "blue",
    blurb: "A calm one-button chain reaction: crack one tile of a kaleidoscope slab and every tile its orb breaks releases another orb, until the whole slab is orbs.",
    genres: ["puzzle", "physics", "arcade"], tags: ["chain reaction", "relaxing", "kaleidoscope", "recycling"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "unhinged_lander_heist_scifi.html", prefix: "unhinged_heist",
    title: "Unhinged Lander Heist", subtitle: "Anomalous Materials Hooligan",
    icon: "rocket-lorc", tint: "green",
    blurb: "Two-stage chaos: a precision lander heist, then free-form cellular-automata destruction with what you stole. Stress relief at a comfortable pixel-art distance.",
    genres: ["falling-sand", "action", "vehicles"], tags: ["heist", "lander", "chaos", "stress relief"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "RussiBiomonster.html", prefix: "russibio",
    title: "Biomonster Neighbourhood", subtitle: "Apartment Ragdoll Rumble",
    icon: "spiked-tentacle-lorc", tint: "magenta",
    blurb: "Play the tentacled flesh blob a regime sends to clear stubborn tenants from their concrete block. They keep rifles in the sofa, and the cheerful propaganda bulletins show who the real monster is.",
    genres: ["ragdoll", "action", "physics"], tags: ["monster", "dark satire", "grappling", "tentacles"],
    status: "concept", added: "2025-10-08"
  }
];
