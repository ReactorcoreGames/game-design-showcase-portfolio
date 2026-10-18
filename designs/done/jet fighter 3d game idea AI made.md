(Note to Claude: This project actually contains two separate games, a V1 - Version 1 - which is a simplified 3d fighter jet game, and a V2 - Version 2 - Which is a more transforming jet-mecha hybrid in more diverse 3D free flight environments both in space, orbit, moons, exoplanets and nebula clouds than just typical planet earth combat flight sim locations. In the initial request, I will specify which one were going to be working on, so only do one of them, while disregarding the other.)

(Another Note: I wrote document as an on-the-fly brainstorm. First I defined broad ideas I want to chase, then piece by piece formed the various main aspects of the game in the order that made sense for this given project, sometimes creating new better version later on that override the ones before. At first I began with the V1 version context, but later added V2 as an alternate game that uses many parts of V1's core systems, while making some changes and additions in V2. Both projects are valid and I want to make both of them eventually.)

# Games

V1 Game - Modern fighter jet simplified air combat sim 
V2 Game - Transforming mecha/jet simplified air/space combat sim

## Inspired by:
+ 'Fighters!' (Mobile 3d jet fighter sim game, very simplified, streamlined/arcade-ish, but realistic).

<description>
Description for 'Fighters!':
Experience the first-ever 3D Air Combat Action Game for your mobile phone.

Accomplish interception, ground attack and escort missions to earn money. Fly four different planes, all with unique characteristics. Select your arsenal before each mission, ranging from air missiles to guided bombs. And take a wingman with you if you need support against your challenging enemies.

"Fighters!" also features a large terrain with a visibility range of ten miles. A dynamic camera helps you to orient during combat and shows the targets you blow out of the sky. Computer pilots that fly evasion manoeuvres, aggressive attacks and react differently everytime will challenge your skill
</description>

## Also Inspired by:
+ Standalone/gunmetal (jet can transform into mecha anytime, Macross style mecha and combat style, overall gameplay).
+ Gundam 00/Wing (celestial being/project meteor, plus the mecha and weapon designs in general).
+ Websim.ai rosebud.ai claude.ai etc. (it can realistically achieve in re-creating a similar simple jet fighter 3d sim game, which could then be easily upgraded and improved with more content, effects, actual, models, etc.).
+ XCOM (each pilot death is a recorded unique name.).
+ Freelancer (the engine cutoff drift thing, maybe some weapons systems too).
+ Michael Bay transformers (their weapons, the explosion effects styles, the brutality and rawness of the action).
+ Nali weapons 3 (its a UT99 mod. Massively overkill super weapons, and the oversurrector thing that overcharges regular weapons and super weapons into hyper weapons).
+ Bomberman hero/starfox 64 (simplified expanding sphere explosions, laser bolts, projectiles and low poly art style).
+ Asset Forge (if ai can't make my stuff, Asset Forge + deluxe prims will be the main suite for all 3d models needed, unless there are other useful sources I can tap into too).
+ Jager (IMAJ system for all entities, including player).
+ Lost planet (player can pickup and use oversized mech weapons on foot, similar to dxm boss weapons grab and use).
+ Floppy heroes/starfox 64 multiplayer combat (flat arena worlds with all range mode and the border bounce launch mechanic at map edges.
+ Freelancer (tractor beam to grab items afar, draw beam and then poof they're yours).


---
## Plot (for V1 mainly, V2 spins it off into its own thing, heavily inspired by the Crusher Joe anime):
Secret international ideological rebel group against dictators develops a squad of powerful fighter-mecha weapons and do the 'Gundam 00 celestial being' thing of going after evil militaries/police/regimes to topple them through simple eradication. 

Basically, they destroy their militaries, kill the cunts, destroy infrastructure of evil (slave camps, organ harvesting hospitals, cover up crematoriums, blacksites, polluting factories/plants/refineries, surveillance and oppression centers, dual use civ-mil things, biolabs, wasteful ghost cities, segregated gate keeping elite communities, corrupt schools, propaganda centers, poison drug factories, apathetic exploitation hubs and greedy profit over lives related places/facilitators/enablers.

Point is to provide a cathartic run n gun experience to live out the fantasy of ending suffering of the common human and destroying evil in the most obvious and clear way that people in power don't bother to do because they're often benefiting from it secretly, naive and are well protected that ordinary citizens can't do anything about it.

### Seasons/DLC:
- Russia
- China
- Isis
- Venezuela
- North Korea
- Afghanistan
- Hezbollah
- Neo nazis
- Black rock/corpo dicks
- Egyptian military elite
- (Other ones, I can look em up later).

Granted, I will use stand in names and flags for them, but color schemes and deco flavors will remain tailored to evoke their things, like Russian z stuff, Chinese ccp slogans, north Korean poverty, venezuelan Hispanic stuff,  Egyptian military elite class vs poor commoners, skinheads with swastikas, etc.

Funnily too, I can also offer skins for player mechs for things that represent mostly good things like Taiwan, Ukraine, Tibet, Uighurs, eu, Israel, usa, +any other countries or groups that have ethics, morals and values human life, diversity, equality and LGBTQ stuff.

Game will take in place on earth in ground, sea environments.

Alternatively game or it's sequel or spin off be moved to a Crusher Joe (anime/OVA) style universe where game takes place in planets, moons, orbit, space, etc. (this is what V2 is about).

---
## Gameplay design:

### V1
Terrain where player spawn at 20% edge of map (already in mid-flight, from sides of map cube area or top of cube, diving down from above at an angle) and then has a bunch of enemy targets to destroy around the map. Some targets are aerial, some ground, some are non-combat and don't shoot back, while others have rudimentary projectile attacks against player and rudimentary attempt to fly towards player. 

Distances are pretty big and player uses jet mode to fly fast with the awkward limits of strafing run nonsense that jets are restricted to, but player can also morph into a mech at will and quickly turn to face any direction with excellent omnidirectional mobility, but jet mode will always provide fastest max speed and acceleration.
Jet: sucks at turning, but very fast at forward flight
Mech: limited max speed and slower forward acceleration but very fast at turning around and can dodge sideways and fly omnidirectionally. Boost centric/driven movement.

Both modes can turn off engine to drift in the direction they have momentum in for even faster turning speed and "self toss omnidirectional strafing runs" attacks.


---
### Weapons are simple: 
dumb fire manual aim and homing with lock on. Smart gun auto aim is also an option. Single fire option, switch with key, carry upto 2-4-8 weapons, can discard and pickup new guns on map.

Maybe have usable items too ala cryptark. Triggered via hotkey.

Weapons are either:
Physical Projectile (comes from barrel, flies and collides).
Cone area, Cylinder area, Line area, Sphere area (charges up visually, when at 100% will actually inflict attack after delay.
Expanding shapes (sphere, cylinder, line, come, but instantly damaging upon contact).

It is possible to create a wide diversity of both ranged and melee weapons.

### Weapon considerations:
- Max range: (lifetime or timed detonation. bullet evaporate or missile breaks or detonates)
- Area of effect final size and Proximity detonation range too:  (Can be instant or progressively expanding)
- Charge up or lock on delay: hold down trigger until 100% to fire.
- Rate of fire.
- Projectile count per shot.
- Projectile spread.
- Projectile speed or expand speed.
- Projectile or shape acceleration (gyrojet, bolter, or sweeping laser beam) (increase speed by x every tic/second).
- Max ammo.+current ammo
- Homing or dumb. (How quickly does projectile try to orient towards target)
- Smart or manual aim. How quickly does true aim (as opposed to player aim) move to match target leading reticle.
- Lock on speed.
- Recoil/kick (Apply momentum to user backward or forward).
- Impact pull or push (same as recoil but applied to target instead).
- Screenshake magnitude (length and intensity affected)
- Impact effect delay
- Elemental type(which overkill visual effects to use upon enemy kill? Standalone inspired.)
- Weapon mass (negatively affects acceleration, max speed, turning speed when equipped or firing, boost force. Positively affects thrown/dropped impact damage of discarded weapon, exponentially boosts solid type melee weapon momentum damage).
- Weapon equip activation delay (require weapon to wait for x seconds before it becomes usable after attaching it to self) can show cool hud info during this.
- Weapon durability: how many times can it hit after thrown or how big of an smash impact can it take before breaking. 0 means infinite.
- Cost/rarity (for metagame and loot purposes)
- Turret delay to turn (how much a turreted/player held gun lags to turn towards cursor? Note mounted guns have
- Mounted gun aiming angle (0 = only straight, must turn entire vehicle to aim, 45 = can still aim towards cursor up to 45' degrees before needing to turn vehicle. Turrets can also be limited by this to create blind spots in weapon arcs. Anchor point based on original placement direction of turret.

### Unique Weapon assets:
-gun/attacking in use frame (note, these may be generic main types (short gun, long gun, missile launcher, melee a, melee b, heavy/light variant, etc.) and then I can represent them via sprite hud ala rainbow six mod gzdoom, taking stuff from mecha soldat/era to do it.)
-name
-desc
-stats file

### Universal assets for weapons
- sounds: pickup, throw, drop, impact scale 1-3, activation ok signal (ready to fire) after pickup, out if ammo click, 
- flash/muzzle
-projectile/activated frame
-firing sound
-charge activation sound
-explosion
-impact fx (various)
Proj boost acceleration fx for missiles 
Trail (smoke, heat orange glow, em blue traces, railgun burn explodings, photon, neutron, positron, tachyon phantom).
Smoke vent, heat vent, shell eject, sabot peel off, electromagnetic surge, spark burst, backblast, plasma vent...

### Limitations/misc: 
+ No firing arcs/trajectories, not gravity affected, projectile goes where pointed at. ultra simple.
+ User of weapon can damage self too. Friendly fire is on. Enemies can FF themselves too. No infighting, just dumb FF.
+ Each weapon is a self contained entity ala hotline Miami.
+ Ammo packs or reload stations can be a thing in the game.
+ Default ammo levels are akin to super cryptark; lots of use that spraying is acceptable. No need to be frugal unless it's a rare superweapon.
+ Weapons used by player and enemy alike, ala Einhander. Player can kill enemy to steal it's weapon.
+ Depending on coding considerations, weapons either work on single mode where you can carry 2-4 of them and switch between them with a press of a button that cycle to the next one or it's a cryptark style 4 slots with four hotkeys instant fire system. Player can pickup fallen weapons by button press with proximity.
+ In V1, no multi stage weaponry like projectile that deploys into another projectile during proxy, time, impact, events. Things like smart redirecting grenades, funnels/gun drones, split missiles, cluster munitions, double/triple payload weapons.


---
## Environment:
Ground worlds are sandwiches of Y layers. A typical world is a huge cube with skybox, a flat terrain floor, an optional liquid layer on top of it, and an atmosphere layer on top of that that extends to the ceiling. Then larger indestructible terrain props are placed over terrain (forming islands if liquid layer exists, or just being hills, mesas, mountains, dunes, etc. if no liquid is present.) after that, smaller destructible deco props are placed over terrain or at specific elevations (underwater seaweed, ground trees, aerial clouds). Finally, enemies are placed within middle areas, of map, where as player/supply caches is placed at edges. Locations for either can be random within their respective zones. Enemies can be clustered in groups, first spawning one thing then spawning stuff around it in patterns, avoiding colliding them into each other on spawn, spacing them out. 

Enemies can also be spawned individually in the general area. When spawning enemies or caches, the logic goes like this:
+From top of level shoot a ray down from ceiling to determine the highest indestructible collider (terrain floor or those hills/islands I mentioned), place the thing and it's sub things, then determine the max occupancy radius of them and delete any destructible props within that radius to make a clear opening for enemies to not collide and spawn inside of a tree by accident. Note that both clusters and individual spawns can exist simultaneously.

Floor can be simply one soft color, simple vertex shading or such, or have a seamless microtexture repeating on it with a tint.

Liquid level could be alterable with superweapons to evaporate and reduce water level, reducing the starting layer height.

Same would be possible for terrain floor too, gradually making it darker tint wise until it becomes unchangeable bedrock at a certain point. It's all a matter of changing the Y coord of the floor of that layer, lowering the collider. Then again, scenery props both destructible and indestructible should be static colliders so maybe don't. Color change is still totally doable. I don't think I'll do crater/burn/damage decals unless it's really easy and performant. I am to use primitive shapes only and low poly models with occasional billboard sprite objects, not really and particle systems or decals per se.

There is also gravity that affects player when they are in mecha's ground ski mode or enemies that clearly can't fly but were picked up, knocked up and thrown, with dangerous fall damage afflicted if gravity is high and impact is too hard/fast. Moon planets or gas giants may have lower or higher gravity. Flying enemies usually resist gravity unless they are under the effect of knockback or recoil which enables gravity upon them temporarily. This can be used to push or bait enemies to fall down.

Collision damage is real and most visible with aerial enemy units colliding with terrain or solid obstacles that players can bait or push them to collide with. Player can also smash into terrain when in jet mode, but mecha mode mitigates most collisions unless extreme momentum is currently in play. There's a minimum speed threshold even in mecha mode. Upon collision player will snap into mecha mode and player will need to move away and switch back to jet mode after gaining some initial speed first. jetmode can stall out and begin to fall due to gravity but that in itself won't change them into mecha mode. Only the collision will trigger that.

Another thing is atmospheric or liquid resistance which affects weapons and movement somewhat. Weapon range decreases, move speed is sluggish, max speed is reduced, acceleration is harder, boost is shorter, projectiles decelerate gradually until too slow to exist and auto detonate themselves. In vacuum of space these don't exist, but certain nebula or liquid fields may inflict these effects too! Some weapons may even deploy smoke or fields that create this drag effect on demand to reduce incoming damage or make the projectiles slower and easier to avoid. Player or weapons may be given a special ability to generate a plasma lance that allow ignoring or reducing drag.

Space maps and orbital maps work different. It's a 3D cube with no floor (except on orbital maps that have a burn up zone below that vaporizes thing that fall into it), but instead the middle may have a radial celestial or clusters of objects (or both) or multiple celestial and there is no gravity unlike on planets/ground worlds do (except orbital maps). Here, player can only spawn at the sides of the cube, not top or bottom, but entry point can have different y elevation. (Or maybe spawn from bottom as escaping planet could be cool too, spawning just above the reentry danger zone.)

(Addendum to above, perhaps I could make it more freeform where a true celestial - planet, moon, gas giant, star, etc. - can be placed on any side with no such restrictions as top and bottom, so if a battle takes place near the orbit of a true celestial it would cover which ever side of cube, sides, top, bottom, eclipsing that side of the skybox (or appearing in various sizes of it's more distant, merely as a bg element and not being an orbital map, a kin to starfox 2's system. Then again, for simplicity, maybe sticking to a Freelancer style flat 2d space is easier to code and easier to make a metagame overworld map with. Or maybe distant celestials can appear on sides, but orbit must be below always. I think that is best.))

The celestials are not planets, moon, gas giants nor stars but planetoids, asteroids, debris fields, wrecks, anomalies, nebula clouds pockets and comets that may move or spawn from one edge of the cubes area, travel across the map and disappear in the other edge as an ambient event. Or just stay in one place. Most are static. Movers are rare for performance and gameplay reasons.

Like with ground worlds, the generation of the space map works similar process but splits "terrain" and "props/chars/loot" into separate algorithms. Instead of defining vertical layers and then spawning props via ceiling raycast downwards, a space map uses center as origin point to first create invisible sectors, labeled as 'core, inner, outer, edge, rest of outside'. These define the local space conditions, creating radial layers that define zones.

These zones can be nebula gas, void/nothing, debris/asteroid field, minefield ala freelancer, occasional floating spawned harmless shootable pebbles like that lava void in Corsair territory in FL, etc. they're always generic and sparse enough to be able to fly through them.

Next, props can either be spawned within those zones in odd number sectors while others can be spawned within the main cube area anywhere in even number sectors to avoid colliding spawns. As before, each spawned entity will creates it own exclusion zone bubble that will remove zone props or any other props from it's proximity to avoid collisions.

(Note I'm unsure about the odd even thing, technical implementation wise, but generally there's probably some good method to rely on that allows safe placement of "from core" or "anywhere in zone" spawns. Otherwise I'll just have to pick one at a time or use them smartly.)

Update to space map spawns: just focus on a radial spawning algorithms; start from center and iterate from it with increments, alternations, curves, spokes, spirals, patterns, offsets and branches. Essential have a budget of spawns, determine max distance, choose center offset, choose direction, choose number of lanes/spokes/branches, spawn one object at initial custom point, add increment to xyz axis,  spawn another there, do one on the other direction if need spokes are more than 1, repeat process until all budget is expended and make sure it doesn't go over max distance/out of bounds or be too dense to end up overlapping spawned units.

### Distances and speeds:
Every map, every battle area is always a 10x10x10km cube within which everything happens. It has a 1km outer margin that is the players zone to spawn and supply.

The rest of the inner 8x8x8km is all for enemy, base/city or loot spawns.

10km traveled at 100kmh is 6 minutes. (Regular jet cruise speed, half/60% that if mecha mode.)
At 300kmh it's 2 minutes. (Mecha Boost 200kmh or jet afterburner 300kmh )
At 600kmh it's 1 minute. (Player max speed overboost)

Plenty enough space and good speeds to not make it boring.

Projectile speeds are double, triple and quad compared to player speeds and have a lifetime of 250m, 500m, 1000m 2000m 5000m.

Missiles and rockets are 50-80% as fast as player. Categorized by cruise/boost/max speeds, so there are "slow, medium, fast" missile types.

Since maps are quite large and the amount of static prop objects is potentially in the thousands, progressive loading may be needed to make the game only load those entities that are in visual range (500m). Either way the props cannot be placed too densely to allow for enough empty space to fly fast in the area. Freelancer did it's asteroid fields well, though it used an endless random regenerating mess spawning as player moves through the area, along with occasional loose objects that spawned even more closer with a fade. V1 would focus on spawning only large and very sparse props that are always loaded with a max budget of 100 pieces.


---
## Enemies/targets:
Enemy entities are prebuilt types that have a modular mounts or turrets for 1-4 weapons. All basic and light easy units only have 1-2 gun, elites have 1-4, boss class have 2-4. Ai is numerous and use same weapons as player, so it compensates fairness by being stupid, slow, delays often, doesn't lead it's fire, can friendly fire units if they are in the way and each unit is roughly inferior to players advanced mechjet in one way or another.

Enemy units include typical milsim stuff like tanks, AA batteries, sam sites, jet fighters, drones, helicopters, naval boats, trucks, artillery, blimps, gunships, bunkers, just cause style explodable silos and other similar objects (or like those red alert 2 exploding props for chain reaction effects to blow shit up). This can be later expanded with starfox 64 style enemies too.

Assets wise, each enemy is built from these:

### Unique:
- Vehicle model with clear mount or turret spots
- Enemy stats/behaviour logic
- Name, description 

### Common:
- Enemy type icon (space, air, ground, base, light, medium, heavy, boss) depending on what they're bound to.
- Sounds, effects, hud stuff. General.
- Overkill specific elemental fx and sounds.
- Same weapon entities as what a player could carry.

No special abilities given to enemies. I want them as simple as possible. Shoot and kill.

### Enemy stats list:
- Hit points
- Move speed accel rate
- Move speed Decel rate
- Turn rate
- Move Action delay wait time
- Shoot action delay wait time (electronics of vehicle, not ai pilot related)
- Max top speed
- Stall speed (how slow to go until begin pulled by gravity)
- Weight (knockback/recoil resist)
- Pin strength (built stationary or held loosely or free?)
- (Note: Aimranges based on weapons max range, and no stealth exists in game so no need for an eyesight range param here.)
- Type mobility (ground, air, sea, space/air. Most to determine behavior if they can apply move force or not ie you can't "drive" if you got into water or midair as a tank, also icon designation as on radar and kill list).
- Size class (tiny, small, medium, large, boss, also for radar icon purposes)
- Cost/rarity (used in meta and map gen)

### Ai parameters list:
Weapon fire with old threshold percentage (shoot at max range or wait till player is 50% of max range of current weapon?)
Reaction speed delay (how long to wait before taking action against player? Separate from unit action delay which is more a thing of physical limits of unit, not the reactions of it's pilot)
Player detection to do move behave threshold (how close to be to player before deciding to move at or away from them).
Ambient move rate (compared to max speed, non avoid or berserk)

### Ai Behaviour roles:
+ Move about and shoot (patrol)
+ Sit tight and shoot (sentry)
+ Just sit (building or parked inactive veh)
+ Just move (pedestrian)
+ Move at player and shoot (berserk)
+ Move away from player and shoot (avoidant)
+ Hunt (always berserk, even at map start)
+ Thief (initially Hunt, but become avoidant when close enough, resuming to hunt if too far again, with a cooldown between switches)

Generally ai is very simple. Mobile units just move about and shoot. Stationary units just shoot.

Stationary units shoot far and accurately but track slower, having poor turn rate.
Mobile units shoot inaccurate and try to get closer before shooting, but turn faster unless heavy and may be able to dodge occasionally with a cooldown (not applicable to all units), dodge may also be limited to one or two directions. (Forward only, backward only or two sides)

Ai does not retreat, dies to the last, has no tactics or strategy. They just spawn, do their limited behaves, player receives kill list and clears them out one by one in battle. AI does not heal or repair in combat. No stealth either for enemy nor player. Can't sneak or be sneaked up on. No ecm or jamming.


---
## Player flight controls and flight behavior:

### V1:
I'm aiming for that simplistic 'Fighters!' style basic flight sim controls of a plane. 
- QE for throttle/air brakes
- WSAD to up down left right 
- B1 to shoot (B1 stands for button 1, I'm just using it as a placeholder for either a keyboard hotkey or mouse button)
- B2 to afterburner (more extra speed)
- B3 to switch current weapon (cycle next)
- B4 (hold) to point camera at next nearest enemy (not switching target until repressing the button again)
- B5 radar range toggle modes (short medium long)
- Pause menu

### V2 (compared to V1):
- Use mouse aim to turn instead of WASD controls
- Transform to mech and back into jet

Player flies forward constantly always having a minimum speed they cannot go below and a max speed they cannot exceed. Turning is relatively slow and wide, but tighter turns are possible with smaller speeds. Player is stuck with doing strafing runs or dogfighting by chasing another jets tail. No mouse controls. Locking on happens automatically when player aiming point is close enough to target after which their fired missile will actually track and home into enemy as opposed to just being launched as a dumb projectile. Collisions with terrain is fatal. Collision with enemy causes heavy damage. Flying enemy is first struck with fire trail and they fall towards ground, unable to shoot or fly properly anymore. These fallers can be shot at again to blow them up completely.

(Mech transform, mouse aim, acceleration momentum movement, multi weapon hotkeys, different move controls, strafing to sides as jet too, vertical up/down movement, switch from walking to skating as mech with double tap, switch mech from ground to flight mode with double tap too, lenient collisions, auto switch to mech on collide) weapon dropping/throwing/pickup, interact key, item/ability keys, overboost, engine kill, target cycle, radar/aux keys.)


---
## Hud: (V1)
Player hit points/status
Player current weapon ammo, name
Player speed, altitude 
Crosshair/lock on box (depends on equipped wep)
Compass+position on map xyz
Radar of enemies vs player (in corner as circle with green dot for player and red markers for enemies, showing dot if same altitude, arrow up/down if above/below player, shows radar max range too with radar scaling internally to match distances.)
Enemy kill list or remaining targets.
Next enemy red box (auto scaling box, only a dot if too far, visible always unless no enemies left, appear on side border of screen as arrow telling which is fastest way to turn to face them again)
Mission status text: (remaining, all clear)

(V2 is similar but adapted to its sensibilities)
---
## Metagame: (V1)
Start at main start screen that has buttons: start new game, continue existing campaign if there is one, win log, info/how to play, settings menu (includes sound volume settings, mute sound toggle, mute music toggle, maybe some other misc settings too), exit game app, credits, link or qr code to author's page. Most of these open their own screen.

'Win log' has a persistent list of previously generated and won campaigns with a seed value so they can be replayed again as flashbacks. Doing so lets player improve end stats that are shown per each stage that are grouped to the campaign they belonged to, which also will improve the stats of that campaign too. If player looses a campaign during the intial playthrough of it (not as a flashback), then it will not be replayable in the win log and its seed value will be skipped in favor of a new one when starting a new game, so the player may possibly never or rarely get to retry that particular campaign if they lost to it the first time. This adds stakes to each campaign to have consequences of missing the opportunity to record it into the win log.

Some stats that the win log displays:
- name of campaign + total completion time (reduceable if stages under this campaign got their times reduced if they were replayed as a flashback)
- name of stage + completion time

Player can choose to "flashback replay" either the whole campaign or a specific stage. One special thing about flashback replays is that the enemy scumbag target's name was already "erased/terminated", so they appear as a faceless shadow with a garbled name, to sell the point that they are already dead and buried. Thus the flashback replays are more about the player's satisfaction of focusing on the gameplay aspect of the unique challenge that old stage/campaign had.

Game has only one game mode generally; the campaign of 10 randomly generated stages as a "low metagame", and the persistent accumulating win log as the "high metagame" which is like a permanent trophy wall the player can polish up if they choose to through flashback replays.

A campaign is a set of 10 random generated stage gauntlet, generated by the high metagame that checks to ensure any generated new campaigns don't have seed entries that already exist in the win log. There is a random difficulty curve per stage. If player dies, they're kicked out back into the main start screen after being presented with an announcement box saying they failed the mission. For flashback replays, they're returned to the win log screen instead.

Goal is reach and beat stage 10 to win, to defeat scumbag character with randomized name in the 10th stage. Upon final kill in each stage, pause time after 1 second and change player controls to rotate camera up down left right with scrolling credits while the game world slows down to a standstill over the course of 5 seconds - as a cool dramatic effect. If blowing up mission-critical target during last stage also show name of scumbag go from white to flash red and fade to black, then delete each character in that name one by one per 500ms with a satisfying confirmation of "erased" or "terminated" written above it to, also for dramatic effect. Then go back to main start screen again that has 

Upon starting new game, show brief intro to scumbag name with a "mental Illness/sin/bad trait + top level criminal type" subtext, so stuff like "sociopath slaver, narcissist dictator, apathetic thug, greedy CEO, asshole oligarch, moron Mafia boss, manipulative cult leader, etc. (note: I'll use chatGPT to compile some wordlists for both of these).

Have a generic vague silhouette female and male portrait too. Apply color tint on their pic and name (not black or white, stay within soft color range).

(V2 is similar but adapted to its sensibilities)
---
## Local play experience: (V1)
After intro get button with label battle 1 start. Below it a chain of 10 boxes in a row, with arrow pointing at which one you currently at (or about to enter).
Start at 10% edge of map middle facing into center of map.
In 3 seconds from start get a message "all systems go" and autolock to first nearest enemy target.
Opponents either sit on ground or fly towards player. All opponents are very spaced apart and should be unlikely to collide.
Player kills them all, time slowed and paused after 1 sec of last enemy kill, get message "battle 1 complete" Repeat until map 10 and get ending and drop to main menu.

(V2 is similar but adapted to its sensibilities)
---
## Object sizes and culling at border of map:
Generally realistic sizes but kept at multiples of 5m.
Player is 10-20m long jet
Largest possible mobile vessel is 1000m

When placing hill/island/mountain props over terrain floor, they may overlap out of map borders if placed on edges. Either don't place them at edges, use gunmetal style infinite horizon terrain after borders or cull the overlapping mega props if they bleed out of cube zone. Also make floor and cube slightly bigger than 10km3 playable area with a 1km empty margin.


---
## Player ships:
Player can choose premade vessels with various stats for armor, max speed/acceleration, weapon slots, item slots. Starting loadouts include one reliable weapon and others are completely random. Or do cryptart where loadouts are fully set and meme themed.
Can choose color tint for booster jet effects.
Skin is set via premade loadout like in cryptark.
Maybe a special reusable ability ala Cryptark would be cool too.

## Player support vessel(?)
V1 may be enough to just spawn, fight and retreat if you're out of ammo or don't think you'll stay alive to complete the mission.
V2 could include a resupply vessel that repairs, rearms and refuels the mechjet. This vessel doesn't move, just provides a box collider to designate a supply spot when within. This could be a floating heli platform, a crawler, a boat with helipad, blimp, hot air balloon, mothership spacecraft, an small ground depot, minibase, or supply cache ala gunmetal regenerator.