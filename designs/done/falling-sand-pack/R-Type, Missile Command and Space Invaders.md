# Falling sand game variants
(I'm making a series of games that fall under the same category of leveraging falling sand game mechanics (cellular automata with physics) in some way and originally I wrote a big mega document with all the ideas in it, then later split them into individual small documents to keep the prompt focused. The stuff after the Game Ideas is the actual game idea I want you to focus on, while the below two paragraphs are merely an intro that is free to be overwritten/disregarded in favor of the actual game idea that takes all priority.)

The idea is to have very simple, short and satisfying game experiences that primarily incorporate falling sand mechanics in some way. By falling sand, I dont exclusively mean sand only, but the general game engine of falling sand games like Powder Toy or similar pixel simulation sandboxes. The range of materials/phenomenom are always limited to the scope of the particular game at hand, so while some games may feature things like fire, sand, water, grass, snow, ice, wood, stone, flammable gas, etc. it always depends on a per-game basis what they'll ultimately have, both to keep them focused and simpler to make.

While falling sand mechanics are at the forefront, the game can feature other 2D game elements and colliders that work in tandem with the falling sand. Also unlike most falling sand games which are merely open sandbox experiences without any structure or metagame, the games I want to make aim to have enough game design embedded into them so they're atleast on the same level as a typical kongregate web game or a newgrounds flash game, in terms of gameplay, small scope and cohesiveness as a proper game experience, even if its simple/basic. 

That said, I aim to mainly release them on desktop platforms (PC, Linux, Mac), maybe web too if its possible to make it performant enough for it to work there. But Windows PC is always priority one as the release platform.

## Game Ideas

### Twin-Stick-Shmup/Missile-Command/Space-Invaders (sideview)

This one is a mix of R-Type, Missile Command and Space Invaders, as a 2D sideview that plays like an autoscrolling twin-stick shoot em up. The falling sand aspect here is that objects are initially 2D objects that turn into fiery dust falling sand particles that shift in color, breaking down with force and momentum based on the impact they suffered from player's weaponry. I supposed techwise theres the 2D game layer and a falling sand layer that acts as the visual special effect for this game.

Although I said R-Type, which is about a starfighter, this game instead has a starfighter mecha (starmecha) that launches missiles in the style of the classic game Missile Command, that fly out of players starmecha towards a spot where the mouse cursor is positioned at and detonate there, with a lingering circle that slowly grows, reaches its apex size and slowly shrinks until it disappears, simulating an explosion that obliterates any invader alien ships caught in the blast, though player is immune to the blast and they're immune to all their own weapons in general too. Enemies are also immune to their own weapons.

The starmecha is also armed with a rapid burst-fire mass driver that allows the player to unleash a burst of high velocity projectiles like the A-10 Warthog's GAU-8 Avenger weapon. These can clear out a whole line of invader ships in a single burst by tearing right through them. Lastly player has a slow-firing frag-shotgun that saturates a wide spread of super heated projectiles to wipe out a group of enemies, although unlike the mass driver, the shotgun does not penetrate through opponents, meaning invaders hiding behind their comrades will survive unscathed.

Space Invaders style enemies appear in waves from the right as various random geometrical formations and they bounce around the stage, either as a unified formation they started with or randomly splitting off chaotically. The players starmecha starts out on left, shooting down invader waves while dodging their sporadict shots by freely moving around the area using WASD. Unlike most shmup games that have a fixed firing direction, the starmecha aims freely using the mouse, able to fire in any direction 360 degrees, with the mouse aim rotating the starmecha with its weapons to face that direction.

The player has a recharging shield they can use by holding down a hotkey, which drains its power until it runs out and will regenrate when not in use at a rate of 9 seconds to recharge 0% to 100%. Theres about 3 seconds to total usage time before it runs out. Useful to get out of sticky situations without taking damage. Player can also teleport to the opposite mirrored/flipped position of their current location in the rectangular stage. This means if player is at the top left corner of the stage, they'll end up in the bottom right corner of the stage.

Player can withstand 5 enemy projectile hits or collisions before being destroyed while invaders will be defeated in one hit. This is to make up for the fact that invaders massively outnumber the player. Invaders focus on quantity, player focuses on quality.

The last enemy of the wave drops an artifact that the player can pick up as a powerup, which will do one of these things:
- repair one hitpoint (if less than maximum).
- increase blast radius and duration of missile explosion by +5%.
- increase firing duration of mass driver burst by +5% (shoots a longer line of bullets, giving more time and chance for bouncing enemies to run into that line of bullets and get perforated by them).
- increase the firing velocity of shotgun +5%, effectively increasing its range.
- +1 defence orb thats orbiting around the player ship, absorbing incoming enemy projectiles and collisions, upto 3 hits before expiring. Can have a maximum of 6 drones.

Game is about doing an X amount of rapid stages that each have a wave of 10-40 colorful invader enemies of varying shapes and sizes, mixed together in randomized formations. Player wipes them out, has about 2 seconds before the next wave begins and keeps going, gradually growing in power with powerups that keep stacking benefits, eventually reaching the last stage.

The amount of stages is chosen by the player to determine how long and epic they want the game to be. Short games will only have 20 stages, then theres 80 stages medium lenght campaign setting, and finally a 200 stages option for an endurance battle. Player can also choose the color of their ship.

Falling sand is visually present with all weapons, trails and explosions happening in the foreground effects layer. When either the player or invader enemies are blown up, the initial color of the falling sand particles that they burst into is the same color as the sprites were or what the player's chosen color was. This color then shifts from that color to a fiery neon color, then to a black color before the particle expires and is gone.

This creates a beautiful display of colorful falling sand particles punctuating the fast paced combat dance. Some rarer dark and muted color secondary particles on a third background effects layer from ship explosions may linger and float about the stage, accumulating through out the campaign, creating a painterly nebula-like background as the stages go on.

Before enemy invaders appear on the stage, there is always an orange '!' exclamation signs shown near the spot at the right edge of the stage where they will enter into the stage. This helps the player avoid crashing into them on accident during the beginning of each wave. Enemies arrive in a unified formation into stage all together before they randomly decide if they want to disperse or stick together for the duration of that stage.

The enemy waves dont get stronger or weaker with later stages, they're always randomized and they may be consisting of any kinds of units, in any formation.

After clearing the last wave, a large orb appears as the alien core, spawning one invader every 1 second, up to 10 of them at any given time, and upon being hit by any of players weapons, will spectacularly explode in a giant burst of particles, like a ship explosion on steroids with a 4x force multiplier.

Context of this game is player assaulting an alien invader hive inside of a planetoid, taking the fight back to them with a starmecha, fighting through hordes before reaching the planetary core and blowing it up. The resulting canvas is saved as a screenshot 3 second after the planetary core had blown up with the player in it, able to strike a cool pose as they wish. It basically creates a cool sharable art piece with each playthrough.

Longer campaigns with more stages will create a more denser and richer art piece, while shorter runs will be sparser and more minimal.

Controls:
WASD - move
Mouse aim - rotate mecha and its weapons
Mouse 1 - Fire mass driver burst
Mouse 2 - Fire frag shotgun
Q - Missile Launch
E - Use Shield
X - Teleport to mirrored/flipped position on stage