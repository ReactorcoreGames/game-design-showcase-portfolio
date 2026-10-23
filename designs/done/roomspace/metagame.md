# RoomSpace: metagame, modes and business

What the player does with the universe: the purpose, the game modes and campaign ideas, NPC dialogue and opinions at the campaign level, and the business notes. The big picture is in `RoomSpace.txt`; the scans add concrete modes and mechanics (181, 191–192, 195, 205, 215, 256–257). Numbers in brackets are scan numbers; full wording in `transcript/`. *(interpretation)* marks Claude's reading; **Proposal** sections are Claude's suggestions.

## Purpose

From the overview: RoomSpace is a platform that simulates a living, persistent universe, and can be set up for empowerment, socialization, self-expression, learning, challenge, or carrying a message. It could become several separate games, each focused on one theme, or one big game where the activity depends on where the player travels that session, "like how I would wake up on a free Sunday and decide what I'd like to do that day".

Framings named in the overview: a **conquest** game (build up your people with an exchangeable hero, fight factions on ground, air and space); an **adventure** with a reincarnating hero chasing grand achievements; an **engineer/gardener** terraforming worlds into a paradise; an **investigator/bounty hunter** uncovering eldritch mysteries; or an **omni-game** that is all of them, an infinite procedural campaign generator in one seamless universe (like TopVerse, but without separate compartments). Each campaign has a clear beginning, middle and end; its outcomes carry over into the next one generated in the same universe.

Purpose list from the notebook (191): empowerment, badassery, gore/gibs/particles, sadism/brutality, surprise/hilarity, meaning. Needs (numbering messy on the page): power fantasy, anger relief, relaxation, growth/learning, challenge.

A later design note (195): **"Purpose/focus: make memories, focus on the past, not the future."** The destination is to make more memories: a trail of success, destruction and progress that the game documents, celebrating or mourning past events. Even the camera idea follows it: "pivot camera towards where you've been, not where you're going".

## Starting small

RoomSpace began as a Floppy Heroes-like ragdoll gladiator game (free rotation, guns and futuristic gear, rooms with hazards) and grew into the universe design. The overview's plan: start as the simple low-gravity ragdoll combat game, but plan the framework so it can grow without an engine rewrite. Several notebook modes are sized for that first step.

**Three variants** (191):

- **Party Hard**: one big room, one player, 100 targets (performance?).
- **Floppy Heroes**: an arena, up to 9 units per side.
- **Hotline Miami**: many small rooms with doors and a few targets each (one-way or returnable).

## Spirit Mode, body possession (191)

The player is an angry spirit possessing ragdoll bodies. Candidate titles: Lifeform Eradicator, Anger Overkill, Gore Frenzy, Triple Kill, Nanoworm/Killworm/Goreworm, Gore Shred Instinct; "GOREFLOAT" appears on a business note (192).

**Streaks**: rather than discarding bodies, keep one possessed character alive to earn ethereal mutations that warp it into a kind of demigod. As its kills, rooms survived and body count grow, it gains random traits, bonuses, passives, abilities, allies, luck, and item and vehicle spawns. The more warped a body becomes, the weaker it gets whenever it's left unpossessed; the spirit is the source of the power.

**Hall of Fame**: past a minimum kill count, a character enters the hall of fame. If it dies, a tiny rule-of-thirds screenshot is taken and its name, kills and rooms are recorded. At max kills it **ascends** to another dimension ("awesome Valhalla") and enters the hall of fame with a win screenshot. "A game within a game." Community members, patrons and backers can lend their names to characters.

## Campaign and mode ideas

**More metagame ideas** (205), loose campaign concepts:

- **Broodmother Infester / Gore Queen Conquest**: kill all, then release hundreds of spiders.
- **Killer Curse Possession**: you become whoever kills you.
- **Murder Cyborg**: "basically Butcher"; kill everything foreign (MD Geist); the sentence "you are 'death force' from…" was never finished.
- **Monster/Beast/Mutant Hunter**.
- **Wrecking Crew**: reduce everything to fine rubble.
- **Pest Exterminator**: kill or capture pests with minimal collateral damage.
- **Screensaver endless battle**: watch AI fight, maybe bet, with counters and stats.
- **Wipeout**: an obstacle course run.
- **Knytt-style relaxing explorer**: help people, playful adventuring.
- **Gardener Robot**: seed worlds.
- **Make life more wonderful**, with an example society and mindsets.
- **Edge of Tomorrow / Groundhog Day**: live, die, repeat.
- **Purge Cop**: a Judge Dredd megastructure infiltrator.
- **Super Metroid maps and areas.**

**Potential metagame ideas** (192):

- **Unique named super NPCs** that can't be possessed (a Nemesis system).
- **"The Soldat story"**: "a whole galaxy has decided to kill each other for fun and you can join in!"
- **Strong Opinion Ragdolls**: everyone has a randomized name and belongs to groups with strong opinions about mundane preferences (players can write their own topic lists; a population counter is shown often). Every campaign opens with a random NPC yelling a preference question at you; answer A, B or Nothing. Answering A makes every B mad and vice versa; Nothing is a wildcard that angers one side or both. The answer picks your allegiance. The first room has 1–15 NPCs; if no one from the offended side is present, some crash through the wall to fight you ("I heard you talking shit like I wouldn't find out!").

## Dialogue and opinions

**Player choices in narrative games** (256): 1. good/compassionate ("better world"); 2. bad/evil ("just fuck shit up"); 3. spontaneous ("YOLO", wildcard); 4. apathy ("whatever bro"); 5. ignore/leave; 6. more info ("explain"); 7. please/thank you (start/end); 8. yes/no.

**Nothing = 3 options** (257): a "Nothing" answer comes in polite ("I don't know"), indifferent ("leave me alone") and hostile ("fuck off") forms, all still wildcards, with many variations. The choice can influence the AI state of opponents for that campaign.

These plug into the AI's opinion system: every NPC keeps an opinion of every character, and offences and answers shift it (see `characters.md`, AI).

## Business and community

From the overview: a modder and creator community with a marketplace or portal so creators can earn from their content (premium content, Patreon-style support, a Netflix/Nebula-style creator platform, commissions, third-party services), with submission guidelines and tutorials to keep quality up, so making content is "easy yet standardized and unified".

From the notebooks:

- DLC possibilities; a "3M+ texture shader?"; a physics stress test of 30 per character (192).
- **Ad circus**: an optional place with ads ("if something cool, click it"; ads rotate, check back now and then) (192). The same idea appears in the Shape Smasher design.
- **Gratitude programs** for contributors to the game's success: free keys to the full game, free access to new content (192). "Throw money at me" (192).
- **Content releases by security clearance** (215): Alpha A1, Beta B2, Gamma C3, Nemesis D4, Archangel X9 ("pricing" corrected to "releases").
- **Credits page** (181): music tracks with a play button and a clickable link to each artist's page.

## Proposals

Claude's suggestions for connecting the pieces, not Reactorcore's design.

- **Proposal, modes as campaign templates.** Treat each idea on 205 and 191 as a campaign template the generator can pick: it names a goal (exterminate, rescue, terraform, explore, survive), a scope (one room, one cup world, a sector) and a rule twist (possession, rebirth, no killing). The generator then places the template in the persistent universe, so a Pest Exterminator campaign leaves cleaner rooms behind for the next one, and a Wrecking Crew campaign leaves rubble that later campaigns find.
- **Proposal, a first release.** Build Spirit Mode in Hotline Miami form first: a single generated cup world of small rooms connected by auto-packing doors, the full ragdoll combat and item system, the room-local atmo, and the hall of fame. It exercises every system the universe needs (rooms, doors, packing, persistence of rooms you revisit) while staying a small, finishable game, as the overview's "start off as the simple ragdoll combat game" intends.
- **Proposal, making memories.** Give the "make memories" goal a concrete form: the universe keeps a chronicle of notable events (ascensions, destroyed MDRCs, terraformed nodes, nemeses killed), shown on the world map and in the background of rooms where they happened (a wreck, a monument, a scorch mark). New campaigns start by referencing an entry from the chronicle, which is how one campaign's outcome carries into the next.
