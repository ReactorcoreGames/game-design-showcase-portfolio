# TopVerse: on foot

The human-scale layer: characters, how they're drawn, the room networks they explore, exits and escapes, destruction, fire and the shared inventory. Sources: scans TN1, TN3–TN5, TN8, TN9, TN18, TN20–TN23, B4, B5, B8; `1 TopverseNotesBU2_Cleaned.txt`; `5 Topverse system layers n mechanics.txt`; the Syndemic report (see [origin.md](origin.md)). Scan codes are explained in [index.md](index.md).

## The on-foot zone

An on-foot zone is a randomised subsection of an area tile (Notes, spheres of influence): it is shaped by every sphere above it (climate, materials, structures of the tile), so its layout is random each time but always makes sense for where it is. Size: max 100 m (layers txt), "10–100 m" on B4's zoom chain; the Notes give "max 100 m², divided into 4 cells if DRC parking area". Minor vehicles can operate there too. Two forms (Notes, "2 modes for each map tile location"):

- **A) a randomised instance**: either a DRC parking area/arena or a usual room network of any size and length, within limits. It is deleted when you leave and regenerated if you come back.
- **B) a DRC/MDRC staging/parking area** for managing and operating your buildings and vehicles, and **C)** a permanent parking room with the player's own decorated DRC plots, allowed only in limited numbers per region and universe (see [metagame.md](metagame.md)).

Up to 2–4 (M)DRCs fit in one on-foot room (B4: "MAX (M)DRC per room = 2–4"; layers txt "up to 4"; B2 places them one per corner quadrant). The max DRC entrance size equals the max room cell size, and the max interior size equals the max entrance size (B4).

## Room networks

The Syndemic room network, generalised (TN22, Notes, hijack). TN22 defines the on-foot exploration network for DRC/MDRC fleets and areas:

- Room types: **E** entry (several), **C** corridor, **L** location (several), **T** layer transit room ("stairs" between layers). E, L and T rooms have 8 door outlets (the 3x3 anchor grid's edge positions).
- Random connectivity; multiple paths possible and likely; a few empty spots.
- Air, underground (soil) and underwater (sea) are present too. Usually an empty surface plot or room lets you enter another layer, or a stairs-like transit room does. Air is reachable only by flight, a scaffold dock (cities only) or a cliff.
- Theming depends on the tile (city, forest, plains, mountain...) and on whether the area is planned or unplanned, official or unofficial (catwalks or wild trails).

The hijack notes add the human-scale version of Syndemic's rules: border walls stay (as hills and rock piles outdoors, "a necessary evil"); highways become real infrastructure (roads, rails, canals, sewers); doors are set into walls with a trigger area: press E, the door opens, controls lock, you move straight through, fade to black, and arrive in the next room with rotation kept and momentum reset. Doors can be locked, barricaded or blown open; projectiles never pass through a door into the next room. Syndemic's 3x3 spawn anchors still work: terrain islands as water or rock, corner emplacements (pillboxes, infrastructure), wall fixtures (lamps, cameras, posters), and green/yellow/red zones for spawns.

## Room exits (TN20)

Standard on-foot exits, in every direction (a room's 8 edge positions plus the walls):

- **Wall/bound exit**, full or partial. A *partial wall exit* is an opening in a thick boundary wall: characters and projectiles both collide with the wall except at the opening. A *full wall exit* is a thinner boundary that projectiles pass through but characters can only cross at the exit.
- Boundary walls can have material properties and be destructible; doors are optional; locks too.
- The boundary wall's look reflects the environment of the cell it leads to (a rocky face toward a cave, a tent toward a camp).
- **Underpassage**: an exit inside the room, shown with a clear slope or stairs in its direction of travel. **Holes** differ by being black pits with no visible bottom.

## Emergency escape (TN21, TN23)

In any room at any time, a character with the right special item can get out of the room network and back to tile travel on the region map. Escape items, each for a layer (TN21):

- **Wall buster** (surface): a charge creates a new exit door in a wall (a collider zone and a hole sprite on top of the wall).
- **Drill digger machine** (underground): aim at a wall, drill, go through; it leaves a hole behind (TN23 notes "multiplayer").
- **Ballast dinghy** (underwater).
- **Fulton blimp/balloon** (surface, or a jetpack): not instant. You rise in altitude through all layers (underground, surface, sky) until a threshold and are still shootable on the way ("balance delay"); full exit at the top of the sky.
- **Excavator bore** (surface, downward).
- **LEO shuttle / deep sea riser bell / bedrock gnawer / deep core penetrator** (covering orbit down to bedrock and below).
- **Orbital escape pod / evacuation rocket** (space).

## The universal cross-character inventory (TN21)

A shared backpack, "like in Pokemon or dungeon games", for items with meta-level functions regardless of the current role (but dependent on the environment): the escape items above, health and status fixes and boosts, portable role **resupply packs** and **switch kits**, and special artifacts, weapons, devices and tools. Not usable by Pokemon/kaiju, minor vehicles or major vehicles/MDRCs. (Each subgame role has its own 10 slots; this inventory sits beside them.)

## Vehicle and MDRC personnel (TN18)

The crew role's kit, inspired by the Knights of Sidonia personnel outfit, in tiers (cheap and weak to expensive and good): survival kit with signal flare, comms and phone; HEV-style protective suit; emergency gun, blade and bazooka; thruster/jetpack/grappling hook/skates/fins/ballast; a life support system (oxygen, temperature, pressure, sustenance, health), a burden compared to a dedicated combat role; shield/barrier bubble for extreme hazards; temporary housing, water, rations, first aid; flashlight, speaker, binoculars, shovel, pick, hammer; scanner, survey equipment, analyser, 3D printer; climbing spikes, magnets, adhesive, forge; a Fulton balloon; wallet, ID, keys and cards.

## Layers seen from on foot (B5)

- Main combat happens in the sky/surface/soil group of layers. A character can go airborne, or burrow or drop through a hole to go underground. Leaving that first group means going out of range.
- Only the layers a character or vehicle can reach are loaded.
- Usually a minor vehicle, device, suit or tool is needed to move to another layer, or a natural route (sinking in the ocean, a hole).
- Entities on other layers are drawn as **ghosts**: options listed are shrunken (below), desaturated silhouette (above), dark or light depending on underground/night or sky/day, a HUD chevron ˅/˄ for below/above, transparent (above me), or invisible and only visible at holes or over transparent floors.
- **Vertical targeting** is pinpoint-based: firing up or down is a special action aimed at a cell.

B5 groups the layers with letter codes: A/S/G (air, surface, ground: the main group), O/UA (orbit, upper atmosphere), B/C/M/S/CORE (bedrock, crust, mantle, shell, core). *(interpretation of the letters)*

## Characters: how a human is drawn

Two rounds of thought.

**TN5, the face-up idea.** In top-down view, the head turns up toward the camera so eyes, nose, mouth and hair are visible while the body faces its direction as usual. Pros: unique, memorable, relatable and emotional, still directional, one rotatable sprite, "looks stupid (meme-worthy)". Cons: "looks stupid". Alternative: head-only characters. Applies to animals and beasts too.

**B8, the later TopVerse human.** Alternatives drawn: a "slug" human, a head-only human with a portrait, a shoulder human, and a "Kenney" human (in the style of Kenney's top-down asset packs) with a hat or hair sprite pasted on top. Requirements: one rotatable sprite with no animation frames or bones; a single piece, no ragdoll or modular parts; customised through tint, shader, pattern overlay, colour and a hat/hair sprite. The **TopVerse human** is three single sprites: the **body** (large enough to hide legs; with the head behind it as a weak spot, in front of it as a weak spot, or face-up showing eyes, mouth and brows), Rayman-style floating **hands** visible only when nothing is held, and the **held item** (gun, tool, object), which rotates freely within an allowed angle, isn't part of the body and hides the hands. Body and face are customisable.

**B8, checking faces.** Instead of customising a top-down face, each character has a single-frame **portrait**. Hovering the mouse over a character shows a HUD panel with name, type, stats, health and the portrait; a "makeover" changes the face by swapping the portrait. Emotions are overlays on the portrait: googly eyes, new brows, a new mouth, and symbols (sweat drop, anger marks, !, ?, bubbles, heat lines). Pros: cheaper, versatile, "not stupid", emotable. Cons: the face isn't on the character, you have to check it, and characters look less unique in play.

*(How the digest reads it: B8 is later and keeps the face-up head as one of three head options, while moving faces and emotion to the portrait.)*

**Scale (TN8).** The grid cell is 64 px; a regular human is 32 px (half a cell); a giant human 64 px (a full cell); larger cells come at 2x (128 px) and 3x (192 px). B3's monster sprite sizes are S 14, M 30, L 62 px.

## Destruction and buildings on foot

**TN3, building collapse.** Walls and supports are destructible. Floors and stairs collapse when no walls or supports hold them and the floor's strength is less than the weight on it; supports in higher floors collapse when the lower ones go; a hole in the ceiling gives access to the floor above if the character can jump, fly or deploy a ladder. Stairs are pass-through and used with E. "World is layered like X-COM, and grid based." Already boxed on the page: "WARN! Not for Unigen mega game. 1 floor interiors."

**B4, rejected for good.** "Build/Struct Collapse Advanced" works out multi-floor buildings (max 3–9 floors) collapsing floor by floor into rubble or crash-compacting, then ends: "Forget this, not viable for Unigen. Use (M)DRC: 1 entrance → 1 floor plan only." So every building and vehicle interior in TopVerse is a single floor.

**TN9, support pillars.** Each grid cell has nine support slots: four corners, four wall midpoints, one centre. Each slot can hold a pillar of a different shape (round post, L-corner, bars, blocks, wedges, crosses), size (1/1, 1/2, 1/4), material and thickness; dashed bars suggest weaker or partial supports. *(interpretation)*

## Fire spreading (TN4)

A **global fire manager** ("FireMan"): an initial source ignites nearby flammable objects through secondary flames; the original source fades and the burning objects become new sources. Two models were compared: **X**, where every new source is a full one and fire repeats until everything has burned down to an unburnable state, and **Y**, where each generation is less likely to ignite more, so fires limit themselves. Rules: each source is minimal in audio-visual cost; spread and burning are slow; particles, effects and sound come from the global manager, not each source; spread, speed and burn time depend on the burning object; after a number of sources, nearby fires merge. This system serves the Fire Fighters subgame and every other game (hijack: "extendable to other games").

## Proposals

Claude's suggestions, not Reactorcore's design.

- **Proposal, fire model.** Use Y (self-limiting) as the default everywhere and X only where a calamity is active (the Fire Fighters subgame or a triggered disaster), which fits the equilibrium universe: fires don't consume the world unless someone provokes it.
- **Proposal, ghost rendering.** Pick one rule from B5's options: entities below you are shrunken and darkened, entities above are a desaturated silhouette, and anything on a non-adjacent layer appears only as a HUD chevron at the screen edge. That keeps one look per relation and needs no extra sprites.
- **Proposal, what a "room network" is per tile.** A room network is 6–20 rooms (the Syndemic size) for a natural tile and up to about 30 in a city tile, always starting from an entry room at the side the player arrived from, with one T room per accessible layer.
