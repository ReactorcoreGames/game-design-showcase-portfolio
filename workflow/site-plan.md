# Site plan: the second overhaul

This is the plan for rebuilding the site around what visitors can get out of it. It came from Reactorcore's review of the first nexus overhaul (the `nexus-overhaul` branch, commit `7d465f0`). Each session below is sized to fit in one sitting. Tick progress in `checklist-todo.md`; this file holds the reasoning and the decisions, so a fresh session can pick up any step cold.

## What the site is for

The site is not a "look how cool I am" portfolio. It exists to serve the visitor with something tangible they can take away. Every page should answer "what's in this for me?" for one of six kinds of visitor:

1. **Builders.** People looking for game designs they can freely adopt and make themselves, under their own name and with their own twist. They also get a glimpse of what Reactorcore is working on or wants to work on.
2. **Hirers.** People looking for an advanced game designer to hire.
3. **Partners.** People who want to team up: either build one of Reactorcore's projects through the revshare system (https://reactorcore.itch.io/reactorcores-revshare-system), or invite Reactorcore into their own project. The second only works if the project is interesting enough to drop Reactorcore's own projects, the pay is adequate and fair, and Reactorcore can come to trust their word. None of that is easy, and the page can say so plainly.
4. **Learners.** People who want to learn game design, through the articles and the book. The designs teach too: a visitor might not care for a project as a whole but take one idea from it in a completely different direction ("the rest isn't my cup of tea, but that one thing is good"). The site is a showcase of designs and an educational resource at the same time, and the project pages should make it easy to lift a single idea, not only the whole package.
5. **Lore fans.** People who like sci-fi lore and enjoy reading about a universe's history, rules and tech. The AAL universe page is for them.
6. **Explorers.** People who want to see what else Reactorcore does: games, tools, socials, everything on the links page.

The designs carry no license and no copyright claim, and they are not secret. That is deliberate, and the site should say why: the industry keeps recycling stale ideas. Talented teams spend years on concepts that fulfill no human need, encourage toxic behaviour or exploit the player. Others take two steps forward and one step back. More people forking these designs into their own versions means more variety and better games. Reactorcore would rather see a design built by someone else than never built.

The core idea behind every design, in Reactorcore's words (raw material for the copy, not final): *a game should fulfill fundamental human needs, because that's where what people call "fun" actually comes from.*

## Identity rules

- The name is **Reactorcore**. The studio is **Reactorcore Games**, a creative label for games and game development work. It is not a registered company, and the site doesn't need to explain that.
- Reactorcore stays anonymous. No real name, anywhere, including file names and document metadata in the repo. Finland can be mentioned where it helps (it has a good reputation), but it is never highlighted or made a selling point. Remove it from the nexus description and hero copy.
- Titles say **Reactorcore's**: "Reactorcore's Game Design Portfolio".
- The AAL universe is not a selling point yet, since nobody knows it. No AAL badges, filters or stats on the nexus. It gets its own page instead (session C3), reached through the lore fans' hero button, which is framed around what that visitor wants ("sci-fi lore to dig into"), not around the AAL name.

## Look and feel

**Mood:** a dark blue-white blueprint grid, a cyan reactor wave flowing through it all the time, and a cyan glow "reactor startup" pulse burst as the intro when the page opens. The burst is inspired by the Cherenkov flash of the JSI TRIGA research reactor in Ljubljana when it pulses. The page should feel energetic and alive: "oomph", not subdued. The AI art mosaic in the background stays, but as dim flair behind the writing, not as the main attraction.

**Fonts** (from `assets/fonts/`, all free):
- Headers: **Nulshock Bd** (`Nulshock Bd.otf`)
- Navigation, buttons, labels: **Oxanium Medium** (`Oxanium-Medium.ttf`; other Oxanium weights are there if needed)
- Body text: keep the current font.
- **Nulshock can't be a web font.** Checked in A1: Typodermic's free desktop licence excludes "embedding in websites", so live `@font-face` text needs a paid MyFonts webfont licence. Pre-rendered images of text (a wordmark, a fixed banner) are allowed. Reactorcore accepted Orbitron Black instead (SIL OFL, shipped renamed as "RC Display", since Orbitron has a Reserved Font Name and the build modifies it).
- Convert only the fonts actually used to WOFF2 in `site/fonts/`, subset to Latin. Check each font's license file or source before shipping it, since "free" sometimes means personal use only. Oxanium is SIL OFL. Nulshock is a Typodermic font, so check its desktop/web embedding terms.
- The other fonts in the folder can serve future pages and project pages that want their own flavour.

**Logo and favicon:** the cyan "Reactorcore Games" logo (`assets/avatars identity/rcg logo color (N).png`, whichever is cyan) is the mark for the game design site, with a favicon set made from it. The other colour variants are kept for other sections of the site (for example a different colour for the book or the AAL page).

**Icons:** `assets/icons/` is the game-icons.net pack, 4,180 PNGs, CC BY 3.0 (a few CC0). Uses:
- a colour-tinted ID badge for each project on the nexus and on its page (new `icon` field in `projects.js`)
- icons for article cards and section markers
- large, faint masks and backgrounds on the nexus and project pages
- Tint them with CSS `mask-image`, so one file serves any colour. Copy only the icons in use into `site/icons/`.
- CC BY needs credit: a credits line in the footer, linking to a credits section that names game-icons.net and the contributing artists (from `!license.txt`).

**Other identity material** (`assets/avatars identity/`): avatars (close, mid, far), mood images, a repeating tech background tile, a circuit board flair element, and a pixel-art guy firing a big gun. These are available for flair, the about-me spots, the links page and 404s.

**Reading surface:** text never sits directly on the moving background. Each page's main content goes on a `.sheet` (in `theme.css`): a near-opaque panel with a still, faint copy of the grid, so the wave only flows in the margins around it. Reactorcore found the wave distracting behind text, so every new page (project pages, the book, the AAL section) uses it too.

**Accessibility:** the startup burst plays once per visit (remembered in `sessionStorage`) and can be skipped with a click or key. With `prefers-reduced-motion`, the wave stops and the burst becomes a simple fade. Text over the moving background must still pass contrast (see `workflow/cookbook.md`).

## Site map after the overhaul

```
index.html            nexus: hero with six routing buttons, then the designs grid
designs (grid)        A–Z by default, square tiles, small gaps, icon badges
work-with-me/         team-up page: revshare + joining other projects
hire_me/hire_me.html  rewritten (URL kept, published URLs are frozen)
links.html            grid of buttons to every link (replaces the drawer)
articles.html         articles catalog, now linking to on-site articles
articles/<slug>.html  the articles themselves, moved off Google Docs
book/                 Game Design Technology: The Holy Grail of Fun (online edition, one page per chapter)
aal/                  the AAL universe: one polished page (index.html) and its images
projects/<slug>.html  the 37 + new design pages, restyled to the new theme
```

The six hero buttons (a 3×2 grid on desktop, stacked on phones) map to the six visitors:
- **Builders** go to the designs grid and the free-to-fork statement.
- **Hirers** go to the hire-me page.
- **Partners** go to the team-up page.
- **Learners** go to the articles page, which also features the book prominently.
- **Lore fans** go to `aal/`.
- **Explorers** go to the links page.

The header and footer also link the articles, the book and the AAL section.

## Sessions

Phases A and B come first, because every later page uses the theme they set up. Phases C and D are independent of each other and of the project-page work in checklist sections 3–6, so they can run in any order after B.

### Phase A: identity and theme

**A1. Theme system and look test.** Build `site/theme.css` (tokens, fonts, blueprint grid, tiles, buttons, header, footer) and `site/fx.js` (reactor wave, startup burst, reduced-motion handling), shared by every page. Make the font WOFF2 subsets, the logo header mark, the favicon set and the icon tint mechanism, and copy the first batch of icons. Deliver a single look-test page (`site/_theme-test.html`, deleted after approval) that shows the hero with the burst and wave, a few tiles, buttons, headings, body text and an article block. **Reactorcore approves the look before B1 starts.** Approved on 2026-10-19. The approved test page is kept at `workflow/a1-look-test.html` as the markup reference for B1 (hero island, routing buttons, tiles, footer). B1 used it and it has been removed. The look will likely take a round or two of feedback, so leave room for that in this session.

### Phase B: structure

**B1. Nexus rebuild.**
- Title "Reactorcore's Game Design Portfolio".
- New hero, as approved in the A1 look test: the bright scrolling art mosaic (the first overhaul's look) with a central island holding the title, a one-line motto and the six routing buttons, all visible without scrolling. No big logo, no eyebrow, no stats strip. The hero is opaque; the colour flow, blueprint grid and reactor wave start below it.
- New copy built from "What the site is for": the free-to-fork statement and the human-needs core idea. Draft it, then get Reactorcore's sign-off on the wording.
- Designs grid: A–Z, big square-edged tiles (min 400 px wide) showing the full blurb, with a tinted icon badge on each. No Concept/Released badges (they'd discourage people from building the released ones), no AAL badge, filter or count, and no search, sort or genre filters at all.
- Header nav gets a "Hire me" button. The footer keeps the first overhaul's plain labelled-links style, plus the icon and font credits.
- Remove the links drawer, which moves to its own page in B2. Fix the meta descriptions (no "from Finland").
- Pick an icon for each of the 37 projects (the `icon` field in `projects.js`, documented in its field reference).
- Merge `nexus-overhaul` into `main` after this session, once the images are in place.
- Done in B1: `articles.html` moved onto the theme too (the old `styles.css` and the drawer's `site.js` are gone). Pages that don't exist yet get live stand-ins, to be swapped when they're built: in `index.html` the Team up button goes to the itch.io revshare page (B2: `work-with-me/`), Sci-fi lore to the lore folder on GitHub (C3: `aal/`), and Everything else plus the header's Links to linktree (B2: `links.html`). Book and Universe join the header nav in `index.html` and `articles.html` once D7 and C3 exist, and the Learn button's line mentions the book once it's out.

**B2. Links page and team-up page.**
- `links.html`: a grid of big buttons from `reference/outreach/Contact Links RCG.txt`, plus homepage, GitHub, catalogue, articles, book and AAL. Leave Telegram out.
- `work-with-me/index.html`, from the revshare texts in `reference/outreach/`:
  - how the revshare system works, briefly, linking to the itch.io page
  - which projects are open for it
  - the honest terms for inviting Reactorcore into someone else's project: it has to be interesting, the pay has to be fair, and trust has to be earned
  - how to make contact
- Done in B2: `links.html` and `work-with-me/index.html` are built, and the B1 stand-ins for Team up, Everything else and the header's Links now point at them in `index.html` and `articles.html`. X (@ReactorcoreDev) is on the links page with a note that it's a news feed, not a place to talk. The links page's Sci-fi lore button still goes to the lore folder on GitHub (swap it to `aal/` in C3). The team-up page lists the open designs from `projects.js` (everything not `released`), so it stays current on its own. `tools/sitemap.py` now lists both pages.

**B3. Hire-me rewrite.** Rewrite `site/hire_me/hire_me.html` from scratch, keeping its URL. Inputs:
- the released games on the catalogue, https://reactorcoregames.github.io/catalogue/
- the designs on this site
- the articles and the book

What's out of date on the current page: Windsurf, GDevelop, Kenney Shape, Asset Forge and "macro scripts, not with AI". Reactorcore now directs production through Claude Code end to end. The location line "Finland, GMT+2" goes, with no time zone in its place. The Telegram handle goes too.

On pay, hourly billing doesn't fit how the work happens: design epiphanies arrive at any hour and the work can't be switched on and off like a shift. Reactorcore has approved this model:
- a **monthly design-lead retainer**, floor €1500/month (covers bills and everyday life with some leeway), with €3000/month as the upper end
- **fixed-price design commissions**: a complete game design document plus a showcase page like the ones on this site, quoted per project
- **revshare**, pointing to the team-up page

No hourly rate. Drop the $1600/month and $50/hour figures.

Done in B3. The page has a TL;DR panel, three services, proof of work (designs, articles, catalogue highlights), how-I-work, pay, terms and contact, and keeps the two red mecha images as framed art. The book stays off the page until D7. Reactorcore asked for the rates to be set for them, and the page uses this scale (the price follows the pressure):
- retainer: part-time with no deadlines or pressure €500–€1000/month, design lead €1500/month (the default), priority lead with tight deadlines, on-call availability and own projects on hold up to €3000/month
- design review (one to four weeks): from €400, quoted per project
- complete design (document plus showcase page): from €1500, quoted per project

### Phase C: content sections

**C1. Articles import tool and the first batch.** The articles move off Google Docs onto the site. The sources are the 20 Google Docs HTML exports in `assets/gd articles raw/` (zips, 131 MB in total, mostly images). Write `tools/articles.py`:
- unzip each export into `_work/articles/`
- strip the Google Docs markup down to clean headings, paragraphs, lists, links and images
- resize the images to at most 1200 px wide and re-encode them (WebP or JPEG q≈80) into `site/articles/images/<slug>/`
- write `site/articles/<slug>.html` from a shared template in the new theme, with a reading time and a "previous / next" footer
- point `site/articles.js` at the local pages, keeping the Google Docs URL as an "original" link if wanted

Convert the 16 articles already listed. Target: the whole articles folder under about 15 MB.

Done in C1: `tools/articles.py build` writes all 16 pages (14.5 MB in total, from about 55 MB of source images). The page template is `tools/article_template.html` and the shared styles are `site/articles/article.css`. Images are WebP q70, at most 1040 px wide, since the reading column is 780 px. `articles.js` entries now carry a `slug` (the page) and an `original` (the Google Doc), and the tool writes each article's reading time back into it. The cleanup drops the doc's title block, lifts the "Summary:" section into an "In short" panel, turns italic "(…)" lines under images into captions, and replaces the identical Patreon/Discord "Closing words" every article ended with by one shared "Talk about it" panel. Long articles get a contents list, a sticky sidebar on wide screens. `tools/sitemap.py` lists the article pages. For C2: add each new article to `SOURCES` in the tool and to `articles.js`. The guest-article header and the project links in Big Projects still need adding to the tool.

**C2. The new articles.**
- "Reactorcore's Big Projects" (30,000 words, 286 images, the bulk of the session). It talks about designs that already have showcase pages. Publish it anyway, since it shows the design thinking behind them in more depth than the showcase pages can, and link from each mention to that project's page.
- "Astroneer – 8th Planet Infinite Metagame Concept".
- The two guest articles, in full: "Exploitative Game Design Beyond the F2P Debate" by Edward McNeill and "Loopholes in Game Design" by Julian Pritchard (Devmag, 2012). Reactorcore has the authors' permission and claims no ownership. The reason for preserving them is that the original sites may not last; Devmag in particular is old and hanging by a thread. Each page opens with a clear guest-article header: the author's name, a link to the original source (to keep sending traffic there), and Reactorcore's short note on why it's reposted. The catalog marks them as guest articles, and they carry no Reactorcore byline.
- Add all four to `articles.js` and the sitemap.

Done in C2. All four are built by `tools/articles.py`, whose `SOURCES` entries now take per-article options (start/stop markers, dropped paragraphs, intro paragraphs, skipped sections, heading cleanup, showcase-page links, a written date, a guest header). Two new shelves hold them: "Designs in depth" (Big Projects, Astroneer) and "Guest articles". Reactorcore's decisions on Big Projects: the Sexy Neuromancy Sessions section is left out to keep the site SFW, and the article starts at "General Design Tenets", dropping the January 2024 funding pitch (Foreword, Help Is Welcome). It's marked "Written January 2024". AAL Superweapon, Admiral Wars Beyond and Astro Industry Freelancer link to their showcase pages; when the standby projects in it (TopVerse, RoomSpace, Standalone, Shape Smasher, Planet Warfare) get pages, add them to its `links` option and rebuild. Big Projects and Astroneer have no "original" link, since their Google Doc URLs aren't in the repo; add them to `articles.js` if wanted. The hire-me page now counts 18 articles (guests excluded). The articles folder is 32 MB, 15.8 MB of it Big Projects' 263 images, all lazy-loaded.

**C3. AAL Universe page.** `aal/index.html`, one polished page for the universe, built from `reference/lore/aal-universe/` (540 KB of lore; start with the all-in-one file). Reactorcore decided against wiki-style entry pages: the lore is too small and too raw to fill a wiki, and nobody knows the universe yet, so one page that people actually scroll does the job better. The raw lore files stay in the repo for Reactorcore's own use, but the site doesn't link to them; the page is the maintained, public version.
- The angle: a sci-fi universe that is its own thing, not Star Trek, Star Wars or Mass Effect, with its own timeline.
- Its outlook is optimistic despite the wars and horrors in it: humanity reaches a good outcome. Altered humans, aliens, robots and AI coexist in a cohesive, kind society that pursues cool things, lives forever and kicks ass. That utopia looks weird by conservative standards and unlike anything people imagine.
- Sections: the pitch, the timeline (the main section), the Milky Way civilization, the rules of the universe, space monsters, FTL travel, and the designs set in AAL. A sticky table of contents keeps the long page navigable. Defence layers and superweapons stay out: they differ from game to game, so they aren't universe canon.
- The rules of the universe (Equilibrium, the Chaos System) are a highlight. They are what makes the universe and Reactorcore's bigger games interwoven: the technical limits every game runs into (processing, memory, storage, entity counts) are baked into the universe as natural law, instead of being ignored until a game becomes laggy, unplayable or crash-prone. The exact solutions differ per game. The universe is not a self-aware simulation and doesn't think it's a game; it's a real universe where those constraints are simply another law of nature.
- Swap the Sci-fi lore buttons in `index.html` and `links.html` from the GitHub lore folder to `aal/`, and write the image spec. The budget is **up to 10 Klein images** for the page, generated in a normal image day.

Done in C3 (images still to generate). `site/aal/index.html` has seven sections: the universe (pitch and the AAL name), the timeline (13 eras in three acts: the old world, the turning, the Mugen age), life in the Milky Way, laws of the universe (ground rules, Equilibrium, the Chaos System with its load ladder, a designer's note), space monsters, FTL travel (the drive, a homeworld-to-homeworld trip, uncharted systems, flying homeworlds) and the designs set there, rendered from the `universe: "aal"` entries in `projects.js`. Era tags link Eradication Wars, Tactical Arsenal Command and AAL Superweapon to their pages, and Standalone and Planet Warfare to their sections of the Big Projects article; swap those two to showcase pages once they exist. Reactorcore's framing decisions: the Eradication Wars and the re-education/reset of holdouts are stated plainly, not as a "dark price". The purity side is the dictators and thugs who'd lose the power to bully, Homo mugen spreads through pleasure, affection and seduction (kept SFW but not sugar-coated), and the early eras are deliberately gritty like our world. The images are `image-prompts/aal.json`, a free-form section spec (`tools/images.py` gained the `out` mode for it), 10 images in the John Harris preset, written to `site/aal/images/NN-name.jpg`. The Sci-fi lore buttons in `index.html` and `links.html` now go to `aal/`, Universe joined the header nav in `index.html` and `articles.html`, and `tools/sitemap.py` lists `aal/`.

### Phase D: the book

The book is *Game Design Technology: The Holy Grail of Fun* by Reactorcore. It was started long ago and never finished. The source is `reference/bible/game-design-technology-original.html`, about 61,000 words. The plan is to finish it in Reactorcore's voice, publish it free online as its own section, and sell an offline edition on itch.io, the way Robert Nystrom does with *Game Programming Patterns*. The original's closing note asks readers not to sell the book. That note gets replaced, since the paid edition is the author's own.

The existing bible (`2a-bible.md`, `2b-bible.md`) was distilled from this material by an earlier model. How faithfully it was distilled is unknown, so the book work doubles as a check on the bible.

**D1. Audit and outline (planning only, then approval).** Read the whole original, both bible parts and the articles. Report:
- what the original covers well
- what it promises in its "Structure of the book" but never delivers
- what the articles have since corrected or extended
- where the bible drifted from the source

Propose the final table of contents, a target length, and a voice guide built from the original. Its features include the "Word1/Word2/Word3" device, the "In other words…" restatements, the direct address and the plain-spoken confidence. **Reactorcore approves the outline before any writing.**

**D2–D6. Writing.** Roughly one part of the book per session, about 10–15k words each. The work is editing and finishing the existing text, not replacing it. Keep Reactorcore's voice. Fold in the articles' later thinking as corrections. Mark anything that needs Reactorcore's judgment with an `Author note?` comment. Reactorcore reviews each part before the next one starts. The exact split follows the D1 outline.

**Format.** HTML/CSS is the book's main format, as multiple pages: one per chapter, with real navigation that a page-based format can't offer. Skip PDF: it lays text out in fixed pages, which reads badly on phones, and it's laborious to typeset well. The chapters are written once as HTML, and both editions come from those same files.

**D7. Book site.** `site/book/`: a contents page, one HTML page per chapter, a sidebar contents list, previous/next links and anchor links on headings. Give it its own colour from the logo variants. Add a link to the itch.io edition on every page. Also add a Book button to the "On this site" group in `links.html`, and mention the book in the hire-me page's proof of work; both were left out in B2/B3 because the book didn't exist yet.

**D8. Offline edition and store page.** A build script (`tools/book.py`) that packages the same chapter pages for download:
- **Main download:** a zip of the book as a self-contained HTML folder (fonts and images inside, no CDN or network calls), opened by double-clicking `index.html`. It looks and navigates exactly like the online edition.
- **Bonus:** an EPUB, for people who read on e-readers or phone reading apps. An EPUB is HTML and CSS inside a zip, and its text reflows to fit the screen like a web page, so it costs little to make from the same chapters. It gets a simpler layout, since e-readers ignore most fancy styling.
- Draft the itch.io page text and suggest a pay-what-you-want minimum.

**D9. Bible refresh.** Rewrite `2a-bible.md` and `2b-bible.md` from the finished book, so every showcase page written afterwards uses the corrected thinking. Project rewrites done before this point aren't redone. They'll be touched up only where the refresh changes something they rely on.

### Phase E: project pages

These are checklist sections 2–6 as before (pilot, 37 rewrites, new pages, images, publish), with one change: the page template adopts the A1 theme. That covers the fonts, the project's icon badge, the blueprint background and a short "free to fork" line linking to the statement on the nexus. Do the pilot after B1, so the pilot pages use the final look. `workflow/page-brief.md` gets updated in the pilot to describe the new template.

## Decisions made

1. **Guest articles:** publish both in full. The authors gave permission and Reactorcore claims no ownership. Each page opens with the author and a link to the original (see C2).
2. **Telegram:** removed everywhere.
3. **Time zone:** left out.
4. **Book title:** *Game Design Technology: The Holy Grail of Fun*, confirmed.
5. **Merge timing:** `nexus-overhaul` waits and merges after B1.
6. **Hire-me pay model:** retainer from €500 (relaxed part-time) through €1500 (the default) to €3000 a month, fixed-price design reviews (from €400) and complete designs (from €1500), and revshare, with no hourly rate. Approved; the exact figures were set in B3.
7. **Book format:** multi-page HTML online, with a downloadable offline HTML zip and an EPUB bonus. No PDF.
