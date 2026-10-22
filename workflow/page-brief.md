# Showcase Page Brief

How to write one game design showcase page, either a new one from a standby design or a rewrite of a published one. It was rewritten after the two pilot pages (session 2 of the checklist), which set the quality bar and the shared template. The two reference pages are `site/projects/AAL-Bunkerships.html` (a big design, rewritten) and `site/projects/graviton-mayhem.html` (a compact one, new). When in doubt about markup or tone, copy what they do.

## What a page is for

Each page presents one of Reactorcore's game designs to whoever might land on it: a player, an employer, a fellow developer, someone who wants to build it, someone learning game design. It is not a full GDD and doesn't list every number in the design. It is a competent, compelling overview that leaves the reader certain this game has been thought through properly, and that they now understand what playing it would be like and why it would be worth playing. It doesn't need to be exhaustive: leave out what's unresolved, experimental or superseded in the design docs.

The designs are free to fork, so a page should also make it easy to lift a single idea: every feature card should stand on its own.

The tone is professional yet blunt, layperson-friendly but with real technical depth, colorful but faithful to the game's theme, and never vague or padded. It focuses on the player's experience: what the game promises to give them.

## Inputs, in priority order

1. **The project's design file(s)** in `designs/`, as listed in `designs/MANIFEST.md`. These are the authority. Many are stream-of-consciousness: later writing overrides earlier writing, and some points are open questions. Where they are thin or silent, fill the gaps as Reactorcore would. Some projects have fuller docs outside the repo (the manifest says where, e.g. `C:\08 Projects\Project_Bunkerships`); read those too when they exist.
2. **The design bible**, `reference/bible/2a-bible.md` and `2b-bible.md`, the short form of Reactorcore's book (`book/chapters/`, which wins any disagreement). Read both in full before designing anything, especially section 14 of `2b` (applying it to these pages) and section 15 (misreadings to avoid). The book's walkthroughs (`c31`) show the reasoning on real projects. Every page must visibly carry it: what need the game meets, how its structure meets it, and why that structure is better than the genre default.
3. **Lore**, `reference/lore/` and the AAL page (`site/aal/index.html`, the polished summary), only for projects set in the AAL universe. Use only what's relevant. The game's own design overrides the lore wherever they conflict.
4. **Reactorcore's articles**, `reference/outreach/article-links.md`: what Reactorcore cares about. Don't link them from project pages.
5. **Recurring mechanics** that designs name without explaining: `reference/supercores.md`.

A design file can hold several games. The manifest says which part feeds which page. If you find a split the manifest doesn't cover, decide it the way the manifest's notes suggest, and record the decision there.

## Titles and outside IP

- If the design names the game, use that name. If it doesn't, choose a title that fits the game's mood, in the format `[Thematic Name]: [Three-Word Game Type]`, which lets a reader grasp the game from the name alone (like "Metal Gear Solid: Tactical Espionage Action").
- **The AAL prefix:** a project gets it only if its design already has one. Many games are set in the AAL universe in spirit only (side stories) and go without it. Those still aren't listed on the AAL page unless they carry the prefix.
- Some designs grow out of someone else's game, IP or trademark (BLAME!, UNO, LEGO, Smash Bros, Metroid, M.D. Geist…). Credit the inspiration openly, in the overview or lore and in the footer ("Inspired by…"), but the title and every in-game name (characters, weapons, factions, card or brick names, enemy armies) must be original stand-ins. The design doc's own shorthand for borrowed things doesn't carry onto the page.
- Never target real-world groups, nationalities or identifiable people. Turn such villains into fictional archetypes with the same dramatic function, ideally built from behaviors anyone can fall into (the bible's sins-and-virtues move).

## Released games

A few projects already exist as shipped games (`released` in the manifest). Their page still presents the design, adds a prominent link to play it, and describes the game as released rather than as a concept. Use the game's real screenshots and promo art for the five image slots instead of generating images, and skip the SDXL minis unless real screenshots can fill those spots.

## Process

The default is plan, then approval, then build. In a batch session whose prompt says to work hands-free, skip the approval stop: make the decisions yourself from the design and the bible, and record the non-obvious ones (title choices, renamed IP, gaps you filled, splits) in the manifest's notes for that project.

1. Read the inputs and decide the plan: title, sections and what each argues, palette and fonts, title animation, diagrams, the five images and the mini-image spots. Outside a hands-free session, show it to Reactorcore and wait.
2. Add the page's fonts (see Visual identity) and icons with `tools/brand.py`.
3. Build the page at `site/projects/<slug>.html`, starting from a copy of a reference page.
4. Write the image specs and generate (see Images). Look at every result, reroll duds, and make each alt text describe what was actually generated.
5. Check the page (see Checks).
6. Add the catalog entry to `site/projects.js` (field reference at its top; `status` is `concept` unless released; pick `genres` from the fixed list) and run `python tools/sitemap.py`.
7. Update `designs/MANIFEST.md`: status and notes. For a new project, `git mv` its design file(s) from `designs/standby/` to `designs/done/`. Tick it in `checklist-todo.md`.
8. Commit on `dev`, one commit per project. Don't push or merge unless Reactorcore says so.

## The template

Every page is built on three shared files. Don't fork them per page. Improve them when a page reveals a gap, and re-check the existing pages when you do.

- `site/theme.css`: the site chrome (header, footer), Oxanium for labels, IBM Plex Sans for body text, and the page background: the looping colour flow (`body::before`, colours from `--flow-1`/`--flow-2`, one speed for all project pages) and the blueprint grid (`body::after`).
- `site/projects/project.css`: the showcase layout, driven by tokens each page sets (the list is at the top of the file): `--flow-1/2`, `--grid-minor/major`, `--p-ground`, `--p-panel`, `--p-1/2/3`, `--p-text`, `--p-dim`, `--p-line`, `--font-title`, `--font-sub`.
- `site/projects/project.js`: the "Download as Markdown" export (a 1:1 text copy of the page with the forked-copy note on top, no images, and a hover hint on the buttons) and the box art sizing (exactly as tall as the send-off card).

A page's own `<style>` holds only its `@font-face` rules, its tokens, its title animation (`.p-name`, `.p-sub`, `.p-sub::after`, and the `.section-mark::after` pulse), and the few page-specific tweaks it needs. Don't load `fx.js` on project pages.

## Page structure

In order. Sections can be merged or renamed when a project calls for it, but each exists for a reason, so drop one only when it truly doesn't apply. Element classes are in the reference pages.

1. **Site header**, as on every page.
2. **Hero** (`.p-hero` > `.p-hero-frame`): the whole 16:9 title image, never cropped, with the title over its lower left: `<h1 class="p-title"><span class="p-name">Name</span><span class="p-sub">Three-Word Type</span></h1>`. On phones the title sits under the image.
3. **ID strip** (`.p-id`, marked `data-md="skip"`): the project's icon badge, the "Reactorcore's Personal Game Design Project" label linking to Patreon, the free-to-fork line linking to `../index.html#free-to-fork`, and the Markdown button.
4. **Game overview:** one to three short paragraphs, the first as `.p-lead`. Credit inspirations here.
5. **Target Audience · Game's Purpose · Core Concept** (`.p-trio`, three cards). Audience: people by the need they're hungry for and what they're sated or frustrated by, plus how demanding the interface is. Purpose: the fundamental needs, in the bible's vocabulary, and which needs the design deliberately avoids draining. Core concept: how the structure meets them, and which genre default it escapes.
6. **Story image** (`_5_story`) with a quote, then **Lore & Story** (`.p-prose`, with `h3` subsections): where, why (the past without spoiling the future), and the goal right now.
7. **Controls & Interface:** the key list as `.p-keys` groups (an even number of groups, or one), plus prose on what the player controls and how it feels.
8. **Vignette image** (`_2_vignette`) with a quote.
9. **Game Layers** (`.p-stack` of `.p-layer` cards): moment-to-moment, low metagame, high metagame, practical game flow. A nested `.p-nest` diagram of the structure fits here or in Game Modes.
10. **Game Modes:** title and purpose for each mode, or one longer description if there's only one. Never invent modes the design doesn't have.
11. **Features & Mechanics** (`.p-stack` of `.p-feature` cards, each with a kicker, an icon and an `h3`): 6 for a compact design, 9 for a big one (3 for a tiny one). Go deep on what makes the game unlike its genre, as a technical document a layperson can follow. The **feature image** (`_3_feature`) and its quote go in the card for the single most important feature.
12. **Trivia:** optional, only if there's something genuinely fun to say.
13. **Send-off** (`.p-sendoff`): the 2:3 box art beside a card with a kicker, the full title as `h2`, back-of-the-box copy that feels like the game (the book's store-page idea: a recruitment letter, a briefing…), a closing line in bold, and the "Fork it: download as Markdown" button.
14. **Footer:** links (linktree, itch.io), "Reactorcore Games · <year> · Back to the designs", an "Inspired by…" line when there's outside inspiration, the game-icons credit, and the fonts used with their licences.

Leave out development timelines, build plans, technical specs, empty stats and anything boastful. These are concepts: nothing may suggest the game exists or is in development. Don't add per-page "how to build it" sections either; the free-to-fork line and the Markdown export cover that.

## Writing

- Follow the bible's section 14: purpose and needs, the infinite overarching goal and finite local goals in the layers, the bible's mechanics named where the design has them. Avoid its list of words that sell the opposite ("addictive", "grind", "earn", "unlock", "loot", "rewarding progression", "leaderboard", "daily", "limited-time"…).
- Where an older design has unlocks, cash rewards, achievements or scaling difficulty, present the bible's version: everything available from the start (with natural limits or campaign parameters), achievements as mementos and living history, feedback rather than rewards. Say so plainly; don't hide that the page fills a gap.
- **Quotes on images** state one interesting mechanic plainly and accurately, as the design really has it. No jokes, no invented anecdotes, no events the design doesn't support. The story quote may describe the setting instead.
- Break long text into short paragraphs. Bold text gets a color (the template does this). Use emoji sparingly or not at all.
- Prefer prose a layperson can follow over jargon. Name inspirations ("as in Advance Wars") when they explain faster than a description.

## Visual identity

Every page shares the template's layout and differs in palette, fonts and title effect. No two pages should look like siblings.

- **Palette:** set the tokens at the top of the page's style. Backgrounds are never pure white or black; aim for a hint of hue. No blue-orange or other cliché complementary pairs. Mono, dual or tri-color schemes all work. Pick the badge `tint` in `projects.js` from the fixed list (cyan, blue, green, yellow, orange, red, magenta) to match.
- **Fonts:** take display fonts from `assets/fonts/` (Reactorcore's curated set), self-hosted as WOFF2. `workflow/fonts/` already has rendered samples of every CC0 and OFL font, a licence table for the whole set, and `usage.md`, a list of which fonts are taken (`python tools/fonts.py list` regenerates it), so start there. Fonts whose glyphs spill outside their own metrics have been moved to `assets/fonts/nah/` by `python tools/fonts.py scan --move`. Check the embedded licence first (`fontTools`: name IDs 13/14 and `fsType`) and prefer CC0 and SIL OFL fonts, which need no further thought. Add the font to the `FONTS` list in `tools/brand.py`, run `python tools/brand.py fonts`, and restore any existing `.woff2` the run re-encoded without changes. Render a sample first and check the glyphs the page needs: Zero Hour's `&` looks like an 8, for example. A very wide font needs a smaller `.p-name` size.
- **Title and H2 effects** use only `text-shadow`, `color`, `box-shadow` and `@keyframes` (glow pulse, sweep, halo, flicker, underline glow…), over layered dark shadows so the title stays legible at the dimmest frame. **Never use `background-clip: text` or `-webkit-text-fill-color: transparent`.** The template turns animations off under `prefers-reduced-motion`.
- **Icons:** choose game-icons names in `assets/icons/` for the badge, section marks and cards, and copy them in with `python tools/brand.py icons <names>`.

## Diagrams

Designs explain better with something to look at than with walls of text. The template's diagram kit replaces mermaid (which is no longer used); use it wherever it beats a paragraph:

- `.p-table` (inside `.p-table-wrap`): comparisons, modes, arsenals, opponent types. Give each `td` a `data-label` when the column name helps, because on phones every row becomes a stacked card.
- `.p-chain`: steps or a dependency chain, with arrows (vertical on phones).
- `.p-nest`: nested structure, such as galaxy > region > mission > battle.
- `.p-keys`: the controls.

## Images

**Five Klein images per page**, at these paths (relative to the page):

| # | File | Ratio | Purpose |
|---|---|---|---|
| 1 | `../projects/images/<prefix>_1_title.jpg` | 16:9 | Hero mood-setter |
| 2 | `../projects/images/<prefix>_2_vignette.jpg` | 16:9 | What playing it feels like |
| 3 | `../projects/images/<prefix>_3_feature.jpg` | 16:9 | The key feature, shown literally or as a visual metaphor |
| 4 | `../projects/images/<prefix>_4_boxart.jpg` | 2:3 | Box art cover |
| 5 | `../projects/images/<prefix>_5_story.jpg` | 16:9 | Zoomed-out view of the setting |

For new projects `<prefix>` is the slug; published pages keep their existing prefix. `tools/images.py finish` makes the nexus thumbnail. If Klein can't manage a complex, structured scene (a cutaway, a diagram-like shot), reroll that one image on Nano Banana 2 Lite.

**Up to ten SDXL mini images** (free): 320×240 mood pictures floated to the right of the text in the lore, game layers and features sections (not controls or modes, and not in a card that already has a diagram or a big image). Each prompt is the section's own opening line behind a shared `lead` style phrase; they add flavor and never try to show a mechanic accurately. They're decorative: `<figure class="p-mini" data-md="skip"><img src="mini/<prefix>/NN-name.jpg" alt="" width="320" height="240" loading="lazy"></figure>`, placed right after the section's or card's `h3`.

Spec format, generation, duds and flagged outputs are in `workflow/image-brief.md`. Images go in with `width`/`height` attributes and `loading="lazy"` on everything below the hero.

## Checks

Before committing a page, view it in headless Edge (`C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe`) served by `python -m http.server` from `site/` (fonts don't load over `file://`):

- desktop at 1440 wide (`--screenshot`, a tall `--window-size`), looking over every section. Very tall headless screenshots leave blank, unpainted rectangles, often right over the send-off, and anchors (`#sendoff`) don't scroll under `--virtual-time-budget`. To look at one section reliably, load the page in an iframe on a scratch page that hides every other `main > *` element and the hero.
- **phone at 390 wide**: headless windows won't go narrower than about 500px, so load the page in a 390px-wide `<iframe>` inside a scratch page in `site/_tmp/` (move it to `C:\trash` afterwards) and read `documentElement.scrollWidth`. It must be 390. Hide the framed page's own scrollbar first (`contentDocument.documentElement.style.scrollbarWidth = "none"`): with it, the iframe leaves 375px and every page, the reference pages included, reads 377 because the site header is 377 wide. A real phone's overlay scrollbar takes no width. If it's still not 390, look for elements with `scrollWidth > clientWidth`: wide display fonts are the usual cause.
- the Markdown export, when the page has unusual markup (capture the blob in the same kind of iframe page).
- that the display fonts actually loaded: in the same kind of iframe page, list `contentDocument.fonts` with each face's `status`. A WOFF2 the browser can't decode shows `error` and the page silently falls back to Segoe UI, which is easy to miss in a screenshot (Motion Control did this).

Then re-read the page as the bible's section 14 asks: does every section serve the purpose, does it show which need is met and how, and does anything quietly promise a reward loop, a grind or a competition?

## SEO head

Every page carries, in `<head>`: a meta description, keywords, author ("Reactorcore Games"), `robots`, a canonical URL, Open Graph tags, a Twitter card (`@ReactorcoreDev`), and JSON-LD (`@type: VideoGame` with `"creativeWorkStatus": "Concept"` unless released). URLs follow `https://reactorcoregames.github.io/game-design-showcase-portfolio/projects/<page file>`, and the share image is always the `_2_vignette.jpg`, as an absolute URL. All metadata must be honest: these are concepts, not released games.

## Rewriting a published page

The old pages were made by Sonnet 3 through a rigid prompt chain, often without the full design docs, so they hallucinated features, modes and lore. Rebuild them on the template from scratch; only the images (and a general color direction, if it fits) carry over.

- Re-read the design(s) and the bible from scratch. Check what the old page got wrong, invented, flattened or left out, especially the purpose and needs, the metagame layers and the design's genuine novelties.
- **Keep the page's file name and image prefix.** The URL has been shared. The one exception so far was `AALSW.html` → `AAL-Bunkerships.html`, on Reactorcore's word, with the old file kept as a redirect stub. Don't rename on your own.
- Keep the existing images unless one no longer fits what the page says. A regenerated image is fine when it clearly improves the page (record why in the manifest). The pages marked ⚑ in the checklist have no story image yet: write a full five-image spec, generate only image 5 (`--only 5`, then `finish --only 5`), and keep the old prompts of the other four as a record.
- Add the SDXL minis like on a new page.
