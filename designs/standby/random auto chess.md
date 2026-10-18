Analyze this plan below and suggest what tech should I use to make this work? I assume web app to make it instantly playable on itch.io as a web app, while phaser mainly for the particle effects and sprites, though perhaps it's not needed and would work better with a simpler solution of some kind. I also wonder if I missed any details in regards to quality_of_life stuff or some basic visual, UI or UX details that would be suitable to the experience.

# Plan:

Make a simple top down 2d chess game that automatically plays itself. As a standalone offline web app with html/css/js and phaser maybe?

The AI for both players works like this: identify if checkmate has happened yet, do a X team wins, press any key to continue or have a checkmark to autostart a new session in 30 seconds.

If game is still on, pick any random chess piece that belongs to own team that is able to do valid moves. First check if any pieces can attack any opposing chess pieces and roll a 50% coin toss if they should do the attack(exception: if king is target 100% attack, always check first if anyone can attack them specific that turn to fullfil a checkmate situation) or ignore it and instead do a regular movement instead with 60% chance forward or forward right or left, 30% chance to side right or left, 10% chance backwards, these are of course adapted per each of the 6 chess piece types (pawn, rook, knight, bishop, king, queen).
Each move/action/event uses simple easing animations (choosing a random type each time, like easeIn, easeOutCubic, etc.) with a randomized animation duration per each move of 1-3 seconds. There's a 0.5sec pause between turns, though only after the animation from the previous move had already finished.

Choose/random team colors of any hue (range 0-255), saturation (range 50-240) and brightness (range 50-220 (depending on dark or light team). Opposing team always uses any offset hue color.
Moving pieces cause permanent color trails on board.
Defeated pieces leave a splash where they stood, while the defeated pieces flies offscreen with direction and speed (plus a randomized 1.5-2.0x speed multiplier on top of that) decided by same movement vector attacker piece used as momentum and is disabled after 3 second flying past the border.
Game creates essentially art pieces automatically from the autoplay that can downloaded as a PNG (512x512px).
Team names are based on hue and brightness value they're closest to (i.e. dark red, bright cyan, medium blue)
Game board uses any hue, but saturation range is between 5-45 and brightness range is 5-45 for dark tiles and 225-250 for light tiles.
Background surrounding the board is also any hue, but brightness/saturation level is between range 5-100.
Text labels contrast against bg for easy readability.
Text labels include:
- web app title label (auto art chess)
- match name (team1name vs team2name)
- who's turn it is currently or who won
- battle status (normal, check, checkmate)
- 30 seconds countdown for new match (if checkbox enabled, see below)
Always have these controls:
Button to start new match (reset current board, even if a match is currently on going. Fresh new board, new teams, new background, all labels updated/refreshed, new colors picked for everything).
Checkbox to automatically start new match after 30 seconds once the last one had reached checkmate statusand fulfilled it by defeating the king piece.
Button to Pause/Resume current auto game.
Button Save current board with pieces, stains and a 6px margin of surrounding background as a PNG image file.
Game board is 500x500px 8x8 grid on the wide right side while the narrow sidebar for status/controls are on the left. Total resolution is 800x600px, with those elements fitted within that area.
I'd do this as a phaser web app (phaser version depends on which one you're most comfortable at supporting coding reliably with, maybe v3.55.2?), providing icons for chess pieces (single set of white pieces at a square 64x64px size, scaled/resized to fit inside grid squares with atleast 2px margin from edges of said grid squares. They are tintable for both teams) and a generic particle/decal texture for both smears and splats... though maybe there's a better option for the smears and splats like drawing onto frame buffer so it's more efficient than keeping decals/particles on screen? I'd have all sprites as PNG files in 'assets' folder.

No sound effects or music for this project.