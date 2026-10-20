# Reactorcore's Design Bible, Part B: The Technical Side

The second half of the short form of *Game Design Technology: The Holy Grail of Fun*, covering the book's Parts IV and V: designing the game, then building, sharing and growing around it. Read `2a-bible.md` first. Everything here is a method, not a rule, and each one is only right when it serves the purpose of the project. Chapter file names refer to `book/chapters/`; the book wins any disagreement.

The last two sections are for whoever writes this repo's showcase pages: how to carry this thinking onto a page (section 14), and what the earlier, discarded bible got wrong (section 15).

---

## 1. Taking inventory

*Book: c20-taking-inventory*

Before designing, find out what you're working with, in all four parts of the Holy Grail.

The purpose comes first, written down where you'll see it every working day, statable in a sentence or two. It also sets priority: primary features (the project fails without them), secondary (they make the primary ones better), tertiary (nice if there's time). When time or money runs short, this order says what to cut.

The technology has hard limits (processing, memory, storage, screen, input, network, battery, engine quirks) and the design keeps it within them. The crab bomb shows what happens otherwise: Cortex Command could only handle 255 objects per level before IDs mixed up and things exploded at random, a soldier took about ten objects, and delivery craft had no cargo limit, so players packed one with free crabs and a flood of ragdoll crabs broke the game. Player freedom is good; freedom that locks up the computer means the foundations are wrong. Good design respects player freedom and the computer's limits equally. Find the limits by stress-testing, not guessing. Lean into what the technology is unusually good at (Cortex Command's destructible terrain was underused). Design for the busiest moment real play will have, not for a showcase of one explosion. Technology includes the player's hardware: optimization decides who gets to play at all.

The human being has limits too: attention (one thing, one place at a time), reflexes, precision and stamina (which drop when tired), memory (especially for returning players), and a body that needs to eat, drink, rest, sleep and move. Cortex Command's early skirmish asked one human to micromanage several fragile soldiers against an AI controlling everything at once with infinite resources and no pause. That's inhuman; small squads of three or four focused on objectives would have fit a person. Controls and interface are where body and game meet. Show important information clearly, write text that makes sense without the developer's head, and regularly play as if clueless, or watch someone who really is.

Skills and resources pull against the rest: time, people, money, skills, tools, health and support. Be honest; optimism here costs years later. A design that needs ten artists when you have none is a wish, not a design. That doesn't mean shrinking the dream; it means designing it to be buildable with what you have (simpler art, generated content, a smallest playable version that grows).

Respect for the human runs through all of it. A game is a guest in someone's life:

- Their time: no padding, no hidden delays, nothing unskippable.
- Their saves: save whenever they need to stop, stop without losing anything, back up and move save files. Progress belongs to the player.
- Their body: pausable, optional reminders to drink, eat and rest, the real-world time shown somewhere.
- Their money: honest about costs, never pressure.
- Their mind: no manipulation, nagging or guilt; leave whenever, welcomed back whenever.

None of this restricts the player. Reminders and a clock, never forced breaks: forcing rest violates autonomy as much as forcing play. Give people what they need to choose well, then trust their choice.

## 2. Foundations before content

*Book: c21-foundations-before-content*

As an official Cortex Command content creator, Reactorcore turned sprite sheets into about fifty guns, tuned by feel (some bullets weighed three kilograms), before learning the game had physical standards nobody had mentioned. Then came the realization: a gun depends on who uses it and where, and characters depend on their environment (lethal debris needs protection, walls need climbing gear, water needs flotation, drops need something to soften landings). Nothing in the official content or mods had looked at what it stood on.

The dependency chain: **performance limits of the computer > premise of the game > basic natural laws of the in-game universe > environment > the vehicle or character that uses it > the gun itself.** Each link depends on everything to its left. Replace "gun" with any content (a spell, a recipe, a building, a dialogue line, a level). Content sits at the end; it's the last thing to design. "If you wish to make an apple pie from scratch, you must first invent the universe" (Carl Sagan). In a game you invent the universe either on purpose or by accident, one inconsistent piece at a time.

So standardize the shared basics first: how explosions, smoke, sparks and liquids behave; how bullets and casings work for every gun; fire, electricity, radiation and poison; flora and fauna; armor and materials for everything; the logistics and feel of moment-to-moment play, controls and HUD; and encourage every content maker, modders included, to build on those standards. Then environments, then vehicles and characters, then finally the guns.

What that buys: content that supports itself and interacts properly; balance that comes from sensible standards instead of arbitrary justifications; more creativity, not less ("the heavily armored climbing specialist needs a weapon for several weak enemies in confined spaces, under these rules" produces new concepts, where "pistol, SMG, shotgun, rifle, sniper, rocket, grenade" produced the same cookie-cutter faction in every mod); and modular content, the basis of content that multiplies.

Buckets or a pipe: the old way is carrying water home by hand every day forever; the new way is building a pipe once and turning on the tap. Foundations are slow, boring boilerplate that produces nothing playable by itself, but they reverse the ratio from five weeks of work for five minutes of play to five minutes of work that stays useful for years. That's also the answer to the developer who spent years on something consumed in minutes.

Foundations give a natural reason to learn about the world (engineering, logistics, physics, biology, history). Learn only what the design needs, and look for openings: real-world logistics, for example, explains why powerful things are rare and expensive, which is free balance.

## 3. Build the forces, not the desert

*Book: c22-build-the-forces-not-the-desert*

Most games are throwaway toys: years of work consumed in hours, playable one way only, because developers still make games like movies, constructing a specific situation and putting the player on rails through it. That forces a medium whose strength is freedom into a constrained, scripted shape, and violates the need to be curious, play, explore and fail without fear.

Framework-driven design builds the conditions for a situation instead of the situation. Don't make a desert; make an area with lots of sand, harsh sunlight and high heat, which results in a desert. Same for forests (fertile soil, humidity, gentle sun, compatible flora and fauna), tundra and lava zones. Don't make prefabs; make the elements prefabs are made of and assemble them with simple if/else rules. It's the common mistake applied to content: the desert is the final result, sand and heat the root cause. Four biomes designed this way become hundreds, with hybrids appearing on their own. The same goes for characters (a paper doll that takes any parts, generated names, rolled backgrounds), campaigns (a generator instead of a script) and level order (open world, or levels playable in any order and shuffled). None of this needs a universe simulator: building blocks with parameters, an if/else tree, and a little random(1,9).

Every mechanic has a purpose too. Ask of each one what it makes the player feel, which needs it meets or violates, and whether it serves the game's purpose. A deep crafting system can meet creation and mastery beautifully and still be wrong for a game about momentum, because every stop to craft breaks the flow. Judging mechanics in isolation produces games that are collections of good mechanics and not a good game.

Think in wholes. Change movement speed and you've changed level sizes, enemy reaction times, the camera, difficulty and pacing; follow every change outward. Look at how nature solves lasting, self-balancing, varied systems and borrow the principle. Build from top-down (galaxies to details) or bottom-up (materials to structures) depending on the scale the player mostly plays at, and check the other direction so they agree.

Believable, not realistic. Realism copies the real world in detail and is expensive and often tedious. Believability is the world making sense on its own terms: consistent behavior, understandable causes and effects, no magic rules that apply to some things and not others. It meets needs for clarity, safety and freedom, lets players plan, and is what makes framework design work at all. When realism and the player conflict, the player wins: favor convenience (carry fifty grenades if that serves the purpose, with a believable reason or no attention drawn to it), abstract and remove middlemen (the starship crew doesn't need toilets), and add systems by necessity, not because reality has them.

Natural limits, not arbitrary ones. No invisible walls or quietly disabled abilities; use cliffs too steep, water too deep, cold that kills without gear. If the player has a gun they can shoot anyone, including a story-critical character, so design the story as if lightning could strike anyone and let the game continue with an ending that reflects it. Use the systems you built: don't add destructible terrain and then fear letting it matter because a scripted moment might break. Suppressing your own systems to force a moment meets the developer's need at the player's expense and creates ludonarrative dissonance. Tightly controlled experiences belong in film, comics or books.

Throwaway is worse business too: a long build, a single sale (often discounted), a narrow window, and so shallow that ten minutes of someone else's video feels like "done".

## 4. Content that multiplies

*Book: c23-content-that-multiplies*

Additive content sits alongside everything else and is used once: a handmade level, a scripted boss, a cutscene, a unique quest, each adding its own few minutes. Multiplicative content is modular, swappable and combinable, and each new piece gives every old piece something new to combine with. Ten weapons, ten enemy types and ten layouts give a thousand combinations; one more weapon adds another hundred. It's about how content is organized, not what kind it is: levels, characters, props, weapons, vehicles and items can all multiply in a modular game.

Additive: five weeks for five minutes, often with special-case code, a treadmill where players consume faster than anyone can produce. Multiplicative: five hours for five weeks, once the framework of standardization, modularity and intercompatibility exists. Additive content keeps its place for a curated story or experience; for any game whose purpose lives in its mechanics, multiplicative content is the future.

Spawn zones make levels multiply: instead of hand-placing everything, place zones (a rectangle is an origin plus width and height, a circle a center and radius) where items, characters and structures appear on load, nested for more variation. Then vary what spawns, how many, in which formations and facings, with what equipment, or nothing at all, and keep random ranges as wide as possible, because narrow ranges produce sameness. Levels can be modules too: in Reactorcore's nanomachine-in-the-body design, "rooms" (basic rooms for action, highway rooms with currents for travel) are linked by a generator into a network holding only what the mission needs. Add one room and it appears in every campaign.

Characters and items multiply when the character accepts anything: hands that can hold, use, stash, drop and throw any object, with context flags on the object deciding what it does. Nothing is bolted permanently onto anyone, and every new item works for every character, player and enemy alike.

Structured randomness, the heuristics randomizer: lazy randomness gives "a thousand bowls of differently colored porridge", all technically different and all feeling the same. Instead, arrange randomness as a decision tree of if/else statements where higher choices lean the lower ones. For a base assault: how many defenders, placed how, how close to what they guard, how healthy, how near their supplies, armed with what, in what mood. Some branches split into subtopics and merge back, others branch off entirely, and at some steps a small chance (the book's examples are 0.01%, 1%, 5% or 10%) injects chaos. For environments, read the general setting first and decide what's common, rare and anomalous: sand everywhere in a desert, an oasis less likely, and very rarely a snowman with a freezer next to it explaining why it hasn't melted. Allow freak occurrences, but always with a discoverable reason. That's the difference between chaos that delights and noise that annoys.

Make content cheap to produce: fewer animation frames, reused graphics (the good kind of reuse, making more variety possible), grayscale art tinted in the engine, mechanics that need little art, and a low barrier so others can contribute. The cheapest strong customization is letting the player tint one to three parts of their character, with a restricted palette if the tone is gritty.

Nothing hard-coded. Prefer scrolling lists, drop-downs and browsers to fixed slots (twelve slots promise there will never be a thirteenth thing). Make even the main character and their control scheme swappable. Don't tie content or difficulty to a fixed level order; make later levels different in style, not just harder. Every hard-coded limit is a future overhaul at exactly the moment the game is doing well.

## 5. Infinite metagames

*Book: c24-infinite-metagames*

The metagame is how a game is structured: how it's organized, begins, flows and ends (or doesn't). The moment-to-moment game happens inside it. A finite metagame ends and must reset; chess always starts with two rows each and ends at checkmate. An infinite metagame has no final goal and no forced reset; you keep playing with all progress valid for as long as the save exists. That's infinite playability, not replayability: you don't replay it, you keep playing it. This means long-form singleplayer campaigns made infinite, not endless-runner mobile games.

It matters to players who want to do cool things themselves instead of spectating, who want to master one game instead of relearning a new one each time, whose favorite mechanics were cut off by an ending, or who wanted updates the story made impossible. Those are unmet needs for mastery, meaning, freedom and continuity. An infinite metagame only makes sense when the enjoyment comes from the mechanics (driving, fighting, building, solving, exploring, experimenting, relaxing, fooling around). If people come mainly for a story or a specific lesson, a finite handmade structure serves better. The purpose decides.

Why the usual structures fail, all because they're linear and work against nature with arbitrary rules:

- Most games boil down to "the longer you play, the harder it gets, until you give up". Winning should be normal.
- The zero-to-hero scam: weak and locked out while still learning, a mid-game slog serving the progression system, and a late game where early content is clutter, nothing resists, and the story has dead-ended. A carrot on a stick that turns out to be cardboard.
- Scaling opponents bring back the endless ramp, remove breather encounters, and make the universe revolve around the player. If you keep beating enemies, shouldn't they get weaker and poorer? Scaled zones are a linear game wearing an open-world mask, and earlier areas freeze in place once you "graduate".
- Roguelites combine scaling and zero-to-hero with a reset at the climax, often tuned so you lose regardless of skill, with meta-upgrades that mean you were deliberately made weak. And every run has the same calm-to-climax shape.
- "Infinite survival" modes are a ramp with no top, guaranteed death with no way to win: arbitrary and futile.

The winning combination is two layers. The infinite overarching goal gives context and an ongoing narrative (role, profession, why you do what you do, how you affect the world) and is never directly reached. The best frame is a service: running a postal service for quirky clients, exploring and charting the cosmos for scientists back home, managing sewer maintenance, fixing broken machines, painting a city to lift its mood, running a demolition company that puts on a show, operating a sustainable interstellar mining company. Serving people is naturally infinite (there are always clients), and it connects to one of the most satisfying feelings there is, seeing your actions make someone happy, so the client's reaction must be a real feature. The finite local goal is the overarching goal's factory of bite-sized sessions with a definite start, progress and end, nested as campaign > quest > objective. A player with a free evening plays a quest or a campaign and stops satisfied, and next week a new one is waiting. The context never expires, locks them out or forces a reset.

Without the overarching goal, sandbox players eventually turn to destroying what they built. That's the need for meaning, unmet, using the last kind of change left in reach: the game ran out of reasons, not content.

New Game+ can bridge a story game toward infinity: the first run is a curated, restricted version (effectively a tutorial), and NG+ lifts the restrictions, shuffles and remixes the campaign, makes the story skippable and unenforced. It still loops its story, which strains meaning; a playful layer that acknowledges the loops helps, but truly getting past it needs the two-goal structure.

The Astroneer 8th-planet proposal is the worked example: the finished game's quests were finite and its planets couldn't regenerate, so players ended with stripped worlds and nothing to use their megabases on. The proposal turns the ending gateway into a teleporter that pulls a procedurally generated visiting planet into the system, with two to five job-like missions using the player's existing infrastructure; the original seven planets stay as the persistent home, each visiting planet is retired after its missions, rare "reset bombs" regenerate exhausted regions, and an intermission screen shows stats and offers a break. Almost all the content already existed; the planet generator is a heuristics tree. The method: keep what the game does well, find what makes the structure finite, replace it with an infinite overarching goal, generated local goals, a persistent home and a disposable wilderness.

Infinite games aren't harder to build. A campaign generator is a branching if/else tree and a random function, simpler than the mechanics themselves. It's organization.

## 6. Pacing, difficulty and progression without the scam

*Book: c25-pacing-difficulty-and-progression*

Campaigns made of modules: each generated campaign gets its own shape (easy-medium-easy, hard-easy-hard, hard-easy-easy, and so on) and length (very short to extra long). Themed zones are shuffled and don't always mean the same difficulty: a lava stage can be calmer than a forest, and a session might be desert, desert, snow, forest. Every aspect is a swappable parameter the generator picks: difficulty, pacing, length, number of zones, supplies, content mixing, starting state, bosses, availability. Settings can be two steps, nine or 1–100; fixed steps nudged by a small random multiplier are both readable and varied.

Balance by real-life logic: an infinite game can't let the player grow stronger forever, so the world gives natural reasons to give power up or lose it. Minecraft simply mimics real life: dangerous unknown places, gear dropped on death, gear that wears out. The principles: powerful things are costly and so rare; nothing lasts forever and maintenance costs resources; everything is connected and careless actions have consequences; things need supplies and logistics give even powerful things weak points; the world is bigger than you; knowledge can be lost. Balance follows without arbitrary numbers.

Abundance from the start: players don't grind out of scarcity; they get resources and abilities from the beginning and the arbitrary obstacles are removed. Challenge moves to where it belongs. Scarcity is never a design goal; it only appears as a natural consequence (you spent your ammunition, your supply line was cut, the planet is poor) or as a campaign parameter the generator chose. Abundance also removes the reasons to cheat.

Progression as perfecting your world: locally, power rises and falls with what the player is doing (investing wealth in a village, building a dam, swapping the giant mech for an infiltration outfit to fit a narrow cave). Globally, they progress by making their world more personal, more their style, more of a masterpiece, like bonsai or gardening. "Making the world a better place", endlessly.

Three kinds of player arrive after an install: first-time, experienced, and returning. First-time players get limiters on how hard things can get in their first one to ten hours, because a safe place to learn is how you welcome someone. Experts get a fast track to turn the limiters off ("pro mode: no limits, not for beginners!"), or, in an open world, riskier routes with higher rewards (Deus Ex's several approaches, Fallout: New Vegas's monster-guarded shortcut). Returning players can skip what they know, get a quick refresher, and find their old save still works. Never an unskippable tutorial.

Tutorials: spell it out bluntly, introduce things as they're needed, let players learn by doing where failure costs nothing, keep the interface clean, and always let them look it up again (a manual, codex, helpful character). Never design anything that only makes sense with knowledge of the developer's own mind.

Never reward, never punish. The common extrinsic motivators are unlockables, progression systems, penalties for mistakes, collectables, money and shop systems, upgrade trees, punishments for not playing as intended, and achievement notifications. All of them damage long-term sustainability. This doesn't ban money, found items or built tools from a game's world: a merchant in a believable economy is part of the world, while a shop whose prices exist to slow the player or push them to a cash shop is a lever bolted on top. The question is always whether the thing belongs to the world and serves the purpose, or steers behavior from outside the fun. Intrinsic motivation is the alternative: moment-to-moment play, mechanics and metagame enjoyable in themselves, easy to pick up, deep and varied however long you play, fun even after all content has been seen.

Feedback is not a reward. Players need to see their actions matter. Feedback is information: what happened, what changed, what still needs doing. It can celebrate a victory with the player and mourn a loss with them. It never rewards or punishes. Gratitude and acknowledgement, not praise and judgement.

## 7. Worlds that last

*Book: c26-worlds-that-last*

The regular world and the wilderness (loosely after RuneScape's split): the regular world is the starting area, then the persistent home the player returns to for rest, upgrades and preparation, where things built stay. The wilderness is a temporary, disposable, randomized space created for a campaign or quest; the player goes in with gear, completes it, brings back resources and trophies, and then it's deleted. Both are needed because storage and memory are finite (an ever-growing save eventually ends the game) while the human need for variety is endless. The wilderness's effects on the regular world persist, and what happened in it is recorded. The only thing that grows forever is the history, kept small and ideally in common formats (images, PDFs, text) that can be backed up and opened outside the game. A wilderness location can be regenerated on revisit from stored flags. Players don't need an infinite home anyway; a human is in one place at a time, and naturally builds a cozy base. The form depends on the project: a walkable base, an overworld map with menus, or simply a campaign progress bar. The names are training wheels; only the concept matters.

Hardware limits are a law of nature, built in like gravity. Literally infinite generated worlds that fill a drive are something software should avoid at all costs, and most of that area goes unvisited anyway. Reactorcore models universes as a bowl: a flat center of permanent locations (say three to nine galaxies or superclusters, sized to the game's scale) and curved sides of virtually endless wilderness where things drift out and return changed. Believable and smooth on an ordinary computer, not realistic.

Mementos and a living history: an active, visual record of everything the player has done, like an artwork that keeps evolving. It shows what's done and what still needs doing, celebrates victories and mourns losses with the player, and never rewards or punishes. Forms: an overworld map whose markers show a wasteland turned green or an empire pushed back; a guestbook of messages from the people you served; a history book; a medal box where each medal remembers its battle; a memorial wall for fallen characters; a home base visibly grown richer; a corrupted place now clean. They can be layered (whole game, campaign, region). The player creates the artwork just by playing, it's interesting from the first minute, and it should be shareable as an image or document, since every player's is unique. Two of Reactorcore's designs: a procedurally generated galaxy mosaic whose gray regions brighten as missions are completed, and at 100% the player names it and writes a line, saved as an image; and a permadeath memorial log of each fallen character's name, colors, cause of death and achievements, with a portrait, and names that can never be reused.

Time never rewinds. Reloading to erase a failure, respawning with a flimsy excuse, and the roguelike's reset-plus-respawn all make the world a game of pretend. In Reactorcore's projects nothing un-happens; the universe moves forward. This isn't about saving: saving to stop and come back is respect for the player and every game should allow it.

Death and respawn: the player's soul is immortal and returns in a new body, gaining its traits and losing everything tied to the old one, sometimes in very different circumstances. Each death skips time forward, which can erode improvements in the world, so rerolling isn't worth it, but the player is never limited in the new life. They keep their knowledge of the world as a cheat sheet. Death matters, and never ends the game.

Start the universe already in motion, in relative equilibrium, not at a primordial big bang where nothing interesting has happened. No heat death either: disasters can reset a region, never the whole universe, and no button ends everything.

These persistent universes come from Reactorcore's real-life view (that souls return, without memories, into the world we're all shaping now), offered as personal belief, not doctrine. The conclusion holds either way: a world where time moves forward and consequences stay is a world where what you do matters.

## 8. What a game designer does

*Book: c27-what-a-game-designer-really-does*

A game designer creates the overall blueprint of a game (video, tabletop or live) and defines the complete experience for those building it and those playing it, from before the player first sees it to long after release. Outside the game: marketing, monetization, community, publishing, the path from first version to ultimate form. Inside: rules, structures, frameworks, systems, features and mechanics. Across time: the whole lifecycle, including maintenance and compatibility.

A developer builds with art, code, sound and writing; a designer glues the pieces into something worth playing. A spider at the center of the web: says what needs to happen and trusts experts with how. In a team the designer doesn't code, draw, compose or market, but learns enough of each to understand those people's needs. Often the designer designs the support structure for content rather than the final content: the complicated, boring foundations, so the team gets the fun part of making content to their own taste within the framework.

One designer per project, and it must be the person holding the driving vision. Dumping design on a coder or artist makes them do two jobs. Nobody taking the job means design by darts. Many siloed designers under a producer, under an executive, each able to override, produce an indecisive mess. Consensus can't produce a unified vision; too many chefs spoil the broth. If the designer leaves, the vision changes and every decision needs re-examining, or the cake becomes a soup. One designer doesn't mean deciding alone: the designer is the one person whose job is to listen to everyone, then find the solution that meets everyone's needs. Consensus asks everyone to agree on a solution and gets a compromise; design asks everyone what they need and finds one solution that meets all of it.

Blueprints with leeway: the designer defines the what, the expert owns the how, adding their own touch as long as requirements are met. Blueprints are tailored to the person following them and readable, with diagrams and pictures where those show more.

Working alone means wearing both hats, so know which one is on. Work smart: don't match big-studio asset detail you can't afford, don't build intricate systems you can't maintain, use asset packs, generators, services and automation. Compelling games can be made with simple, cheap solutions.

## 9. The design process

*Book: c28-the-design-process*

Scope creep is not the enemy. What's called scope creep is designing while already building, usually after skipping or rushing the design phase: building a house and drawing the blueprint while the walls go up. The results (convoluted mechanics, bloat, lost direction, an interface reworked for every feature, every addition needing its own rules, self-contradicting code) get blamed on ambition, and the advice "keep your games small" spreads. That advice costs games without ambition, longevity or innovation, and tells newcomers to postpone their dream and make copies "for training". Reactorcore advocates the opposite: make your dream game your first project, in a scaled-down version feasible for your current skill. You learn to make the dream game by making the dream game.

Scope maximization: before opening the engine, chart the maximum range of possibilities the project could have over its whole lifespan, on paper, where scope creep costs nothing. Fill knowledge gaps by searching, playing, watching, going outside. Test theories with throwaway prototypes and explore the technology's limits. Don't rush it, and keep the details flexible: general, open to change, but coherent. Then build the absolute minimal version. The maximized scope becomes the roadmap: build order, room left in the interface for what's coming, no dead ends that force a restart.

Tools of the design phase: pen and paper doodles; mind dumps (the idea, everything uncertain about it, pros and cons, alternatives with theirs, completely free-form); cheap disposable experiments; documents your future self can read, all in one place; frequent backups.

Prototypes are proving grounds. Prove or disprove one thing, then throw it away; never build the final game on a prototype's shortcuts.

The barebones game first: a minimal version playable from start to end, however basic, then systems and content added toward the full scope. Start-to-end proves the whole structure; a polished slice proves one slice. Know the minimum viable product, the smallest version that actually fulfills the purpose. Prioritize primary, secondary, tertiary, with a checklist for dependencies. Kanban, scrum or a list all just organize building; none replace design.

Good design is paranoid design. With the scope done and theories tested, problems come from outside the design (engine limits, funding, store terms, a discontinued plugin), and only the implementation changes. Always have a plan B and backups; be paranoid about the engines, plugins, people and companies you depend on; prefer offline, installed tools. Planning isn't predicting everything; it's resilience, which is why the details stay flexible until the framework meets the real technology.

Everything takes longer than it seems. Reactorcore's rule of thumb: estimate, multiply by eight (five for familiar work), and look honestly at that number. Use it to judge feasibility: if the ×8 version is longer than you can sustain, don't drop the dream, find an easier way to build it (simpler art, generated content, a smaller first version). And if a part runs far past even ×8, step back and look for a simpler path to the same purpose. It's a tool for shrinking the plan, not for stretching a deadline.

Ready to release when the barebones version fulfills the purpose: someone with the need plays it and has it met without other needs violated. Not "finished", not polished (polish on a hollow core is polishing a ball of crap). Time to kill a project when evidence shows the design can't be saved: another strategy meets the purpose far better, the strategy can't meet the need, or it can't be finished with resources that really exist. Killing a project isn't defeat; keep the notes and what you learned. Never rely on miracles.

You will make mistakes; it's about becoming progressively less stupid. Beware enjoying the making so much it becomes the game. And rest: burnout fails the project too.

## 10. Working with people

*Book: c29-working-with-people*

Clarity and empathy run every working relationship. Compromises don't exist: everyone can be satisfied. Needs are universal and strategies clash, so ask what need each side's strategy serves and look for a third option; sometimes understanding a strategy's cost makes someone let it go willingly. Be firm but compassionate: you can say no to a strategy and fully honor the need behind it.

Message sent = message received? Ask for a recap in the other person's words, and recap theirs back; say it's to check your own explanation, so it's a gift, not a quiz. Make requests specific, positive and doable ("show the health bar at all times", not "stop hiding it"). Describe observations, not judgements ("the build was two days late and the save system wasn't in it", not "you're unreliable"). Never cry wolf.

Share the purpose, not just the plan, so people can decide well inside their leeway; show the vision with a playable build. Expect few helpers until the project is visibly playable. Never trick people into working for you.

Gratitude, not praise. Praise is a judgement, vague, and teaches working for approval. NVC gratitude names what the person did, how it made your life better and which need it met. Celebrate milestones together.

Players are excellent at detecting problems and bad at explaining them. Take the detection seriously and the prescription with a grain of salt; translate each complaint into the feeling and need under it, and find the root cause before changing anything. Players ignoring a game is feedback too. Some people act in bad faith (trolls, paid opinion-pushers, people who hurt others as a strategy); you don't need to label them, just look at whether the behavior seeks a need or seeks to make you feel wrong, and remember judgements describe the judge.

People don't always know what they want; ask what a request is for and how they'll know it worked. Real deadlines get honest scope and the barebones-first order; artificial deadlines are punishment wearing a calendar. Choose your influences consciously, and be a good one.

## 11. Beyond the game

*Book: c30-beyond-the-game*

The game starts before the main menu. Ads, box art, screenshots, the store page, a cardboard cutout: the experience has begun, so all of it should serve the same purpose. The outside can even blend into the game: a starship pilot game whose store page reads like a flight-academy acceptance and pilot's license, a strategy game's page formatted like a military briefcase, a gardening game's box art like a gardener's toolkit with an invitation to a garden in your care. Main menus, pause menus and even the game folder are part of the presentation.

Marketing is honest communication: showing people who have a need that the game meets it. Clarity of value: make it obvious at a glance what need it meets and how, show the inspiration, let the presentation feel like the game. Choose an accurate, simple, searchable name and check it's free. Be findable. Make the first hour excellent. Don't fear copycats; ideas are cheap and execution is everything (keep only the name private until release). Tad Hargrave's Marketing for Hippies is the recommended way to learn it.

A CEO's four questions are design questions. Hear the need behind them first: security and predictability for people responsible for others' livelihoods.

- "Can you guarantee a hit?" No one can; popularity is a side effect. What can be promised is a game that fully meets the needs it sets out to meet, without violating others, plus an honest picture of who has that need and what currently meets it worse.
- "What's the hook?" Not the theme, tech, story or mechanics, which are delivery. The hook is a clearly stated need that many people have unmet, and a game that meets it better than anything else ("People who love tactical combat finish every match tired, and everything they built is thrown away. Ours is the one where every battle counts."). If "hook" means a compulsion loop, the answer is no.
- "How do we reach non-gamers?" They have the same needs; they're uninterested in what games have offered them, or sated elsewhere, or blocked by hard controls, jargon, time and price. Describe value in their terms, lower the barrier, meet the need in the first ten minutes, show it where they already are, and never trick them in.
- "How do we advertise?" Show real moments of play that give the feeling the game is for. Never appeal to a need the game doesn't fulfill; that's how nonsense games sell, and every refund and angry review is the bill.

Monetization is the designer's job, because only the designer sees the whole game well enough to find the model that fits it. If you ever see customers as anything other than human beings who deserve care and respect, you've taken a wrong turn. Free value first, then something more for those who want to support it, so paying becomes gratitude. Support models: an honest price for a complete game with nothing held back; ongoing support for ongoing development (a Patreon-style page with behind-the-scenes posts, polls and work-in-progress, while the base game and honest expansions stay as they are); cosmetics as a thank-you, never status; and a creator economy where modders and creators can earn from content for a game built to make creating easy and standardized. When you need more money, ask honestly.

Pricing and inequality: most people don't live where games are made or own powerful computers. Optimize, mind compatibility, use regional pricing where possible, localize (keep text translatable, avoid culture-bound jokes), and support modding.

Forking, not competition. "Healthy competition" is a contradiction. Real innovation is forking: seeing something with potential, keeping the good, dropping the bad, and going your own way, thinking about the work, not about beating anyone. "I want to do it my way", not "I'm going to beat you". When every studio forks from the best ideas of others, the directions multiply, like multiplicative content at the scale of an industry.

## 12. Handle with care

*Book: c30a-handle-with-care*

Violence. By the book's definition (any use of power over people), the most violent thing in many games is the dark patterns, time gates and manipulation, which reach real people; the explosions don't. Fantasy violence alone is one strategy among many and often healthy (play-fighting is as old as play; the robot game's plasma cannon is a peaceful outlet for real anger). It goes wrong four ways: when the victim is real (griefing, harassment, structures that pay out for another person's misery; consenting friends are fine), when it carries a message about real people (enemies that look like a real nationality, religion, ethnicity or political group rehearse contempt for hours, which leaks into how people talk, vote and treat neighbors; build opponents from behaviors anyone can fall into, such as sins and virtues), when cruelty is the reward (showing horror so it's felt is different from points for tormenting the helpless), and when the line between game and life blurs (constructive fantasy sends people back calmer and more capable; destructive fantasy feeds tension; a recruitment-ad shooter is a tool in disguise). Test: do people leave the game feeling better or worse about the world and the people in it?

Flammable content. Taboo subjects (grief, abuse, suicide, addiction, atrocity) aren't off-limits when they serve the purpose: research, listen to people who lived it, treat it honestly, and tell players up front so they can choose. Never use them as decoration or shock. Provocation for attention is an extrinsic goal with a side effect you can't take back. Offensive and judgemental content is the joke scenario again. But sanitizing what the purpose needs to avoid any complaint is the same mistake from the other side: handle with care, not with fear. Unlicensed material is someone else's work and a time bomb (one takedown erases years); make your own, license properly, or use free licenses with exact credit. Unpopular subjects are fine; just plan resources for a small audience honestly.

Gender equity. Needs have no gender; strategies differ by culture and experience, not by box. "Games for boys" and "games for girls" design for a label instead of the need and shut out everyone who doesn't fit. Offer real range in character creation, don't lock abilities or roles to gender without an honest in-world reason, write characters with needs rather than roles, and don't make anyone's body the bait. In the team: equal pay, credit to whoever did the work, hiring by ability, every voice heard, and no tolerance of harassment, which also matters practically because unheard people take information with them.

Out there be monsters: troll operations, people in pain who want company in it, people who see creators as prey (rights-grabbing contracts, "exposure", key resellers, pay-to-win awards, fake download services), and hate mobs. Know it's coming and isn't a verdict on you, keep trusted people close, protect your inputs, rest, remember the quiet players the game was made for, and reach out for help if it ever gets dark. Read every contract in full and never sign away a dream project because you're tired.

## 13. Putting it together, and what a good game is

*Book: c31-putting-it-all-together, c32-growing-as-a-designer, c33-what-a-good-game-is*

The three walkthroughs apply the whole method:

- From Floppy Heroes (a ten-level ragdoll gladiator game that satisfied and then ran out) to RoomSpace: the mechanic was wonderful, the structure was the problem. The beginner's idea (more gear, more levels) was additive content on a dead end. The purpose became the tactile joy of free-flying physics characters in a world that never runs out of situations, which led to rooms as terrarium-like building blocks with local climates, connected into planets and a universe, biomes from forces, equivalent exchange as a natural law, only the current room fully simulated, and a metagame that's a platform. The first build is the small idea (one character, one room); the framework lets it grow without a rewrite. The same ragdoll base fed several smaller designs with different purposes.
- A project to spread NVC: the need is mostly the need to give. The tempting "fun game that teaches NVC" would be gamification and would make people associate NVC with manipulation. So it's an honest interactive tool: re-create the moment a conflict dissolved, show the needs underneath, practice on the user's own material with the feelings and needs lists at hand, and invite them to try it in real life and note what happened. No points, streaks, praise or nagging. Free, because the purpose is to give. A separate game could let NVC appear only as a side effect of its world.
- The dream game, AAL Bunkerships (on the site, Tactical Arsenal Command): Cortex Command's physics combat, Advance Wars' grid, Forts, FTL's ship systems, XCOM's squads and the mobile fortress fantasy. Feelings revealed friction and the reset as the unmet needs (meaning, continuity, ease, autonomy). Inventory shaped it (one-sprite physics bodies, a Command Core capacity as the in-world limit, emergency floats instead of bottomless pits). Foundations came first (one weapon system, one character system, standardized elements; every ship system a physical module). Content as brands from a neutral arms supplier, all mutually compatible. The wall was red-versus-blue resetting matches; the way through was the service frame (an agency clearing threats from galaxies), progress that never goes backwards, a persistent named fleet, friction moved to peaceful economy regions, abundance from the start, a galaxy artwork memento, and AI commanders styled on the seven deadly sins and virtues amid an ecosystem of wildlife, bandits and independents. The first build is a series of small complete games, each proving one system.

The pattern: start from the inspiration and the feelings on both sides of it; translate them into needs and a purpose; choose the medium and decide honestly between game and tool; take inventory; build foundations and forces before content; make content multiply inside a structure that doesn't have to end, when the purpose calls for it; maximize scope on paper and build the smallest complete version first; carry the purpose into everything around the game; and at every decision, ask whether it serves the purpose.

On growing as a designer: start with something easy, quick and visible in something you love (mods, skins, silly engine experiments), or, with a clear vision, start the dream right away in minimum viable form. Build a library of experiences by playing, watching and observing people with questions in mind; it becomes intuition. A thief takes from one place and changes nothing; an artist takes from a hundred and makes something beyond all of them. Always design from the purpose, never from what's trending; expect new ideas to be met with something like the five stages of grief. Teach the method, not the final result.

A good game is one that fully meets the needs it set out to meet, without violating any others. It knows what it's for, delivers it, does no harm along the way, is honest about what it is, serves the player rather than the creator's ego, and lasts as long as the need does. Graphics, budget, length, genre, popularity, sales and originality aren't on the list; any of them can come as a side effect. A good game is not one that appeals to needs without meeting them, one that's compelling because it's compulsive, one that harms real life (sleep, rent, relationships), or a fantasy that teaches escape from a life then neglected. A good game sends people back to their lives better off than it found them. The method works because it's honest, it works with human nature rather than against it, and it comes from experience. Make a design you'd play yourself, care about the project, care about the people who will play it, and follow the purpose.

---

## 14. Applying this to a showcase page

This section is for writing pages in this repo. The page skeleton and all format rules are in `workflow/page-brief.md`; this is about the thinking that has to show through it. The design file is the authority on what the game is. The bible is how to understand it and argue for it, and how to fill gaps the way Reactorcore would.

Before planning, find the design's purpose the way the book does: what inspired it (often named in the design file: a game Reactorcore liked, an anime, a frustration), what that made Reactorcore feel, which needs that points at, and how the design is a strategy for them. Try the OFNR sentence on it privately. If you can't fill it in from the file, that's the gap to fill thoughtfully, not to skip.

How the page sections carry it:

- **Purpose card.** Name the fundamental human need(s), using the grouped list's vocabulary (Freedom/Power, Growth/Variety, Enjoyment/Play, Meaning/Belonging…), and say which needs the design deliberately avoids violating (rest, respect, autonomy, the player's time). Purpose is not the theme or genre.
- **Target audience.** Describe people by the need they're hungry for and what they're currently sated or frustrated by, not by demographics. No "games for boys/girls" framing.
- **Core concept.** State bluntly how the structure meets the need, and why that's better than the genre default. The genre default is usually one of the failures in section 5 (zero-to-hero, scaling, roguelite resets, a finite scripted campaign) or a padding method from Part A; name which one the design escapes and how.
- **Game layers.** These map directly onto the book. Moment-to-moment is the intrinsically fun core. Low metagame is the finite local goal: a campaign, run or arc with a clear start, progress and end, often generated from modules. High metagame is the infinite overarching goal plus the regular world and the living history: a service frame, a persistent home or overworld that campaigns change, mementos. Practical game flow should show a session that ends at a satisfying exit point the player chooses, with nothing punishing them for stopping.
- **Features & mechanics.** Go deep on the things this bible names, wherever the design has them: foundations and standards, forces instead of handmade results, multiplicative content, heuristics-driven generation, natural limits, balance by real-life logic, abundance from the start, mementos, time that doesn't rewind. Explain the reasoning, not just the feature.
- **Box art copy and the whole presentation** should feel like the game, the way the book's store-page examples do.

Language to avoid on pages, because it sells the opposite of what the designs stand for: "addictive", "hook", "grind", "earn", "unlock", "loot", "rewarding progression", "compete for the top spot", "climb the leaderboard", "daily challenges", "limited-time". Write about needs met, freedom, mastery, discovery, play, meaning.

Scale. Not every design is a universe. The design file decides the scope, and a small, tight design is presented honestly at its own size; don't graft a sprawling simulation onto it. Most of Reactorcore's designs are mechanics-driven, though, so they usually do have (or should get) a high metagame that keeps the game from running out. A design whose purpose is a handmade, curated experience is the exception, and its page should say so plainly rather than pretend to be endless.

Things older design files sometimes contain, and how to present them:

- An "achievements log", "graveyard", "kill tally" or "newspaper of victories" is a memento and living history, not a reward system. Present it that way: it records, celebrates and mourns, and never pays out.
- An end-of-campaign ranking or stats screen is feedback, not judgement. Present it as information and celebration.
- A versus or multiplayer mode: Reactorcore doesn't design around competition, and several design files say so outright. The designs are almost always the player against NPCs or the world (the UNO spinoff, for example, is singleplayer against AI opponents). Present cooperative play, play against AI or the world, and consenting friends sparring as what they are. Never add competitive structures, leaderboards or ranked play a design doesn't have, and don't make a versus mode the selling point. The rare exceptions, like the ETCC tabletop rules, began as a way to make solo play rule-bound, so the dice decide the outcome instead of the player controlling the narrative. Where such a game can be played against another person, put the emphasis on the tactile fun of the combat, not on who wins.
- Real-world groups as villains: per the page brief, turn them into fictional archetypes; the book's own move is opponents built from behaviors anyone can fall into.
- Educational value: if a design has some, it's a side effect of the world working a certain way. Never pitch a game as teaching something.

Before finishing a page, check it the way the book checks a design: does every section serve the game's purpose? Does the page show which need is met and how the structure meets it? Does anything on it (copy, features, framing) quietly promise a reward loop, a grind, a time gate or a competition the design doesn't stand for?

## 15. Misreadings to avoid

The earlier bible, discarded in D9, said many things that sound like Reactorcore and aren't. They tend to come back because they're common industry wisdom, so they're listed here as corrections. None of the following is Reactorcore's position:

- **Educational elements in games.** Games have zero intent of real-life consequence. Learning is only ever a side effect. Educational games and "inspire real-world action" designs are interactive tools in disguise (Part A, section 9).
- **Achievements, praise and "celebrate progress" reward systems.** Achievements are doggy biscuits for obedience; hollow praise is padding. Feedback celebrates and mourns with the player and never rewards (sections 6–7 here; Part A, section 13).
- **Seasonal events, limited-time or rotating availability, paid conveniences.** These are time gating and removed conveniences sold back. Cosmetics are fine only as a thank-you (Part A, sections 12–13).
- **Adaptive difficulty that monitors performance and scales opponents.** Scaling opponents and zones are listed failures. The alternatives are modular campaign parameters, soft limiters with a "pro mode", riskier routes, and balance by real-life logic (sections 5–6).
- **Mandatory rest periods or forced breaks.** Reminders and a clock only; forcing rest violates autonomy (section 1).
- **The ×8 rule as a deadline multiplier**, or extra multipliers for team size and new tech. ×8 is a feasibility check that shrinks the plan (section 9).
- **"Competition drives innovation", or competing as one strategy among others.** Forking replaces competition entirely (section 11), and competitive structures aren't designed around at all (Part A, section 12).
- **Fixing toxicity with fast, consistent moderation and bans.** Toxicity is structural; bans don't touch the cause and make it worse (Part A, section 12).
- **Scarcity as a design tool for meaningful choices.** Scarcity is only ever a natural consequence or a campaign parameter, never a goal; abundance from the start (section 6).
- **Small games as learning projects or portfolio pieces, and "make copies first as training".** Start the dream game in a scaled-down form (section 9). (A small design presented at its own size is a different thing; see section 14.)
- **"Waterfall after planning", "the architect approach", "the lock-down moment", "every project is purpose-built".** None of these exist in Reactorcore's work. The real idea is that everything exists for a reason, plus scope maximization with flexible details.
- **Learning styles** (visual, auditory, kinesthetic learners). A debunked theory and not Reactorcore's.
- **Invented frameworks** such as "the 5-minute rule", kill/pivot/continue checklists, backcasting steps, forest-ecosystem or predator-prey models, chaos percentages and theme odds, user testimonials, and feelings-to-needs translation tables. None of it comes from Reactorcore. The real tools are the NVC feelings and needs lists, OFNR, the purpose test and the complete investigation.
- **"Not every project requires super game treatment" as a design philosophy.** It's a page-writing instruction about honoring each design's scope (section 14), not the book's view, which is that a mechanics-driven game should have a structure that doesn't run out.
