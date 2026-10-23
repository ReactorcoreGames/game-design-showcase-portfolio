# Shape Smasher: design digest

This folder is the text form of Shape Smasher's design, transcribed from 16 scanned notebook pages (`C:\08 Projects\Project_ShapeSmasher\Scan_Shapesmasher\SS1–SS16.jpg`) plus three text docs. Read this instead of the scans. The process is in `workflow/scan-digest.md`.

## Summary

Shape Smasher is a 2D physics game for phones (vertical and horizontal) and PC, built around two halves: **make art, then smash it**. In a level editor, players build "sculptures" out of scalable geometric shapes in different materials, colours, backgrounds and lighting. Those sculptures become levels that other players (or the author) wreck with physics: flinging objects slingshot-style, dragging them around, and using a player-controlled wrecking shape that can change form, size, material and element. Before smashing, the player can choose to **spare** the art instead, and afterwards they rate it with one feeling-emoji. The author receives those reactions, so every level is also a message from an artist and every smash is a form of critique.

The motto from the overview page: *Make art, then smash it! Make art for others and let them smash it for you! Break art made by others! Share art to be broken by others!*

Stated player needs (SS1): stress relief, power, self-expression, socialization, sharing, receiving, anger venting, communication.

Inspiration (from the summary doc): an Angry Birds / Crush the Castle style game without scarce-resource puzzles, retention systems or intrusive monetization, a pocket stress toy for spontaneous carnage. The level editor came first out of necessity, and the "levels are art, smashing is critique" framing grew from the problem of motivating people to make levels.

## Two versions of the design

The notes contain two directions, and a page should know which it shows:

1. **The original social-art platform** (scans, `Shape Smasher.txt`): online server, accounts, level browser, spare/smash choice, emoji feedback to authors, remixing, campaigns of user levels, ad circus and season-pass business model, ideas for artists earning from their levels.
2. **"Shapesmasher Simplified"** (a later text note): drop the accounts, in-app social features and level selling. Share levels mod.io style (like Streets of Rogue chunk packs, a touch of Mario Maker). Make it more of a game: levels contain randomly placed characters to eliminate, Angry Birds style, and the player chooses how much of the sculpture to respect (a needle for just the bad guy, or a sledgehammer for everything, no penalty either way). An automatic low-res screenshot of the final kill shot is uploaded to a simple image server, browsable per author. Alternative framings floated: a top-down drone view over compounds where combatants write messages on the ground and the operator chooses mercy (capture, Fulton balloons) or bombing; or orcs occupying ruins; or a mix of rescue and destroy missions.

The scans describe version 1 throughout. Version 2 is text-only.

## Files

| File | Covers |
|---|---|
| [gameplay.md](gameplay.md) | The smashing side: the play screen, touch mechanics, the wrecking shape (PWSO), destroyable level objects (DLO), the spare/smash/rate sequence, game modes |
| [level-editor.md](level-editor.md) | The creating side: editor layout, shape/material/colour menus, multiselect, background mode and lighting, level settings, procgen and blank-canvas helpers |
| [structure.md](structure.md) | Everything around it: metagame and campaigns, player log, feedback emojis, server and storage, ad circus and business model, controls ergonomics, credits page, menu flow, open to-dos |
| `Shape Smasher.txt` | Reactorcore's original condensed summary doc (the long pitch text), kept as is |

## Glossary

- **Art / sculpture / level**: the same thing. A level is a sculpture someone built in the editor.
- **DLO (Destroyable Level Object)**: any shape placed in a level by the artist or by procgen. Breakable, spawns debris and effects, can be picked up and thrown.
- **PWSO (Player Wrecking Shape Object)**: the player's own indestructible wrecking shape. Only one exists at a time.
- **Spare / Smash**: the choice a player makes when a level opens. Spare is respect/endorsement, Smash proceeds to destruction.
- **Bad**: "blam it", a dismissal/report button that deletes and blocks a level for that player.
- **Remix**: open a clone of the level in the editor and make edits.
- **Framing word**: a word, phrase or question that names what a piece of art is about. Can be random, to beat blank-canvas paralysis.
- **Framing ground / framing terrain**: optional indestructible ground (and wall) pieces that frame the art zone.
- **Ad circus**: an optional, out-of-the-way section of ads that players can choose to watch to support the game.
- **Minidudes**: small ragdoll characters ("interactive buddy like") that players can sprinkle into a level for extra gore.

## Source table

| Scan | Title | Content | Goes into |
|---|---|---|---|
| SS1 | Shape Smasher Overview | Player needs, phone vertical / PC+phone horizontal mockups, shape and material system, PWSO and DLO, mottos, business model | all three |
| SS2 | Touch mechanics | Slingshot-style grab and fling, ALT drag mode | gameplay |
| SS3 | Player Experience | Play screen, Spare/Smash screen, after-smash results screen, player log, campaigns, minidudes, weekly theme | gameplay, structure |
| SS4 | Level Editor | Editor layout, shape editor box, delete zone, shape/material/tint buttons, multiselect tools, system menu, framing word | level-editor |
| SS5 | Level editor background editing mode | BG mode, preview mode, lighting | level-editor |
| SS6 | Level editor submenus | Shape menu, material menu, colour tint menu drawn; spawn, templates and multiselect panels drawn as **empty boxes** | level-editor |
| SS7 | File System & Server Management | Player vs server storage | structure |
| SS8 | Browse Individual Levels from server/cloud | **Title only** | structure (open) |
| SS9 | Todo | Open tasks list | structure |
| SS10 | Level Editing Accessories / Sharing Server Publishing | Short list of topics, not developed | structure |
| SS11 | Level browser (Local, old/new) | **Title only** | structure (open) |
| SS12 | Player log / feeling rating | Title, plus the 3×3 feeling-emoji grid | structure |
| SS13 | Hand/thumb control ergonomics | Thumb zones and grips | structure |
| SS14 | Ad circus | Ad circus screen, rules, entry types | structure |
| SS15 | Credits page | Credits page principles | structure |
| SS16 | Feature Brainstorming | Feature list, DLO placement modes, framing terrain | level-editor, structure |

Not transcribed (outside the 16 scans): `Foto_ShapeSmasher/` (photos, five `ShapeSmasher1–5.jpg` pages that may duplicate scans, thumb-map PNGs, a Unity system flow chart) and the mind maps `Game3`/`Game4` (`.mind` + `.png`). They may add detail if a page needs more.

Notes marked *(interpretation)* are Claude's reading of an unclear drawing, not Reactorcore's words.
