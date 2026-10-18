# Showcase Page Brief

How to write one game design showcase page, either a new one from a standby design or a rewrite of a published one. This brief replaces the old numbered task docs (`workflow/legacy/`). It keeps every requirement they held, but it is written for a model that can be trusted with judgement rather than one that needed every step spelled out.

## What a page is for

Each page presents one of Reactorcore's game designs to whoever might land on it: a player, an employer, an investor, a fellow developer, a curious stranger. It is not a full GDD, and it does not list every number in the design. It is a competent, compelling overview that leaves the reader certain this game has been thought through properly, and that they now understand what playing it would be like and why it would be worth playing.

The tone is professional yet blunt, layperson-friendly but with real technical depth, colorful but faithful to the game's theme, and never vague or padded. It focuses on the player's experience: what the game promises to give them.

## Inputs, in priority order

1. **The project's design file(s)** in `designs/`, as listed in `designs/MANIFEST.md`. These are the authority. Where they are thin or silent, fill the gaps as Reactorcore would.
2. **The design bible**, `reference/bible/2a-bible.md` and `2b-bible.md`. This is how Reactorcore thinks: purpose-based design, games as satisfiers of fundamental human needs (NVC), infinite metagames, multiplicative content, low and high metagame layers, player-centric ethics. Read both parts before designing anything. The bible is why the old pages were "half-cooked". Sonnet 3 skimmed it, so the pages lost the reasoning that makes these designs distinctive. Every page must visibly carry that reasoning: what need the game meets, how its structure meets it, and why that structure is better than the genre default.
3. **Lore**, `reference/lore/`, only for projects set in the AAL universe (title prefixed "AAL", or the design says so). Use only what is relevant to this game. The game's own design overrides the lore wherever they conflict.
4. **Reactorcore's articles**, `reference/outreach/article-links.md`. These are titles only; the articles themselves are Google Docs. They show what Reactorcore cares about. Don't link them from project pages.

A design file can hold several games. The manifest says which part feeds which page. If you find a split the manifest doesn't cover, stop and ask.

## Titles and outside IP

- If the design names the game, use that name. If it doesn't, propose a title in the plan that fits the game's mood and feel. AAL-universe games get an `AAL` title.
- Some designs grow out of someone else's game, IP or trademark (BLAME!, UNO, LEGO, Smash Bros, Metroid…). Credit the inspiration openly on the page ("inspired by…"), but the title and every in-game name (characters, weapons, factions, card or brick names) must be original stand-ins. The design doc's own shorthand for borrowed things doesn't carry onto the page.
- Never target real-world groups, nationalities or identifiable people. Where a design's villains are drawn from real groups, turn them into fictional archetypes that keep the same dramatic function.

## Released games

A few projects already exist as shipped games (marked `released` in the manifest). Their page still presents the design: what the game is, why it's built the way it is, how it plays. On top of that it has a prominent link to play it, and it describes the game as released rather than as a concept. Use the game's real screenshots and promo art for the five image slots instead of generating images.

## Process

1. Read the inputs. Then write a short plan for the user: the title, the section list with what each section will argue, the palette and typography, the title animation, the diagrams, and one line for each of the five images. **Wait for approval before building.** Reactorcore reviews and tweaks plans at this stage, and it's far cheaper than reworking a finished page.
2. Build the page at `site/projects/<slug>.html`.
3. Write the image spec at `image-prompts/<slug>.json` (see `workflow/image-brief.md`) and run `python tools/images.py check <slug>`.
4. Add the project's entry to the nexus (`site/index.html`).
5. Update its status in `designs/MANIFEST.md`. For a new project, move the design file(s) from `designs/standby/` to `designs/done/`.

## Page structure

This is the default skeleton. Sections can be merged, renamed or reordered when a project calls for it, but each one exists for a reason, so drop one only when it truly doesn't apply.

1. **Project label.** Top-left, `position: absolute`, small and unobtrusive, with its own background so it reads against the hero: "Reactorcore's Personal Game Design Project", linking to `https://www.patreon.com/ReactorcoreGames`.
2. **Hero.** The title image (`_1_title`) fills the top area, and the title sits over it. Use the format `[Thematic Name]: [Three-Word Game Type]` (for example "Metal Gear Solid: Tactical Espionage Action"). The second part is a subtitle in a smaller size and a different color. If the design's own name doesn't fit this format, write one that does. The title must stay legible on any part of the image (see `workflow/cookbook.md`).
3. **Game Overview.** One to three short paragraphs: what this game is and what it offers.
4. **Target Audience · Game's Purpose · Core Concept.** Three cards, one row on desktop and stacked on mobile. Audience covers interests, UI/UX complexity and which needs they're hungry for. Purpose names the fundamental human need(s) the game fulfills. Core Concept states bluntly how it fulfills them.
5. **Story image** (`_5_story`), a zoomed-out view of the wider setting, with a quote overlay. Then **Lore & Story**: where the game takes place, why (tell the past without spoiling the future), and what the goal is right now.
6. **Controls & Interface.** Default controls as a list, or prose if a list doesn't fit. Also explain what or who the player controls and how it feels.
7. **Vignette image** (`_2_vignette`) with a quote overlay that captures what the gameplay feels like.
8. **Game Layers.** Four wide stacked cards:
   - **Moment-to-moment:** directly controlling a character, or issuing direct commands in a scenario.
   - **Low metagame:** the local campaign, gauntlet or arc that ties challenges together, end to end.
   - **High metagame:** the persistent layer above the campaigns. It can be an evolving overworld that low-metagame campaigns shape, or something as simple as a log of finished runs with replayable seeds. If the design is silent here, invent one that fits.
   - **Practical game flow:** an average session from launching the app to a satisfying exit point.
9. **Game Modes.** Title and purpose for each mode (short session or epic campaign, high or low intensity). If there is one mode, give it a longer description. Sequels and spin-offs are not modes; they get their own pages.
10. **Features & Mechanics.** 3, 6 or 9 wide stacked cards, scaled to the game's complexity. Write them as a technical document a layperson can follow, going deep on what makes this game unlike its genre. Put the **feature image** (`_3_feature`) and its quote with the single most important feature. Use diagrams (mermaid or styled HTML tables) where they explain better than prose, either between cards or as a section of their own.
11. **Trivia.** Optional, only if there's something genuinely fun to say.
12. **Box art send-off.** Two equal columns at every screen size: the 2:3 box art (`_4_boxart`) on the left, and a card on the right with the game's title and back-of-the-box copy that leaves the reader excited.
13. **Footer:**
    ```
    All my links: https://linktr.ee/reactorcore
    All my releases: https://reactorcore.itch.io/
    Reactorcore Games - <current year>
    ```

Leave out development timelines, technical specs, empty stats and anything boastful. These are concepts, not products, so nothing on the page may suggest the game exists or is in development.

## Images

Five per page, always at these paths (relative to the page):

| # | File | Ratio | Purpose |
|---|---|---|---|
| 1 | `../projects/images/<prefix>_1_title.jpg` | 16:9 | Hero mood-setter |
| 2 | `../projects/images/<prefix>_2_vignette.jpg` | 16:9 | What playing it feels like |
| 3 | `../projects/images/<prefix>_3_feature.jpg` | 16:9 | The key feature, shown literally or as a visual metaphor |
| 4 | `../projects/images/<prefix>_4_boxart.jpg` | 2:3 | Box art cover |
| 5 | `../projects/images/<prefix>_5_story.jpg` | 16:9 | Zoomed-out view of the setting |

For new projects `<prefix>` is the slug. Published pages keep their existing prefix (see the manifest). The nexus thumbnail is `../projects/thumbnails/<prefix>_2_vignette_thumb.jpg`, which `tools/images.py finish` generates.

Images go in with `width`/`height` attributes (1280×720, or 784×1176 for box art) and `loading="lazy"` on everything below the hero. That keeps the layout from jumping while they load. Every image scales with the viewport. Quotes on the vignette, feature and story images sit bottom-left, clearly separated from the image (cookbook recipes) without dimming the image itself.

## Visual design

- **Every page has its own identity.** Palette, typography, title effect and layout follow from the game's theme, so no two pages should look like siblings. Be brave and expressive.
- **Color tokens** go at the top of the CSS as a `:root` block, so the page can be recolored in one place.
- **Backgrounds** are never pure white or pure black. Aim for 10–90% brightness with a hint of hue, and 20–90% saturation for most elements.
- **No blue-orange.** Avoid it and other cliché complementary pairs. Mono-, dual- or tri-color schemes are all fine.
- **Cards and sections** get colored borders and/or shadows. Hover may change border or background color, but never position or size.
- **Layout:** no awkward card counts (3 + 1 orphan). Layer cards and feature cards stack vertically. Check the page at phone width: no horizontal scroll, and the two-column box art section must still hold.
- **Readable prose.** Break long text into short paragraphs with clear spacing between them, especially in technical sections. A uniform wall of text is the failure to avoid. Bold text always gets a color too. Use emoji sparingly and purposefully.
- **Title and H2 effects** are animated with `text-shadow` + `color` + `@keyframes` only. Options: glow pulse, color-shift glow, breathing glow, neon flicker, multi-color glow, directional glow, intensity wave, halo, electric buzz, ember glow, underline glow (`::before`/`::after` + `box-shadow`), or a combination. Pick one that suits the game and stays legible. **Never use `background-clip: text` or `-webkit-text-fill-color: transparent`.** They render blurry or invisible on some browser/OS combinations.
- **Typography** should be bold, cool and specific to the game. Load Google Fonts with `<link>` tags in `<head>`, plus the two `preconnect` links. **Never `@import` fonts inside `<style>`**, because it triggers Firefox security errors that stop local images loading.
- **Mermaid** is loaded from a pinned version (`https://cdn.jsdelivr.net/npm/mermaid@11.4.1/dist/mermaid.min.js`) and themed to the page's palette. Diagram text must be legible on desktop and phone.

## SEO head

Every page carries, in `<head>`: a meta description, keywords, author ("Reactorcore Games"), `robots`, a canonical URL, Open Graph tags, a Twitter card, and JSON-LD (`@type: VideoGame`). URLs follow `https://reactorcoregames.github.io/game-design-showcase-portfolio/projects/<page file>`, and the share image is always the `_2_vignette.jpg`, as an absolute URL. All metadata must be honest: these are concepts, not released games. Twitter handle: `@ReactorcoreDev`.

## Rewriting a published page

The old pages were made by Sonnet 3 through a rigid prompt chain. The images and general color direction are usually worth keeping. The content is what needs the most work.

- Re-read the source design(s) and the bible from scratch. Don't just polish the old text. Check what the old page got wrong, flattened or left out, especially the purpose/needs reasoning, the metagame layers and the design's genuine novelties.
- **Keep the page's file name and image prefix.** The URL has been shared, and the five existing images stay at their existing paths. Five early pages have no story image yet (see the manifest). Give them one, which means a one-image spec for those.
- If a rewrite changes what an image should depict, say so in the plan. A regenerated image costs a slot from the daily budget.
- The theme can be refined, not thrown away, unless it clearly doesn't fit.
- Fix the shared defects of the old pages while you're there: the unpinned mermaid, missing image dimensions and lazy loading, the 2025 footer year, and the `@ReactorcoreGames` Twitter handle in the head (the real one is `@ReactorcoreDev`).
- `abyssal_caretaker.html` has no design file. The page itself is the design, so revise it in place.
