# Bunkership Exhaust Port Breaker
(loosely inspired by the brick breaker game genre)

An attempt to make a brick breaker game that isn't abstract or meaningless by giving it a grounded setting, framing the bricks as pieces of starship. There's an emphasis on leveraging the desirable situation from most brick breaker games to get the ball into a confined shaft or tunnel so that it will break a lot of bricks on its own without the player having to bounce it back off - framing such openings in a stage as similar to the exhaust port on the Death Star from Star Wars movies.

The ship designs of this game are fairly random intended to let a procedural generation algorithm handle creating a diverse range of ships for the player to demolish. The general idea is to create ships that are tough from the outside by having hardened rock as their outer shell, with ship systems as scattered/shuffled modules inside that are more prone to damage.

Lorewise they're either built/carved from hollowed out moon rock or asteroid rock, while filled with a superstructure, engines, power systems, electronics and thrusters, with mostly exhaust ports, antenna, signal lights and armored turrets exposed on the surface. The ships themselves are never standardized aside from the modules inside them as tiles; neither in what shape or configuration the ship is like nor how the internal layout is set up. Each ship is unique unique and quite random.

The ships are generally great at combat against other large ships, but they're somewhat vulnerable to anything exploiting their weaknesses, which usually requires tremendous courage to get close enough and have the right kind of weapon to do it right. The smaller turrets of the bunkership also pose a hazard to any would-be attacker trying such a thing.

The procgen process of a stage with a bunkership looks somewhat like this:
- first define 1-4 rectangle areas where the ship will be set up. These areas can overlap each other, but they're always meant to leave an open area of atleast 20% at the bottom stage for player to have enough space to operate there. The ship construction rectangles can be any width or height and any x and y origin point within those confines. The whole stage is a square tile grid map so the build area rectangles always fit to it.

- then fill those rectangles with hardened rock tiles, hollow them out so they become a 1 tile border that serves as a shell for that bunkership. Also for the same tiles(including the ones that were hollowed out) apply a background tile graphic that makes it look like it's part of the same ship as opposed to the space background behind the ship.
- next fill the insides of those shells with random tiles that aren't hardened either using a pattern, or completely jumbled. Optionally limit the palette of tile types to 2-5 types.
- then select about 5-15 tiles as turrets and place them over non-hardened tiles. Randomize their armor value and rarity type (normal, super, mega).
- carve random shafts and tunnel within the ship, maybe with a random marching square, essentially just deleting tiles. These can tile deletions can affect the shell tiles too.
- then at random replace 10% of all hardened shell tiles with either an empty tile or any non-hardened tiles.
- then set the color tint for the inside tiles of the ship and a color tint for the outside shell of the ship, whatever is left of it.
- finally choose 0-2 ambient space weather events for the stage, along with a colorful stylized nebula/orbit/deep space background.

During the brick breaker styled game, random powerups can drop from any tile at a random chance, somewhere in the 5% range. Unless multiplied by another powerup.

Lorewise game is about flying an experimental spec ops ship to sabotage and destroy the warship fleet of an authoritarian nation in a future human colonized star system somewhere in the milky way galaxy within the Helios sector, an area of about 60 star systems. The nation has devolved into thousands of gangs/clans that fell victim to the seven deadly sins, controlling a large zone of asteroids, planetoids and moons around a gas giant. Sort of like Russia in many ways, sadly. They're entire society are crude, brute, unwise, mafia like, militaristic, control by fear and force, endear evil and abuse, low-trust, zealous and self-absorbed.

Neighbouring nations were upset about their raids and poor behavior so they created an elite task force to dismantle their military with advanced technology and tactics. Sending drone ships with experimental weapons purposefully designed against the enemy nations warships/bunkerships. A much better plan than trying to fight a costly head on war with capital ship slugfests.

## Game elements

### Ball powerups
- ultra ball: more speed = more damage per impact\more tiles destroyed before bouncing off. Stackable.
- explosion on every impact with tile
- grow: large ball (wider hitbox, doesn't change mass/density/damage) Stackable.
- shrink: small ball (narrow hitbox, doesn't change mass/density/damage) Stackable.
- heavier mass (increase damage per hit or how many to plow through before bouncing off, stackable)
- rail ball (new temp ball. perforate through 20-100 tiles before exploding)
- asteroids ball (new temp ball. Start big, split into 3 smaller every 3 collisions depending on size until too small to split, then will explode.)
- thunder ball (hit another random tile on every tile collision, stacks increase damage per single tile)
- arc ball (similar but hits multiple tiles, each for one damage)
- sprayer/disco ball (new temp ball. Shoots projectiles wildly as it spins, hitting tiles to damage/break them, expires when it's ammo is spent)
- flubber ball (bounce angle is always random within 170 degree range from surface of tile. Paddle collision is always normal bounce.)
- multiply balls all by two
- multiply balls all by three
- multiply highest current ball by 3-8 at random
- autogun ball (new temp ball. Shoots projectiles continuously at whatever tile is closest to it in the previous last second before switching to shoot at another target)
- Homing ball (new temp ball. locks onto a random valid tile and is pulled towards it by gravitational acceleration force, it will collide against any time upto 5 times before giving up and behave as a normal ball until it's reactivated into homing ball mode again after collision with players paddle ship. Each bounce except for the last one while in homing mode will give +20% speed boost to the ball, mainly to compensate for the gravity force potentially slowing down the ball. Max total of 25 tile bounces before the ball breaks and vanishes.)
- raptor ball (like flubber ball but as a temp new ball and tries to aim for a closes tile after bouncing against a tile, with 170 angle range from tile edge it just bounced off instead doing a random angle. Does up to 10 bounces before expiring.) 

Note: some powerups can stack for increased effect and will affect all non-temp balls. Some powerups usually last 60 seconds with additional same type pickups adding another 60 seconds on top of the existing time remaining.
Note2: other powerups just spawn a temporary ball that will expire once it runs out of ammo/energy/time.

### Ship powerups 
- barrier (temporary invincibility).
- shield auto-consumable (incoming hazards will automatically be absorbed and nullified by shield if player hits them, deducting one use from inventory).
- ball net field (temp barrier at bottom of stage that bounces balls up as if the paddle had bounced them. Like a safety net that last for X amount of seconds.)
- ball saver net (same as above but limited hits instead of timer).
- ball glue (catches balls and cancels it's existing momentum, mouse 1 to release again)
- ball magnet (similar to glue, catches balls but preserves it's existing momentum on re-launch)
- ball gravity field (auto pull/guide balls towards center of paddle of they're traveling in a downwards trending direction.
- ball elastic tethers (activate on demand to reel balls towards center of paddle no matter where they are, using ethereal tethers)
- powerup chance luck increase (set powerups to appear 10% each time a tile break)
- bounce angle control (normally balls will bounce off paddle as is, but with this powerup the more left or right the ball is when it hits the paddle, it let's player force it's bounce angle to go that way.)
- laser blasters (shoot 2 laser bolts upwards from sides, 1 dmg per bolt).
- micro missile salvo (shoot 4 projectile that each choose a random tile and fly towards it, dealing one tile damage per hit.)
- (Note to self: below four weapons with a + are directly inspired by javagameplay alien invasion weps)
- spreader blaster + (shoots 5 projectile in a spread, 1 dmg per projectile).
- laser line beam cannon + (from center of paddle, drop an projectile emitter at the last location paddle that stays there even if paddle goes away. This emitter continuously fires a beam that deals 1 damage rapidly to anything in its way, usually punching pretty deep into a tall vertical column tiles of tiles, especially if its rampage isn't dampened by hardened tiles. This emission lasts for 1.5 seconds, launching about a total of 25 projectiles worth of damage. Not sure whats the best solution for the beam performance or implementation wise, but that's the general idea)
- striker missile + (single high damage exploding missile, deal 3 DMG in a 3x3 area where it hits. Locks on to high value targets like turrets or enemy roaming drones of those are present, steering sharply towards them as it flies up.)
- nuke detonator bomb + (first press launches a bomb, second press or impact detonates it, creating a large slowly expanding circle shockwave that deals 1 damage every 1 second it touches anything. Expands for about 3 seconds before rapidly shrinking Afterwards for another 1 second, still dealing damage during that time).
- emp wave gun (fires a wide projectile that phases through all tiles, but if it passes over a turret, the enemy turret will be stunned for 5 seconds additively. Otherwise harmless, just gives player breathing room to have one less hazard flying at them, especially if they deeped into the enemy ship that players balls can't reach yet.
- auto pd turret (within a limited radius around the player if there are enemy projectiles incoming, this weapon will automatically aim at them to nullify them if the player presses the firing button.)
- graviton beam emitter (charges up a single shot for 3 seconds that once ready, launches directly up and annihilates anything in its path with some width, despite visually looking like a very thin intense projectile that has an invisible aura of destruction. It flies up and exits the stage from the top.)

(Note: All weapons have limited ammo and will expire once spent. Additional powerups that award the weapon will give an additional supply of ammo on top of what still left.)
(Note2: All weapons(and other non-weapon powerups) may have a super and mega versions of them, having enhanced damage, shot count, width/size, blast radius, ammo count or status effect duration. These depend on per weapon basis and are rarer than regular weapon powerups.)
(Note3: some powerups will override others of the same type like glue vs magnet, or the various weapons, while others can be used together with other powerups seamlessly.)

### Tiles types
- normal (ball collides or weapon shot connects, tile breaks. Simple).
- multihit (normal with more than one hitpoint)
- hardened (normal balls don't damage it and it doesn't count as objective. Certain powered up balls and weapons can demolish it though and against those it only has 1 hitpoint).
- multihit hardened (same as above but with more than one hitpoint)
- hardened on one side, but normal on the other
- actuated (initially tile will let a ball pass through it, but then will become solid)
- actuated multihit (same as above but takes more than a single hit to break)
- TNT (blows up stuff in a circle area)
- frag (launches an even radial spread of projectiles instead of aoe blast)
- Claymore (narrow spread of projectiles depending which direction tile is facing)
- unstable claymore (same as claymore but narrow spread direction is completely randomly aimed in any 360 direction.
- thunder (fires lighting at random tile it can blow up/damage)
- rocket (launches an explosive projectile in direction tile is facing)
- cluster rocket (similar to above but besides the main central explosion, it releases 4-8 small bomblets around, creating smaller secondary explosions too. Bomblets self destruct if they travel longer than 2 seconds.)

Note: some tiles have super and mega versions that either are tougher and/or have stronger or more numerous effect.
Note2: all tile types can be rotated to face up, down, left or right.
Note3: names above are placeholders; in reality the game is themed as a taking down large armored imperial military ships with many tiles as various random internal components, subsystems, modules, electronics, crew quarters, machinery and superstructure. As the game's name implies, these big ships often have a design that has exhaust ports or similar weaknesses that a small nimble ship can exploit to create massive damage with a few well placed bouncing projectiles tearing up the inside of these armored hulls for satisfying carnage. So instead of a TNT tile, it might be a fuel tank, while a thunder tile might be a power capacitor or a reactor unit, etc.

### Turret tiles 
(some tiles have a turret installed on them that occasionally shoot predictable and often easy to dodge projectiles. They sort of override the tile underneath them with an new hitpoint count contextualized as bolted-on armor. This means to destroy the tile player has to hit it the amount of times the turret has armor and then the tile underneath the turret will perform its own effects (TNT, thunder, rocket, frag, etc.) as both the turret and the tile simultaneously break. Turrets therefore cannot be installed on multihit tiles nor hardened tiles.)
- single blaster (launches a medium speed projectile towards last player ship position, fairly easy to dodge)
- double shot (same as above, but shoots two projectiles with a slight spread)
- Triple shot (same but shoot a wider spread of three projectiles)
- Charge sniper (starts dormant but may randomly decide to activate, which will activate a laser line pointer, trying to track player, then growing the line in intensity until locking on to a spot to shoot at, then firing a single high velocity projectile at that spot. Player can dodge the shot as long as they get out of the way in the 1sec delay period after spot lockon happen and the shot launches.)
- plasma orb launcher (a slow moving large projectile that is lazily launched towards player ship, trying to use it's wide hitbox to hit the player.
- dumb artillery (randomly designates a spot to fire somewhere in the players movement zone, creating a timer before an AoE blast occurs at that spot. Player simply has to avoid that circle not to get hit.)
- tracking artillery (same but leaves the targeting circle right on top of the player, so player simply has to move out of the places circle not to get hit.
- laser pulse cannon (point directly downward and fires a short-lived line that player shouldn't touch to avoid damage. Has a 3 second charge up before firing it's pulse laser. Has a 3 second cooldown period.)
- laser beam cannon (same as above but the laser line lingers for 3 seconds before vanishing. Sort of an area denial. Has a 5 second charge up before firing it's continuous beam. Has a 10 second minimum cooldown.
- missile turret (launches a slow homing missile towards player that tracks and course corrects towards players ship, but have limited/slow turning ability and stop tracking after flying for 2 seconds. They are easily dodged/juked into missing the player.)
- zap-drone (randomly wandering contact bot that may collide with player ship to damage them. Hit drone with ball or weapon to break it) (inspired by n++)

Turrets work as a network by firing one turret at a time, with a random 1-15 seconds delay between choosing to shoot the next turret in the queue. Generally all turrets are  only one of various hazards, so theyre not relentless.

Turrets may have light, medium, and heavy armor or none.
Turrets may have regular, super, or mega versions with more damage, or some other stat that makes them more dangerous than their lower tier variant.

### Non tiles 
(placed on background, they don't collide with balls but a ball passing over their area collider may apply effects on the ball or trigger an effect from that tile. Does not count towards destroying ship but can be destroyed by a nearby explosion. May have one or more hitpoints. Some will only trigger if ball meets certain criteria, like not being too wide or not being too narrow etc.)
- one way portal/tunnel (a pair of objects that are linked together; one is entry, the other is exit. ball will enter one end and leave out of the other one, preserving momentum and direction. Has size restriction of not allowing large balls in)
- two way portal/tunnel (same as above but both linked paired portals allow entry/exit instead of being limited one way.
- launcher (if ball gets caught into these, they will ejected in the direction the launcher is rotated to point at, one of 8 directions.
- rotating launcher (same as above but instead of firmly pointing in one way, this one may rotate clockwise or counterclockwise, 

### Events
- anomaly floaters series: these arrive on the stage at random edge and flutter/float about randomly around the stage, disregard all tile collisions entirely, bouncing off the edge walls about 5-15 times before exiting by floating off screen and deleting themselves. Usually they will have some interactions by colliding with paddle or balls. Lorewise they're part of the weird space weather, normally not belonging to anyone, just a natural local occurance. Some may be useful, some dangerous, some a nuisance or exploitable.

## Player controls
- widen/contract ship width.
- timescale control (slowmo, normal, speedup, 25-200% range with 25 increment/decrement per press, plus additional range of 5-25 with increment/decrement of 5 per press.
- cycle available weapons/consumable bonuses.
- player doesn't launch balls; they release them gently and then can use their paddle ship to punt them and give them speed.
- player can soften their ships bounce surface on demand to halve the momentum of the ball to make it slower. They can also harden it to make it double the momentum too, on top of using a paddle smack.
- paddle ship is a smooth bar with rounded edges; balls bounce off according to their own trajectory of hit in the flat surface, but player can intentionally use the rounded edges to alter the trajectory with clever positioning.
- the paddle ships backside has thrusters and a ball generator.
- the balls are energy orbs and each newly released ball takes a good chunk of energy that gradually slowly regenerates, giving the player infinite slowly replenishing ammo. Player is encouraged to use the ball they have as long as possible before launching a new one.
- losing balls is fine. They will not result in a game over or lost lives.
- the gravity launcher from Momentum Missile Mayhem 2 is the primary inspiration for the balls, energy system, HP system and selectable ball types. Paddle behavior and ball bouncing is primarily inspired by Winbrick 2000.

Generally game is primarily controlled with mouse, mouse buttons and mouse wheel, with several hotkeys on the keyboard for auxiliary functions.v

## Metagame

### Low Metagame
Demolish a specific local clan/gang fleet. They have their own colors, own clan name, somewhat inspired by those mechwarrior/battletech universe clans.

### High Metagame
Wage a tactical war against the war fleet of many clans to bring their nation to ruin, receiving randomly generated news as reward, saying how the leaders and people suffer in all sort of mundane and bizarre ways and end up getting replaced by a new person after they push the last guy out of an airlock. After about 100 campaigns the nation is in tatters and the player hunts down remnants, with some extra new quirk or twist added to the low Metagame campaigns - featuring even more badly designed ships and even wilder generations. Creating a log of trophies of yet another scumbag clan/gang deleted from the Helios sector permanently.

## What I wrote first before writing any of the above when I got the seed of idea of this game in my mind
(heavily inspired by the brick breaker game genre)
(straight up winbrick 2000 clone, but themed with blowing up an oppressive empire's armored space stations, space battleships and fortresses, plus many other changes and upgrades.)

Old name: "Death Star Exhaust Port Havok"

Basic idea is that player controls a typical arkanoid paddle as a drone ship that launches a ball and tries to get it flung inside the exhaust port(s) of a large brutalist style warship or a military spacestation or battlestar or spacefort, with the aim to obliterate it from within by exploiting its exhaust ports and shafts as a weakness, playing into the best parts of the brick breaker genre while changing everything that sucked about it. Meanwhile said ship is trying to shoot down the player with its turrets and unintentionally "shooting the player down" with it's exploding fiery debris that get chaotically ejected out of the target ship as some specific tiles of it explode, like fuel tanks and what not. Usually the outer plating is hard, but there is one or more convenient narrow exhaust port to aim for. Supplies will drop from the breaking ship, giving you weapons, powerups and other goodies to further devastate it both from inside and outside.

Momentum Missile Mayhem 2 style energy orbs as balls, an energy system that limits spamming and promotes preventing ball from escaping below instead of forcing player lives to be tied to the ball.
Have an elastic tether as default equipment to avoid annoying "oh crap I punted the ball wrong and too gently, now its really slow and going to take 14 seconds before I can punt it again" problem. Elastic tether is a powerup in some arkanoid clones that lets the player press a button to pull balls back towards the center the player's paddle from anywhere on the stage.

Name ideas: "death star exhaust port brick breaker", "bunkership exhaust port havok", "brickship breaker", "stoneship fleet takedown", "bruteship ball buster". Something that evokes the spacecraft destruction that has an outer shell that is rocky or concrete like - looking like a flying bunker with greebles, with maybe a reference to brick breaker genre in some way.