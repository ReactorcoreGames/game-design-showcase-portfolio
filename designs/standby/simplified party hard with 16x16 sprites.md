Player unit does stabby stabby.
Player can delete party goers if they in proxy with useful interactables.
Player can trigger contraptions to delete one or more characters, either without trace or as normal corpse.
Level has party goers that patrol routes, some roam, some stay in place, some change based on events during game (like seeing a body). Uses AI nodes for them to path find to them as best as they can, assuming the world wasn't designed poorly where they'll get stuck.
Has police to go arrest someone who got sus'd.
Bouncers can knock you if you try to get close from front.
Secret agents will chase and get you unless you sneak behind them.
Besides people, there are animals that can also count or not count towards kill count.
Player can run until police get more chase time and eventually outrun the player in most cases.
Level has shortcuts that close if used during escape with a long cooldown.
Medics will enter map to cover dead ppl with body bags.
Player can pickup and drop/dispose of bodies to avoid other live ones from seeing the body and becoming more frightened. Use dumpsters etc to hide bodies.
Player can poison things to get party goers killed off.
Party goers may go to spots to sleep or just doze off where they stand.
Player can get items to aid in killing or getting away. (Smoke bomb, katana, pizza, disguise, bomb, etc)
Player can have different classes with special abilities or traits (ninja, cop, default, chainsaw, lady, etc)
Trap types include timed, wandering npc proxy activated, instant activated (aoe), player n npc proxy instant use, repeat use activate (think horse).
Characters have vision cones in left or right. Maybe expand this to 90'.
Staff members also are characters amongst party goers.

AI nodes:
Security:
Go here and Flip left
Go here and Flip right
Go here and Pause 1, 5, 10 seconds

Staff:
Go here and Flip L/R
Go here and Pause 1 5 10 
Go here and sleep for 30 secs, occupy space if free, otherwise pause for 1-5 then move else.

Party goers:
Same as staff but different node set to not conflict with.

Level:
Walls.
Doors(only open and visible through if anyone near).
Props/furniture solid (see thru or vision blocking).
Non solid decor obj.
Spot for police/medic/maintenance guy(shortcut blocker).
Spot for party event arrivals/leavers.

Random event:
More party goers arrive (1-9)
Bear arrives (it will randomly eat someone)
UFO land and steal someone, no one bats an eye
Pizza man
Engineer/item giver

Game is about the thrill of how much you can eliminate before anyone notices anything.

===

Alt idea to simplify:

Play as dude armed with stabby knife, wide zone (short range wide cone) shotgun, coilgun, super revolver. All have infinite use, but cooldowns and make sound or light.

Also flashbang, proxy mines, smoke bomb, big bomb, turbo shoes, pizza, disguise, onimusha blade (Party Hard 2 ability), poison flask as a random assortment of consumables.

Basically player has the power of traps on them and they try to use them on party goers without them noticing them shoot directly. If they do, dozens of police officers immediately break through the border walls and tackle/pile up on the protag.

Levels are much more simple.
- a base plate of texture ground
- square grid based everything 
- random walls squares with random texture as floor, 50% chance per wall to have a either a door or a opening (50% chance too).
- half walls snippets (no collision) as furniture with random texture. Either near wall, in middle, outside - each snippet uses a random texture.
- random deco object on floor (pass thru) based on indoor or outdoor.
- a few pick ups for extra items anywhere that isn't a wall or halfwall
- people spawned in random facing directions in clusters around free spots + a few stragglers. (Deco spawn spots count as free spots too)
- start/exit spot 

There's a random pool of indoor floor textures, outdoor base plate textures, party goers sprites (player uses these too), wall segment textures, door textures, deco object interior sprites, deco object outdoor sprites.

There's generic blood smear when character is obliterated, a generic black gun sprite with white hand, a X shaped muzzle flash, weapon effects are done with basic particle systems, but have a pixel or slanted rect as particle texture.

V3 idea: kill all alcoholics

Go to party, plan out the area, exterminate them drunks stealthily or open fire on the as they become zombies that try to stop you once you've been noticed to have killed someone. No police. Avoid chain reaction by alerting someone that cascades the alert to potentially everyone. Divide n conquer, reduce their numbers before using loud tactics or risking discovery.
