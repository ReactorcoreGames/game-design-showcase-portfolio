## Goal:
Develop a typical classic Bomberman game, but instead of setting bomb down, you put it on the tile you're on and immediately launch it, letting it travel a distance in the direction you were facing at the moment of the launch. Bomb placement is auto centered and it only flies straight automatically on a rail, only stopping when colliding with wall or another bomb. Bombs have no collision for powerups, npcs, player.
I reckon this is more of a 'rocket propelled grenade man' game.

## Controls: (playable one-handed)
WASD move
F to fire
Q to detonate
R to pull blocks, barrels, crates (move into them to push them)(face a block, press R, you and block will move 1 tile back)
E to interact
In menus Q is no/back, E is yes/enter.
Space use blast shield. (Has heat meter, unusable if full, must wait to decrease, movement is slowed down while active, optimized against explosion flames so player can withstand them better, whereas enemy non-flame projectiles/attacks will rapidly fill the heat meter by comparison, making it less suitable to protect self with.)
ZXC (use/swap consumable/toggle item ABC (tap or hold)).

## Upgrades:
Throw/fly distance - default bomb flight is 3 spaces/tiles from start and 3 seconds detonation time. Increase distance by one more tile and +0.2 detonation time.
Fire length - increase length of cross shaped blast by one more tile.
Fire power - increase how much damage bomb deals to tiles by one. (Some tiles take more hits to break.)
Fire penetration - does fire keep going through blocks instead of being stopped by the first one? How many tiles?
Bomb quota - can have one more bomb in the area before needing to wait for the existing ones to blow up.
Runspeed - walk faster by 1.2x.
Backblast - create fire behind player by one more tile, like an rpg bazooka backblast. (Maybe default feature?)

## Consumables: 
use it to augment next bomb launch or activate/perform an ability. May have multiple uses.
Shaped charge - removes backward blast portion and makes detonation time shorter by -25%. (Default bomb behavior?) (Maybe backward blast is reduced to fraction of the other blasts? Back to front/side blasts ratio 1:1, 1:2, 1:3, 2:4, 2:5, 3:6, 3:7, 4:8, 4:9, 5:10, etc.
Impact detonation - if it hits a wall or enemy, it detonates right away. (Also default?)
Cluster bomb - after detonating, lay another bomb in the same spot. Come in 1x, 2x, 3x and 5x super version. The repeat detonations happen after every 2 seconds.
Fire branches - explosions are normally cross shaped but the main directions could have potential for branching out. Lvl 1 has first fire branch by 1 fire on either side of fire. Lvl 2 adds subsequent fire tile have branches from 2 to second to last by 1 tile on both sides. Lvl 3 makes those second to third last fire branches 2 tiles long, lvl max adds a curve of increasing fire branches that taper towards the end. The effect is more noticeable with more fire length.
Sequence detonator - instead of all bombs blowing up together during a chain reaction, each bomb detonates with delay.
Moab - instead of cross blast, use a rectangle blast.
Dash
Airburst - if rocket doesn't collide and just stops, don't wait for it to detonate, just explode it right away
Health/armor - survive hits
Blast shield - ability that player has to protect against fire with a cooldown to literally cool down the shield to use it again.

## Cycling and stacking of upgrades:
In original Bomberman I gain upgrades until I max out and just keep em, that's kinda boring and makes upgrade pickups meaningless in lategame. I want to implement a durability system that isn't time based (countdown timer until powerup expires) but is instead based on "durability"; each pickup has a durability value that decreases each time a relevant action is performed, mainly firing the rpg. Player can essentially find powerups, stack them up to a max amount, be unable to pickup more until the old ones expire, and each time they use their rpg bazooka, each of the upgrades tracks how many uses it has left. The amount of uses is generally generous, around 10-60 uses, depending on which one it is. Player may have multiple upgrades expire roughly at the same time, having had plenty firepower prior and now being reduced, but slots being free now to pickup new powerups 
Powerups on floor are burned away if they're caught in the flame of an explosion, so player is discouraged from spamming their weapon in favor of using it tactically, gathering newly revealed powerups, avoiding not to burn them, building up stacks so that when they fire their weapon, it hits extra hard and they have to use it less to obliterate the map.
GUI wise, player will see a vertical list of powerups as icons with a number beside them, indicating remaining uses. It's somewhat satisfying to watch the list grow with stacked powerups.
Below powerups are consumables, up to 3 slots will show too as logo, with number of remaining uses and if it's toggled on/off with some visual marker or just "ON/OFF" text as blue/red.

## Detailed nuances of mechanics:
- When explosions happen they never trigger all at once, they enter a queue, each happening 0.3 seconds after the last one detonated.
- Fire from blasts lingers; a tile engulfed by fire burns for a solid 1.5 seconds before ending. During this time, entering/being in tile will damage player or enemy, triggering their invincibility frames.
- Bomberman style movement QoL stuff; when walking around blocks and trying to turn a corner but you walk and press against a solid block by accident (you didn't move far enough past it to clear it where the opening is),  then automatically slide the player character to left or right depending whichever open side is closer to player.
- Explosions don't appear instantly; first upon rpg impact or bomb detonation a growing flash occurs, the 0.5secs later the full cross of fire appears, extending over the tiles that it can (based on powerups) all at once, then lingering and vanishing after 1.5secs. this gives player a moment to deploy their blast shield if they messed up and are about to be BBQ'd by their own fire.

## Battlemap color shift:
A campaign has the battlemaps start with one specific profile for color, including hue, saturation and brightness and over the course of a 10 map campaign gauntlets of battlemaps, the values shift per level towards a another profile of hue/sat/bright. This affects the floor, border walls and maybe UI borders. This simple system creates a sense of progression from the first map to the last one, gradually map-by-map. The hue value shifts aim to be between 2(common) or even 3(rare) adjacent colors so it's not going to loop the entire rainbow but keep it focused and subtle, keeping the value shift range rather narrow. Saturation and brightness shift depend on whether the starter value was low or high to begin with, going in the opposite direction as levels progress, with these ranges being clamped to random portions of the scale, so they're not the same for each campaign. Saturation can choose it's clamp anywhere between 1-99%, while brightness has a usable range between 30-70% where it can decide the randomized lower and upper values within that range.

## Objects:
Spawn point (lower left corner)
Exit point (upper right corner)
Crate (wood, metal, reinforced) (1, 3, 5 hits)
Stone blocks (immovable 10-60 hits, soft, hard, obsidian)
Explosive barrels (tier 1-5)
Enemy S, M, L class spawner (easy/soft, medium, difficult/hard) (enemies are similar entities to the player, dealing with the same collision if blocks and border of the battlemap, walking on the grid just as the player does. See boss enemy for various ideas of attacks what an enemy unit can do too, although with lesser speed and power.)
Boss spawn (3x3 boss, 2x2 miniboss, 1x1 elite)
(5 hits to eliminate elite, 15 to eliminate miniboss, 40 hits for boss.)
(Boss is a free roamer that slowly floats around level, bouncing of borders with a random starting direction and  maybe occasionally changes direction. They perform a randomly assigned attack. It can involve rpg or bomb that boss can't hurt itself or minions with, it can spawn minions, it can collide with player, it can fly past over player burning them below, it can fire generic slow projectiles in a burst or spread randomly or towards players with a second delay before firing. They can also do a sniper tile attack, causing fire to spawn on a tile, either random tile(s), or on player tile with a warning delay of 2 seconds or longer. Boss only get one or two of any attack.)
(Bosses disregard the grid in regards to movement, they only consider the level borders and bounce around within the confines of those. If boss spawns outside borders or happens to be/get outside borders for some reason, then  make them go towards the center of the map from wherever they are, turning off their border collision detection until they are firmly back inside the battlemaps borders and then turn border collision detection back on.)

## Game Flow:
Enter overworld to select next campaign type. (Gentle, structured, chaotic).
Start gauntlet of 10 maps, one battlemap at a time.
Generate map with random blocks in specific ratio between empty-soft-hard-props-enemy. Early levels are less chaotic, later ones more chaotic, but not necessarily harder. Use an algorithm that always creates structured but wildly randomized generated battlemaps with entry having a 5x5 pixel cleared area form player to start in and use their bazooka safely. Since player has infinite ammo and everything solid is destroyable, player will always be guaranteed to reach the exit and defeat all foes, so it's ok if some layout result in blocked paths. Player merely has to be careful not to blow themselves up nor get hit by the enemy units. Player can survive 3 hits and each hit offer a generous 2 second invulnerability period - this applies to enemies too. At start of battle player also gets 15 second entry invulnerability period too or which cuts short if player fires their bazooka, giving an extra 2 seconds of invulnerability to survive the lingering fire. Only player gets this one, NPCs don't.
Final level features a boss enemy.
Always Spawn in upper left, exit at lower right.
Play the Top-down battlemap. Win or lose. Losing happens by losing all player hitpoints. Winning happens by eliminating all hostiles and going to exit in battlemap.
After 10 maps (boss included), return to overworld for another campaign start. In between, show a satisfying short cutscene of a place exploding and vanishing with multiple small explosions, then a big one, crescendo as a white flash and fade to normal to see it's gone, then fade to black and return to overworld with a down from up screen transition.

## High Metagame:
This is premise specific.
For the Twink stuff, maybe liberate new outfits for your Twink. Or liberate Twink for a bigger harem or just to set them free so they can go on and love happy wherever.
For yandere, maybe she keeps raiding a mall to find unique gifts for her bf.
For AAL miner mech, add a new mine to the expanding galactic empire, now cleared of threats, ready for production.
(Note: I want to avoid the super meat boy syndrome where player repeats the same objective without it ever actually fulfilling or getting reset/rolled back, making the whole game pointless and anything the player does dumb/useless. Don't redo/repeat; Do advance/complete)

## Inspirations:
- Bomberman/Super Bomberman 2 (general idea)
- Breakout (tiles/blocks with more than one hit points)
- Sokoban (player can push blocks)

## Experimental inspirations or ideas:
- snake/deathworm (as an enemy/boss)
- AW Dual Strike (combat mode)

## Premise ideas:
- bazooka armed yandere goes to rescue her captured subby man/woman from toxic macho men trying to make the sub "man up". (Each campaign is a different yandere/sub pair).
- crusader goes to clean up Islam. With a bazooka.
- tomboy/goth goes to save her twink from gay conversion therapy. Also with a bazooka. (Each campaign is a different tomboy/twink pair).
- Ukrainian bazooka android (incl. theaters in Russia(forest/fields), Iran(mountains), Africa(desert), Arctic(snow), Moon, Europe (city warehouses). Removing Russian presence all over the world.
- AAL underground bazooka miner mech (vs ishimura zombies buried underground and markers or cave monsters).