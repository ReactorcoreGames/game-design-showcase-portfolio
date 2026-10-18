# Falling sand game variants
(I'm making a series of games that fall under the same category of leveraging falling sand game mechanics (cellular automata with physics) in some way and originally I wrote a big mega document with all the ideas in it, then later split them into individual small documents to keep the prompt focused. The stuff after the Game Ideas is the actual game idea I want you to focus on, while the below two paragraphs are merely an intro that is free to be overwritten/disregarded in favor of the actual game idea that takes all priority.)

The idea is to have very simple, short and satisfying game experiences that primarily incorporate falling sand mechanics in some way. By falling sand, I dont exclusively mean sand only, but the general game engine of falling sand games like Powder Toy or similar pixel simulation sandboxes. The range of materials/phenomenom are always limited to the scope of the particular game at hand, so while some games may feature things like fire, sand, water, grass, snow, ice, wood, stone, flammable gas, etc. it always depends on a per-game basis what they'll ultimately have, both to keep them focused and simpler to make.

While falling sand mechanics are at the forefront, the game can feature other 2D game elements and colliders that work in tandem with the falling sand. Also unlike most falling sand games which are merely open sandbox experiences without any structure or metagame, the games I want to make aim to have enough game design embedded into them so they're atleast on the same level as a typical kongregate web game or a newgrounds flash game, in terms of gameplay, small scope and cohesiveness as a proper game experience, even if its simple/basic.

That said, I aim to mainly release them on desktop platforms (PC, Linux, Mac), maybe web too if its possible to make it performant enough for it to work there. But Windows PC is always priority one as the release platform.


## Game Ideas

### Fire Extinguisher Megalodon
(2D single stage sideview scene of a city on fire. Control an FPS style cursor, aiming where to shoot water. Heavy emphasis on falling sand game style mechanics and rules.)

materials:
- wood/ash (not gravity affected, flammable, conducts fire to other wood pixels gradually at a rate of 1 pixel per second), burns for 300 seconds before turning to ash, creates heat that transfers to nearby stone at a rate of 10 per second)
- stone/lava/obsidian (not gravity affected, heats up with burning fire pixels adjacent to it, if reaches 100 heat points that it accumulates, turn into gravity affected lava that flows and generate heat into adjacent stone at a rate of 2 per second. lava lives for 600 second from birth before turning into inert obsidian. Hot stone can be reset to 0 with a water blast and lava can be turned into obsidian with a water blast too, to prevent further damage spread.)
- water (gravity affected, flows/moves freely horizontally, vanishes in 60 seconds or if it touches burning wood then it removes the fire and saves the wood at the expense of water pixel sacrificing itself. Water touching lava instantly changes it to obsidian also sacrificing the water pixel in the process. Similarly water will sacrifice itself to reset a stone with more than 20 heat points down to 0. Ash will be instantly deleted on touching water without anything happening to water in the process; water sort of "cleans" ash away and continues flowing/moving like it had no effect on the water pixel itself.)
- terrain (completely inert and immune to everything. water, ash, lava all collide with it.)

Use water blast explosions to stop fire in a FPS helicopter gunner view style. (player is actually controlling a big, bulky and powerful azure blue mecha-helicopter hybrid vehicle designed specifically for turbo firefighting missions.)
- rapid auto fire small shots
- charge up big shot altfire
- both shots create an circle area of effect extinguishing effect while also spawning an exploding circle of water as falling sand type pixels. Both the area of effect circle and the water pixels will immediately extinguish burning wood, reset stone's heat to 0 and turn lava to obsidian. The pixels will vanish when they do any of the aforementioned extinguishing effects or evaporate automatically after 60 seconds.

Randomly generate a building with various geometrical methods using rectangles and lines, then later in the sequence use lines, small rectangles in a smart if/else decision way to add detail to building using simple patterns. This random building procgen is versatile enough to create anything from a small, tall, wide, big building composed of one or more rectangles and use additional smaller rectangles and lines (horizontal and vertical only) for lesser details to create all kinds of wild structures that are all nevertheless still connected to the floor/ground.

wood and stone would each use one random color per level to make each level unique.
wood would use colors that imply wood, cable, insulation. Brown, tan, green, yellow, blue. Generally colors are only mildly desatured, but brighter than stone though not overly garish.
stone would use colors that imply stone, metal, brick, concrete. Grey, red, white. Generally colors are only heavily desatured and darker than wood.
terrain color uses earthly tones and is darker and even more desaturated than stone.

Context: Game is about arriving at scene of meteorite/spacewreck debris shower falling from space in small hot fire starters thrown all around the level. Fire gets a small headstart to begin burning and player tries to minimize damage while shooting down additional pieces with FPS gunnery cannon. The new pieces fall from the sky during the firefighting process but impact anywhere on the map from a first person view, not by colliding from top - player has to judge whether they shoot it down with guns or let it impact and use water guns instead to avoid blasting buildings to pieces with their gunnery cannon unintentionally as they'll cause more fires than the meteor will upon impact. Successfully detonated midflight meteorites/debris turn to ash with momentum they already had plus some added extra radial explosion momentum from its epicenter. If meteorite hits the ground, it goes off like a cluster bomb, spraying lava pixels from the point of impact.

9 level gauntlet comprises of a single crisis where 9 clusters of the falling meteorite attempt to wreck havok on an area with 3-7 complex buildings per level.

Effects: burning wood has a fire particle effect, lava produces smoke emission that rises up.

Controls:
Mouse cursor - position crosshair
Mouse 1 - launch water shots/charge up water blast. Uses up player's reserve of water.
Mouse 2 - hold down to replenish active water tank/capacitor. Water ammo: 100 rapid shots or 50 big shots.
(player has a much larger ultra-compressed reserve tank of water that they draw from and it has a finite yet very generous amount of water, so player can freely spam water to do their fire extinguishing work, albeit there is a limit to how much they have before it runs out, which will prompt a mission failure if fire is still ongoing on the current stage when water reserves are fully depleted.)

---
Added:

Hmm, I noticed in the controls section that its missing the "gunnery cannon" that I failed to properly elaborate in the doc. Basically the mecha is equipped with both a dual-fire mode water cannon, but it also a secondary weapon: a kinetic AP-HE munitions autocannon that is intended to shoot at meteorites or demolish obstacles out of the way. Player can switch between those two weapons. I suppose for the autocannon it can have a quick fire mode and a charged up electromagnatically accelerated shot for a more powerful and penetrating hit against harder (and rarer) meteorite targets or other hardened obstales that get in the way of fire fighting.

I also want to clarify that the game sort of plays like a light-gun game akin to virtua cop or time crisis or The House of the Dead, although instead of player being in danger its the scene being in danger and player tries to save it or atleast minimize the amount damage it suffers.

In regards to high metagame, just have a log of completed campaigns that player can regenerate with the seed it had to play it again and try to increase the final score, sort of like retaking the exam. In fact, lets reframe the context of the game to be that of a unique time traveling one-of-a-kind mecha-copter hybrid that travels to prevent disasterous fires as they happen. It has some anomalous time-space connection that it got tangled with during a mission that involved a space-time rupture that it temporarily fell into and but managed to escape, having gained a power to change course of history, but is forever trapped in warping into different times and location every so often.

Besides that, the image quotes should be more tied to game mechanics or tech involved with falling sand stuff, albeit layman friendly worded.

Generally rest of it is on the right track though. I say incorpate the above changes and proceed to HTML building.