# Falling sand game variants
(I'm making a series of games that fall under the same category of leveraging falling sand game mechanics (cellular automata with physics) in some way and originally I wrote a big mega document with all the ideas in it, then later split them into individual small documents to keep the prompt focused. The stuff after the Game Ideas is the actual game idea I want you to focus on, while the below two paragraphs are merely an intro that is free to be overwritten/disregarded in favor of the actual game idea that takes all priority.)

The idea is to have very simple, short and satisfying game experiences that primarily incorporate falling sand mechanics in some way. By falling sand, I dont exclusively mean sand only, but the general game engine of falling sand games like Powder Toy or similar pixel simulation sandboxes. The range of materials/phenomenom are always limited to the scope of the particular game at hand, so while some games may feature things like fire, sand, water, grass, snow, ice, wood, stone, flammable gas, etc. it always depends on a per-game basis what they'll ultimately have, both to keep them focused and simpler to make.

While falling sand mechanics are at the forefront, the game can feature other 2D game elements and colliders that work in tandem with the falling sand. Also unlike most falling sand games which are merely open sandbox experiences without any structure or metagame, the games I want to make aim to have enough game design embedded into them so they're atleast on the same level as a typical kongregate web game or a newgrounds flash game, in terms of gameplay, small scope and cohesiveness as a proper game experience, even if its simple/basic.

That said, I aim to mainly release them on desktop platforms (PC, Linux, Mac), maybe web too if its possible to make it performant enough for it to work there. But Windows PC is always priority one as the release platform.


## Game Ideas

### Unhinged Anomalous Materials Heist
(sideview 2D game with a simple physics low gravity platformer and also a sideview 2D game with a falling sand scene separately)

Its a two stage game:

## STAGE ONE
1. Land an unlicenced space taxi (looks like a lunar lander and controls like one, has infinite fuel and is collision resistant, but can be blown up by weapons fire) onto an anomalous materials containment site, which is essentially a randomly generated lunar bunker maze with shafts, tunnels and spacious rooms (very simple and basic, just tiles map with guaranteed layout, baby's first 2d dungeon generator basically) that is occupied by roughly 15-30 drone bot armed with plasma guns that are programmed to guard the area to keep troublemakers away, to prevent them from taking canisters that contain dangerous and unpredictable anomalous materials. Once landed, player can exit the taxi lander from the top as a small dude with a blaster shotgun, some grenades and jetpack - a troublemaker - and try to fly/fight past the guards and the somewhat easy maze to collect all 3-5 randomized canisters and bring them back to the taxi and then blast off, reaching the top of the level to win. The scene is seen through the eyes of a long range surveillance artillery drone. It initially announces that "this area is restricted, turn back and leave", but as player starts collecting canisters, it gives the player a last warning to put down the canister and get out, when the player picks up the second and subsequent canisters, it is authorized to use lethal force and begins to track the coordinates of the player as they are going around the maze and firing explosive shells with an AoE blast radius that arrive at the last player location with a delay of 8 seconds before the shell hits that spot. The after every shot, the shot velocity increases by 0.2 seconds, down to a maximum delay of only 4 seconds before the explosion hits that spot and the rate of fire also increases from 1 shot per 6 seconds down to 3 seconds per shot, with a 0.1 increase per shot after the first one has fired. Player will have to move fast to get out of the way and try to grab the last canisters before they're either blown apart by artillery or shot by drone bots or accidently have their taxi lander getaway vehicle blown up.
Player is armed with blaster shotgun that fires a simple projectile with a constant velocity that flies straight and deal damage to what it collides with. Grenades are launched forward with an initial velocity and they gradually slow down with air friction, collisions and gravity. They will bounce off surfaces and detonate with a AoE blast after 3 seconds, dealing triple more damage than a shotgun projectile, but having limited ammo (start with 10, find packs of 5 in the level as powerups). Shotgun can be powered up by finding powerups that increase projectile count (default start with one slug projectile only, additional ones with give +1 projectile +5% spread.), increase rate of fire, increase damage per shot, increase projectile velocity, replenish ammo (ammo start with 99 shots, can find packs of 20 shots. Projectile count does not affect ammo consumption rate).
Guard drone bots are just a humanoid bot that stands around with a rifle and shoots at player with a similar weapon like the players shotgun if they have a line of sight on the player. Player should either move quickly to dodge shots or hide behind cover to not get shot at or throw a grenade with a bounce to take out the bot without risking exposing self if trying to use player shotgun against guard bot. They dont chase the player, the just shoot and get knocked around like a physics object if hit and have some hitpoints that let them survive a few hits before they break.

## Player controls

### Small dude:
Mouse aim - point shotgun/grenade launch direction freely 360 degrees.
Mouse 1 - shoot shotgun
Mouse 2 - launch grenade
AD - rotate character left and right
W - apply jetpack thrust in whichever direction characters up is currently facing
S - apply air breaks to slow down gradually, keep holding to hover midair in place
E - enter lander taxi (switch control over to Lander and hide/disable small dude)
(dude has 10 hit points, they're wearing a armored battlesuit rated for space infantry, don't ask how the dude got it, they're sketchy as heck)

### Lander taxi
W - upward thrust (100% power)
AD - thruster left and right (70% power)
S - downward thrust (60% power)
E - exit lander taxi (make small dude appear outside taxi right on top of it and switch control to them)
(Lander stays upright at all times. It has 20 hit points. Artillery does about 3 damage per hit, good to know when finally getting in and trying to fly away. Collisions do progressively more damage with more speed, player can insta-blowup their lander if they go high speed and crash into something solid. Slower collisions will do less damage and below a certain threshold no damage occurs.)

2. In the previous stage player succeeded in stealing canisters of anomalous materials. Now the player gets to use them. They strap a C4 explosive on them and then drop them from above into a scene that they can customize before entering it. Before the scene begins, player is presented with a menu 
"You got some nasty things there, where do you want to use them?"
Name of location: text field input
Type of location: drop down menu; outhouse, small house (1 floor), tall building (5 floors), wide building (2 floors), big building (4 floors and wide)
Building is above or underground: toggle
Number of people: slider with range of 1-50 people
Time: Day, Night, Dusk, Dawn (determines background vertical linear gradient colors)
Terrain: drop down menu; flat, crater, hill, cliff (randomly left or right sided), mildly wavy, bridge
(Have a button to randomize all but amount of people and name of location. Name of location has its own optional button to randomize.)

Once set, the game will generate an ultra-simple 2D falling sand stage with these elements:

Based on selected terrain, add a desaturated muted colored dirt that starts from the bottom and goes up to 15-35% of the scene's height (for example, flat terrain end at 25% of scene height).
Drawn over it at the very bottom, a jagged layer of dark grey stone bedrock (indestructible, inert, random frequency, goes up only about 2-3% from bottom in scene height.)
Drawn over the dirt too, a medium grey with a faint color tint of concrete rectangle, based on the building type selected and if its above ground or underground. If underground, building cannot be lower than 8% from bottom of scene. If above ground, match the bottom origin of rectagle to average height of the dirt layer's surface, so it roughly sits on top of it, though slightly sunk down about 3%.
Over the rectangle drawn in the previous step, draw multiple evenly spaced smaller rectangles in light blue color to represent windows of that building, based on building type.
This forms the surface of the scene and the last thing to add is to people as 1 pixel wide and 5 pixel tall figures where the top most pixel is of absolutely any color, while the 4 pixels below it are of one globally-chosen-per-scene skin color, be it be caucasian, hispanic, asian or african. Pepper these figures anywhere on the surface at random, based on how many people were chosen. Even if they up standing on top of the roof of a building or just standing somewhere in on the dirt or bedrock.

The add a text label up top that says the location name and a background gradient as defined.

Now player can choose to click anywhere in the scene where there is open space (no solid pixels) to spawn the 3-5 canisters they picked up, one at a time per click. It will be spawned as a simple small physics object pulled down by gravity and likely just fall and settle somewhere, resting on the scene. Spawning happens with mouse 1 button, while detonation happens with mouse 2. Player can spawn all and detonate all at once, or spawn one or few and detonate them individually.

The detonation payload will spawn a group of randomized cellular automata pixels, one unique type per each canister that will likely grow out of control and apply physics forces, convert existing scene material into more of itself interact with other cellular automata payloads violently and probably obliterate the entire scene in a spectacular way where all the original pixels of dirt, concrete, glass and wax are probably going to be obliterated, assimilated or thrown out of the sides or top of the scene. It would be like a chaotic storm by simply leveraging the different cellular automata types like conways game of life or what not. Each detonation will likely be unique and result in different outcomes, especially since the cellular automata pixels that break out of the canisters are assigned a random color as they spread and another random color when they interact with something other than themselves or empty space.

Player can enjoy the spectable or cancel at any time by pressing Esc to open a pause menu to either resume and exit back to main menu, to start a new game or to view a log of saved games to replay any Stage 2 they previously managed to get into and completed defining the level. It contains the seed so reloading that level lets them replay it again like it was the first time without needing to do the heist stage again. The log list of saved games include name of location and seed number.