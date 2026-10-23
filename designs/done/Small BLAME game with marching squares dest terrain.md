I saw this script library for destructible terrain via marching squares algorithm for Godot. Seems like it'll be perfect for a Killy with GBE bite sized 2D game.

Proc gen megastructure spaces with start and end zones.

2d Parkour platformer

Shoot GBE at Z background, with some consequences to play area (falling debris, earthquakes, collapsing platforms), and use it in foreground... with caution.

Title "Do you have the Net Terminal Gene?"

Each level is a landmark or pivotal moment that holds a clue that can help Killy navigate the maze faster to reach his goal.

Killy usually meets a random sitting somewhere and asks them "Do you have the Net Terminal Gene?" to which the person will reply "no, but (clue to get closer to it)". (Sometimes they can say useless gibberish and you leave them be... or they maliciously lie and you'll meet them again to give them a punishment as you want (GBE, blade or shotgun or push off the edge or slam into wall). A bit of social sus out mechanic.

Killing innocent civs will spawn local police units as killbots that try to kill both Killy and monsters on the level. Killy has to balance between killing enemy creatures while ensuring civvies don't get fragged neither by him or due to monsters eating them. When cops show up, it's a moment of chaos where Killy either can stay and kill the wave or just run for the nearest exit.

Levels have multiple one-way exits. Civvies can show which is the right one, the rest will be a detour, some mild, some worse. Sometimes Killy may want to take a detour on purpose to find goodies to take a chance, though even detours may contain monsters.

Regardless, Killy tries to get to location of his goal ala Slay the Spire, whereby good info gets him closer to goal, while bad info makes him do a lengthy multi room (2-7) detour with a random chance of finding random goodies like food bricks, ammo, kits, consumables, lore, surprise shortcut clues or other stuff.

Mostly the game is chill parkour walk, with rare moments of thrill. Sometimes the GBE can be used to make a path easier to traverse or even for the fun of it.

Silly idea: instead NTG, Killy just wants to find the next cozy elevator or train he can ride so he can chill for 572826 hours with his buddy driver just for fun. The NTG is just an excuse.

Between levels, show a random art of Killy traversing the megastructure as a loading screen/intermission/progress tracker.

Gameplay:

Enter limited small area scene rect with destructible megastructure terrain (concrete, pipes), randomly scattered fragile platforms (walkways, stairs, bridges), 1-2(rare) clue objects (person, terminal, infopad, machine/device). Occasionally there may be low tier or high tier creature(s) that is hostile - they maybe in foreground or z background. Builders may occasionally make an appearance in level. There may be ladder/chain link frameworks that Killy can stand on as emergency platforms if everything else on the level has been wiped out. They're sort of between foreground and background, Killy can't blast them with a GBE. He can go through them in any direction, maybe it's just a Mario climb wall ala SMW.

Killy is a 2d soldat sized character platformer that can jump, climb, cling, grapple, use rocket boots. Armed with a GBE that by default shoots into the background at point where mouse is aiming, but by holding down right mouse button, can be brought to fire a beam soldat style with mouse aim, with disastrous consequences to level.

Firing the GBE will produce shaking, falling debris and flashing, giving weight to its sheer power, even when fired into the distant background.

Killy can also use melee attack (kick, punch or megastructure blade) or rapid-auto-shotgun-multi-gun as a safer method of attack when needed.

Killy can also grapple pull, arm grab and throw loose stuff. And press E to talk/interact.

Background enemies are conversion towers, hives or bombardment/sniper units ala DKC3 hoot hoots. Some creatures may begin as background units but arrive to foreground. And maybe go back too.

Foreground enemies are similar to Killy; platforming, jumping, climbing, hanging, stationary, crawling, walking, running things. Some slow, some fast, some melee, some ranged. Each usually has 1-2 attacks they do plus 1 core function that usually involves creating an obstacle an inconvenience or to mess up and ruin the clue target, much to Killy's dismay.

Dying:
Level boundaries feature bottomless pits, ceiling and walls ala smash bros. If Killy fall or flies out of level, he'll usually say a short profanity and then seconds later crawl out of the level entrance good as he was prior to being ejected. Some monsters are defeated outright by throwing them out of the level while others are like Killy and crawl out of one the exits to continue their havoc.

Thusly, usually weapons, damaging level hazards and attacks will kill Killy or these stubborn and non stubborn creatures. If enemies die to GBE, they vaporize. If via other attacks, they gib or become corpse.

Killy on the other hand is semi immortal. If he sustains enough damage, he'll blackout and wake up later in another random room and walk 1-5 room detour to meet the enemy again, get revenge on it and then continue as if the lost level was passed successfully.

As a fun twist, the enemy may have stolen Killy's GBE and depending on the creature that killed Killy, is possibly able to fire it. Maybe one and blow up from the recoil. Maybe not at all. Maybe repeatedly but a slow rate of fire. Maybe   have it fly out of its hands upon the first or other shot, landing somewhere stuck to a net where Killy can go get it.

Generally, Killy is pretty durable and has a slow passive health regeneration at all times. 200 hit points, 1hp heal per second always.

Parkour:

Generally Killy is mostly grounded and relies on terrain and grapple hook points to get to the exits. If those are catastrophically erased by GBE fire or explosions, there are the backup nets that ensure a path to exit no matter what but are slower and more annoying to traverse. Jet boots have limited flight fuel that carries over level to level though lacking it won't stop from using dodge maneuvers like backflips or dashes or running. (Limited flight fuel verniers vs infinite recharging rcs impulse thrusters).

Killy is also generally relaxed and slow, but can sprint into action in bursts quickly and violently, but not constantly like a quake/ultrakill Duracell bunnyhopper; everything has a cooldown, winddown, moment of slowness after. Killy don't run or prone, but he can walk, crouch, dodge, climb (over fg mesh, like ladders, nets, etc.), jump, rocket slide, rocket jump/boost, rocket fly, zero g move with rcs, pull small things with grapple and grab with arm(and throw/drop afterwards), pull self to large things with grapple and latch on whatever Killy grappled to.

Environments feature variable global vertical gravity with occasional destructible movers or force pushers (moving platforms, mini elevators, blowing large fans, sucking air ducts, sideways gravity surfaces, orbital gravity node spheres (if possible), spinning/rotating platforms. There can also be hazards like radiation sphere/pylon nodes, electron surfaces, crushers, grinders, hot exhaust, explosive tanks, molten metal flow, exposed electrical surfaces, slippery ice, sticky fungal growth (like mud), unhookable surfaces, rebar spikes, proximity spikes, jump/push plates, contact mines, laser beams, zero g fields, n style auto bots (dumb, reactive, turrets), etc. all of these affect both Killy and monsters and cops, so they can be used opportunistically by Killy.

Metagame:
Already mentioned it feels loosely like slay the spire progression where during a campaign Killy's mission is to go from checkpoint to checkpoint. How he gets there can be variable and random via the rooms he stumbles through; he can get there extra fast or extra slow but this game is more about the journey and moment to moment gameplay than the destination. Most rooms will be interesting vistas or spaces to walk through and you never know what kind of combo you'll stumble through next or what you'll encounter. Every room more or less brings you closer and you can never truly fail the entire mission due to being immortal and deaths resulting a detour that merely forces a different path to the next goal room.

One idea is that the game is more about being a Net Sphere Engineer, where you troubleshoot problems - either with GBE or just interacting with a device/terminal/character like a traveling mechanic/doctor/sysadmin. Sometimes it's a hive, a hive with boss, a jammed machine, an obstruction/obstacle, group of bandits, some creepy weirdo, juggernaut boss or swarm of thing that is a persistent threat for that campaign run. If Killy fails and dies trying to take it down in a particular room, he'll run into it again but in a different room to try again until he finally succeeds.

So the metametagame or high metagame is about restoring the netsphere and fixing the city sector by sector. Each cleared sector will have the governing agency move in and finish up securing the location, reconnecting it to the netsphere. The people stranded in the disconnected sectors will be able to connect to the net and gain immortality by digitizing themselves, uploading their soul so that they can either exist in the virtual space of the netsphere or respawn in real space with whatever body and style they want, just to hang out mostly.

Lorewise, originally there was a cult of pure/cyborg human luddite fanatics that opposed the idea of digitization and caused a major disaster that caused a severe outage and mass disconnection of the netsphere, causing builders in the outer sectors to go haywire and people unable to join and be left in a chaotic environment. Meanwhile another faction was into converting people into hive creatures/bugs/insectoids as a way to evolve and "be more productive, common, and nature aligned", similar to Omar in Deus Ex Invisible War, with a touch of Zerg. Others saw their future in become silicon life forms instead of staying carbon, hive insect or digital+androids. All this divergence resulted in utter clusterfuck that left all but the core of the megastructure in disarray, which was controlled by the governing authority whom is all about digital/android life. There's also ghosts that transcended to another realm but some spirits still linger like curious anomalous ghosts. There was also a death cult but they already all died, though left some decorations and smug messages behind how their method was the better one. Occasionally there may be some rare unhinged psycho assholes among the ruins. Then there's a majority of confused civilians that are just dismayed their services got cut and their access to the net was lost. Most are sensible people with a few jerks and morons mixed in, but they're mostly friendly, kind and helpful. They may have opinions and concerns over the methods and ideology of the different factions, but ultimately governing authority is the real power and caretaker and they're ok if some people want to choose different style as long as they don't being down the whole system for everyone. Oh yeah governing authority rogue safeguards that are hostile due to being severed from the net and corrupted are another group too. If governing agency gains control of a sector, they'll be restored to normal or atleast shut down because they're support system are no longer in their service of illegitimate safeguards.

High metagame reward:
Dunno. Maybe a memory montage of epic moments, a personal auto screenshot library with automatic personal customizations and signature of player.

Low metagame flow:
Player arrive to transit point via elevator or train and begins their journey to objective of that particular campaign.
They finally reach it, resolve the issue.
Now they head to a new transit point for to take them to the next destination.

Between campaigns, player can choose what kind of mission to undertake, includes intensity level and what task. The mission card options are randomized each time unless player locks them. They can also replay missions by getting their seed and pasting it via flashback play which let's the player do it again in flashback mode which gives options to cheat or activate other new game+ mutator for their run. The idea is they're storytelling to someone what they did. The mission won't contribute to high metagame if played like this.

Context wise player is a special agent among few/many. They're not part of safeguard, they're more of a sysadmin, tech support or CIA equivalent of the governing agency. They have special all-access and privileges to use any governing authority cache or depot or facility as they need to. They are a superweapon and the GBE - Graviton Beam Emitter - is their ultimate offensive capability, while their immortality and endless regeneration is their ultimate endurance capability. Most of it is fueled/drawn power/invoked by the megastructure itself, as Killy and agents like him wirelessly/ambiently receive energy and nano-support in the sphere of the megastructures influence. Killy is essentially a conduit of the megastructures vast power that is intervowen into it's very walls and marrow.

Controls:
WASD - left right, jump, crouch.
Hold S + Press W - drop down from one way platform once.
Mouse - aim these: gun, grapple, grab arm.
M1 fire GBE into BG at a point.
M2 hold arm GBE into FG, M1 to fire a shot from Killy towards room border.
E - interact/grab arm (toggle)/throw arm (press and hold, launch speed based on hold time)
F - melee attack (generic swipe with a blunt short superheated surface rectangular sword, imparts knockback and some damage on target. Damage gains multiplier based on Killy's momentum in relation to target momentum vector)
Q - use rocket move (context sensitive; if on ground, prime rocket jump, do it if W is pressed, do nothing if Q is let go. If sliding, Q will boost the slides momentum when it's pressed. If dodging, same as above. If Q pressed mid air, jetpack thrust in desired direction via WASD.)
M4 - grapple (shoot, release. Pull is automatic if it hits. Apply momentum force to either target or Killy.)
M5 - Shotgun (firing mode depends on power up status. By default it's a Doom shotty. Inspired by time crisis/metal slug/battle clash powerups, it can become rapid auto shotgun, quad mega shotgun, tribarrel burst fire shotgun, fire breath shotgun (linger flame), explosive shotgun, cont. laser beam shotgun, remote grenade, sticky proxy mine, plasma bomb blast, smart autoaim twoshot shotgun, force shotgun, arc lightning shotgun, nuke shotgun, blackhole shotgun, minigun, expulsor, slicer shotgun, hypervelocity shotgun, cannonball shotgun, instagib shotgun, burner shotgun. Each has limited ammo before reverting back to default shotty.)
Shift - dodge/dash/lunge/slide (instant press+hold, context sensitive: if not moving, do nothing. if walking left or right on ground or in mid air, do lunge(forth) or backhop(back) in that direction (Killy facing direction depends on mouse aim, left or right). If crouching and moving, do floor slide.
Mouse wheel - slomo 0.2 timescale as long as you keep scrolling every 2 seconds or sooner.
M3 - open time freeze menu to choose shotty or use consumables ala SMB3. Can collect up to 4 shotties, and 4 slots for consumables.

Movement is based on physics and momentum. There's air friction, terminal velocity, ground friction and counter movement to slow Killy down.

Killy is a 32x32px sprite.

Consumables:
- rocket fuel
- food bricks (faster stamina recharge, lesser cooldowns)
- health kit (instant heal instead of waiting slow regen)
- ammo (for current shotty, works like heavy ammo pickups in ME2)
- era bricks (instakills melee attackers, defuses heavy hits, works passively if in inventory)
- deflector orb (allows for a number of light projectiles to pass through as if Killy isn't there before running out of charges, works passively if in inventory)
- electro armor vest shielding (absorb 75% damage while letting remaining 25% hit HP directly. Like doom's blue armor or SOR armor vest).

The various consumables may come in S M L sizes and some can stack up to a max amount.

GBE:
Idea: using it causes campaign damage. There's a quota threshold of acceptable uses but beyond it, it will start having consequences to other rooms and attracting more attention from rogue safeguards that work like the GTA police stars. GBE is like an F-bomb, use it sparingly or face more chaos and heat than normal. A general rule is 2 uses per medium class enemy in room + 2 extra uses. On normal setting and on foreground. For background it has a separate quota, it's 10x that.
Idea2: limit cancel: normally the GBE is an infinite use rapid fire capable nuclear beam semi auto pistol with an additional ability to charge up for even more overkill. Lowest power is a beam that is 16px wide. Medium is 32px, large is 48px. After that, it will stay at 48px while charging but if limit cancel is activated after lengthy charging ala Vector Cannon from zone of enders, it will go to 96px wide beam.
Anything hit by a GBE beam will violently rip apart instantly. It's overkill even at its lowest setting and absolutely absurd on higher levels to the point it's comical. Nothing can stop it, no terrain, no defense, it goes through all with impunity and deals extreme damage, one shot will kill anything.
In shotty/consumable freeze menu, user can set default mode for their GBE for faster/easier GBE use without charging it, just wait for cooldown instead to fire at specific fire power level. This mode is less flexible and limit cancel is still achieved by lengthy charge up as firing happens on M1 button release.
For bg point shots, higher power levels mean larger blast radius and stronger after effects, such as more debris, earthquakes and lingering gravity distortion.

Campaign gen:
Works sort of like FTL, Slay the Spire but doesn't actually have a real map or clear 100% predetermined structure. The megastructure in itself is a messed up maze due to netsphere disconnection, equipment failures causing collapses and builders running amok "fixing" things.
It also works sort of like Starfox where each next room is based on the surrounding/adjacent/previous room in terms of direction and whether it's an interior, exterior or hybrid interior exterior room.
One thing is sure is that there are landmark nodes where a room is going to be a specific kind, but it's not locked to that particular room only. It's more of a "at this node, there are endless variants of a room that are located at this node, sort of like different vantage points to the same location.", hence why no room is permanent or locked in; it will simply contain the expected objects, characters, hazards, terrain and backdrop, each being a randomly placed if Killy ever returns to a "same place", like if he reaches a boss room, fails, wakes up in a random "ditch room", works their way back to the boss room node where they can retry the boss from a different angle via freshly generated new room variant at the same node location.
Node types include
- sector entry (train/elevator endpoint that brought Killy to this sector.)
- goal node(s) (where boss, objective or what else resides that is the goal of the campaign)
- sector exit (train/elevator station which Killy uses to leave the sector behind and finish the campaign.)
- ditch node(s) (random "awaken from death" room, bottom the barrel, only way is up, minimal hazard or chaos)
- cache node(s) (random nodes Killy can stumble upon where he can find goodies, consumables or extras to help him in his quest. They're uncommon and after finding them, they usually run dry and offer no goodies after 1-4 visits, citing "out of service", much to Killy's disappointment.
- vista node(s) places that are just scenic serene places with minimal activity. It just looks unusual, somber, calm, odd, epic, awesome, creepy, bland or tranquil.
- between these nodes are pathway room chains. They're not nodes in themselves, they're just routes Killy takes to eventually reach one of those nodes. They can be a quick 1 room chain or even up to 9 rooms long treks with their own shortcuts and long ways that all ultimately lead to the next node Killy is headed for. These transit rooms are mostly lofi but random, on occasion they may even be more chaotic and intense than the landmark nodes during the campaign. They're 80% calm with minimal combat and occasional hazards generally though, with the overall pace of the game mostly easy, ambiance filled, chill and calm as Killy walks through the megastructure towards his destination, bursting into violent action only on occasion when he encounters something hostile that threatens his quest or goes against the governing authority's stabilization and safety of the megastructure.

Level gen:
Room sizes are standard.
There is always an entry point and 1-3 exit(s). The exits remain closed until all hostiles are cleared. Not physically, Killy just says "I haven't finished clearing this room yet." and refuses to leave.
If more than 1 exit exists, there must be atleast one clue entity added to level.
Both entry and exits have one sided platform frame in fg. There are sufficient hook points, climb meshes, platforms  and walls to guarantee a path between all of them should all other terrain become destroyed.
After that, using similar procgen schemes from Topverse, random solid terrain is created. Then various props are places in varying amounts while clearing out terrain out of the way to slot them in.
Some rooms are designated as interior while others may be exterior or hybrid interior+exterior mix. Interior means that instead of bottomless borders, they're solid so you can't fall/fly out of the area (it's a floor/wall/ceiling wide one-way mesh platform in essence, same as one used under entry/exits.
Backgrounds are procgenned too, both interior and exterior ones. Exterior ones have 1-3 parallax layers.
Campaign gen invisible "world map" determines what type each room will be, interior or exterior, what it has present, what kind of bg makes most sense for it and what events can occur within it or cannot occur.
Generally it doesn't matter whether a map is "completable" in it's initial state as Killy can always just blast away a path for himself with his GBE. The room generator will try to some degree to make sure there's atleast one clear path without needing a GBE, especially if it was stolen from him prior, but given infinite melee and shotgun attacks, player will always be able to break or dig through to the next exit no matter what.

Difficulty modes:
Generally player chooses difficulty during campaign selection via intensity of choices present. But player can also choose an optional alternative difficulty mode that comes with a more sluggishness and tighter limitations to GBE use, forcing player to rely more on shotgun and melee in combat, maybe even exacerbating the adverse effects of the GBE by having the player wield an even more overpowered version of it than the normal Killy one.

Futurism, philosophy, transhumanism, messages:
Albeit the game itself is a fun 2d platformer action shooter game with some parkour and trekking/walking, it does serve a great platform to discuss about technology, future of humanity, and other scifi topics.
Player can stumble upon datalogs that offer a small bite sized "ahaa moment" via a tldr style snippet/summary/blurb/infographic about anything related to future, science, humanity, tech and half as interesting side stuff, like mentions about limitations of certain weapons tech in our current world or other issues that modern irl humanity is struggling to solve as an inspiration or hint to the player of "hey, are you bored and aimless in life, maybe you could try solving this particular challenge?" as a way to spark life into them, so to speak.
I could mass produce these snippets via ChatGPT or take summaries from wikipedia as separate popup logs player could find out in the wild. There'd be a cycling order so player won't see a log they've already seen prior until all entries have been seen atleast once after which they'd be shown completely at random subsequently.