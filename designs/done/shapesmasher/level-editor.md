# Shape Smasher: level editor (the creating side)

Back to [index.md](index.md).

## Building blocks (SS1, SS16)

**Shapes.** All are scalable on the x and y axes independently.
- Basic: square (4), triangle (3), hexagon (6).
- Advanced: right triangle (90°, 3), diamond (4), pentagon (5), heptagon (7), octagon (8), and two flat triangles of 1/3 and 1/4 height.
- Special: four-pointed star, five-pointed star, six-pointed star, and a few slanted/trapezoid/half-round pieces. The text notes add arrow, diamond, star, hexstar, quadstar, circle (if cheap), capsule, oval, and explicitly exclude swastika, cross and Star of David.
- Unique entities (SS6): a row of small character/prop icons *(interpretation: creatures, a little figure, a vehicle, a hazard symbol, a small fire or torch prop)*. Likely related to the minidudes and the text notes' "dynamic objects (explosives, burners, heater, cooler)".

**Material** is laid over the shape via a shader, on the final stretched shape. A material gives a texture graphic and properties defined by size (area): bigger is heavier, smaller has less HP, with thresholds, mass and total HP. A colour tint goes on top. The summary doc names wood, glass, stone, metal, dirt and ice.

**Other DLO types** (SS16): standard shapes plus colour, text and symbols, ropes/cables/vines, desaturated background shapes for decoration, lights and lighting. The text notes add attachable text decals on shapes, text shapes, ragdolls and minidudes, chains, and shader effect overlays.

**DLO placement modes** (SS16):
- Individual physics objects, loose (solo) or coupled via joints (multi).
- Composite stacked shell: DLOs stacked or glued on top of each other into one piled/fused object that is still breakable through the parts it's built from.

**Optional framing terrain** (SS4, SS16): indestructible framing ground. Five layouts are sketched: floor only, right wall, floor (thin), both walls, and floor plus right wall.

## Editor layout (SS4)

Vertical phone screen, top to bottom:

1. **System menu bar**: menu icon plus the art's name (an automatic default name that can be changed). On SS4's second sketch the bar also shows the framing word.
2. **Shape editor box** ("LevEdit zone"): the current shape sits in the centre with a crosshair. One shape at a time snaps into the centre.
   - Left column: **spawn/create/duplicate** (default, or from saved templates), **save current as template**, **multiselect tools**.
   - Sliders: **height** (vertical) and **width** (horizontal) adjust size between allowed min and max values. A curved arrow handle **rotates** it.
   - Right column: **shape menu**, **material menu**, **colour tint (RGB)**.
   - The current shape is dropped into the level when duplicate is pressed or another shape is dragged in.
   - A hatched **delete zone** appears at the side when a shape is being dragged.
3. **Art zone**: the canvas, with the optional framing ground at the bottom.

## Submenus (SS6)

Each opens as a panel, left or right of the editor.

- **Shape menu** with categories Basic, Advanced, Special, Unique Entities. Each category has a dice icon and a checkbox to include or exclude it from randomization. Bottom: **Randomize** (places a random shape with random x/y scale at the top of the screen) and **OK**.
- **Material menu** with categories Common, Rare, Exotic, Special (each a grid of texture swatches), the same randomization checkboxes, a **Random** button and **OK/Cancel**. The top row has view toggles *(interpretation: grid vs list view)*.
- **Colour tint**: a Random button, a saturation/brightness square with a colour (hue) slider, and new vs old colour swatches.
- **Spawn, templates, multiselect**: drawn as **empty panels**, never filled in.
- Two type layouts are sketched on SS4: Type A (icons in a scrolling list with category headers, the panel docking beside the three right-column buttons) and Type B (a plain list with a close button).

## Multiselect tools (SS4, text notes)

Box selection (with a toggle for inverse selection), select similar, shift/ctrl handpick, select all, select none/cancel. The text notes add "deselect random" with a 0–100% chance slider.

## Background editing mode (SS5)

The system menu switches between **BG mode** and **active mode (foreground)**. In BG mode the whole canvas behind is editable and the shape editor toolbox slides up and down (an animated wheel turns as the panel slides).

- Preview mode hides the shape editor and selections.
- Background shapes get an automatic desaturation overlay plus settings/shader, so they read as background.
- A narrower colour palette for the background.
- One directional ambient light, rotatable.
- Up to 4 freely placeable point lights: adjustable radius, colour, intensity, placed anywhere in the background individually. No shadows on mobile.

Background colour rules from the text notes: tint limited to roughly 50–200 RGB or narrower; two-colour gradients in vertical, horizontal or diagonal orientation. The summary doc adds patterns and solid colours, and lighting from bright day to dark night with moody colours.

## System menu (SS4)

- Change level settings: background, gravity, environment, weather, name, metadata, author, background colours, type, settings and texture, lighting setup. SS16 adds wind, temperature, hazards and events as level parameters.
- New / Open / Save / Save As. Publish.
- Guides, hints, tutorials, help.
- Set a framing word or phrase to draw to / associate the art with.
- Play/test level. Exit the editor (confirmation required). Special misc options.

## Blank-canvas help

- **Framing word** (SS4): to help with blank-canvas paralysis, the game can randomly provide a word, phrase or question that frames the art, giving direction and a concrete subject.
- **Weekly theme** (SS3): level gen can give a random theme every week to constrain artists and help them pick a subject.
- **Procgen** (SS16, summary doc): generates complete or partial random sculptures as starting points, or infinite nonsense levels for pure destruction. Works offline. Mixing procgen with user levels: in campaigns, as level-editing hybrids, and as a rotating temporary selection on the server (SS10).
- **Templates**: save shapes as templates and spawn from them (SS4).
- Text notes: tutorials for level makers, a "lite art tutorial", productivity/icebreaker boosters (SS10).
