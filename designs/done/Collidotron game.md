# Collidotron
(loosely inspired by the brick breaker game genre)

## Core Game
Start a chain reaction; spark one tile into a ball with a fixed velocity, as it bounces against other tiles, they will break and release ball too, creating a cascading chain-reaction that will eventually result in all tiles being turned into balls. When last tile is broken, all balls are flushed downwards. Sort of a relaxing zen experience of watching balls multiply and tiles break. Player can use mouse once to initiate one tile to break and send the ball flying at a random angle at constant speed, then later they can press mouse button which will slow down time to 0.1x timescale, they can hover over any ball on the scene so far, click on it to select it, then click in a direction in relation to it to sent to flying at the standard constant speed. Clicking again anywhere else will cancel slomo and ball selection mode. Playable with mouse only using only mouse 1 button. Mouse 2 will toggle timescale to 1.5x - cancelling/overriding/pausing any mouse 1 stuff until turned off.

Top down view inside of a clean-looking precision machine with a faint 32x19 grid, with a titanium white frame border around it. Either with a center origin offset or randomly anywhere else, there is randomly generated collection of square tiles in a kaleidoscope or fractal pattern, including pockets of empty spaces in random frequency between 1-50% of all tiles on screen. The colors of the tiles usually have 2-4 randomly chosen colors, with an animated gradient background (either linear, rectangular, curved or spherical) also with 1-3 randomly chosen desaturated colors compared to the tiles which are generally more vibrant with color, have a beveled edge with very dark 2px outline around each tile, so they visually pop out more in the scene. Absolutely minimal UI/HUD, simple stylized look.


## Lore and Context
By the 23rd century, centuries of human waste and recycling had filled landfills beyond capacity. Instead of burying or burning, scientists pioneered a new innovative solution: they seeded landfills with **synthetic microbial and chemical catalysts**. These agents bonded with plastics, metals, and organics, accelerating geological processes until the entire mass **lithified** — transformed into hardened crystalline blocks of hybrid matter.

The resulting material, nicknamed **strata-mass**, is mined not in chunks of ore but in **loaves**: solid blocks cut directly from lithified landfill. Each loaf is then further sliced into **slabs** and loaded into the **Collidotron**.

Inside the processor, the operator initiates a reaction with a single precision pulse. One tile fractures, releasing a reaction orb. The orb ricochets through the crystalline lattice, shattering other tiles in a chain reaction cascade. The reaction continues until the slab is fully collapsed.

The liberated fragments are then flushed into sorting conduits, where advanced phase-separation extracts them into standardized **material pebbles**. These pebbles feed **universal assemblers** — next-generation 3D printers that can fabricate anything from utensils to circuit boards to industrial components.

What was once soft smelly landfill waste has become a new shiny mine for plethora of useful materials. Both the environment gets cleaned up and the materials are recovered and reused.

This framing keeps the game's lore believable despite not being based on hard science:
* The cascade = controlled disassembly process.
* The slabs = cut or grown materials in tablet form.
* The gallery = logbook of processed materials (with incidental fractal/kaleidoscope aesthetics).

### About the Collidotron
The **Collidotron** is a next-generation **material disassembly reactor**, built to break down sliced slabs from lithified blocks of landfill mass into usable energy and trace elements.

Once one tile ruptures, it releases the energized pebble version of that element, travelling at a constant speed maintained by the machine and bounces off against other tiles, releasing them into pebbles too. This sets off a chain reaction of controlled collisions, breaking down the entire field piece by piece.

The technician (the player) only intervenes at crucial moments:
* **Initiate** the reaction by sparking/cracking the first tile.
* **Intervene** in slow time, nudging a selected pebble into a more efficient trajectory to ensure faster full lattice collapse.

The rest is simply watching physics running its course as a mesmerizing cascade. Once all tiles are broken, the stored energy is siphoned into batteries, the pebbles are flushed downwards and autosorted by material type, for later use civilian, industrial, laboratory or military use with appropriate material printer stations.

---

Each slab is locked into a containment frame, its structure resembling crystalline or dendritic growth patterns. Once inside, the machine requires only one action: the operator fires a controlled pulse at a chosen tile. That single fracture releases a reaction orb — a micro-shard of stored kinetic energy — which ricochets through the lattice, rupturing other tiles in a cascading chain reaction.

The process is largely self-sustaining, but technicians can briefly intervene by slowing time and redirecting one of the reaction orbs to improve efficiency. This step is not mandatory — it’s simply a convenience to guide stubborn slabs to full collapse.

When the last capsule breaks, the slab’s contents are flushed into **sorting conduits** beneath the frame. There, metals, ceramics, polymers, and silicates are automatically separated into reservoirs for downstream use in **object assemblers** — compact 3D fabricators that provide tools, supplies, and everyday items.

---

## Metagame Structure

### Low Metagame A (Campaign Flow)
- **Loaves as Campaigns:** Each campaign represents one **loaf of lithified landfill**. A loaf is sliced into **9 slabs** (mix of 16×9, 24×13, and 32×18 grids), processed one by one in the Collidotron.
- **Campaign Variants:** Loaves may have subtle quirks based on their origin (urban landfill, industrial slag, electronic scrap, biowaste strata). These appear as 2–3 quirks per campaign:
  - *Ball trails:* line trails, micro-explosions trails.
  - *Slab generation quirks:* porous voids, dense crystalline clusters, reinforced ridges.
  - *Visual quirks:* fracture glow colors, altered flush animations.
  - *Volatile Compounds*: Some tiles explode in larger radius.
  - *Heavy Elements*: Balls move slower but break through multiple tiles.
  - *Quantum Instability*: Tiles occasionally phase in/out of existence.
  - *Magnetic Fields*: Curved ball trajectories.
- **Completion Ritual:** Finishing all 9 slabs assembles the loaf into a **3×3 gallery collage**, permanently archived.

Stage sizes (small, medium, large)
- 16 * 9 = 144 tiles
- 24 * 13 = 312 tiles
- 32 * 18 = 576 tiles

(Frame borders adjust based on slab/canvas size)

### Low Metagame B (Campaign Flow)

- **Campaigns as Material Batches:** Each campaign represents processing one **source rock or synthetic batch**, sliced into a series of 9 slabs.

  - The slabs vary in size: smaller 16×9, medium 24×13, and full 32×18 arrangements.
  - They are presented as a sequence of 9 processing chambers, ending in a complete **3×3 collage** of the source.
- **Campaign Quirks:** Each batch carries 2–3 unique quirks that alter the feel of its breakdown, for example:

  - **Ball behavior:** glowing trails, minor speed variance, delayed bounces.
  - **Tile properties:** reinforced edges, fragile porous gaps, shattering animations.
  - **Visuals only:** alternate fracture sparks, different flush animations.
    These quirks ensure that every campaign feels distinct while staying true to the base mechanics.
- **Completion Ritual:** Once all 9 slabs are processed, the entire 3×3 collage is archived as a finished record of that source batch.

### High Metagame A (Persistent Layer)
- **Archive of Loaves:** Every finished campaign is saved as a **gallery entry**, recording:
  - The loaf’s procedurally generated name.
  - The 3×3 collage of its slabs.
  - Processing stats (reaction duration, total collisions, efficiency, quirks).
- **Replay & Re-extract:** Players can replay the cascade of any slab exactly as it unfolded, thanks to seed saving.
- **Experimental Loaves:** As the archive grows, the system introduces anomalous strata-masses with stranger lattice behaviors (exotic symmetry, unstable reactions, anomalous flush effects).
- **Living Catalog:** Over time, the archive becomes a **logbook of reclaimed matter**, half industrial record and half accidental art collection.

### High Metagame B (Persistent Layer)

- **Gallery of Processed Slabs:** Every completed slab is saved as a **pixelmap + seed**, so it can be replayed exactly as it appeared.
  * The gallery arranges slabs both individually and as completed 3×3 collages, turning raw industrial data into a visual log of material processing.
  * Each record includes its seed ID, processing stats (reaction duration, total collisions, efficiency), and the quirks that defined its behavior.
- **Replay & Study:** Players can revisit any saved slab to replay them again but with a different starting point.
- **Anomalous Slabs:** Rarely, the system may generate anomalous or synthetic patterns — test batches that carry more unusual quirks (e.g. unusually porous layouts, extreme symmetry, or unpredictable cascade speeds).
- **Ever-Growing Archive:** Over time, the gallery becomes a personal catalog of unique slabs — both practical records of processed matter and coincidental kaleidoscopes of industrial beauty.

(Note: merge info from A and B in both low and high metagames)

## Extracted Materials - Pebbles/Balls/Tiles
Here’s a possible list of universal materials, inspired by Astroneer-style simplicity, mixing real and semi-fictional names:

Compound
Resin
Organic
Graphite
Ammonia
Acid
Ceramic
Carbon
Quartz
Silicon
Copper
Aluminum
Iron
Gold
Titanium
Lithium
Zinc
Tungsten
Plastic
Alloy
Steel
Glass
Hydrogen
Methane
Nitrogen
Sulfur
Helium
Argon

Each slab has 2-4 randomly chosen colors for its tiles and thus that means 2-4 randomly assigned materials per each color.
Each material may influence how the tile behaves and what kind of ball it releases. For example a steel tile may require more hits (6) to break if its being collided with a compound originated ball, but a steel ball would be able to break another steel tile in fewer hits (2), while a steelball would also not bounce away after breaking a compound tile but keep going, plowing through tiles until it encounters one that requires more than one hit to break, in which case it would bounce off after damaging that tile.

I haven't yet assigned the exact mechanics per each tile / ball, but generally they alter behavior of tile or ball in some way, offering benefits and drawbacks.

Game can first be built with just one generic material type, then expanded/updated with new materials can be added to the mix, making the game richer and more varied.

Machine frame skins can also be supplied as new content, as well as shader filters.

## Performance
The game should use technology that would allow up to 600 balls to exist simultaneously that all have basic arcade physics. Note: the balls do not collide with each other, balls only collide with tiles, so atleast thats one less strain on performance.

Besides the balls and tiles, the game should also handle basic effects like simplified trails, tile breaking animation effects (either as sprite animations or as particle emitter bursts, handling about 1000 particles maximum at any given time.)