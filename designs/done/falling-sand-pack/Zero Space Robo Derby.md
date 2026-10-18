# Falling sand game variants
(I'm making a series of games that fall under the same category of leveraging falling sand game mechanics (cellular automata with physics) in some way and originally I wrote a big mega document with all the ideas in it, then later split them into individual small documents to keep the prompt focused. The stuff after the Game Ideas is the actual game idea I want you to focus on, while the below two paragraphs are merely an intro that is free to be overwritten/disregarded in favor of the actual game idea that takes all priority.)

The idea is to have very simple, short and satisfying game experiences that primarily incorporate falling sand mechanics in some way. By falling sand, I dont exclusively mean sand only, but the general game engine of falling sand games like Powder Toy or similar pixel simulation sandboxes. The range of materials/phenomenom are always limited to the scope of the particular game at hand, so while some games may feature things like fire, sand, water, grass, snow, ice, wood, stone, flammable gas, etc. it always depends on a per-game basis what they'll ultimately have, both to keep them focused and simpler to make.

While falling sand mechanics are at the forefront, the game can feature other 2D game elements and colliders that work in tandem with the falling sand. Also unlike most falling sand games which are merely open sandbox experiences without any structure or metagame, the games I want to make aim to have enough game design embedded into them so they're atleast on the same level as a typical kongregate web game or a newgrounds flash game, in terms of gameplay, small scope and cohesiveness as a proper game experience, even if its simple/basic. 

That said, I aim to mainly release them on desktop platforms (PC, Linux, Mac), maybe web too if its possible to make it performant enough for it to work there. But Windows PC is always priority one as the release platform.

## Game Ideas

### Zero Space Robo Derby

Fly in solid ship asteroids style, drifting with momentum in zero gravity, shoot at other solid ships in a free for all rectangle arena shootout. Unlike asteroids games, no screen warp here. If their HP goes 0 then turn them into falling_sand style particles (cellular automate with physics) with inherited impact momentum that flies towards off screen or vanishes after X seconds, going from burning hot neon colors to a random dark muted (kinda like fireworks I suppose, of any color or color combo). 

Sort of like a demolition derby with a Robot Wars (the british entertainment TV show) theme, but instead of head on-collisions, the robo-ships use a slow charge up blaster that has a quarter second delay before firing and when it fires, it launches a projectile at medium speed going directly forward and deals more damage the longer it was charged (charge time range min/max is 1sec to 5sec), with a maximum damage potential of 60hp hit and minimum 5hp hit. All ships start with 100hp. Amongst ships, theres also random asteroids floating about that will behave as they would in asteroids games, splitting into two several times before being fully gone. Collisions with asteroids are harmless and they're mostly used as pushable physics cover to soak up incoming blaster hits. When asteroids break apart, they also spawn falling_sand style pixels. Blaster impacts and roboship thrusters also spawn falling_sand pixels akin to a typical particle effects emitter.

Players can pick up powerups that randomly appear on the level every 15 seconds and bounce around until picked up via ship contact, to add an ability to their blaster:
- phase: shot goes through asteroids and ships.
- scatter: shot explodes on impact, splintering into 6 smaller 50% power shrapnel hits.
- homing: shot will slightly curve to adjust its trajectory towards opponent in line of fire within the 20' degree firing angle calculater from the shooters ship.
- warp: shot will warp around the screen once.
- triple: ship will fire 3 projectiles in a spread pattern, each only 75% powerful compared to default single shot.
- hypervelocity: doubles weapon damage output and projectile launch speed but also doubles charge time.

These upgrades can stack and last for 60 seconds before expiring.

#### Control ship with just mouse:
- mouse aim: rotate ship to face direction
- mouse 1: hold to charge weapon, release to fire
- mouse 2: apply forward thrust
(a dandy easy to learn, hard to master one-handed game of exciting fun)

Player has maximum speed and there is automatic braking/air resistance that will slow the ship down gradually as it drifts with its momentum using basic physics.

#### Lore:
A hobbyist community event where some space colonists get together to have fun crashing visually customized (yet standardized hardware wise) robot ships for the entertainment of everyone. Each ship has a unique name and unique short-lived cellular automata particle core which has its pixels break out of it when its blown up (maybe they're customized fireworks or sets of substances that behave in interesting ways in zero gravity), creating a randomized fashion of a cellular automata spectacle that lasts for 1-5 seconds, mostly as a cosmetic pinata delight for the eyes.

Its a laid back event, so its less about competition and more about having a fun time together. I guess the prize for the winner is to have the honor of setting off a big zero-gravity bonfire/megafirework that has a much larger payload of randomized cellular automata pixels that lasts 4-6 times as long with way more pixels.

#### Metagame:
Low metagame is a set of 6 stages of roboship blaster derby whoever scores most points get to be a winner. If the score is tied, then the two player must share the honor of pressing the button to launch the surprise payload big bonfire show.

High metagame is about collecting a photo/videoclip album of the different bonfire payloads - they're generated with a seed so they can be replayed exactly each time. Each entry will show who won and with how many points. Each contestant except player has a randomized name for controller/pilot and a random name and 2 color scheme for the roboship they control.

There is only that one game mode, albeit player can choose if they want 3,6 or 9 stages. Bigger stages each result in a +30% larger surprise bonfire bang at the end to compensate the extra effort.