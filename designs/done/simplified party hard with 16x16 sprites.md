# Party Hard but Mini Hitman Spinoff idea

## About
"Party Hard" is an indie game by the developer Pinokl Games that has the player take control of a serial killer that goes to random (celebration) parties across the country and attempts to kill everyone in the party before leaving the area. Player character tries to kill each character (party goer, bouncer, staff) in a way where no one sees them do it as it would cause the police to be called (the witness would run to a phone and call the cops) and have them chase down the player to attempt to catch them. Player can attempt to evade, but each police summon is more persistent than the last one and eventually it will become almost impossible to not get caught - so player must be as stealthy and efficient as possible.

Party Hard as a game was fairly fun - despite its gruesome/unhinged/controversial theme/premise, it offered a cathartic puzzle game that was both challenging and stress-reducing. It featured a plethora of parties from bikers, to stoners, to nightclubs, to halloween parties, and other wacky locations. It had a level editor too which allowed users to create an endless amount of new levels - and they did, hundreds if not thousands of new levels.

But it also fell short in how many elements in that game hard-coded or assets were rigid in the sense that they were only allowed to exist in a specific direction and couldn't be rotated - weren't modular or standardized. My project aims to capitalize on those short comings and offer a better version of the game, but go for an even more low-rez look so that the violence is kept cartoony and vague much like in the original. Theres clearly a market for game like this to burn away frustration in a safe way by letting the player let off some steam as a serial killer solving a puzzle of how to clean up an entire venue of people without being seen/caught in the process.


## Design parameters of Party Hard

### General rules
- Player unit does stabby stabby.
- Player can terminate or outright delete party goers if they in proximity with "useful" interactables, like push someone into a fan blade box or make a stack of logs roll on top of someone, crushing them.
- Player can trigger contraptions to delete one or more characters, either without trace or leaving a normal corpse that can be detected/found.
- Level has party goers that patrol routes, some roam, some stay in place, some change based on events during game (like seeing a body). Uses AI nodes for them to path find to them as best as they can, assuming the world wasn't designed poorly where they'll get stuck.
- Has police to go arrest someone who got sus'd.
- Bouncers can knock you if you try to get close from front.
- Secret agents will chase and get you unless you sneak behind them.
- Besides people, there are animals that can also count or not count towards kill count.
- Player can run until police get more chase time and eventually outrun the player in most cases.
- Level has shortcuts that close if used during escape with a long cooldown.
- Medics will enter map to cover dead ppl with body bags.
- Player can pickup and drop/dispose of bodies to avoid other live ones from seeing the body and becoming more frightened. Use dumpsters etc to hide bodies.
- Player can poison things to get party goers killed off.
- Party goers may go to spots to sleep or just doze off where they stand.
- Player can get items to aid in killing or getting away. (Smoke bomb (obscure vision to allow easier killing without being seen), pizza box (group lure), disguise (evade police), timebomb (kills), stun bomb (knocks out a bunch of people that are easier to stab without them calling the cops), running shoes (better chance at outrunning the cops), etc)
- Player can have different classes with special abilities or traits (ninja, cop, default guy, chainsaw man, lady, etc)
- Trap types include timed, wandering npc proxy activated, instant activated (aoe), player n npc proxy instant use, repeat use activate (think horse).
- Characters have vision cones in left or right. Maybe expand this to 90'.
- Staff members also are characters amongst party goers.

### Player classes

Darius (default guy):
He starts with a standard knife and no bonus items or abilities. The main lore of the game is "its 3:00 AM and theres a loud party that doesn't let Darius sleep, so he goes there to shut them up". Obviously not something to act out in real life, but definitely something that is a relatable situation and this game lets a player live out that revenge fantasy in the safe confines of a video game with a mildly cartoony stylized artstyle.

Police guy:
Is able to carry dead bodies without any suspicion, but he is unable to use traps or pick up bonus items. He starts with the standard knife and a wrench item that allows the Policeman to transfer suspicion to any partygoer.

Ninja:
If anyone sees him moving they call the cops, but he can stand still to turn "invisble" to partygoers. He comes with a ninja sword and an endless supply of smoke grenades, which should be used to evade detection. His smoke grenades can be tossed in any of the 8 cardinal directions by holding a direction while also pressing the "use" key, and detonate after a second or two.

Lady:
She knocks people out before killing them. Otherwise same as Darius.

Chainsaw Man:
The Butcher starts out with a chainsaw that can be used for a duration of 3 seconds for a burst of kills by running through a crowd freely, the drawback being he has to rest for 5 seconds after use and doing a chainsaw sprint in the wrong place at the wrong time can leave them easily detected by other party goers and rapidly arrested afterwards.

(Comment: Interesting lineup, but kinda rigid, lacking loadouts and modularity. Makes either modding/creating new characters too difficult. I think a better solution is a base character that can be customized in color and starting equipment + passive ability + special active ability on cooldown using a simple but robust system that could work as a relatively simple character creator.)

### AI nodes:
Security:
- Go here and Flip left
- Go here and Flip right
- Go here and Pause 1, 5, 10 seconds

Staff:
- Go here and Flip L/R
- Go here and Pause 1 5 10 
- Go here and sleep for 30 secs, occupy space if free, otherwise pause for 1-5 then move else.

Party goers:
- Same as staff but different node set to not conflict with.

### Level:
- Walls.
- Doors(only open and visible through if anyone near).
- Props/furniture solid (see thru or vision blocking).
- Non solid decor obj.
- Spot for police/medic/maintenance guy(shortcut blocker).
- Spot for party event arrivals/leavers.

### Random event:
- More party goers arrive (1-9x)
- Bear arrives (it will randomly eat someone)
- UFO land and steal someone, no one bats an eye
- Pizza man (drops a pizza box that causes a bunch of party goers to flock to it)
- Engineer/item giver

Game is about the thrill of how much you can eliminate before anyone notices anything.

===


## New - more Hitman adjacent gameplay

Play as covert hitman (player can choose outfit and colors freely in character customization), that goes to club parties of known thug/gang ownership and eliminates them all for their crimes. It refocuses the game to be less about waiting and having more proactive abilities to make play relatively faster - sort of like playing a Hitman/Agent 47 game. Player still has to worry about being detected and being chased down by police/bouncers/agents.

Player gets to pick a loadout of 2 weapons to carry from a limited pool of 4 weapons offered per stage, and two stacks of consumable items, also chosen from a grid of 4 choices. The total pool of available weapons and items is much bigger, but the starting selection in each stage is deliberately limited and random to make each run varied and surprising.

Player can find weapons and items that they can swap to and items and weapons are often plentiful. leaving the previous item on the ground can be picked back up/swapped to again, they don't vanish. Weapons are simple a spawn a raycast, rect/circle collider to determine if target is knocked out or killed or outright deleted (no body, just a stain).

While typical traps seen in Party Hard exist that require waiting for people to be in range for them to succeed/work, in the hitman version of the game items are more common and often times the weapons/items provide the power of traps more readily. This prevents the game from being mildly a chore to play especially in situations where a level is sparse with traps or items and therefore the player is forced to tedious stab each party goer one-by-one in a painstaking way that is less fun.

To counter the added ease the new abundance and portability of weapons/items, items will more commonly create sound or light which can attract unwanted attention more easily, forcing player to still be careful not to have their cover blown.


## Graphics & Levels
Original party used a freeform pixel canvas to place walls, objects and spawns/nodes. Characters were animated sprites of 16x32px with animations for walk, attack/action, sleep(draw zzz over head)/fall/die(no zzz like sleep and draw a blood pool/stain decal)/get up(if animation reversed)), dance/party. "Run" animation was just walk animation sped up. Any other effects/states of a character were depicted with icons over the head of the character, like a phone to run to a phone to call the cops, or a siren over a dead body if said body was discovered by another person - eventually either police or medics would find them and carry them away. I'd say the animation frames were around 2-4 frames depending on the state, so fairly cheap.

For my game, while the original freeform walls were for building stages in broad strokes, it made it less compatible for procedural level generation, destructible walls were less of a thing and overlapping walls were an issue.

So instead I'd want my game to use a 16px square grid where wall, floors, objects characters all that a standard 16x16px size - allowing me to utilize the plethora of 16x16px asset packs that exist out there for creating tons of different party themes and party goers.

Characters are freely moving 16x16px sprites and theres sort of XCOM Apocalypse style floors and collapsing mechanics so the levels can be procedurally generated as multi-floor buildings, the supports can be knocked below or walls broken to make new routes, and cause above floors and walls to collapse down if all supports below said floors have been destroyed.

This will allow for destructible terrain + tools/weapons to affect it, multiple-floors to explore instead of a single flat stage, procedural generation of stages that work similar to roguelike dungeon generators with "stairs/ladder" tiles that let a character traverse between floors of a stage, but commonly having a base plate with buildings placed over it instead it being an enclosed underground dungeon thing.

While walls and props are destroyable - usually through interactable objects, explosives or certain player weapons like slow-use sledgehammers - it will be uncommon/rare for said destruction to happen and it is also disadvantageous to break too much, since it can either destroy traps or increase sight-lines that otherwise would have provided privacy, making stealthy kills less easy.


## Weapon & items parameters expanded
Generally the items and weapon system would have a bit more parameters - things like if it can damage/destroy walls/objects/props, how big of a sound and/or light radius it produces, how concealable it is (how close can player be with this weapon on them near a party goer before they notice and freak out to call the cops), and how many points of damage does it do (props and walls may have different hitpoints before they break). 

Melee weapons wise can include the knife(single-target one-by-one instant kill), baton(knockout one person, then kill if used again, one-by-one), katana (instant kill multiple targets in a hitbox/raycast area at once), sledgehammer (deletes person into a stain, good against breaking walls, loud) and maybe a few others that have different parameters and have different swing time and post-swing recovery time, range, concealability, loudness, damage against props/walls.

Simple firearms can be a thing too that launch a projectile, have an ammo count (no reloads or magazines, they're more like guns from hotline miami - use up and discard), projectile speed, rate of fire, spread, number of projectiles per shot, damage (per projectile), as well as the usual sound/light thing + damage flags.

Still, given the game is about stealth, firearms are rare and very risky to use due to light and sound, have limited ammo and are harder to conceal. Like a 9mm pistol is very concealable, but loud, meanwhile a silenced pistol is less concealable due to long silencer, but quieter. A shotgun can take out multiple targets, but its absurdly loud and almost impossible to hide from line of sight.

Weapons are always concealed when not in use, but concealability proximity detection depends on the least concealable weapon equipped on the player.

## Controls
WASD for typical top-down movement
Shift for running with limited but recharging stamina meter
Mouse to aim Weapon
Mouse1 (left-click) use weapon 1
Mouse2 (right-click) use weapon 2
E to interact (context sensitive, usually used by standing in proximity to trap trigger object or trap object itself and then waiting for a victim to walk by to use it, hopefully not wasting its limited use(s).)
F to use selected item
R to use cycle to next item (can carry up to 4 items at once)
hold Q to dance/disrupt - if done for atleast 3-5 seconds continuously may cause some people to either gather around to enjoy dancing with player character, leave the area out of annoyance to player character or rarely punch in the face (temporary knockout, no damage). Its random and unpredictable as people and their preferences are.
Shift+M1 or M2 or E: drop that weapon/item to floor. Pickups can stack on the ground with a first-in-last-out principle if trying to pick them back up.

## Metagame Stuff
Low metagame, high metagame, Trophy Log + exaggerated memory replays (no sepia filter, but yet to vignette, film grain, deeper sound, 3x more bombastic explosions and particle effects.).

High metagame is a worldmap with pins for each succeeded campaign of 3-12 stages. Stage amount in campaign determines pinhead size. Color code of pin tell the style of campaign it was. High metagame acts as a loadout screen and generator for endless new low metagame campaigns. Its satisfying to fill up a world map with pins of completed runs - starting with a blank map and adding more and more pins until its so full the map disappears underneath them. These runs can be also viewed as a list that the pins link to as seeded campaigns the player can replay as a flashback with the exaggerated memory effects/filters turned on, sort of as a mini-newgame+ thing.

Low metagame is a linear string of 3-12 stages as per player choice in how long of a session they want to go for today 3 stages is small, 6 is normal, 9 is big, 12 is extra long.
Usually the first stage is always quieter/sparser/easier, and the middle ones are a fluxuating random difficulty/busyness, and the last stage is usually crowded or harder in some way. And as a bonus for playing longer campaigns, they tend to get crazier and bigger ranges for the last map or otherwise make something accumulate in a bigger way than with smaller campaigns.

About the color of pins, to be honest I don't have a clear idea for this aspect yet, but I envision a mutator or modifier that influences the campaign so that besides the stage randomization via map procgen and placement of characters, choosing a theme, time of day, weather, pickups, etc. a modifier/mutator would also change something about how it feels to play a campaign - usually in some fun way in how it affects mechanics or events in some way. It could be just the theme of the parties, as different parties have different color codes assigned to them, as different parties have their own tilesets and partygoer character skins/graphics.

But if it did affect gameplay, then maybe stuff like "1.5x more partygoers, partygoers are slow/fast, items have smaller sound/light radius than usual, explosions are 2-3 times crazier" ...stuff like that.

Maybe the pin's color is indeed a theme color code, but a pin outline or symbol on it indicates a gameplay mutator. That way its best of both worlds.


## level gen and assets notes
- a base plate of texture ground + areas of water (inaccessible to everyone, but must never block off player/partygoer access to the rest of the stage.)
- square grid based everything, though characters are not locked to grid for movement and move smoothly, not by grid space hopping.
- when making buildings out of rectangles, have some tiles of edges have a chance to be a either a door (walk through, blocks view while closed, is closed while no one near it), an opening (just that wall segment removed, free access and vision) or a window (cant traverse, but can see through).
- randomly placed furniture or props or carpets/walkthrough on-the-floor-props near walls, usually center is clear unless its a really big room. Placement of furniture should not block passage even if its otherwise destroyable.
- random deco object on floor (pass thru) based on indoor or outdoor. with an ultra rare chance for indoor objects to appear outdoor.
- spots for pickup items to spawn on floor so player can walk up to them and pickup/swap them for what they have. Items/weapons that would alert others if carried by player will not cause alarm or be cared about if they're on the floor (its a game contrivance that is deliberate. I could add a mechanic to cause people to call a janitor to take risky items away, but the usual chance of people walking by item spawns is too common that I must have them ignore them for sake of more fun gameplay).
- people spawned in random facing directions in clusters around free spots + a few stragglers. (Deco (pass-through) spawn spots count as free spots too)
- start/exit spot
- since everything is a 16x16px sprite, party goers will depict they're sleeping by rotating their sprite to lie on their back and small particle effect to spawn "Zzz" above them or equivalent light-blue pixels to communicate it symbolically. If they're knocked out, use yellow particles/pixels spinning above them to indicate that state. Draw a red blood pool on tile if they got killed there. Draw a stain with tiny meat kibble if they were obliterated so hard no corpse was left.
- game is data-driven in terms of assets, weapons and items. Maybe moddable, but atleast easy to expand with new content. Everything added to the game is loaded into the pool next time a new campaign is generated. Game auto saves between campaigns (permanent persistent global savefile), so theres no issue if content is removed/uninstalled from the pool - the generator will simply work with what it has available without running into a "missing content" error.

There's a random pool of indoor floor textures, outdoor base plate textures, party goers sprites (player uses these too), wall segment textures, door textures, deco object interior sprites, deco object outdoor sprites. Some are tied to specific party themes/sets, others are global/common.