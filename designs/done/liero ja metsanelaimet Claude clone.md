# Liero clone made with Claude
Game's title should be "Metsanelaimet" inspired by the text seen when the old MS-DOS game Liero boots up, saying "Liero ja metsanelaimet" (I know its missing the ä, its purposefully mispelled due to MS-DOS unable to handle the ä character.)

The game itself is strongly inspired by the old game Liero, which was a 2D shooting/digging game where two or more worms blow each other up with a variety of wacky guns in real-time action within stages with mostly destructible terrain.

While Liero was more intended as a multiplayer PvP party game, my Metsanelaimet is intended as a singleplayer campaign game that replaces/extends the worm characters with a variety of woodland animals and insects, all scaled to the same size, wielding a gun/bazooka like Liero did. General metagame is more akin to bomberman's singleplayer maps (map with breakable terrain and some pockets of air where enemies await for player to fight them, or like Super Smash Bros' 'break the targets' levels where player explores/parkours a complex map to hunt for targets(enemies) and blow them up.

There would be a metagame, randomly generated levels or premade levels with randomized elements or randomized props.

## Fuzzy initial gameplay design notes 
(I'm just brainstorming here, not proper thoughts, the real stuff is more towards the end of the document):
- destructible terrain with invincible(hardened?) rocks
- solid borders 
- mouse aim
- possible top-down view instead of sideview with trees and buildings as obstacles instead of underground dirt.
- random spawn of player eläin in corners.
- random spawn of eläimet anywhere middle.
- multiplayer collaborate potential where players spawn in and blow up the elaimet.
- randomized sprites via ai for elaimet.
- randomized goofy player sprites.
- randomized gun sprites.
- lorewise just go with silly non-serious context for some unhinged fun
- some cryptark and soldat influences in terms of combat, less reliance on ninjarope and jumping, more about floating or jet boots. Maybe take place in zero gravity entirely.
- each stat in below lists has a valuableness point value for auto generating new entities stats sheets in a balanced way.
- use mouse 2 to dodge ala Jager boost mechanic.
- sideway perspective with gravity but players float like cryptark.
- clonk/cc style maps with multiple material types of different strengths with small stuck loose nuggets embedded in terrain that can be picked up and used tactically (rock, flint, loam, t-flint, firebomb, dirt, etc, thrown like a cc grenade)


## weapon stats
+ Damage
+ Knockback (radius or inherit vel, can be neg)
+ Recoil
+ Reload speed
+ Max ammo
+ Mag size
+ Shot speed 
+ Shot amount
+ Shot spread
+ Shot gravity (no global gravity in this game)
+ Shot acceleration over time
+ Shot lifetime/det time
+ Affected by char motion? (Inherit player vel scalar)
+ Fire rate
+ Weight (move speed slower)
+ Cumbersomeness (mouse aim track delay)
+ Terrain delete radius
+ Proj, cone, line, sphere, curve line, sinewave line, etc.
+ Stun time
+ Noise range
+ Det trigger type proxy, time, contact 
+ Proj (collider) size
+ Proj trail spawnable
+ Proj trail rate
+ Proj submunition (blast or proj)
+ Proj det proj inherit vel or random dir
+ Wep ui sprite 
+ Wep ui name
+ Wep in-game sprite
+ Wep shot sound
+ Wep reload start
+ Wep reload end
+ Wep empty click
+ Wep muzzle sprite/fx
+ Proj sprite
+ Wep rarity/cost
+ Firing particle fx
+ Proj particle fx/trail fx.
+ Proj hit particle fx type and color tint.
+ Damages rock flag (treat rock same as dirt)
+ Weapon shake quake value (accumulate to trigger level event to cause dirt to spawn into level due to collapse.)

All projectiles are stopped by terrain, either removing some dirt on hit or nothing at all. No piercing terrain, no ripper of bots.

## Lore
Name of game: Metsanelaimet.
Play as one of animals in a fight for survival of the fittest. Eat or neutralize your opponent before they eat you for whatever typical animal reason; territory, food source, mating ritual, entertainment, annoyance, whatever.

Basically same as Soldat 2D: "bunch of dudes decided to kill each other and you can be one of them". Silly, but works.

Each character is an animal but inspired by the bot system from Soldat where each bot (animal species) has its own stats, sprite and name.


## Bot stats:
+ Max health 
+ Move speed
+ Jump height/jet thrust
+ Jump count/jet fuel max
+ Knockback resist
+ Sprint/boost | speed/range
+ Accuracy
+ Gravity
+ Bouncyness
+ Friction 
+ Regen/heal rate
+ Air control factor
+ Sight range (line of sight, can track when shoot)
+ Hear range (ignore terrain, but can't tract, shoot last pos if weapon has shoot through walls ai flag).
+ Smell range (how far can detect player?)
+ Smelliness (how much can reduce detection range, 0.0 undetectable, 1.0 full smell range, 2.0 double smell range, no hiding)
+ Carry slot amount (1 active + reserve slot X)
+ Wep slot switch frequency in seconds (next reserve gun, but will switch always if no ammo for gun available).
+ Species name
+ Species sprite
+ Gib type (particles, chunks, explosion or projs?)
+ Species happy sound (kill, spawn, win, loot grab)
+ Species pain sound (die 2x loud, lose, hurt)
+ Species melee attack damage, rate, knockback, recoil, noise, line/cone/sphere, cumbersome, stun time, attack sound, attack graphic, disarm chance.
+ Species cost/rarity (how many points worth per kill, how likely to spawn as enemy, how long is respawn time.)
+ Species particle hit fx
+ Species particle gib fx
+ Species move particle color tint/override 
+ Species boost particle color tint/override 
+ Species ability use particle fx 
+ Species digging speed
+ Ability cooldown
+ Ability bonus/penalty value/multiplier

Make tool to make balanced entries automatically and another tool to make unrestricted entries. Both for bots and weps.

Each weapon or bot is separate file/entry. Game loads entries during load and populates drop down lists for player loadout selects, random enemy spawn select lists (bot + random weapon). Weapon includes and handles its own projectile data, while environment vars can apply multipliers like gravity, air resistance and interference (ion storm maps that mess with ranged weapons, forcing melee fights).

## Spawnables

Game also has a list of spawnables for detonation effects that bots/projectiles can call to spawn.

Stats for spawnables:
+ Blast radius
+ Blast damage (none/skipped if no radius)
+ Knockback/pull
+ Stun time
+ Det sound
+ Det sprite/anim
+ Create terrain radius
+ Terrain color/material
+ Det particle fx 
No fall off, no reducing damage, no duration, no damage over time. No irregular shapes/offsets. Spawn center always. Just apply effects on spawn and fuck off.

Besides wep and det which only allow to spawn one tangible thing, additionally a particle effect can take place. These do not have gameplay effect, only visual ones to convey emotion or style. There's is a list of universal particle fx that happen for all regular events:
- jump
- boost/sprint
- land/slap into terrain/wall sideways
- proj hit light, med, heavy, super
- bot spawn
- steal/return
- nest hit
- nest gib


## Particle fx stats:
- amount
- base color (usually white for move/proj relates, tintable/overridable. Rest have unique colors)
- gravity 
- speed 
- accel/decel 
- lifetime
- inherit parent/deliverer vel scale (-1.0 to 0.0 to 1.0, can go over too.)
- bounce
- friction
No spread or direction settings, only radial bursts. No sprite anim particles. Just pixels.


## Deco props:
Embedded in terrain or loose on any surface in any rotation, these are shootable objects that may create a spawnable effect upon gib. They could be static only, but making them free floating, affected by gravity or knockback.
Prop stats:
+ Max health
+ Gib spawnable
+ Gib particle fx
+ Knockback resist factor
+ Gravity
+ Bouncyness
+ Friction


## Game modes:
Dominance - earn X points before others, respawns. Basically soldat DM. Lorewise establish dominance and everyone else goes home a loser.
Last standing - deplete enemy lives, be last one alive
Duel - 1 on 1 smash bros stock style. 5 lives both.
Eliminator - play has X lives and hunt all enemies whom only have 1 life, but outnumber player.
Defend - protect nest from enemies until time runs out
Rescue - get to prisoner and escort them out alive. Prisoner has 1 life but player can respawn x times. Guards spawn in x times to stop attempt.
Gauntlet - player has 1 life and tries to make it A to B. Hazards and enemy try to stop, but player doesn't need to kill anyone. They can, but don't need.
Steal - like prisoner and gauntlet mixed, except it's A to B to A and "prisoner" is indestructible object.
Hoard - like defend, but enemy tries to drag your prize to exit zone. You need to return it if they try that.
Forts - you try to attack and destroy enemy nest, they try it too. Have to attack and defend. Usually deplete their lives before going in to destroy their nest. Like KAG.
Vaults - same as forts, but goal is to steal stuff. Longer respawn times to get a window to go in.
Behemoth - one enemy is boss, scaled up and health/stats multiplied for that entity + active minions. You try to defeat it with X respawns.
Kaiju - you are boss, fight against stock of enemy respawns.
Beast Wars - both teams duke it out with boss class units exclusively. No regular sized characters.
Two titans - two ai controlled mega monsters fight it out while you respawn and try to help make enemy team fall, killing both minions and distracting their titan so your titan will do more damage.
Psycho - start off in a map with unarmed and armed pedestrians whom all remain passive until you fire the first shot or kill someone with witnesses (via smell or sight). May include police spawns that hunt you down. No respawns.
Bar fight free for all - walk into a place with various armed idle characters that remain passive until you fire the first shot. Instead of hunting you, they shoot at anyone who's most likely to shoot at. Last standing wins. No respawns.
Gang den shootout - same as psycho, but no police, instead a gang boss shows up after only few enemies remains. No respawns.
Bank heist - initially peaceful and everyone is passive, but as soon as player steal something from safe or kill anyone, be it guard or pedestrian, then all hell breaks loose. No respawns.

Note that the above requires a team system that supports atleast two teams and one unaffiliated neutrals (hazards, rogues, neutral bystanders).


## Map designs:
(Original idea: Played at 640x480 resolution, Fullscreen stretch with a scrolling zoomed in view.)

Maps should be made easy to create and generate with two options:
+ Random generated - which include dirt fill, hard rock sparse static spawns, empty gaps, random embedded props in dirt. Dirt can have repeating texture image of any color.
+ Image based multi, which needs a 2 color picture for dirt/empty layer material map (yellow, purple), and an accompanying image for bg. Both should be same resolution. Txt list for xy coord spots to spawn player, bots, props, based off top left corner origin of image, also txt specifies map type/game mode type, list of material textures for dirt. Program will check map on load and delete anyone that is out of bounds or/and throw an error announcing this.

If player/bot is 32x32, in a 480px high resolution that fits 15x that character.

Honestly I'd want level sizes not be constrained to 640x480, but offer standardized templates for map sizes, such as:
- 640x480, basic arena (duel, chill, compact small fights)
- 1280x480 long horiz (gauntlet, forts, vaults, steal, etc)
- 640x1440 tall verti (same as long horiz, tower maps)
- 1280x1440 big map (epic battle, mountain, megastruct)

Gravity param global override:
Normally everything handles its own gravity so this kinda allows to force gravity to be 0 on everything.
By default everything is balanced to regular "normal earth surface" gravity, so perhaps making a factor that multiplies positive values while dividing negative values (not zero though), and a wise versa for antigravity situations could be good.

Movement speed standards:
As levels are relatively small, only 15x of character height from absolute floor the absolute ceiling (480/32) and 20x width (640/32), it is too easy to reach one end to the other. This means characters have to be slow and deliberate, make minimal damage to terrain, have methods to refill terrain during battle both intently and ambiently via weather/expansion. Any kind of mobile dash/boost/jump would need to be fairly short. At the same time I do still want to have momentum driven movement, with the ability to rapidly move through the level within a second. Liero had the problem of having too harsh of gravity and unrestricted terminal velocity plus weak air control. It needs more float, more air resistance, slower acceleration rates, lesser gravity, better air control. I can't give exact values here but look at default liero gameplay and do things I just mentioned.

Weather:
Gravity alter/surge.
Spawn proj from any edge towards level with random direction.
Spawn particles.
Create fresh dirt randomly (earthquake)
Random neutral animals enter (rogue or bystanders)
Bonus spawns via teleport via visible ether wave that arrive via edge to signal where and when it comes, giving enough warning to dodge/get to it.


## Special abilities?:
Ninjarope
Gravity gun
Overboost
Lobster retreat boost
Grab and hold
Invert gravity (self)
Moonjump
Warp blink forward

(All work with only 1 button + facing direction)


## Dirt digging and terrain:
I plan to make levels begin mostly filled with dirt, so players will have to dig to get around. I think the best balance is achieved with these factors:
+ Continuous digging with held button + direction instead of tapping. (Or hold down dig button and go towards cursor, with more distance more speed).
+ Reduced move speed while dig, kinda like clonk/worms blowtorch but not that slow. Have constant dig anim.
+ Weapons dig between liero and cc, not too fast but not too slow. Dirt should be a tactical consideration during combat, movement and objectives. Some weapons can be powerful to shred the map quickly, much like the balance aspect between Big Nuke and Uzi. Weapons also limited by max ammo.
+ Passive terrain regeneration over time, or via periodic events, random quakes, dirt weapons of creation, level hazards/emitters, lava clefts, mud floods, dirt burst upon enemy kill.


## Controls:
Wasd - up, down, left, right (cryptark style)
M1 - shoot gun/melee atk/menu click 
M2 - dig/shield/menu back cancel
H1 - pickup/drop/throw/swap wep
H2 - use ability
H3 - boost/sprint/dash/jump 
=
H4 - reload wep
H5 - carry cycle (or hotkey to fire)
H6 - item use/grenade toss/clump throw
H7 - cycle item (or hotkey to use)
H8 - interact/activate
=
H9 - slomo focus toggle (game setting has options to make it either infinite or use the same style of defaults like my equivalent doom mod; 100 point, decrease when on, replenish when off, replenish rate multiplier can be tweaked in settings as well as max points. Slomo strength can also be tweaked between 0.1 and 0.9 timescale.
H10 - esc/pause menu/resume game/submenu back/cancel change


## Regular Battle Gameplay experience:
640x480 resolution, fullscreenable, scrolls, surrounded by black void background walls, soldat style camera, centered between player and crosshair. Feels freer but can drift into void often.

Alt, clamped to map edges, only do letterboxing/pillarboxing if wider monitor, camera centered to player. Optional direction bias offset when turning character left or right. More restrictive but contained.

Maybe have a toggle mode like cryptark has shift hold for camera look. Maybe camera max scroll distance is reduced per species stats, giving player an idea what it's like for enemy if they were that species too.

Depending on game mode, usually spawn repeatdly from designated area with some randomness or intent/choice, with brief invulnerability. Alternative spawn at exact coordinates as specified by map/game mode.

This spawning logic applies to enemies and props too. Some come via area, some via point, but the key here is that there is always an element of randomization for each combat start. Even if spawn locations are locked, props, loot, enemy loadouts, enemy species and enemy starting conditions may be shuffled.

After map initialization player will begin combat according to game mode rules and either win or lose. If lose, seed is kept for player to have a retry of that specific setup again. Seed may be set in/by metagame for consist repeatable runs.

In combat, player will dig through some terrain, use weapons to destroy terrain as alternative means of digging and carve their path to their targets, using their resources smartly. Resources are somewhat semi abundant and max starting ammo is generous enough to not end up in a situation of running out of ammo too quickly and having to do scarcity survival scavenger strategy. Some modes can influence that via metagame telling map to cut starting ammo and reducing/downgrading loot, but generally default is super cryptark at 60% ammo amounts comparably.

Digging and navigation should not be tedious, but I also want the terrain to provide a buffer of tangible cover as well as parkour opportunities. I think some species and loadouts could provide enough boost to plow through terrain and even rocks like it's nothing, but usually there may be some other shortcoming (species or weapon wise) to balance it out. That said if all matches begin mostly filled with dirt that has to be dug through to get to the opponent/objective/goal, then it would feel like friction that slows down momentum each time which may feel irritating if there is desire to just jump in and enjoy some action without dealing with obstacles and annoyances. For this reason map design, atleast the starting conditions, should make it so that there is a path of least resistance but most risk while still offering other paths of higher resistance with probable lesser risk.

When it comes to opponents they will have these modes of operation:
- hunt you down anywhere (deathmatch behavior)
- hunt you in proximity (hungry chasing predator)
- sentry guard overwatch (territorial defender)
- idle unaware until provoked (concerned self-defense, becomes one of three above, also a defender may escalate into hunter if hurt or pissed off)
- active flee (terrified civilian, runs for exit to escape to metagame map)
- proximity flee (avoidant, but lazy. Active flee will have npc run out of the level entirely via designated exit. This one stays on level, cowering without fighting back.)

Again, these roles and designations are game mode, metagame and map initialization/randomization driven. Enemies will dig too, shoot through dirt too and generally move about the level, according to predefined or randomly set 2 personal patrol points. This means the onus isn't solely on player to initiate a fight unless the game mode demands it. It's also worth noting that the ai smell mechanic allows enemies to know where player is with delay via proximity only, without needing line of sight. So they can start shooting at terrain to get to you or shorten the distance/obstacle to reduce the time to get to you.

Overall some maps feature entire level filled with dirt, while others offer open spaces and tunnels, and some merely have a few island or nuggets of dirt/props. This provides enough variety for every type of encounters.

Ideally all maps are proc genned or atleast partially randomized using heuristics tree patterns.

Combat itself is a mix of chaotic and tactical, both messy and deliberate. Player and enemies can eventually demolish all dirt terrain and props in a matter of a few minutes, if not faster with the right loadouts and deliberate action. Stage events may replenish this terrain the less of it has and trigger when a certain amount of "shake" value has accumulated. Any newly spawned terrain will be shown a warning and location where it will occur with enough time to notice and get out of its way. Each weapon has a "shake" value that creates a shockwave, making such an event trigger. Some maps have more stability than others and will have higher shake values that must be reached to trigger a dirt quake drop. After a dirt dump, the shake will reset until it's accumulated again.

All maps will have an exit hole(s) that is intended for metagame and civilian escape from stage. Npc/player must first reach it and then hold interact for 2 secs to exit into it, so exit isn't instant, allowing shooting down escapees.

Stages have enemies, dirt, props, exits, hazards, events, stability, loot and goals/objectives, solid borders and a background.

## Player has a hud that shows these things:
- hit points
- current weapon(s) (equipped and reserve)
- max ammo/remaining (equipped and reserve)
- refire delay (as bar or number)
- ability cooldown status / name or icon ,+ (as bar or number)
- global current objective / status
- crosshair
- event warning or hazard prop shape overlays (i.e show circle where dirt will dump into in 3.0 seconds or a flashing ! symbol)
- in game local objective arrow/direction marker 
- held item name or icon
- level status(es), warnings, countdowns
- loot name hover text
- homing weapon lock square 
- ai emoji reactions and telltale signs of signaling an action or reaction.


## Metagame:
V1 idea:
At start, player would get the option of playing either "good guy" or "bad guy" and the game would generate a campaign with a bias for modes that fulfill those. I suppose they could also be labeled "resistance" and "terrorist", where former has player overthrow, sabotage and make a better justice chill world while latter has player do warcrimes and chaos to become an evil tyrant that selfishly only benefits themselves or just plunges world into chaos just because they can. Maybe have a good, bad and crazy/chaos as options.

Simultaneously player could choose between 3 alternative worlds with similar good, bad and chaos split. Good worlds feature healthy open natural democracies. Think modern European green cities.
Bad worlds feature oppressive dystopias. Think Soviet bunkers, gulags, commieblocks and fortresses.
Chaos is a mix of post apocalyptic and toxic jungles. Think fallout pollution wastelands, madmax stuff and warped hostile brutal exotic murder jungles, flesh horrors, savages, punks, raiders and mutants.

Thus player can mix and match what they wanna do in what type of world they wanna do it in.
Good on goodworld usually means takeout thugs or corruption.
Good on badworld means overthrow dictator.
Bad on badworld is two warlords scheming against each other.
Bad on goodworld is terrorist being malicious dicks.
Good on chaosworld is rebuilding the world.
Bad on chaosworld is trying to conquer it, enslave it.
Chaos on any world is to make it a worse chaosworld.

The game modes and maps that occur on them are thematically alligned. I suppose an extra fourth random setting that is a mix of all could be neat too, merely being a slice of life of a worlds different parts with no real connection. Sort of a mercenary adventurer raider doing whatever gets them another banana/fruit. No reason, no regret, no remorse, no other sense than "why not, I get new banana frum this lul".

Tying the metagame together:
So as a player I now have the ability to choose the kind of session I'm in the mood for, but I still need something that ties all sessions into one contributive timeline, to feel like there is continuity and it's not resetting to zero after each session.

I want the game to be playable infinitely, so the driving element of this metagame wrapper can't be finite nor unreusable. No progression systems, prewritten storylines or unlock systems. All those are finite and rob/buy off the motivation from the game proper.

The game can take place literally anywhere, ground, water, space, dimension, etc. so I'm talking about an infinite universe. Because the game is goofy, the universe does not matter at all, it's all nonsense and silly anyway, so the universe shouldn't even be shown or tracked or display progression. It just exists, things take place somewhere out there, in random planets, random regions, random local areas as a mixed complex universe that is neither good or bad. In theory it's always equally 33/33/33 split between good/bad/chaos. This means it doesn't even matter if player exclusively does bad missions or good missions only, the universe will always have one or another place that is either good bad or chaos at all times, no matter what. Player cannot change the universe, they can only participate and make stories/shenanigans/achievements within it.

One idea I have is a Galactic Newspaper that reports on the players exploits in a humorous, random, spontaneous way that hopefully isn't repetitive or too boring after the first few runs.

I think the focus should be on these pieces:
- location name (greater region+local places per map, like street names, town names, neighborhood names, etc.)
- situation name
- rating for how well it was done with a golf inspired score card (first try = hole in one, etc) + gunmetal style total time taken to win that can be shaved by replaying individual maps faster.
- a randomized food dish or sculpture to commemorate the event. (This is reward, featuring fruit sprites, colors, name of meal and freshness/delicious rank based on performance.
- a seed attached to it. + Game version to keep track of what content was actually available at the time. (Note: add each piece of content under a version list number. That way game will know what to include and what to omit (lower number than game ver number = include, higher means omit, player can make a refresh remix version of that same campaign but with newest content loaded in.) this system ensures maximum backwards compatibility.
- some screenshot of player char with randomized name individual whom is a local to that area that the player roleplays as + true player profile name, if I were to implement a profile system to support player profiles/accounts.

Thusly this creates a personal log of campaigns with an ability to replay them and improved the final score with an s rank, or purge them from memory.

The game will remain nonsense and not have a lasting impact in universe but irl it will accumulate a catalog of personal unique campaigns that are special to them specifically. They can also be shared thanks to the seed thing + version number combo. Any procgenned artworks will also be tied to the unique computer or profile signature, slightly modifying the resulting art to be specific to them and sort of like that shiny Pokemon thing too. Player can also optionally add a label and a marker of satisfaction per entry to signal they're happy with it and a personal reminder clarifier that lets them be like "oh this was that one!".

Furthermore, individual campaigns could be grouped together as seasons that follow a specific theme, like elemental, summer/spring/autumn/winter, location or some other gimmick that runs every year. Optional opt out.

Also, game could log each enemy, or their skeletonized remains, as a reward cake pile thing. Sort of like trophies or gluttonous food hoards, reinforcing natures brutal dog eat dog world reality.


## GameTech requirements list:
Destructible dirt map
Destructible props system
Weapons system (usable, pickups, projectiles, switching)
Character system (+basic physics, +damage, +digging, +abilities, +ai controls, +ai signs/emotes)
Game modes logic (various)
Hazard props
Map events/weather/quakes
Metagame local campaign maker
Metagame global type selector
Metagame history log
Metagame history reward system (procgen fruit art, text gen, seeds, management)
Metagame random gauntlet variant. V1 too.



## Building process info:
Note to Claude: The stuff below isn't meant for the HTML pitch showcase generally, its mainly me figuring out prompts on how to build this project using Claude Code. If theres some tidbits that answer some questions for the stuff higher in the document, you can use those details from the things below, otherwise just ignore the stuff below.

<building_process_stuff>
Claude intro:
Type1:
Let's make a simplistic and minimal real time action game project loosely inspired by the freeware game liero and worms with the game window size being 640x480. I need the first version to have these features:
Game runs at 60 frames per second.
A map that is the same resolution as window size, completely filled with dirt. Dirt is destroyable and will turn into empty if an invisible terrain detonating/removing circle spawns.
A player character the size of 32x32 pixels whom collides with the dirt and cannot pass through it.
Player character will be placed at a random position within the map, creating a circle detonation that destroys dirt terrain within a radius of 32 pixels around the spawned player, once.
Player character moves by momentum drift using the WASD directional keyboard keys, floating weightless in the zero gravity, able to propel themselves in the desired direction by applying speed with a maximum speed acceleration cap of 2 distance units per second (1 distance unit is 32 pixels long). Players momentum/speed is reduced/stopped on collision with dirt or map border edges.
As long as player character is alive, the user can click or hold on the screen using the mouse anywhere they want and it will delete dirt terrain in a 32px radius around the mouse pointer location, like a paintbrush/eraser.
In the code, put placeholder lines where I should plug my pixel art sprites into and tell me how do I load my art assets/which subfolder I should use, etc. To keep things simple I will only use simple PNG images without animations or effects at this early stage of development.

If you can handle all this in one go then go ahead and build it fully, but if it's too complex or difficult for you then take an agent like approach to it, creating an outline/plan to build this out in steps where I will say continue and you will do the next part and so on, bit by bit. Up to you.
###
(Then continue with adding various features one by one.)
Mouse crosshair, directional digging, tweaking base move/dig values (speed, radii, caps), implementing a basic gun (projectile shooter type), so make a gun class and projectile class. Formalize playable character class too.
Expand all classes with the full value types they should contain.
Implement max/current ammo
Implement pickup item that can be interacted with to deposit equipped gun with its current ammo into box and retrieve new gun (with its own stats file) with the ammo it comes with/has remaining.
Fullscreen mode, prop entity, prop entity full expand, develop out all entity types doing their each component one by one so the basic dynamics of the system become robust.
Character abilities/dash/sprint/boost etc system.
Multiple characters that player can swap between by pressing button + left/right.

Next make a barebones set of content; characters, weapons, props.

Then, make the default level randomized with X amount of holes, props, weapon pickups and dummy characters that are not controlled by player.

After that, start plugging in the ai controllers into the mix, including team/affiliation/rogue framework, build out the ai entity and all it's components.  Make the enemy move and shoot with hunt mode, using weapon range to determine best distance to keep (based of the % of max/min range told by weapon itself, telling ai when it's usable to fire, making them try to get close and stay away as needed to use weapon effectively).

Then make a rudimentary placeholder metagame that player 10 randomized levels in gauntlet, giving ai opponent an extra bit of health multiplier or spawning more enemy units. (Give the boosted enemy an indicator to let player know they hax)

- Release worthy demo -

More content.
Implement actual game modes.

- Release worthy game -

Implement all game modes, including special logic like scaled up Kaiju characters, reactors, stealables, goals, etc.
Implement hazards, events, weather.

- Free version, paid version with more content, shareware style -

Implement selector metagame
+ Karma type
+ World type

Implement wrapper greater metagame log
+ Seed
+ Random text (location, op name, enemy group name)
+ Win reward + banquet of multiple foods via multiple campaign runs (seasons with themes)
+ Seasons system, themes implementation.


Pi explains solution for blood stain pixel data trick:
==
That sounds like an interesting project! Yes, you're right, if Liero used a static image for the terrain, it's possible that they simply modified the pixel data of the image to create the blood effect. This could be done efficiently by directly manipulating the image data in memory, rather than using a more complex decal system.

For your clone, if you want to create a highly performant way of permanently staining the terrain without using decal images, you could consider using a similar approach. You could store the terrain as a grid of pixel data in memory, and when a paintball hits the terrain, you could modify the pixel data at that location to add the paint effect.

To make the effect more realistic, you could use a simple particle system to create the initial splash effect of the paint hitting the terrain, and then use a simple algorithm to spread the paint out over time, modifying the pixel data as needed. This approach should be highly performant, as you wouldn't need to create and manage individual decal objects for each paintball hit.

Get open liero x source code 
</building_process_stuff>


