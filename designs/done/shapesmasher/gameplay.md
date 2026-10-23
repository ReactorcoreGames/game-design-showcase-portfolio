# Shape Smasher: gameplay (the smashing side)

Back to [index.md](index.md).

## Platforms and screen

- Phone vertical and PC + phone horizontal are both sketched (SS1). The vertical mockup shows a little temple/arch and a lamp post being hit by a falling cone-shaped object. The horizontal one shows a cannon-like launcher on a block with a ramp, firing a spinning textured block toward three tall triangular trees.
- The vertical play screen (SS3) is split into a **player spawn zone** (hatched band along the top) and the **art space** below it, with the sculpture sitting on ground at the bottom and the phone's system bar under that.

## Objects

**DLO, Destroyable Level Objects** (SS1)
- Placed by the artist/user, or by procgen.
- Breakable/destroyable, spawning debris and effects.
- Can be picked up and dragged to throw around freely.
- The player can destroy an entire level without ever using a PWSO.

**PWSO, Player Wrecking Shape Object** (SS1)
- Indestructible. Only one exists on a level at a time.
- Can be made sharp by making it small. Can be imbued with fire to burn things.
- The player can: spawn/remove it, change its shape, change its size, change its material (friction), modify its density (hollowness), imbue it with elemental properties.

**Shapes and materials** (SS1) are shared by both: see [level-editor.md](level-editor.md). Physical properties come from the material and the shape's size (area): bigger is heavier, smaller has less HP, with thresholds, mass and total HP derived from size.

## Touch mechanics (SS2)

Similar to Angry Birds slingshot controls, but you can grab any object on the level:

1. **Point and hold** an object on the level. This cancels its current momentum and creates a temporary joint between the finger and the object.
2. **Drag** the finger in the desired direction to set a new directional momentum on the object while holding it.
3. **Let go** once a desirable trajectory (direction plus speed/force) is set. Provided nothing interfered, the object launches with the momentum the player set.

- Any other moving object that collides with the held object knocks it loose from the finger/mouse, cancelling the joint and the interaction.
- **ALT: drag object.** To have the object move with the finger instead, press and hold anywhere else on the screen with a second finger. Instead of setting a momentum, the object is attracted to the first finger's new position. ALT also reinforces the joint's strength threshold (so it's harder to knock loose).

Further control ideas from the text notes: a player force multiplier boost ("overdrive mode"), and physics limits (max velocity, max and min size).

## The play sequence (SS3)

1. **Level opens.** The top shows two buttons, **SPARE** and **SMASH**, the art's name (custom or a random name) and its ID number (e.g. ID#1062048).
   - **Spare** = respect, endorse, like, show mercy. The art shows a randomized reaction such as "Thank you!".
   - **Smash** = proceed to destruction gameplay. The art reacts with a randomized line such as "oh no D:".
   - **Bad** = "blam it" for deletion, total dismissal.
   - **Remix** = create a clone of the level with edits.
   - Whichever is chosen is signalled to the server.
2. **Smashing.** Free physics destruction with the touch mechanics and the PWSO.
3. **After smash** results screen: "Your stats" (example: 86% destroyed, X newtons of damage caused, time taken, the last marked with a question mark), **NEXT**, **REMIX**, current campaign progress shown as a row of circles with the finished ones crossed off, current time, and a **BAD** button in case you wanted to smash first and then report it.
4. The player rates the art with one feeling (see the emoji grid in [structure.md](structure.md)).

Extras on the same page: users can **sprinkle minidudes** into a level to add more gore.

## Defining when a level is done (text notes)

From "ShapeSmasher Thoughts": no total-destruction requirement, no arbitrary percentage. **The player defines their own finish**, then a screenshot of the aftermath is sent to the author. Also: no timers, no stats, no user tracking (this contradicts the stats on SS3's results screen, which is marked with a question mark; the text notes seem to be the later view).

## Game modes (summary doc)

- **Social critique mode**: a wide arsenal of weapons, powers and art tools (spray paint, markers, paint brushes, paint buckets), plus temporarily opening the sculpture in the level editor to change it as part of the critique. The aftermath screenshot goes back to the author.
- **Pure game mode**: destroy a sculpture in a specific way with randomly generated objectives, so each level replays differently. For when the player doesn't want the social side, just short sessions of wrecking with some push-back. "A satisfying scratch card stress toy."
- **Simplified version** (see index): eliminate randomly placed characters, with a random weapon loadout per level, and choose freely whether to spare the sculpture around them.

## Feel and session (SS9)

"Easy-play one-handed play session flow from start to end": whip it out, boot it, hit quickplay, have a blast, easily exit anytime.
