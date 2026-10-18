# City Buster
(loosely inspired by the brick breaker game and falling sand game genres)

Control a alien paddle warship from above and demolish cities and bunkers below. Faster hits generate a large AoE.

Goal is to reduce the scene below into a fiery molten slag.

Inspired by powder toy scenes with terrain and building/tunnels that are fully destructible with bombs, lava, etc.
The more you destroy, the more retaliatory projectiles launch towards you. There loose sand as rough layered terrain, rectangles that represent buildings, small figures of wax that represent people, and bodies of liquid that is usually water.

## Game idea

Falling sand sideview city scenes bombarded from above by a brick breaker paddle ship hovering in orbit, spawning and launching orbs of energy as balls, except instead of just colliding and destorying bricks like in a typical brick breaker game, its about hitting the solid pixels of a falling sand terrain canvas where the ball creates a fiery AoE blast upon collision with solid pixels or creates an on-demand energy blast by charging it up by holding down mouse 2 button and releasing the button to detonate mid-flight, though this does not break the orb itself, just releases a blast of energy that can be done again after a short cooldown as long as the ball remains on the stage. This mouse 2 blast affects all balls currently present on the stage, it applies a 10% speed increase on the balls too and also creates a 50% larger blast radius for balls that collided with terrain within half a second of their bounce.

The blast will either shatter and/or ignite the pixels with an outward spherical force, causing them to spread destruction to surrounding pixels either by kinetic collision or by heat convection, causing other static solids to become "broken" loose solids in the former case or by turning into fiery molten pixels that spread fire and heat, melting other nearby pixels, the surrounding pixels absorbing the heat as a chain reaction until the temperature diminishes enough between the pixels. Fiery pixels will also begin to cool down gradually, reducing in temperature as time goes on, eventually turning into inert burned slag. Broken and burnt pixels do collide with other pixels but they do not collide with the ball anymore.

Balls will fly at a constant velocity set by paddle ship collisions, so they don't lose momentum upon impact with terrain and they're not affected by gravity. Balls also do not collide with each other.

Initially, the paddle ship will select its payload by cycling through available munition types using the mouse wheel, similar to the ones inspired by the Angry Birds game, albeit adapted to better suit this game.

### Ammo Types
- Normal Medium Sized Ball (medium blast yield, reliable and easy to manage.)
- Triple Small Ball (smaller blast radius/yield, reliable more balls create more even spread of destruction, albeit 50% small bang per terrain collision.)
- Accelerator Ball (will gradually accelerate up to max speed, high potential power, but difficult to control, starts slow)
- Splitter Ball (Start as a big ball, will break into 3 medium balls, which then break into 2 small balls. Breaking happen after 3 terrain collisions.)
- Charge Ball (small ball, tiny blast yield, but if charged and detonated, it will only make a small energy blast but gain 3x speed, become energized and the next impact with terrain will create a big blast, after which it resets to normal mode again, but only halves its speed from the 3x speed from before. Essentially each charge blast use makes the ball makes the more powerful, but increases its base speed, making it harder to keep on the stage with the paddle. Its possible to power this one up to ridiculous levels if player is able to keep charging and detonating them over and over without losing it on accident.)

Then there are powerups that player can pick up during gameplay action that can further augment the existing or next launched ball(s), making them even more devastating or help the paddle ship with enhancements to keep balls in the stage more easily or to protect/heal from incoming damage.

## Possible powerups include these:

### Ball Powerups
- bigger detonation +20% (stackable)
- triple launch projectiles (normal shot is tripled, while triple small shot launches 9 balls, etc.)
- same as above, but quintuple shot.
- more mass (detonation shockwave causes falling sand solids to fly harder and shred more pixels due to increased force and speed)
- more heat (sets projectile on fire if it isnt already and detonation will impart +20% more heat, stackable on the heat increase aspect)
- piercer (punches through terrain but doesn't detonate on contact - instead it detonates after a delay of 0.5-3 seconds depending on how fast or slow it was going, respectively.)
- superheated (has an aura of fire that causes nearby pixels to become hotter. Stackable as more of this powerup will grow aura size and intensity.)

### Paddle Ship Powerups
- magnetic catcher (balls colliding with paddle dont bounce off, they instead are stuck to the paddle but keep their momentum so when the paddle presses Mouse 1, they get launched at the same velocity they previously had, but their relaunch angle depends on how much to the left or right of the paddle they are when they were glued to the paddle initially.)
- gravity field (balls traveling towards the sky have their trajectories curve towards the paddle ship.)
- hypervelocity launcher (new balls are launched at a high velocity instead of the released without momentum.)
- stronger engines (allow the area in which the paddle ship can fly around in be extended further, so instead of only having the top 20% be available as flight area, make it +10% lower, so they can fly anywhere in the 30% top area of the stage, stackable up to 80%)
- wider paddle (extends the paddle by 20%, upto a maximum of 200%. Makes it easier to intercept balls trying to escape into the sky, but makes more vulnurable to incoming attacks)
- armor repair +1-5 (heals/adds to the hp of the paddle (start at 10 hits, can stack armor up to 50 hits))
- shield generator (makes the paddle resist all incoming damage temporarily)

(powerups last 30-60 seconds (depending on rarity) and are often stackable in their effects)

The paddle ship is allowed to fly anywhere using the mouse movement, limited to a narrow 20% of the top area of the game's stage. The paddle ship will generate a new ammunition that will be ready to be released. It does this automatically once 2 seconds have passed since the last shot was released. It does not matter if the ball flies outside of the stage by flying off into space, this will not cause a life lost for the player.

Attacking the terrain with a ball happen by pressing Mouse 1 button to release ball with barely any velocity, almost zero, then using the paddle ship to physically slap the ball downwards via mouse movement. Whatever velocity the player "gave" the balls there will be what it will fly with until it collides with the paddle ship again. This system allows the player to set up many balls floating in the sky, then slap them one by one or all at once with a swift or soft movement of the mouse, colliding the paddle ship against the balls to send them flying downwards into the stage's falling sand stuff below.

Speaking of terrain, the goal is to destroy all objectives that are scattered over the terrain, both on surface, mid-air and underground. The objectives are usually various props like fuel tanks, silos, liquid barrels, storage boxes, cargo containers, crates, industrial machines, electrical infrastructure devices (transformers, capacitor banks, large batteries, conduits, repeaters, etc.) and other such things that are satisfying to break and can maybe explode. These objects aren't falling sand pixels, but actual objects that are merely occupying space in the terrain, embedded in it.

The goal of the player is to use their weapons to dig through the terrain hit-by-hit, reach those props and blow them all up to complete the level. Each time one of those props is hit, they send out hazardous projectiles in an upward spread towards the sky and maybe a powerup with a 30% chance or so. The player's paddle ship essentially creates dangerous debris with its attacks that it must dodge, while trying to keep the ball in the stage to more damage, while also trying to catch powerup ups that otherwise will be lost into the sky if they miss catching them as they come up.

The aforementioned hazardous projectiles come in the form of stylized fireballs, lighting bolts, sharp metal shards, shrapnel, etc. all as small objects with a constant starting velocity with mild randomization and random spread. Each reduces player armor by 1.

## Terrain itself is usually layered from top to bottom this way
1. Wood, Grass, Water
2. Sand/Soil
3. Stone
4. Bedrock

Those are falling sand type materials, among many that are in this game. Some are static, some are loose and affected by gravity.

Generally in stages, its is common to have these things:
Floating in midair, there can balloon(cable material) suspended objects. 
On the surface and underground there can be rectangles (filled or hollow) made from concrete, lines from cable, little wax dudes sitting, standing or in lying positions, facing left or right. Underground may also have empty spaces to emulate caves, tunnels, hallways, shafts, etc. There may be small details using materials glass, cable or concrete for artificial things, while wood and grass for natural things. Also water may be here and there.

Each stage may assign one color to each natural and artificial, both having certain palletes or ranges of colors that they're supposed to use for purposes of visual clarity and what seems right. The game takes place on far away exoplanets, so its ok if the soil is desaturated cyan or the water is purple.

## Some materials info
Water - thrown around by kinetic force, turns to steam if heated too much.
Steam - evaporates into the air by going upwards until they fade away completely.
Sand - light sand, turns to hot glass if molten, which will cool down into regular glass. Otherwise blown away into nothing by kinetic force/particles. 
Glass - can turn into lava or shatter in glass dust.
Dirt/soil - medium sand, slightly sturdier, can be shredded into nothing, but melts into lava instead of turning to glass.
Grass/leaves/bush/green growth - torn to nothing if hit by kinetic force or pixels, set on fire if heated enough.
Aggregate - heavy sand, turns to lava if molten, or sand if struck with kinetic impact/force. This is what concrete and stone turns into if they are shattered, going from static to loose pixels affected by gravity.
Wood - flammable solid turns to fire and Ash if burned, to wood pulp (like medium sand) if shattered.
Fire turns to smoke as it ages for 2 seconds.
Smoke flies upwards, doesn't interact with anything but is blocked by solids.
Lava - does not collide with ball, convect heat into nearby pixels, cools itself down gradually into ash.
Ash - also doesn't collide with ball. Maybe have to embers in it, so its not uniformly dark grey, occasionally does orange/yellow pixels color shifting for its pixels.
Wax1 - breaks into dark crimson red goo viscous liquid or burns into ash. Usually a human skin color initially, set by stage.
Wax2 - same as wax1, but this is meant for "clothes", so they can be any single random color per stage.
(Wax1 and Wax2 are meant to represent humans in the scene as tiny 2x9 pixel characters standing, the top 2x2 pixels being wax1, while the rest are wax2 - a clothed person essentially.)
Concrete - artificial hard solid that shatters or melts into lava.
Cable - Like wood, but reserved for artificial solids that aren't as tough as concrete.
Stone - natural hard solid shatter or melts into lava.
Bedrock - indestructible. Shape wise it can be a flat, jagged or wavy/hilly surface or something in between or a mix of those.

(Note: sort these out to be more consistent and may also add some materials that I'm missing, perhaps also add Steel and Deep Rock as harder versions of Concrete and Stone, respectively.)

## Controls
Mouse movement - controls the paddle, directly tied to cursor position, albeit confined to the limited flight area where the paddle ship is allowed to be.
Mouse 1 - release a ball, letting it float without velocity until the player smack it with their paddle ship.
Mouse 2 - charges up a energy blast that will originate from every ball currently in the stage.
Mousewheel up/down - changes current weapon/ammo type.
Spacebar - trigger slow motion on/off at will. Unlimited usage.

## Lore
Play as a reckless renegade for hire that has come to sabotage the supply lines of an enemy nation, similar to the game Just Cause 2 and its protagonist and antagonist, generally speaking. AI can figure out a more fleshed out story and plot. All I'll say here is that the game takes place in the lawless outskirts of Helios Sector - a region of space about 50 star system that mankind has recently colonized and some of the colonial leaders have gone corrupt and greedy, becoming mafia leaders. Part of a local weapon research group that was affected by these unlawful activities, they formed a vigilante gang to take them on using this experimental weapon system called the Paddle Ship.

Theres plenty of mafia gangs, corrupt mayors and other thugs that have taken over the means of productions so its not about a single particular tyrant, but a whole varied plethora of them across multiple different exoplanets.

The renegade vigilante group is sponsored by an unhinged religious cult to go and take them down, since they are they affected by the mafia too and arent worried about collateral damage as long as "the evil will be put down".

## Metagame flow

### Low Metagame
These are campaigns to take down a particular mafia gang, namely by bombarding several locations that either house members of the gangs or have their sources of wealth, power, machinery or resources. The player does 9 stages per campaign, surely obliterating the culprits in the process, although they're never mentioned or acknowledged during the combat stages. Each stage is randomly generated using an algorithm that creates terrain from falling sand type pixels, solids and loose ones, then over them artificial surface and underground structures are populated as randomly placed rectangles. then, terrain and structures are randomly hollowed out (some are, some aren't), creating caves, tunnels, shafts and rooms. Then water is optionally and randomly poured as small pools here and there. Then trees, bushes, cables, grass and small decorative objects from pixels are built and placed all over. Then a bunch of wax dudes that placed here and there at random in open spaces. then finally, a bunch of goal props are scattered around the level for the player to destroy. This map is generated with a seed and a random name influenced by said seed, saved and recorded into the high metagame log page as a level the player can replay again if they wish to.

Each metagame starts with a one page intro screen that introduces a gang name and their leader name and what color scheme they use, what planet they're on and which region and what is their list of 1-5 crimes.

More crimes is an indicator of campaign difficulty, or rather the density and amount of stuff on the stages related to that particular generated campaign, causing it to be more chaotic overall due to more stuff to blow up and more hazards to dodge, but also more powerups to pick up and stack.

### High Metagame
A vague starmap of the fringe sector. Player can choose one from 3 new random options that are presented for player to take on, offering an easy 1 crime intensity campaign, a medium 2-3 intensity campaign or a chaotic/hard 4-5 intensity campaign. All of them will have 9 stages and whichever the player chooses, the other two are discarded and dealt by other vigilantes in the meantime. Once player finishes that campaign or forfeits it, they get 3 new ones to choose from.

Each campaign and their stages are recorded into a log from where player can go revisit and play those specific stages again, contextualzed as a "flashback memory", so canonically player had already defeated that mafia gang, but they can relive the experience of that particular stage.

Each new campaign may have a quirk in regards to different gravity or a multiplier for explosions or forces or something that influences the stage generator, that makes each set of stages related to that campaign feel a bit different.