# Standalone: art direction, effects, assets and production plans

How Standalone was meant to look and sound, the asset standards Reactorcore set (and partly built), and the 2011–2012 production and business plans. Sources: A1–A18, M2–M4, E5, the AoY design document v3, the AoY content lists, the construction plan, master plan, action component plan, construction todo, S5, S17, S53, the demo renders.

## Look

The direction stayed the same from V0 to V2: **low-poly 3D, small pixel textures, believable physics, over-the-top effects**.

- V0 (E5): "Low-poly 3D, pixel textured, lowres. Realistic/believable feel." Barren worlds. "Lots of explosions! Big explosions!!" Heavy armour, high speed, high power; movement physics and momentum matter.
- V1: "somewhat believable and semi-realistic in terms of object interaction and physics", semi-cartoony textures, over-the-top effects; simplified, maybe abstract art because one person makes it.
- V2 (design doc v3): "very simple, low-detail 3d models and pixel art textures on either 128 or 256"; a smoother interface "that of a green, jet fighter display in a serious mindset"; effects in the stylised manner of manga and anime rather than realistic particles; sound "realistic, but beefy and satisfying".
- The 2013 demo models follow this: blocky grey-white mecha and carrier with red accents and hazard stripes, green-and-black enemy ships, simple flat-coloured planet grounds.

### Ultra Simple Graphics Style (A1–A2, A7)

A deliberately minimal look ("Check Proteus" in the corner):

- An **untextured white rectangle** whose colour tint, opacity, scale and rotation carry its meaning and animation. Fire as a stack of billboards fading from big, solid black/grey to small, transparent yellow/orange/red.
- **Scaled 2-sided planes**: rectangles for projectiles, beams, barriers, mechanical gibs; triangles for blades, boosters, muzzle flashes, organic gibs.
- **Basic primitives** for larger effects, explosions, large projectiles and big gibs.
- Extensions: single-colour "anime explosion" animations with no gradients (++), then simple gradients for flashes, glows, shockwaves, waves and advanced beams (++2), then both combined (++3).
- **Models**: Stage 1 is ultra-simple geometry, flat colours, one colour per polygon, no detail or bevel; modular mechs, fused organics. Stage 2 adds hand-made low-size pixel textures, 32–128 px, crisp; polycount under 1000, ideally 100–500.
- **Microart scenery** (A3): a sheet of about a hundred tiny faceted scenery pieces: crystals, spikes, mesas, domes, an animated tornado, monoliths, trees, cacti, boulders, mountains.
- A **pixel-art scenery pack** (A6): plants, rocks, foliage, vines, formations, pillars; several themed packages.

### Effects (A10–A15, generic effects list)

- **Star Fox 64 destruction effects** (A12): dual shockwave rings; flash red on hit, turn red when killed; animated fire-smoke and explosion particles; 2-sided plane gibs (squares for mechanical, rounded for organic, with scale variants); a **space mega blast** (expanding sphere with a flat ring shockwave, breaking up and fading); lightning that moves like a worm, tail following head; an expanding, fading sphere with a scrolling fire texture.
- **Great Fox booster** effect (A10), an expanding crown **water splash** for explosions on water (A11).
- **Effect textures** (A13–A14, mostly ticked as made): greyscale 50% transparent textures for clouds, gas, mist, haze, rain, snow, energy, plasma, lightning, water, sparks, jet boost, projectiles, bush, grass, impact marks, blood splats, signal flashes; micro rocks, dust, micro-organisms, space debris, radiation. Substances (gas, grains, liquids, dusts, solids, haze, mist, fog, radioactive glow, waves, bubbles) and energies (heat distortion, electricity/EMP, plasma, GN-drive-style energy particles, void/dark matter, energy projectiles, lightning, fire, gravitons, beams).
- **Texture guidelines** (A15): alpha-transparent backgrounds; seamless static screen-effect textures; no clipping seams on particles; 64×64 particle textures with very soft edges, 128×128 seamless tiling textures; mostly greyscale and value-based; generic style; animated sequences numbered 001, 002, 003.
- The generic effects package list (2011): explosions in four sizes (+ shockwaves, added by hand), fire, smoke, sparks, explosion trails, liquid splashes (water, lava, acid) and their sounds.

### Tools and standards (A5, A16, M4)

- **Naming convention**: `type_GenericDetailVariant`, e.g. `tex_RockLarge1`, `mesh_GrassBlue5`.
- **Basic Primitives Mega Pack** (A16), marked COMPLETE: planes, cubes, pyramids, crosses, cloud planes, spheres (low/mid/ico, half, quarter), cones, ramps, slopes, flat pyramids, cylinders, flat cones, rings, donuts, a large two-sided hollow sphere, half and quarter rings, diamonds, polyhedra, barrels, gems. OBJ format, no animation, no separate UV files.
- Planned mesh tools (M4): **Mesh Colorer** (character customisation), **Mesh Exploder** (the overkill effect), **Mesh Baker**.
- First asset list (A5 sticky note): ReWaR (humanoid), mothership, rifle (simple/advanced), shield, tree/rock pillar, basic enemy, EM missile, gun turret, bomblet/fusion bomb.

The scan folders were named "i already built this" and "i already built this too" for A13–A16: the textures and the primitive pack were actually made.

## Sound and music

No music in the game (intro spec, 2012-01): sounds and ambient soundtracks only, and the player is encouraged to play their own music or radio. V3 keeps the idea and leans on it: the game should feel like playing Beat Saber, Audiosurf or Beat Hazard to "any kickass music", a flow state, without being a music game.

## Production plans (2011–2012)

From the RTF plans (now `AoY production and marketing plans (2011-08 to 2012-01).md` in the project folder) and S5, S17, S53.

- **Components**: an *action component* (entity system with damage and material systems; world system with space and planetary templates and environment content; player character: carrier, robot, drones; enemy factions starting with RS; control schemes; UI), a *meta component* (quick game, campaign, persistent world and character, metagame interface) and a *menu component* (main menu, profiles, game type selection, options, Database).
- **Engine**: Unity3D or UDK considered; Unity chosen.
- **Build order** (master plan): placeholder menu → barebones action component → quick game → Database → metagame and profiles → first content set → intro → full player character → tutorial → content sets, repeated. Menus first, all screens drafted with unfinished parts greyed out; entity and world templates before content; grey test content to find scale and feel; mothership first, then the ReWaR fitted to it. "Code with modularity in mind!"
- **Prototype 1** (S17): a playable but barebones release with only the mothership, setting up the world and entity systems.
- **The demo** (S5, built 2013): a one-way click-through of every screen, to be uploaded as a web player.

## Business plan (master plan, 2012-01)

- Free alpha/beta at the first playable step, with **discounted pre-orders**; a trial or demo with a purchasable key once there's content; free updates until the content sets begin; then **expansion packs/DLC** of any size, and later a complete edition. "A core game being released as a platform." Episodic releases (S17).
- A simple website with a news blog and comments; "not every comment and email may be replied to, but all of them will be read"; pitch to local gaming sites.
- Audience 10–35. Strong points listed: infinite replayability, persistent world and meaningful customisable character, satisfying fast and dangerous combat, metagame planning that matters.
