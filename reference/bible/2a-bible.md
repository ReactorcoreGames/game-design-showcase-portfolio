# Reactorcore's Design Bible, Part A: The Mindset

This is the short form of Reactorcore's book *Game Design Technology: The Holy Grail of Fun*. Part A covers the mindset (the book's Parts I–III): the common mistake, purpose, human needs, what fun is, game versus interactive tool, and why good intentions fail. Part B (`2b-bible.md`) covers the technical side (Parts IV–V) and ends with how to apply all of it to a showcase page and a list of misreadings to avoid.

The book is the source. Its text lives in `book/chapters/` and online at `site/book/`. Each section below names the chapters it condenses, by file name (`c08-purpose` is `book/chapters/c08-purpose.html`). Where this bible is too short to settle a question, read the chapter. Where this bible and the book disagree, the book wins.

This version was written from the finished book in session D9. It replaces an earlier bible that was distilled from the unfinished original by another model, which drifted into generic game-design advice and in several places said the opposite of what Reactorcore thinks. Nothing from that version was kept.

Read both parts in full before designing or writing anything. The technical side is useless without the mindset. A tool in the hands of someone who doesn't know what they're building is just a faster way to build the wrong thing.

---

## 1. The common mistake: final result vs root cause

*Book: c01-final-result-vs-root-cause, c02-three-projects-two-designers, c03-how-i-learned-this*

The easiest mistake in game design is to take the initial vision/inspiration/fantasy/idea and build it directly, imitating it as it is, instead of understanding the reasons behind it and letting the right result follow from those reasons. The vision is only a guess, one of infinite possible strategies for meeting the root cause behind it, and possibly a flawed one. Built directly, nothing tells you whether a given decision serves what the vision was for.

The root cause is always fundamental human needs. Video games and interactive tools are just some of the infinitely many strategies for meeting them.

The alien-planet example shows how much it changes. A movie about exploring alien worlds inspires a game. The beginner builds alien worlds and systems that repeat what the movie did. The specialist asks what the movie made them feel and which need was behind it, and the answer reshapes everything:

- Challenge: survive the hazardous planet with skill and limited resources.
- Empowerment: conquer and reshape the planet with godlike power.
- Variety: a planet full of mysteries and random things to find and document.
- Beauty and satisfaction: fly through it, take in vistas, enjoy being there.

Four games about the same planet, and they'd barely resemble each other: genre, style, mechanics, UI, controls, marketing, all different. Without knowing the root cause, you make decisions that conflict with it, and you usually find out only when the game is built and the months or years are spent.

The book contrasts two designers across three situations (a new project, an improved version of an old one, joining someone else's project). The Unaware Beginner copies what seems to work: more guns, more content, multiplayer, leaderboards, open world, leveling, better graphics, because tradition and popularity say so. The Experienced Specialist looks at the inspiration, asks how it makes them feel, translates the feelings into needs, and uses those needs as the purpose that settles every decision. The labels are a convenience inside the book and never a judgement of a person. Never say them to anyone.

The specialist's decision method is always the same: lay every option you can find on the table, get familiar with each one (testing unknowns in the cheapest possible way), compare each with the purpose, and choose the one that serves it best. "I don't know, but I'll find out." Never "I don't know, so I'll ignore it."

Never copy another project's design questions. The questions a project raises arise from its own purpose. Forcing someone else's checklist onto it can damage the design.

For an improved version of an old game, find the original's purpose (ask its creator what they were feeling and needing, or play it and note what each part makes you feel), then keep what serves that purpose and rebuild what doesn't. Upgrading features at face value loses the purpose, which is how sequels lose their soul.

For a partner's project, the six core questions (what are you trying to create, why, what inspired it, how should the result be, what is success, what is failure) each get a follow-up about feelings and needs, and every existing decision gets "Why do you think this will work?" and "How would you achieve that?", down to the color of a character's shoes. People often ask for A while doing B. The designer's job is to hear what they actually need, and to recap it back so message sent = message received.

The interactive-tool version of the same mistake: teaching a subject or raising awareness directly, with no context. The fix is to give the user the reference experience that made you care, show how it makes life more wonderful, and teach inside that context. Your outspiration becomes their inspiration.

## 2. Question everything

*Book: c04-question-everything, c05-popularity-is-a-side-effect*

The common mistake survives because decisions go unquestioned. The traps that lead into it: popularity, profitability, trends, tradition, originality, "someone said so", forecasting and statistics, and mistaking one failure for impossibility. All of these are cognitive biases, and every cognitive bias has the same crux: believing something is true without verifying it yourself. Knowing that one root defeats them all, including the ones nobody has named.

Ask "why?" about everything, as many times as it takes: why is this feature here, what need does it serve, where did the idea come from, why this option and not the others, why is the game structured, marketed and monetized this way, and if it came from another game, why do you think it worked there? "Why" is x-ray vision for a design. It isn't the Holy Grail itself, only the path to it.

Popularity, trends, tradition, profits and statistics are final results, not paths. A feature that made one game popular was developed together with everything else in that game; lifted out of its context it may not work at all ("let's add multiplayer, it's popular"). Popularity is a side effect of a design whose primary focus is value for the player.

"Be original" is destructive advice. Originality is a side effect of making something genuine for a real purpose. Creativity is remix: taking existing things and combining them in a new way, in service of a purpose nobody else had in quite the same way. You can never know what the final result looks like until you get there, and the chaos in the middle of a project is normal, not a sign of failure.

Games can change the world just by existing, because they change people's mindset whether that was intended or not. That's why skipping verification costs far more than the time a shortcut saves.

## 3. Extrinsic goals

*Book: c06-making-games-for-the-wrong-reason*

Making a game PRIMARILY for an extrinsic reason (money, fame, being heard, changing the world, teaching, acceptance) is doomed, because an intrinsically good game and an extrinsic goal pull in opposite directions, and the extrinsic goal needs the good game to happen at all. As a secondary or tertiary priority, extrinsic goals are fine.

The six effects of an extrinsic goal as the primary focus (after Alfie Kohn's *Punished by Rewards*, read "rewards" as "extrinsic goals" and "students" as "developers"): it doesn't motivate you to make a good game, only to get the goal; it clouds your interest in the reasons behind things; it discourages risk-taking and so creativity; it undermines interest in the game; it's addictive, leaving you empty after each win; and it creates pressure, because you're trying to make the result be the path.

The fix is not to let go of the need. Acknowledge the need behind the extrinsic goal and that it matters, acknowledge it can't be reached as the primary priority, stop going for it directly without smothering it, set it aside and make something worth making for its own sake, then bring it back as SECONDARY, pursued only in ways that don't compromise the game or violate the player's needs. From the outside it looks like the goal arrived as a side effect. That's the intended route. Fear and urgency are when people slip back, so watch for rushing.

## 4. The Holy Grail

*Book: c07-the-holy-grail*

The best way to make a game design has four parts:

- Understanding of technology: the platforms and tools, their capabilities and limits.
- Understanding of human beings: how a human thinks, behaves and works.
- A clear purpose for the project: why make it at all?
- Plus business needs: the time, money, people, skills, hardware and support that can concretely go into it, and surviving it without burnout or bankruptcy.

The first three are about making the best game. The fourth pulls against them, but without it the game never becomes real, so it's treated as another need to satisfy.

A perfect design satisfies all four: the technology kept within its operating limits, the player respected morally and given a convenient interface, a purpose rooted in fundamental human needs that meets them without violating others, and logistics and business planned so the project can afford its size. Game design is finding the combination that meets the needs of every party at once: the player, the platform, the purpose, the people building it and the business that keeps them alive.

There's a mindset side (how to think and decide) and a technical side (methods and tools). The technical side is useless without the mindset.

## 5. Purpose

*Book: c08-purpose*

Purpose is the most important thing in any project. Everything that happens, happens for a reason. Everything that exists in the project exists for a reason, and in a certain way for a reason. Every decision has a clear, verifiable reason behind it.

Purpose is not a fantasy, a theme, a style or an idea. Those are ways of fulfilling a purpose. The purpose answers the blunter question: why did you want to make this game in the first place? In the book's terms, the purpose is the needs the project exists to meet.

Without purpose, every decision is a guess. A game is thousands of decisions, and the small pulls away from what it was meant to give add up and hide inside each other: a bad camera makes the controls feel worse, which makes the difficulty feel unfair, which prompts an easy mode, which makes the challenge meaningless. Nobody sees the tangle until people play the finished game and leave.

Purpose is also the source of motivation. A project that started exciting and became a chore has usually drifted from its purpose; the motivation noticed the drift first. The fix is to go back to the purpose and cut or change what doesn't serve it.

In a team, purpose is what lets everyone make the same game. Without it, the artist, programmer, writer and marketer each build for their own guess, and disagreements become contests of opinion. With it, "I like A, you like B" becomes "which serves the purpose better?", which can be tested.

## 6. Understanding human beings

*Book: c09-understanding-human-beings, b1-needs-at-a-glance*

Nonviolent Communication (NVC), Marshall B. Rosenberg's work, is the most compact, reliable way to understand people. At its simplest: connect with what's alive in you (clarity), understand what's alive in the other party (empathy), and a path to a solution that works for everyone becomes visible.

### Fundamental human needs

At NVC's center are fundamental (universal) human needs, also described by the economist Manfred Max-Neef, whose matrix lists games among the things that meet the need for leisure, next to friendships and shelter. Reactorcore's grouped list, with several words each because English has no accurate single word:

- Subsistence (food, water, air, warmth, health, rest, sex, exercise, basic survival)
- Safety/Protection/Peace/Order/Harmony/Reliability/Predictability
- Freedom/Power/Participation/Access/Choice
- Growth/Learning/Advancement/Creation/Variety/Understanding
- Enjoyment/Leisure/Play/Beauty/Silliness/Movement/Whim/Excitement
- Meaning/Identity/Belonging/Self-worth/Celebration/Mourning/Purpose
- Equality/Respect/Acceptance/Empathy
- Love/Giving/Receiving/Affection/Care/Socializing/Connection/Touch

Needs are not a pyramid. Maslow's hierarchy is outdated. Needs work like the independent need bars of a sim in The Sims: each rises and falls on its own, and they don't wait in line. A player arrives with some bars full and some empty, and a game fills some and drains others. A game can fill challenge beautifully while draining rest so hard the player quits. Watch all the bars, not just the one the game is about.

William Glasser's Choice Theory reaches the same conclusion (all behavior is the best current attempt to meet needs) and ties the need for fun directly to learning.

### Feelings point to needs

Feelings are the dashboard of needs: pleasant when a need is met (relieved, joyful, calm, excited, grateful, empowered, awed, free), unpleasant when it isn't (frustrated, bored, anxious, lonely, angry, exhausted, disgusted). No feeling is "negative" in the sense of bad. Anger at an unfair game points exactly at the need it violated. Asking "how does it make me feel?" isn't sentimentality, it's measurement. For other people's needs, ask, listen and observe. The CNVC needs and feelings inventories (cnvc.org) are the working vocabulary.

### NVC for game design

- Everyone has the same needs, so you can design for strangers. Strategies differ, needs don't. Two players arguing about difficulty want the same need met in different ways.
- Needs contain no specific actions by specific people. "I need the developer to add a sniper rifle" is a strategy; the need might be power, variety or the satisfaction of a skillful shot.
- There are unlimited ways to meet a need, so you're never stuck with one idea.
- Everyone's needs can be met without sacrificing anyone. A compromise means everyone loses a little. A design that only works by hurting someone isn't finished.
- Every game, mechanic, feature and menu is a strategy, and strategies are smart (meets needs, no drawbacks), dumb (fails and makes things worse), useless (does nothing) or flawed (meets one need and breaks another). Most bad game design is flawed, which is why it's hard to spot: a loot box meets a need for surprise and drains fairness, safety and trust. Look for the need a strategy breaks, not only the one it meets.
- Everything anyone does is an attempt to meet a need, including cheating, griefing and quitting.
- People are shaped by their environment, and a game is an environment. Whatever it makes easy, cheap and pleasant, players do more of. This is the designer's most powerful tool and the most dangerous.
- People can always change, and always have a choice. Players are never "just like that"; they respond to what's around them.
- The root of human thought is two questions: what is alive in us, and how can we make life more wonderful? The first finds the need, the second the strategy. That's the design process in miniature.
- Retributive justice doesn't work; restorative justice and the protective use of force do. A ban that exists to make a cheater suffer is punitive. A system that stops cheating from ruining other players' matches is protective.
- People only ever say "please" and "thank you". Every complaint is a "please" in disguise.
- The purpose of life is to make life more wonderful, and a game's purpose is the same in its own corner.

### Rewards and punishments are one coin

A reward and a punishment are the same tool pointed two ways: do what I want and I'll make you feel good, don't and I'll make you feel bad. Both attach a consequence unrelated to the activity itself, which makes them power over people, and violence in NVC's broad sense (any use of force, including guilt, shame, duty and obligation).

Rosenberg's two questions expose them: what do I want this person to do, and what do I want their reasons to be for doing it? Nobody wants a player to explore because a checklist pays them, or to stay in a match because leaving costs rating points. Once a reward is attached, the reason moves from the activity to the reward, the activity becomes work, the reward has to keep growing, and when it stops so does the behavior, often with resentment. Punishment does the same from the other side. The alternative is to make the thing itself worth doing.

### Power over and power with

Power over people is force: punishment and reward, guilt, shame, pressure, threats, manipulation, tricks, and any system that blocks equal access to resources and justice. It works short-term and breeds resentment. Power with people is getting things done together by meeting everyone's needs. A designer has enormous power over players (what's possible, easy, hard, rewarded, punished, how long things take and cost). A game designed with power over players is full of timers, penalties, nagging, artificial scarcity and carrots on sticks. A game designed with power with players gives them what they came for and trusts them to come back. The same choice applies to teams, partners and customers.

### Self-fullness

"Selfish" and "selfless" are both false and often used to manipulate. What people actually do is meet their own needs, ideally with the least harm and most benefit. Helping others meets our own need to contribute. Because needs are universal, a need a game meets in its creator is a need other people have too, so making the game for yourself, honestly and completely, is the most reliable way to make it for them. And sharing a need gives others the chance to give, which is why a player is happy to pay for a game they love.

## 7. Fun is the fulfillment of needs

*Book: c10-fun-is-the-fulfillment-of-needs*

Fun is the satisfaction of fundamental human needs. A game that meets a need feels fun; one that meets several strongly feels amazing; one that fails to meet them is boring; one that violates them is frustrating, insulting or exhausting. "Is this fun?" becomes "which needs does this meet, and does it violate any others?", which can be checked against your own feelings and the players'. "Will people like it?" becomes "do people have this need, and is this a better way to meet it than what they already have?"

Games meet needs by offering something that is otherwise unavailable, too expensive, too distant, too difficult, too dangerous or too consequential in real life. Flying at Mach 20 with a plasma cannon is all of those; the need behind it (power, freedom, excitement) is completely real. Someone who feels powerless at work can feel capable for an hour and go back steadier. That's a need met, not escapism.

The designer is an architect of the future. Millions of people spend hours in environments designers built. What those environments make easy, people do more of; what they reward, people learn to want; what they make normal, people come to expect. Games aren't inherently entertainment. Entertainment is one result a game can end up being, never the starting point.

Some needs pull in opposite directions. Excitement and relaxation can't be met by one strategy. A game that's both calming farm life and tense survival horror ends up neither. Choose the bundle of needs that belong together, and serve it completely.

Every piece serves the purpose: mechanics, interface, menus, text, characters, story, audiovisuals, marketing, publishing, community. A menu in an empowerment game can feel like a cockpit powering up; the same menu in a companionship game can feel like opening a letter. Same function, different purpose, different design.

Six ways games fail to satisfy needs, all from not knowing what the game is for: trying to serve every need at once and satisfying none; pulling in two opposite directions; copying traditions without knowing why they worked; getting lucky with a prototype and ruining it without knowing why it worked; not caring about the player and making the game for the creator's own validation; and actively exploiting the player. The last two lean on impressive audiovisuals to hide how hollow they are underneath.

## 8. From inspiration to purpose

*Book: c11-from-inspiration-to-purpose*

Purpose arises from needs, either an unmet need calling to be met or a met need calling to be celebrated. Inspiration is a stimulus that draws attention to a need and a possible strategy for it. Every project ever made is a strategy to meet or celebrate needs.

A purpose can't be pulled out of nowhere; something has to stir a need. So explore the world in every context. What looks like procrastination is often the mind filling its library of references.

Three layers are always present: the basic need (too deep to make concepts from directly), the inspiration (an event that touched the need, often by showing it unmet: "this must never happen", "I wish I had that", "there must be a better way", "I'm bored"), and the dream (a strategy to meet the need, where game ideas live). A dream starts vague and matures, and maturing it includes checking whether it's a good idea at all.

The five steps: an event stirs a need; the event brings inspiration, a willingness to meet it; the inspiration asks for a strategy, which is your vision, only one of infinite ways and never guaranteed; identify the need (possibly several, but connected ones, or the project isn't focused); and the purpose is to satisfy exactly those needs, with the vision as the method.

The OFNR sentence (Observation, Feeling, Need, Request) tests an idea: "[This event] brought out an inspiration in me, which made me feel [these feelings] because I'm needing [these needs], and I think [my game idea] is a good strategy that might fulfill that need." If it reads strangely ("...because I'm needing rest, and I think a hardcore competitive shooter is a good strategy..."), you've found a problem before building anything. The NVC lists catch misread needs: "bored" can be "lonely", "I want more guns" can be "I want to feel capable".

The formula: **Unmet needs + Strategy to meet those needs = Purpose of the project.**

Because the motivation lives in the need and not in the first idea, a bad strategy can be replaced without losing motivation.

Choose the right medium. A game is media plus interactivity, for a fantasy that's impossible, improbable or less efficient in any other form. If the purpose is better served by a film, a book, an app, a real-life activity or an organization, don't force a game out of it. The purpose dictates the medium, never the reverse.

Good design takes time. The purpose doesn't hand you answers; it hands you a way of checking answers.

## 9. Game or interactive tool

*Book: c12-game-or-interactive-tool*

A project is either a game or an interactive tool, never in between. Anything in between triggers a natural defense, violates a need, and kills the project.

- A game has no intent, none, zero, of real-life consequences. Fantasy, play, freedom to fail. It may cause real-life effects as a side effect, but the intent is never there.
- An interactive tool intends real-life consequences and is honest about it. Failure is not desirable. "Tool" isn't a lesser word; an honest tool can be as compelling as a game because it visibly makes your life better.

Games are effective because they're non-consequential (a safe space to experiment, enter and leave, without real-life judgement) and honest about it (the need for authenticity isn't violated). Take away either and the effectiveness is gone. A game with real stakes isn't safe to fail in; a game that hides real stakes is a lie, and lies get found out.

So "educational games", gamification and edutainment fail. Gamification is masking an interactive tool as a game, and it's manipulation. Its chain: points and streaks get bolted on and usage rises (the reported "success"); the reason moves from the task to the points; novelty wears off and pressure must rise; the manipulation becomes apparent and feels like betrayal; the person leaves and now associates the task itself with being manipulated, so they're less willing than before.

The side-effect influence is allowed and powerful, but only as a side effect, found after the game's foundation is designed, never as a goal. A space game whose ships obey orbital mechanics teaches orbital mechanics because that's how you get anywhere. A world where cooperation is the most effective way to survive gives practice at cooperation without a lecture. The moment any intent to change real life enters the design, it turns into a tool in disguise.

> If you want to make a game, make a game.
>
> If you want to make an interactive tool for a real-life issue, make an interactive tool.
>
> Be honest, don't fake it, keep it real.

Learning doesn't need to be made fun; it already is when it meets needs (people learn complex game systems for hundreds of hours unasked). It stops being fun when it's cut off from the needs it serves, and when it's forced. An honest learning tool starts with the reference experience, shows concretely how the knowledge makes life more wonderful, teaches inside that context, lets the user use it on something real, lets them fail freely, and has no points, grades, streaks or shame: the progress bar is their own growing ability.

The human need to give is a need in its own right. Most awareness efforts use guilt, shame and duty, which is power over people. People want to contribute; what stops them is not knowing, not feeling why it matters, not seeing a way to help, or never seeing whether their help worked. An honest awareness tool re-creates the inspiration as an experience, shows the need behind it, offers a concrete doable request, and shows the effect of the contribution. The same need explains honest monetization: paying for a game you love is saying thank you. Give real value first and make it easy to say thank you; trap and pressure people and their thank-you becomes a toll they resent.

## 10. Purpose as a compass

*Book: c13-purpose-as-a-compass*

The purpose test, at every decision, of any size, anywhere in the project (UI, art, marketing, mechanics, sound, updates, story, the smallest details): "Does this fulfill the purpose?" or "Does this bring the project closer to fulfilling the purpose?" Yes: do it. No: change it, remove it or don't do it. I don't know: find out.

The test has a second half: does this violate any other need? A game is about one need or a bundle; it can't meet every need, and that's fine, but it must never violate the others. A challenge game can meet challenge brilliantly and still violate respect (wasted time), autonomy (one way to play), safety (threatened progress) or rest (punished for stopping). Players don't experience those as separate problems. They experience one game that's somehow exhausting, and leave without saying why.

The robot game example shows the speed of it. Its purpose is freedom, power, challenge, variety and play, with momentum and flow. A fuel system forcing you back to base every ten minutes: no. Boosting to extreme speeds: yes, and now the camera and level scale must support it. A long cutscene before each mission: no, tell the story in motion. Unpredictable enemy tactics: yes. Levels unlocking one by one: no, let the player choose. Five decisions in seconds, none by asking what other games do.

A bad idea is cheapest to kill at the moment it appears: a crossed-out line on paper, days in a prototype, months after release, and forever if it's never caught. Test every idea, especially the ones you love. A loved idea that doesn't serve the purpose may belong to another project; write it down for that one.

Some people aren't interested in your game because they're sated by other means: the need is met elsewhere, more cheaply or more powerfully, or their bar for it is full right now. Don't chase everyone by adding a bit of everything. The best strategy in the world for one bundle of needs finds its people.

Meaning comes differently from handmade and procedural campaigns. In a handmade campaign the player follows an author's trail to see what gift they'll be given (a spectacle, a message, a thrill, a fair challenge, sometimes bitter medicine); the player is closer to a guest. In a procedural campaign meaning comes from remarkable moments during play that become the player's own story: doing something cool, overcoming something uncertain, discovering something yourself, laughing at the absurd, expressing yourself, experimenting freely. Both are valid tools; the purpose decides which. What fails is choosing one out of habit.

Keep the original inspiration in the project. The context that made you start is the context players need to care. If the robot game came from watching that anime with drum and bass in your ears, the first minute should feel like that, not a menu, a tutorial and a text crawl.

Where good games come from: the creators of Pokémon (childhood insect collecting), The Legend of Zelda (exploring countryside and caves) and Minecraft (building freely in a living world) started from a need, not a genre or a market gap; gave the inspiration to the player as an experience; and played their own game. Many of them worked by intuition, which works but can't be reliably repeated, protected or explained to a team. That's why a sequel can miss everything the first game got right once its creator leaves. The mindset makes the intuition visible.

## 11. Intention is not action

*Book: p3-intention-is-not-action, c14-intention-and-action*

Intention and action are separate things. Players never experience your intention, only your action: the design you actually built. From the player's side, the design is what you meant. A developer who intends a friendly community and builds a game where you win by making someone lose has built a game about making people lose.

The mistake mostly comes from not knowing about needs and feelings, which is what lets a designer predict whether a design will violate them. It also comes from false information in society and the industry, and from skilled designers making design look easy.

The four stages of learning: unconscious incompetence ("nothing can stop me"), conscious incompetence ("I need guidance"), conscious competence, unconscious competence. Confusing intention and action belongs to the first. Skip it by assuming you know nothing about any new subject and studying it before attempting anything serious.

The complete investigation, before building: gather information, organize it, look at each decision however small, reduce it to what it does and relies on, list every effect you can deduce, on the mechanics and on players' needs (which needs does it meet, which could it violate, what will a tired, broke, angry, ten-year-old or desperate-to-win player do with it?), test whatever you're unsure of (mind maps, experiments, earlier games, cheap prototypes, spreadsheets, asking people), and repeat until the design is foolproof. It costs hours or days; skipping it can cost years.

Murphy's law is arithmetic at scale: a design that goes wrong for one player in a thousand goes wrong a hundred times among a hundred thousand players. Good design is paranoid design, in the sense of having already looked at every way it can break and closed those ways.

## 12. What the scenarios teach

*Book: c15-when-players-misbehave, c16-good-intentions-violent-methods, c17-money, c18-afraid-the-game-is-too-short, c19-more-ways-good-intentions-fail*

The book's twelve scenarios are all well-meaning developers whose design said the opposite of what they meant. The developers aren't villains; they're who most of us are at some point. The lessons:

**Toxic players (competition).** A PvP game makes victory artificially scarce: winning requires everyone else to lose. Hostility, tilting and mind games are among the most effective strategies for winning against humans, so the structure rewards them and therefore teaches them. The developer's real intentions (growth, challenge, respect, connection) need nobody to lose; the competition was a bundled extra that poisoned the rest. Report buttons and bans don't touch the cause and punish people for what the game rewards. Competitive games run a lifecycle of honeymoon, mastery, cheating, elitism, failed rescue attempts and abandonment, while good singleplayer and cooperative games stay timeless with wholesome communities. A competitive core generates drama, rewards hurting others, limits innovation to whatever passes balance, diverts engineers to anti-cheat, turns modding into a taboo, and makes most players lose most of the time. Reactorcore's position is total: don't design around competition. Every need it claims to serve (challenge, mastery, excitement, social play) can be served without it. Friends who agree to play-fight are fine; that's consent. A structure that pays out for other people's misery isn't. (Alfie Kohn, *No Contest*.)

**Cheating.** Cheating originates in the design, not the player. Artificial limits (classes that lock content, unlock grinds, "not appropriate at this stage", RNG gates, inflatable artificial economies, admin tools kept out of reach) and the controlling mindset behind them ("the player must earn it", "there's only one way to play", "I'll punish them to teach them") violate autonomy, freedom and power, and cheating is a creative strategy to take them back. The same act is a beloved feature in a singleplayer sandbox (console commands, speedrun glitches, mods). To guide without restricting: shape through the environment rather than locks, use the world's own natural laws as limits, guide with information, use soft limiters with an off switch, and make everything available and let the player choose. A hand that offers instead of one that grips.

**Making education fun.** Gamification, cute characters as a manipulative bonding tactic, rewards and grades, and moralizing and shaming produce a short-term bump, then collapse, and leave people disliking the subject more, because the subject is now tied to the memory of being manipulated. Intention doesn't validate an action taken without awareness. The honest routes are in section 9.

**A joke that caused a backlash.** Humor always needs a victim. A joke or reference built on a judgement or label of people, or of what matters to people, threatens their need for safety, and the backlash (boycotts, refunds, lost goodwill, and in the worst cases harassment) is a foreseeable consequence. Choose humor whose target can't mind (absurd situations, physics going wrong, systems colliding), and check who pays for each laugh before it ships.

**Money.** A developer sells vanity items, meant for wealthy players, with ordinary manipulative advertising (dark patterns: artificial scarcity, bait and switch, hidden costs, easy to join and hard to leave, preventing comparison, and endless others). Poor players, children and depressed players get hooked; an ad doesn't check your bank balance before it reaches your feelings, and manipulation hits hardest the stressed and the poor it was meant to spare. Metrics look like success while "timebombs" build: unpaid bills, a child's shock bill and the family fallout, a depressed player soothed into dependence, a player who can't let go of sunk time and poisons the community. Numbers can't show any of it. Cosmetics aren't the problem; the marketing is. Sell cosmetics as a thank-you, never as status that splits the community into payers and non-payers, and keep the game complete and abundant for everyone. The test isn't cosmetic versus functional; it's whether the player pays to say thank you or because the game pressures them.

**Afraid the game is too short.** Fear makes developers pad a game, adding time without adding need satisfaction. The full catalogue is in section 13. The mistake is fixing a problem of value with a strategy of length. The real answers are structural: an honest short game priced honestly, content that multiplies, a structure that doesn't end, or foundations that fix the effort-to-result ratio.

**The trailer vs the game.** The fantasy shown was a role ("be a fighter pilot"); the game delivered a finite scripted campaign of the developer's flights, finished and forgotten in weeks. A scripted campaign is the right tool for a curated message and the wrong one for a role people want to live in again and again. Build the forces that produce such situations, in a structure that never ends, and the game delivers the trailer every time.

**The sequel that failed its fans.** Upgrading the original's visible features without knowing its purpose removes the reason people loved it. Vague fan comments ("soulless", "off", "forgot what made it great") all say the sequel aims at different needs. Find the original's purpose first and make every sequel decision by it.

**User acquisition keeps failing.** Interrupting ads, contests, referral rewards and broad generic targeting bring people for the prize, annoy everyone else, and make the game look like every other game. Marketing is part of the game's design and should serve the same purpose. Find the people who have the need, show the inspiration honestly, make the presentation feel like the game, give easy ways to try it, and let genuine word of mouth do the rest. Clarity of value.

**Adapting another medium.** A board game's dice, cards and phases and a film's fixed cameras are solutions to those media's limits, not the source of their magic. Copied one-to-one, they become arbitrary constraints that keep the old medium's costs and waste the new one's strengths. Find the feelings and needs the original met and design natively for the new medium. Sometimes the honest answer is to make the original available again.

**Retention is always too low.** Retention is a side effect: people stay as long as the game keeps meeting their needs. Dailies, streaks, events and battle passes bolted onto a finite campaign are padding and punishment; they trade trust for short-term numbers, like adding locks to a building scheduled for demolition. Games that keep players never run out of reasons to play: an infinite overarching goal, finite local goals, content that multiplies, a world that keeps going.

**Customers angry about business decisions.** Raising prices while cutting content into DLC, cash shops, season passes, paid conveniences and time-limited availability are manipulative by nature even when the company isn't, and a press release saying "more choice" widens the gap between statement and action. Translated with NVC, the angry comments are requests for fairness, honesty, consideration and consistency. The better strategy is an honest request: what we need, why, what we'll give, and what we ask, after giving real value first.

Five more sketched for practice: "make it fun!" with gimmicks everywhere (fun is needs met, not cleverness shown); a fitness or study app dressed as a game; taboo subjects handled carelessly as "only fantasy"; a story nobody needed, added to an experience that needed no narrative; and a design that only works if every player behaves sensibly.

## 13. The padding catalogue

*Book: c18-afraid-the-game-is-too-short, b3-the-padding-checklist*

Almost none of these techniques are destructive by nature. What makes something padding is the reason it was added: to make the game seem longer or more valuable than it is, out of fear. For anything that looks like padding, ask: would this be here if I weren't afraid the game is too short, shallow or not worth its price? And does it serve the purpose?

| Method | What it looks like | Not padding when |
|---|---|---|
| Filler content | arbitrary collectables, fetch quests, timed trials, side stories or systems that exist to give "something to do" | it serves the purpose of the game |
| Artificial difficulty | scarce saves, punishing precision, luck over skill, trial and error, hidden information, blocked views, lying to the player | the difficulty is what the game is for, and it's upfront about it |
| Arbitrary unlocks and progression | modes, characters, items, story or mechanics held back until enough time is put in | never as a time-stretcher; access can follow believable in-world logic |
| Blatant recycling | the same item, area or dungeon under a new name, color or numbers (Borderlands 2's millions of reskinned guns, Skyrim's identical dungeons) | parts are reused cleverly to make more variety cheaply |
| Tacked-on features | side activities, hunger meters that slow everything, minigames, extra modes, companion apps | the purpose called for the feature from the start |
| Time gating | real-life waiting, daily play limits, time-of-day content, event exclusives, rotating shops, streaks you lose by missing a day | never; the player decides when and how long to play |
| Arbitrary content splitting | near-identical parallel versions, content cut to sell back as DLC | an expansion is new work, fairly paid for |
| Hidden delays | long animations, fake loading, slow menus, unskippable scenes, crawling text, hold-to-confirm, a 0.9 timescale | every pause has a reason the player would agree with |
| Rewards for staying | real-life incentives, contests, achievements ("doggy biscuits for obedience"), idle rewards, non-stacking periodic bundles, bonus overload, celebration effects for trivial actions, hollow praise ("Good job!", "You're awesome!") | never; feedback and gratitude aren't rewards |
| Punishments for leaving | disapproval of short sessions, denied bonuses, missed bundles, one-off real-life events, labelling the player, threats to erase all progress, unbanked progress lost if you stop now | never; a punishing experience is honest only when chosen knowingly |
| Forced failure through randomness | misses beyond the shown odds, crafting that destroys materials, tiny drop rates, random downgrades | randomness creates variety and choices still decide the outcome |
| Splitting across playthroughs | classes, "choices" or endings that force a full replay for a few new scenes | the choice really changes the experience |
| Dailies and offline progress | expiring quests, capped resources waiting for collection, "something is ready" notifications | never; the game waits for the player |
| Drip-feeding | slow walking, empty roads, huge empty maps, one coin per pot | the distance is the experience, and it's full |
| Removed conveniences | no fast travel, no quick-save, tiny inventory, no bulk actions, and above all any of these sold back | the purpose is about travel, survival or planning |
| Difficulty as padding | "beat it on hard for the real ending", items that only exist at higher settings, settings that only add enemy health | limits for new players plus a "pro mode: no limits" for experts |

Time gating deserves its weight: it makes the game more important than real life. With it, the game controls the player; without it, the player controls the game. The harm is concrete: missed obligations, accidents when attention was needed elsewhere, neglected eating, drinking, rest and family, broken sleep.

Masochism is different. Some players choose brutally hard or unforgiving games and genuinely enjoy them; that's a real strategy for challenge and relief. The difference is consent and honesty. A game whose purpose is a punishing experience should say so plainly.

Fear is a bad motivator because it rushes people to the most convenient fix. Padding adds time without meeting needs, and drains respect, freedom, rest and trust along the way. Players want more needs met, not more time spent. An honest short game is respected; a short game disguised as a long one is resented.

Continue with `2b-bible.md`.
