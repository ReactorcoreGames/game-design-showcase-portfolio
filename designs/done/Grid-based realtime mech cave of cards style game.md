## Inspired by:
Cave of Cards (by Adam Saltsman) - using WASD to move, tile by tile, performing actions instantaneously upon entering tile or colliding with adjacent tile.
Just Cause 2 - premise: destroy a dictator army in region, room by room. Population/military reinforcements cap counter, explosive props, chaos, civilians, eliminate bases and targets.
Red alert 2 - explosives to trigger chain reactions, military units as enemies.
Momentum missile mayhem - enemy army, style effects and destruction.
16x16px pixel art rpg tilesets (top-down, advance wars style) - how it looks and plays.
08th MS team - play as mech, environmental destruction and pollution, large weapons, sand to glass via beam weapon.
Wanzers/front mission - tacticool feel, scale of combat, mech loadouts.

## Control system for player:
WASD to move on grid. Character rotation is locked to whichever is currently set so moving on its own doesn't change it.
Hold down R + WASD to rotate towards direction to aim there.
HJKL - Fire/Use equipped slot 1-4 weapon/item
Hold Y + press HJKL - grab to replace existing wep/item slot. Drops existing item on floor.
E - interact
Q - character screen/inventory
M - map (overworld ala super metroid)
ZXC - quick ability/item prev/next + use(x) (like gzdoom inv items) (optional and probably overkill, maybe just stay with 4 wep/items for simplicity sake)

### Alt; Mouse + keyb
WASD to move, but mouse pointer in relation to character decides nswe aiming direction. 
M1,2,4,5 fires/uses wep/item.
Hold F + M1-5 - replace wep/item on floor.
(Rest are the same)

Has potential for a one-hand controls scheme around: WASD region (keyb only).
WASD to move
R + WASD rotate aiming direction 
Space to fire current wep (can only fire 
Ctrl+WASD to select wep
Shift+WASD to replace wep
Q inv+tabs, f back, r confirm.
X map
E interact

## Control for NPCs:
NPCs move and rotate but with a delay and visually telegraphed outcomes where they will face next and which tile they will step on. The default player technically has a 0.1 delay too, but it's barely perceptible to matter. Because it's a one player vs many NPCs, the latter are slower and clumsier overall to make the experience more balanced and fair.
Visually, there's a wide arrow/triangle on the floor that shows direction of a unit, while tiles that an npc will step on are highlighted with a marker that grow brighter the sooner the step will happen/attempt to happen.

## Gameplay:
Looks and feels like turn based tactics, but plays in real time like a tactical pseudo twin stick shooter.
Player movement is akin to cave of cards, with buffered inputs for rotation and shooting/using items.
Player or NPCs can only do one thing at any given moment; move, rotate, shoot, swap item with whatever is on floor.
Tiles can contain underlying terrain type tile, pickup item on tile or an obstacle/structure installed on tile (not both at the same time), a mobile unit - be it player, enemy npc, neutral/civilian npc, which can coexist on the same tile as an item on floor, but not coexist with an obstacle on same tile.
Player enters battlezone, takes out all objectives, goes to exit point and presses E to leave.
Between levels, player can alter mech parts. Maybe the parts work like XCOM long war soldiers that get fatigued and need to be rotated, forcing player to swap loadouts to try various combos. Some may have mission durability uses until they are no longer usable, so player keeps a stockpile of new rotating parts that the engineer provides  so that there's never a situation where player doesn't have a part to launch with.
Mostly overworld is a MegaMan style thing. Choose a region, do it like a 10 map gauntlet, beat it and do the rest in any order to win it. Failure means retry from start of region. Maybe there's a lieutenant or some local leader/boss that player decapitates at each region.
Once all are down, demolishing a satisfying mega explosive finale. Doesn't need to be a boss fight, but can be one. A fortress that is generated ala Warning Forever.
Then get a newspaper report on the aftermath and a log entry for all the campaigns done, all showcasing the Type 3 Mecha's different aspects with randomized sentences and headlines, with some influence on what player did during that low metagame run.

## Combat:
Units/obstacles/structures have hitpoints. Weapons, attacks and hazard reduce these. If they reach zero, the thing explodes and is removed from the game.
Player/npcs/structures can have weapons equipped that can only fire in nswe directions, mainly based on what direction they are facing or how the weapon/item behaves.
Weapons are flying projectile based or instant grid based.
Directfire weapons don't affect shooter, but subsequent area of effect detonations or explosions can cause self harm.
Projectiles are spawn at the edge of character/tile and travel until they reach the middle of target tile and vanish, leaving behind a hit effect or micro detonation or projectile shattering. Lifetime of projectiles is thus calculated with speed by how many tiles they are meant to travel before they expire.
Projectiles fly in a straight line at a constant speed.
Some weapons are instant fire (player only, lightweight or slow cooldown weps), but other weapons may have a windup delay before they fire (heavy player weapons or most npc weapons.)
Supported explosion types are limited to Bomberman style cross '+' explosions or square explosions only. The latter is rare. The former can have directional shaped explosive charge versions that only go 1 way or 3 ways instead of all 4 ways.

## Destructible world:
The game prominently features mass destruction and pollution mechanics by having the underlying terrain tiles be subject to changes based on events that happen over them:
- grass can turn to ash by fire. Fire can spread to nearby nswe flammable tiles over time once a tile becomes too saturated with it. Basically grass tile catches on fire, fire grows bigger and when it gets big enough it will jump to all (or 50-75%) tiles around it vertically and horizontally but not diagonally. When this critical point happens and the fire jumps, the tile turns from grass to ash. The fire will gradually shrink on that burned tile and vanish. The speed of fire is relatively slow. Objects/structures/units cannot have a on-fire status but if they stand on a tile that is on fire, they will gradually take hitpoint damage at a steady interval. Structure hitpoints for hardened stuff like bunkers often exceed the damage a fire can cause so they'll survive the burning intact, albeit mildly damaged. Other things like trees/forest obstacles will usually burn down. 
- Obstacles/structures/units could have a special case where damage tranforms them into a "ruins/ruined" version of it that is weak and brittle. Like a gibbable corpse. If it's shot at, then it will gib into particle effect chunks/effects. This is usually reserved for hardened stuff so weaker stuff will instantly gib without going through the "ruin" version phase.
- Plasma blast/beam weapons can turn sand into glass, causing slippery movement like those ice puzzle levels except you can still change direction mid slide.
- lake/sea ice can turn to water, while frozen ground can be molten into regular ground through explosions.
- grass/asphalt/road/ash/mud/dirt/soft stone/gravel ground can turn to molten lava via intense plasma/atomic explosions that solidifies to obsidian craters which cannot be turned to lava again. Sand turns to glass. Water generates steam/fog that stops laser weapons from going through.
- snow, asteroid(ice or rock or volatile ore or lava), nebula (inert or methane), reef, cloud (storm, rain or safe), metal debris, glass/crystal/prisms.
- explosive props - just cause 2 inspired. + Cross explosion fuel tanks, square explosion fuel silos, directional fire jet gas tanks, pressure propelled explosive tanks (launches same direction as the bullet that hit them as an explosive projectile on its own), fire spreading oil drum, transformer lightning strike in 1-3 different directions with variable distance if 1-3 spaces. Various size/severity/material/volatility classes for all these.
- interactables that player can go up to, face them, hold E and it will start a trigger that may sabotage or detonate something on the map. Like say a gas/fuel pipeline, a regulator for a set of volatile electric transformers, a power box that turns off powered items nearby/on level, etc. linked things.

## Weapons have these parameters:
- damage per hit
- distance in tiles: lifetime/speed
- burst size (how many times to fire gun per button press)
- rate of fire (used with burst)
- cooldown
- wind up delay
- detonation/impact type: cross, 3 way, 2 way sides or back forth v/h, 1 way (forw or back).
- projectile or detonation element: fire/HE, kinetic/blade/frag/hammer, plasma/atomic, laser, particle, electro/emp, steam/smoke/fog, lava, water, freeze, dirt, pollution/chem/gasoline, wind/force, hack/cyber, shield/hard photon, microwave, flashbang, stun/tether (auto detonate on lifetime/distance end)
- knockback direct (how many tiles to push forward)
- knockback detonation (how many tiles to push outwards) (both can be used for pull/grapple/tractor too)
- recoil (how many tiles to push self backwards... Or forwards if negative values, can be used to ram opponents)
- max ammo/durability (latter for melee or energy weps)
- rarity/cost
- Stun type: move/rotate/fire/mix of 2
- stun length
- self stagger lenght
- penetration count (if target hit, continue or stop? how many times can projectile continue? If target was hit it can't be hit again by that same projectile.)
- larpa y/n (leave something in trail upon each tile where bullet travels through?
- larpa drop (fire, steam, flam-gas, explo-gas, plasma, cryo haze, grav well, goo/sticky, foam, dust/chaff, dirt/solid, growth/bio, lava, dry to sand, water submerge, emp storm, particle energy residue, object drop (laser prism/mirror) temp or perma.)
- larpa start (earliest drop? First tile or later?)
- larpa end (do drops end before bullet expires?)
- ignite gas y/n? (Usually for burning bullets or lasers)

All weapons are semi auto or burst attack.
Most weapons tend to be condensed/compact/packed/pulsed. Even things like machineguns fire a packet of rounds with a sound effect that sounds like multiple shots were fired when just a single or few "blobs" of shots were launched ingame. It's very 'front mission tbt combat' esque in that sense.

In terms of content, weapons range from firearms to melee, modern to futuristic, kinetic to energy, elemental to mundane, combat to utility, terrain altering or object/tile floating effect spawning. The potential is mostly endless and players can loot guns and stuff off the battlefield to replace/swap/bolster/resupply current loadout. Caveat is that only one item can be on the floor at any given time, so if an opponent were to be blown up over a tile with an existing item on the floor, it will be crushed and replaced by whatever loot that particular npc will drop.

## Player & mobility:
Player character is a multi terrain combat mech.
Lorewise it could be a prototype TYPE 3 Mecha that is being tested against conventional forces, while doing some good by taking out regimes and other monsters/threats/hostiles.
There's mild armored core customization where Mecha are built from top part, bottom part, maybe some internal parts.
Mobility is similar to Advance Wars 2, but instead of fuel, it's "stamina", replenished by the unit's reactor.
Each terrain type has a traversal difficulty value/type, meanwhile mechas bottom part has a multiplier per terrain type and restrictions/allowances which they can go through or not.
Some bottoms are able to travel smoothly through most tiles at regular speed (hovercraft) but have problems with recoil, knockback that bipedal doesn't have. Meanwhile spider legs allow walking over mountains or obstacles, but are slowest.
Bottom, internal or top parts influence stamina point amount and stamina recharge rate per second.
Similarly NPCs also adhere to these rules.
Some terrain types and bottom types grant zero stamina cost to movement, like wheels + road, rollers + rail. Ones that understandably don't have friction.
Top, bottom and internal parts may also influence total hitpoints, special passive bonuses (fire resist, improved melee attack, can't be pushed away or damaged by npc trying to move into players tile) or negative traits (out of 4 equipment slots, only 2 slots carry weapons/items while others can only accommodate items).
Weight/Mass is another attribute of units that determines what happens if a unit tries to move into another units tile. Either the attempt is blocked with no effect to either. Or one is merely pushed away but not damaged. Or pushed and damaged. Pushed more than one tile and maybe damaged. Or damaged if opposing unit is pressed against wall.

## Enviro Theaters:
Air mobility/air combat (auto move, npc patrol, turn restrictions, minimum speed, stalling, hovering/floating, 
Sea mobility (technically same as ground combat, but mostly water areas. Mecha is sort of amphibious like how infantry can walk into lakes in advance wars 2.)
Space/orbit mobility (momentum drift. Must counter move to brake and stop moving)
Hyperspace (zone compresses towards middle of route and decompresses towards exit, or something akin to Topverse. Maybe strafing only and rotating only, movement disallowed.)
Undersea mobility (slower everything, auto break, shorter push from knockback recoil)
Ground mobility (regular combat with terrain)
Underground (same as ground)

## Switching between ground-air-underwater-space:
I'm thinking of a WhiteBase/Cryptark style mobile all-environment base that is armed to protect itself but the mech it carries is it's versatile spear that can go as a one-man army and decimate opposition while adapting to battlefield conditions by looting stuff and being armed with up to 4 weps/items.

Each battle scene focuses on one layer of battle at a time, be it ground, air, space or underwater.

The core mech itself is perfectly comfortable on it's own on the ground combat area, but for other places it may use Strike Packs, like from Gundam Seed where these addon jets can be launched and attached to the mech to augment and make it airborne, spaceborne, uw-borne. The core top/bottom/internal parts remain the same but the jetpack mildly changes them, hence each part has some benefit and traits per each enviro as they too adapt to environments. The strike packs do force the realities and movement rules upon the mech so player only uses them if they have to, hence why ground combat doesn't need one.

Btw sea surface, limited shallow underwater and underground enviros are fine with the base core Mecha.

Perhaps ground strike pack is a thing but it gives support for ground, sea, ug and uw enviro combat, but it's perhaps built in so space/air strike pack goes on top of it.

Maybe I just need default + air/space strike pack after all instead of more than those. Maybe a hyperspace addon to the air/space strike pack will cover hyperspace portions of the game.

## Mobile base and crew:
You get a captain/astrogator, mechanic/engineer, scientist/doctor, janitor/maid and you as the crew of the ship. They support and react to your adventures.

One silly idea is that the captain is a older man (like captains/admirals in Japanese scifi commonly) that will vomit if you do atrocities and war crimes during low metagame. He's not unwell or disgusted at player, he just reacts to the dystopian violence around him with that vomiting to mild comedic effect, especially because it happens often.

## WIP Todo or ponder:
Human scale vs mech scale? Deploy a killbot/pilot from mech to go indoor to kill baddies in dungeon style enviros? Tacticool slower deliberate style compared to Mecha that are faster and more destructive.
Fog of war?
World gen? (Battlemap, overworld map)
Low/high metagame? (Low: obliterate map. High: Collect glowing reviews for the missions conducted with the TYPE-3 Mecha. Killing civvies or causing a lot of pollution will frame the news to be more renegade and unhinged instead of paragon and heroic, highlighting the lesson of why using force should be done with restraint. Still, won't stop you from doing "evil" playthroughs and have cathartic fun with it. It's two different ways to play, both supported and rewarded in their own ways. Some scenarios will make more sense to play evil while others more heroic (civilians vs leadership, if they too similar, playing evil is fine and even encouraged as they may not be grateful for your actions if you spare/save them). 
Weather/events/aw2 style volcano etc.
Idea of "Pollution of war" as a secondary theme in game?
Supercores as upgrade modules that expire with durability, attached to boss enemies? Boosting weapons or player mech, making it able to do stuff that it's loadout doesn't allow?
Forests that units can go inside and fire from/through without demolishing the forest on the tile necessarily?
Mountain tiles that do support units standing on them and they can be shot at without hitting the mountain, but if the opponent stands behind a mountain, putting it between you and the enemy, then your shots will hit the mountain instead.
Mountains shrug off most damage unless it's specifically able to blast it away (graviton, nuke, mega beam, ultima protoss, etc.).
Bullets go through forest, but explosions or larpa'd (that weapon from Liero that drops a trail of bomblets at it flies over the area) fire/plasma will erase them.

## Sprites: 
everything is 16x16px. Terrain tiles are seamless tiling textures, no 9-patch stuff. Objects and units are sideview sprites that face towards left or right(flip mirror). GUI/HUD will determine if they face up or down via arrow marker, but sprite itself will face one direction. Make it easy to create new content by requiring only one sprite per object. Rest are handled by particles, muzzle effects, overlaid sprite anims.

## HUD:
Aw2 style. Compact on demand info boxes. Press L, R, Select to bring up additional info menus, inventory, etc other screens with tabs - all navigable with WASD EQ.

## Enemies:
Any 16x16px sprites including aw2 military units, space monsters, dungeon freaks, rabid animals, angry humanoid mobs/zombies, robots, cyborgs, undead things. Each can be its own expansion pack. Along with structures/obstacles/objectives/tiles.