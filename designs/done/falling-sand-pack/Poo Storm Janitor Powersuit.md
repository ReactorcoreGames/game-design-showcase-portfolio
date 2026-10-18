# Falling sand game variants
(I'm making a series of games that fall under the same category of leveraging falling sand game mechanics (cellular automata with physics) in some way and originally I wrote a big mega document with all the ideas in it, then later split them into individual small documents to keep the prompt focused. The stuff after the Game Ideas is the actual game idea I want you to focus on, while the below two paragraphs are merely an intro that is free to be overwritten/disregarded in favor of the actual game idea that takes all priority.)

The idea is to have very simple, short and satisfying game experiences that primarily incorporate falling sand mechanics in some way. By falling sand, I dont exclusively mean sand only, but the general game engine of falling sand games like Powder Toy or similar pixel simulation sandboxes. The range of materials/phenomenom are always limited to the scope of the particular game at hand, so while some games may feature things like fire, sand, water, grass, snow, ice, wood, stone, flammable gas, etc. it always depends on a per-game basis what they'll ultimately have, both to keep them focused and simpler to make.

While falling sand mechanics are at the forefront, the game can feature other 2D game elements and colliders that work in tandem with the falling sand. Also unlike most falling sand games which are merely open sandbox experiences without any structure or metagame, the games I want to make aim to have enough game design embedded into them so they're atleast on the same level as a typical kongregate web game or a newgrounds flash game, in terms of gameplay, small scope and cohesiveness as a proper game experience, even if its simple/basic.

That said, I aim to mainly release them on desktop platforms (PC, Linux, Mac), maybe web too if its possible to make it performant enough for it to work there. But Windows PC is always priority one as the release platform.


## Game Ideas

### Poo Storm Janitor Powersuit
(tongue in cheek 2D platformer with single screen stages to suck up falling-sand pixels to collect them and deposit them into pots that will grow into plants once watered. Does it make sense? no. Is it funny? yes.)

An office building has suffered a massive shitstorm - literally! - and they have no greenery in there either, oh the humanity, its unbreatable! No mortal is able to enter the premises to clean it up, so a janitor has to don a heavy-duty hermetically sealed power armor suit with an industrial vacuum cleaner and a watering hose to save the day.

Stages are a cutaway of a multi-floor office building with pixels of brown sand, light brown liquid, and hardered dark brown solids. There are plant pots, standing office fans (implying that someone threw shit in the fan), office chairs and water coolers.

Its built like a vertical platfomer stage so player is able to jump up some platforms to reach high floors and drop down to lower floors.

Player must:
- Vacuum the sand poo, mop up the liquid poo, powerfist punch (causes a circle AoE blast that affects multiple pixels at once) the solid poo to turn it into sand poo, pick up and place the fallen water tanks back onto water coolers and spray water at them to refill them, deposit/distribute poo into the flower pots evenly (the correct amount happens automatically, player doesnt have to worry about details, its enough they collect all the poo and press E at every pot to reduce the collected storage of total poop into the pots), then spray water at the pots filled with poo to make a verdant green plant appear out of it, wash and turn all the shittified fans back on.
- Player can see a checklist of things that are unfinished/done. The offices are mostly white/light grey, so poo and various objects are highly visible/contrast against the solid walls and background.

All poo types are falling-sand. Walls are static colliders. Water tanks, water coolers, fans, flower pots, plants are sprite objects that player interacts with either pressing E on them or by spraying water at them when that tool is selected. Sprite objects are rendered between the office background and player sprite. Sprite objects are not solid, player can walk past them, same with falling sand stuff.

#### Controls:
AD - move left/right
W - jump and double jump
S - drop down (if were having one-way platforms, otherwise this does nothing)
E - interact with water tanks, water coolers, cleaned fans, pots and level exit (when it opens after all tasks are done)
Mouse 1 - use currently selected tool
Mouse 2 - cycle to select next tool (powerfist, vacuum, mop, waterhose)

Its a fast paced game, but doesnt enforce it. Player can enjoy cleaning up the stages at their own pace. After completing a stage a celebrational image appears with a random quote of wisdom that would be helpful for a person that wants to avoid them from having the shit hit the fan, metaphorically speaking, promoting patience.

Metagame wise player has a log with all the office buildings they cleaned up with a goofy randomly generated name for a company and stamp saying "Cleaned!"

#### Poo monster idea
One idea is to have each building have a poo monster that sprays different poo types as it walks about (sand, liquid, solid), so player's first priority is to have an epic yet simple powerfist fight against it by getting close to it to smack it with the powerfist a total amount of 4-8 times or by spraying water at it with a rate of 30-60 seconds total of spraying to defeat it, assuming full health. Or player can use a mix of those attacks. Poo monster has randomly 100-200hp, so each punch would deal 25dmg, and a single water spray shot would do 1dmg at the whatever rate of fire that adds up to. Player has 20 hp, so poo monster can either punch them for 3 dmg or throw a poo projectile at the for 1 dmg. When the poo monster is reduced to 0hp or lower, it will gloriously explode into a big blast of poo sand and poo liquid. Generally the poo monster's AI has it run around the office, disregarding the player, causing as much of a mess as it can, only attacking player if player has hit it in the last 5 seconds or if they about 2 meters away from the player. Their attacks have a 2 second delay to show they're about to do an attack, so player can use that warning to try to dodge the attack.

Thus each stage works in two phases: fight the poo monster first, then clean up the mess. Lorewise someone caused a (metaphoric) shitstorm so bad it manifested into a physical malevolent poo monsters who's first instinct is to throw actual poop into random fans to signify to everyone that indeed, shit has hit the fan(s), both literally and figuratively.

#### Revised Metagame V2
Actually, lets make it so that player can choose if they want to have a relaxing campaign session or an action campaign session or a mixed session.
- relaxing = 9 stages, no poo monster phase. Just clean up a mess.
- action = 9 stages, always start with a poo monster. Defeat the poo monster, then focus on cleaning up the mess.
- mixed = 9 stages, but its random if a poo monster is there or not.

In each stage, places are already just covered in poo to random varying degree each stage. The level of dirtyness can be minimal, maximal or something in between. Its also random the ratio between sand, solid, and liquid poo present on the level. The amount of fans, pots, water coolers+tanks is also random between 0-9 of each per stage.

Those randomly generated 9 stage campaigns are considered the "low metagame". "High metagame" generates those campaigns and its context lorewise is about running an office washing company with a speciality to deal with "absolute shitstorms". The tone of the game is intentionally humorous and absurd.

As mentioned before, each completed low metagame campaign has a log with all the office buildings they cleaned up. Each building has its own satirical corporate-sounding branch name that people on r/linkedinlunatics on reddit would get a good laugh about. Each building would also get the stamp saying "Cleaned!" and for each cleaned poo pixel player would receive profits of 10 dollars, for each interactable sprite object, player would also receive 100 dollars too. The earned dollar value is mainly a cosmetic, as a way to determine afterwards how dirty a level was.
Meanwhile, each building is grouped under a randomly generated corporate company name that also would be funny to r/linkedinlunatics users on reddit.

Each campaign is generated with a seed so player can look at a log and go replay old level exactly like they were, with a subtle sepia overlay to indicate they're playing a flashback. Doing so will improve the completion time in the records, reducing the overall completion time per company.