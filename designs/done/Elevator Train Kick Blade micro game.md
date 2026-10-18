Ultra simple premise of a kicking dudes away satisfyingly with relatively minimal controls that can be played with one hand.

Lorewise it's about a civilian going after greedy CEOs, using nothing else but his kick and blade. Similarly, enemy goons are loyal employees without any weapons other than batons. CEO just stands and just uses condensending words to scare the player into giving up.

Each battle is a single screen that happen on a moving elevator, moving train, or static CEO room. There's a swipe to black transition between rooms that happens automatically 3 seconds after room objectives are complete.

There's a sense of Virtua Cop to the whole game where player defeats an X amount of goons in a room, can use a cover move to dodge an attack and does a gauntlet of rooms before reaching the end of a stage, defeating a boss at the end of it.

Movement and attacks are modeled sort of after Kirby/smash bros, minus the flight or ability copy.

AD - move left right
AD double tap and hold - sprint
W - jump/double jump
S - if in air, plunge down
E - kick (whichever direction you facing)
E while mid air - air kick
Q - blade (whichever direction you facing)
Q while mid air - air blade
X - dodge(stationary)

Sprint + kick/blade = powered attack
Falling + kick/blade = plunge down attack
Going up + kick/blade = up strike
Sprint + fall/jumping + kick/blade = flying powered attack
Hold Dodge + kick/blade = parry/special (with cooldown)

Esc and enter for pause/menu nav.

(Notice how game is playable one handed!)

Every opponent goes down in one hit, but player can withstand several hits (with ways to heal) before being subdued by baton strikes. Kicking enemies sends them flying and exploding on impact with a surface (wall, ceiling, floor). Trajectory is based on player position in relation to enemy. Enemies gib on exploding. Blade is similar but enemies are gibbed immediately and spray the place with blood particles, gibbing is based on momentum while kick gibbing is radial. Normal attacks weakly gib characters with a delay, while powered attacks strongly gib them immediately, ala Invincible going serious mode on reanimen.

Overall it's an easy cathartic game taking place on trains, cargo elevator, funiculars, and CEO penthouses with a big glass window. It doesn't have the bs of endless mode or infinitely spawning enemies, highscores or nonsense stages without purpose or structure. 

Enemies telegraph their attack 1 second before following through and player can usually dispatch enemies easily and quickly without getting hit.

Game uses basic arcady physics for character movement, jumping/falling and kicked enemy trajectories. Basic downward gravity is standard.

High metagame has randomized made up CEO names, name of industry and a crime they've done in the style of "stole millions from people", "sexually harassed employees for years", "green light a poisonous product", "knowingly used slave labor", "ruined a local community ", "paid less than minimum wage", "ruined ecology of a region", "blatantly lied to customers", "chose profit over people", "pure greed", "forced people into debt", etc. crime and industry don't need to match.

Basic room & game flow:
Player is placed in the middle of the platform. Room can have solid side walls(vertical elevator), solid ceiling (tunnel train), only ground under platform (train. Falling onto said ground will instagib enemies or cause player to be kicked up and lose a hitpoint.) or a fully closed room with optional window wall on either side or on ceiling (CEO/barracks room/sealed elevator.)
During CEO encounter, player spawns on left/right, while CEO is on the opposite side.).

Each stage begins with a stylish rapid swipe from black transition with a player spawned on middle of stage, with a text "Stage x/x" and "ready" and "go". Then enemies begin to spawn from 1-3 designated spawn points from a total of 8 positions, corresponding to nswe egdes+corners of stage. Spawn rate is also dynamic and randomized and may intensify, weaken or fluctuate during stage, but always ensuring atleast 1-4 goons are active. Total goon amount is also randomized per stage.
Once last goon is defeated, a text saying "complete" appears, and after 3 seconds, a swipe to black transition comes. Repeat this for all except last stage that simply spawns CEO and player on opposite ends of stage. No "ready go" text here. CEO will simply begin spouting bullshit as top subtitles that are shattered as soon as CEO is defeated. Game plays in gauntlets of 8+1 levels. If player loses, they reset to start.
Recorded CEO kills to log as trophies in main menu screen.

Player fail:
Upon losing last hitpoint, player does a typical Super Mario Bros fail scene where time pauses and player hops down off stage with a goofy face. Player may regen lost HP points slowly. Or they replenish between stages.

There's potential for a tough difficulty mode where HP does not regen, or not replenish between stages. Or have a time crisis style time countdown to keep player aggressive to prevent villain/CEO from escaping.

Optionally CEO may fight back as a baton thug too. Maybe with more hitpoints than just one. Successful hits stun and throw/push CEO. Maybe even have a SMW style Iggy fight where they're resilient to hits and are more reliable/faster to kill by knocking them off.
CEO fights can also happen in other spaces instead of just penthouse room - do the final confrontation on a train or elevator too!

Collision mechanics:
Player doesn't collide with enemies.
Player attacks are colliders overlap player sprite + directional area where they're aimed at. Enemies within attack collider are hit once and cannot be hit again until collider turns off and on again (so the same attack of player only hits once.) Attacks spawn/enable a collider that automatically turns off after attack is over. An attack lasts several milliseconds, with power attacks lasting a bit longer (+50%), then turning off, even if player holds down kick/blade button. Attack process on activates on button down press and abruptly can be cancelled by button up release.
Enemies don't collide with one another.
Enemy attack colliders (baton swing) only affect player sprite collider. Player attack will affect all enemies within collider, but only deliver one hit per each.
Enemy attacks if successful hitting player, causes player to lose one hitpoint and be mildly knocked back, and receive 2 seconds of invulnerability.
Enemies track a position in front of themselves and try to move and jump to player into that spot. Once they achieve this, they will stop, telegraph their intent to attack and follow through a second later. They stop moving and tracking the player until they're done with performing their attack. Then they resume pursuit. Occasionally goons will stop to stand still for 2secs + mild randomization, as a way to catch breath when trying to catch the player. Goons may rarely may also jump out of random impulse while moving or just attack the air, with a random cooldown per spawned character, giving them all subtly a personality based on how often they pause, jump, swing. Their move speed is also mildly randomized. Enemy aerial movement is momentum based, but they have minimal to no air control.