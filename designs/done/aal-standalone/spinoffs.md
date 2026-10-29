# Standalone: spinoffs and offshoots

Separate games and tools that branched off Standalone. None is part of the main design. Sources: X1–X6 (a later grey-grid notebook, undated), R1.

## Standalone 2D editions (X1)

A side-view 2D version.

- A vertically **looping, layer-based** game space.
- **Horizontal chunks** of about 1 km divide areas (for performance, biomes, scenery population). Each chunk has a population percentage that sets how much scenery it gets.
- **Circular space maps**: position by distance from the centre plus angle, divided into distance sectors and angle chunks around a core area.
- Scenery placement is procedural each time a sector loads; organic scenery may grow its population toward the maximum over time.
- **Omnidirectional far-vision** through the background (marked experimental): background layers at increasing distances (0 m, 10 m, 100 m, 1 km, 10 km) around a "Horizon Core".
- Characters as skeletal ragdolls, or sprites made from ragdoll snapshots (probably the latter, for performance).

V3 notes that the whole design could be made in 2D as well as 3D.

## Cyberspace Alternative (X2–X4)

"AoY – Cyberspace Alternative (Gungeon / [Isaac?] RogueLite)".

- Start with a barebones ReWaR; fight groups, areas, rooms and objectives that reward upgrades, consumables and add-ons. All content highly synergistic.
- A finite start-to-finish run, random in every possible aspect, getting stronger as you go. Linear: easy start, rising difficulty, a grand challenge finale. Variable objectives and length. Sketched as a strip of stages START, 1–6, END, and as a branching node path.
- "Cyberspace because it's contrived/arbitrary/artificial/magical": the setting excuses the gamey structure.
- **Randomisable**: starting equipment and stats; campaign length; enemy types, numbers, equipment, AI, appearance; which consumables and upgrades appear or are excluded; campaign structure and map layout; locations (planets, space, arenas, buildings, rooms); anomaly events; location events (weather, gravity, elements); locational content; enemy grouping (individuals, squads, armies, waves) and composition (one faction, many, mixed); upgrade frequency (minimum to 3×); upgrade acquisition (loot, scanning live enemies, finding, Doom-style auto-upgrade per kill; "ReWaR experimental types"); healing (auto-repair, medkits, Isaac-style consumables, level clear, none).
- **Reverse upgrade mode**: start as a random overpowered character and discard upgrades to continue.
- Advanced settings: dropdowns per setting (Force ON / Remove OFF / Include in randomization), custom randomisation presets, save/load.
- Campaign shapes (X4): **Wormhole chase assault** (a tube of areas ending at a boss), **Drop Tunnel Assault** (a vertical drop through platforms to a core), and a "R[?]force Campaign" descending stage by stage from orbit to a planet's surface.

## Standalone 2 (X6)

A modular mech whose systems sit on its limbs. Arms: manipulator, emitter, main gun, passive shields. Legs: propulsion, auto 360° turret, dashing system, passive shields. (Part of the page is blurred.) Compare the 2024 Jager-gun modularity in [the-unit.md](the-unit.md).

## User Creative Tools (X5)

- **Camera actor**: a controllable, indestructible unit in cheat mode that can control time, spawn and kill anything, teleport to any unit or place, switch to night-vision, thermal and 360° views; a control switch between your units and the camera.
- **Screenshot mode**: hide the HUD and adjust visual settings.
- **Record**: save action data and input to replay a sequence.

Related: the 2013 skirmish mockup's developer menu (cheats/modding aid) and "disable mods", and the moddability promised in every version.

## Double AI co-op (R1, V2)

Two players control one SA unit, one in the mothership and one in the ReWaR. Both AI cores live in both machines but only one is active in each at a time; they can **switch places at any time**, but only by mutual agreement. The sketched mothership carries the hull marking "SA-56", which fits the unique IDs for SA units on S4.
