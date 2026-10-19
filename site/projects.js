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
    universe  "aal" for Armored Assault League games, otherwise omit (for the AAL section, not the nexus)
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
    page: "admiralwars.html", prefix: "admiralwars",
    title: "Admiral Wars Beyond", subtitle: "Strategic Warfare Evolution",
    icon: "chess-knight-skoll", tint: "blue",
    blurb: "Advance Wars–style tactics fought across four simultaneous battlefield layers: orbit, air, surface and underground. Every decision ripples through a persistent, procedurally generated universe.",
    genres: ["strategy"], tags: ["turn-based", "multi-layer", "procedural campaigns", "space"],
    status: "concept", added: "2025-10-04"
  },
  {
    page: "abyssal_caretaker.html", prefix: "abyssal",
    title: "Abyssal Caretaker", subtitle: "Environmental Survival Action",
    icon: "diving-helmet-delapouite", tint: "cyan",
    blurb: "A reverse Subnautica: rise from the deepest trench as an ancient ocean guardian, upgrading your suit zone by zone while you clean up pollution and restore the ecosystems above.",
    genres: ["action", "sandbox"], tags: ["underwater", "exploration", "ecology", "survival"],
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
    page: "AALSW.html", prefix: "aalsw",
    title: "Tactical Arsenal Command", subtitle: "Strategic Squad Combat",
    icon: "crosshair-delapouite", tint: "orange",
    blurb: "Directly control well-equipped operatives through fully destructible environments, with modular loadouts, real ballistics and a persistent galactic conquest metagame.",
    genres: ["strategy", "action", "physics"], tags: ["squad tactics", "loadouts", "destructible terrain"],
    universe: "aal", status: "concept", added: "2025-10-04"
  },
  {
    page: "antigrav_deconstruction.html", prefix: "antigrav",
    title: "Antigrav Deconstruction", subtitle: "Therapeutic Brick Breaker",
    icon: "cubes-lorc", tint: "green",
    blurb: "Brick breaking as meditation. Derelict space stations dissolve into cascades of colorful particles, with no timers, no fail states and no stress.",
    genres: ["arcade", "falling-sand"], tags: ["brick breaker", "relaxing", "zero gravity", "space"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "colossal_devastators.html", prefix: "colossal",
    title: "Colossal Devastators", subtitle: "Rampage Fighting Combat",
    icon: "battle-mech-delapouite", tint: "red",
    blurb: "One-on-one duels between 20-meter titans for dominion over worlds. Build your own fighter with an auto-balancing character system and switch between mech and beast forms mid-fight.",
    genres: ["action", "mecha"], tags: ["fighting game", "kaiju", "customization", "transforming"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "astro_industry.html", prefix: "astro_industry",
    title: "Astro Industry Freelancer", subtitle: "Engineering Sandbox Simulation",
    icon: "bucket-wheel-excavator-caro-asercion", tint: "yellow",
    blurb: "The industrial engineering fantasy in a peaceful universe: pilot heavy vehicles, reshape terrain, build factories and solve problems for beings across endless star systems, without pressure.",
    genres: ["sandbox", "vehicles"], tags: ["engineering", "automation", "exploration", "space"],
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
    title: "Zero Space Robo Derby", subtitle: "Cellular Automata Celebrations",
    icon: "firework-rocket-lorc", tint: "green",
    blurb: "Combat as celebration: customized robot ships duel in zero gravity, and every destroyed ship bursts into a cellular-automata fireworks show. Not about domination, about making beautiful moments together.",
    genres: ["action", "falling-sand", "vehicles"], tags: ["arena", "zero gravity", "fireworks", "cooperative"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "EradicationWars.html", prefix: "EradicationWars", thumb: "EradicationWars 2_vignette_thumb.jpg",
    title: "AAL Eradication Wars", subtitle: "Apocalyptic Mecha Warfare",
    icon: "missile-mech-lorc", tint: "red",
    blurb: "Fast, Soldat-style mecha combat with dual-form transformation. Command Type-3 Mechas through brutal token-driven warfare with real strategic depth.",
    genres: ["mecha", "action"], tags: ["transforming", "2d shooter", "apocalyptic"],
    universe: "aal", status: "concept", added: "2025-10-08"
  },
  {
    page: "Poo Storm Janitor Powersuit.html", prefix: "poostorm",
    title: "Poo Storm Janitor Powersuit", subtitle: "Cleanup Action Game",
    icon: "broom-delapouite", tint: "green",
    blurb: "A power-suited janitor tackles corporate workplace disasters with industrial equipment and falling-sand physics, turning office catastrophes into garden paradises.",
    genres: ["falling-sand", "action"], tags: ["cleanup", "comedy", "powersuit"],
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
    icon: "mecha-head-delapouite", tint: "blue",
    blurb: "Physics-driven humanoid mecha duels with limb-by-limb targeting. Lose the suit and the fight goes on: pilots eject and keep fighting as fragile humans.",
    genres: ["mecha", "ragdoll", "action"], tags: ["limb targeting", "ejection", "duels"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "City Buster.html", prefix: "citybuster",
    title: "Orbital City Buster", subtitle: "Sand Breaker Ball",
    icon: "meteor-impact-lorc", tint: "orange",
    blurb: "Breakout from orbit. Steer an experimental paddle warship and bring whole cities down with physics projectiles and falling-sand destruction.",
    genres: ["arcade", "falling-sand", "physics"], tags: ["breakout", "orbital", "demolition"],
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
    title: "Cathartic Dismount", subtitle: "Ragdoll Destruction Game",
    icon: "knocked-out-stars-delapouite", tint: "yellow",
    blurb: "Toribash-style ragdoll destruction with a moral justification system. Preview the carnage with precognition before you commit to it, for guilt-free catharsis.",
    genres: ["ragdoll", "physics"], tags: ["planning", "catharsis", "stunts"],
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
    title: "Megalodon Firefighter", subtitle: "Tactical Crisis Response",
    icon: "helicopter-delapouite", tint: "red",
    blurb: "A time-displaced mecha-helicopter fights fire disasters simulated with cellular automata, combining water suppression with kinetic meteor interception.",
    genres: ["falling-sand", "action", "vehicles"], tags: ["firefighting", "helicopter", "time travel"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "Skullhead.html", prefix: "skullhead",
    title: "Skullhead", subtitle: "Death Journal Vengeance",
    icon: "burning-skull-skoll", tint: "red",
    blurb: "A cathartic 2D physics action game. A devil-contracted vigilante works through a journal of society's worst people with chainsaws, blades and firearms, healed by dark powers.",
    genres: ["action", "physics"], tags: ["vigilante", "supernatural", "catharsis"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "AAL-Stealth-Sector.html", prefix: "stealth_sector",
    title: "AAL Stealth Sector", subtitle: "Covert Battleship Wars",
    icon: "battleship-cathelineau", tint: "blue",
    blurb: "Battleships rebuilt for real tactics: command 8 specialized warships with unique firing patterns and stealth systems, where every ship matters and every shot counts.",
    genres: ["strategy"], tags: ["naval", "turn-based", "stealth"],
    universe: "aal", status: "concept", added: "2025-10-04"
  },
  {
    page: "StardustAssault.html", prefix: "stardust",
    title: "Stardust Assault", subtitle: "Twin-Stick Mecha Shooter",
    icon: "interceptor-ship-delapouite", tint: "magenta",
    blurb: "Classic shmup action meets particle physics. Every explosion from your starmecha's arsenal becomes a canvas of colorful falling sand.",
    genres: ["action", "falling-sand", "mecha"], tags: ["twin-stick", "shmup", "space"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "HazardMissionTeam (2).html", prefix: "hazardteam",
    title: "Hazard Mission Team", subtitle: "Settlement Crisis Response",
    icon: "gas-mask-lorc", tint: "yellow",
    blurb: "Lead an elite crisis-response team of android operators through real-time logistics action, tackling impossible missions across exotic worlds.",
    genres: ["strategy", "action"], tags: ["crisis response", "logistics", "androids"],
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
    icon: "ray-gun-lorc", tint: "cyan",
    blurb: "A 2D action platformer: an immortal galactic agent wields modular, physics-driven weapons through vast alien laboratories. Unrestricted destruction, true empowerment.",
    genres: ["action", "physics"], tags: ["platformer", "power fantasy", "weapons"],
    universe: "aal", status: "concept", added: "2025-10-04"
  },
  {
    page: "Mosh_Pit_Mayhem.html", prefix: "moshpit",
    title: "Mosh Pit Mayhem", subtitle: "Heavy Metal Brawler",
    icon: "guitar-lorc", tint: "magenta",
    blurb: "A ragdoll brawler set at heavy metal concerts. Momentum-driven fights in microgravity mosh pits, with healing between songs.",
    genres: ["ragdoll", "action"], tags: ["brawler", "music", "heavy metal"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "bunkership.html", prefix: "bunkership",
    title: "Bunkership Exhaust Port Breaker", subtitle: "Tactical Demolition Action",
    icon: "brick-wall-delapouite", tint: "orange",
    blurb: "Brick breaking made meaningful: a spec-ops vessel exploits the one weakness of colossal armored warships, their exhaust ports. Every procedural bunkership is a new tactical puzzle.",
    genres: ["arcade", "physics"], tags: ["brick breaker", "procedural", "space"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "MutantLoveQuest.html", prefix: "mutantlove",
    title: "Mutant Love Quest", subtitle: "Morphing Ragdoll Romance",
    icon: "tentacle-heart-lorc", tint: "magenta",
    blurb: "A post-apocalyptic romantic comedy: a mutant fights through social obstacles to make their date, while their body parts transform every 30 seconds.",
    genres: ["ragdoll", "action"], tags: ["romance", "comedy", "mutation"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "Planetary Ring Miner.html", prefix: "ringminer",
    title: "Planetary Ring Miner", subtitle: "Breakout X Falling Sand",
    icon: "ringed-planet-lorc", tint: "yellow",
    blurb: "Mine exotic asteroid rings with Arkanoid precision and falling-sand physics, and turn the haul into interstellar infrastructure.",
    genres: ["arcade", "falling-sand"], tags: ["breakout", "mining", "space"],
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
    title: "Justice Will Glass Them", subtitle: "Orbital Vengeance Obliteration",
    icon: "police-badge-andymeneely", tint: "blue",
    blurb: "A space police warship delivers precision justice by orbital bombardment, drilling through criminal fortresses layer by layer in falling-sand physics.",
    genres: ["falling-sand", "arcade", "physics"], tags: ["orbital bombardment", "space police"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "Mafia_Takedown.html", prefix: "mafiatakedown",
    title: "Mafia Takedown", subtitle: "Dismemberment Ragdoll Vigilante",
    icon: "fedora-lorc", tint: "red",
    blurb: "Ragdoll vigilantes take apart organized crime one limb at a time. When a hero falls, the next one picks up the mission.",
    genres: ["ragdoll", "action"], tags: ["vigilante", "crime", "dismemberment"],
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
    title: "Chain Reaction Demolition Punch", subtitle: "Cyclops Building Destruction",
    icon: "fulguro-punch-lorc", tint: "orange",
    blurb: "A one-eyed alien superhero recycles buildings with cosmic strength. Pick the right spot to punch and alien heat transfer sets off chain reactions.",
    genres: ["physics", "falling-sand", "puzzle"], tags: ["demolition", "superhero", "chain reactions"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "Underground Brawl.html", prefix: "underground",
    title: "Underground Brawl", subtitle: "Ragdoll Combat",
    icon: "boxing-glove-lorc", tint: "red",
    blurb: "Hand-to-hand ragdoll fights in dim underground venues, where positioning and real collisions decide every knockout.",
    genres: ["ragdoll", "action"], tags: ["brawler", "melee"],
    status: "concept", added: "2025-10-08"
  },
  {
    page: "Collidotron.html", prefix: "collidotron",
    title: "Collidotron", subtitle: "Cascade Physics Processor",
    icon: "crystal-cluster-lorc", tint: "cyan",
    blurb: "23rd-century precision demolition of crystalline waste slabs: pick the right tiles and let cascading physics reactions restore the environment.",
    genres: ["puzzle", "physics"], tags: ["cascades", "sci-fi", "environment"],
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
    title: "Russki Biomonster Neighbourhood", subtitle: "Apartment Ragdoll Rumble",
    icon: "spiked-tentacle-lorc", tint: "green",
    blurb: "Play the amorphous flesh monster loose in a Soviet-era apartment block, using tentacles and bone spikes against tenants who fight back with hidden weapons.",
    genres: ["ragdoll", "action"], tags: ["monster", "horror comedy"],
    status: "concept", added: "2025-10-08"
  }
];
