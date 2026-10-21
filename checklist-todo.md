# Checklist

Everything left to finish the portfolio, in a sensible order. Tick items as they're done. Per-project details (sources, slugs, notes) live in `designs/MANIFEST.md`.

## 0. Setup

- [x] Move the workspace into this repo, with `site/` as the only deployed folder
- [x] Write CLAUDE.md, the manifest, the page and image briefs, and the cookbook
- [x] Build `tools/images.py` (spec → BAIG → resized JPEGs + thumbnails)
- [x] Re-encode the existing images (39 MB → 27 MB)
- [x] Switch GitHub Pages to deploy from GitHub Actions
- [x] Connect Cloudflare Pages to the GitHub repo (build output `site`), replacing the wrangler deploy script
- [x] Review the `restructure` branch, merge it into `main`, push, and check both mirrors still work
- [x] Rename or delete the old workspace folder `C:\ClaudeWorkspace\HTML Game Design Showcase Maker` (Reactorcore handles this manually)

## 1. Nexus page overhaul, first pass (`site/index.html`)

Done first, so every page finished afterwards only needs a one-line entry. Built on the `nexus-overhaul` branch. Reactorcore's review of it led to the second overhaul below.

- [x] Project cards come from a single data list (title, subtitle, page, thumbnail, blurb, tags), not hand-written HTML
- [x] Badges telling concepts apart from released games, and ways to browse (genre/tags, AAL universe…)
- [x] Articles catalog subpage (`reference/outreach/article-links.md`)
- [x] Links sidebar (articles, itch.io, Patreon, linktree, Discord, contact/hire)
- [x] Fix its SEO head: `og:url` points at the wrong address, and `og:image` should be an absolute URL
- [x] First visual refresh (Cherenkov theme) and the hire-me review. Both are superseded by the second overhaul.

## Second overhaul

The full plan, reasons and decisions are in `workflow/site-plan.md`. Read it before starting any of these sessions. Phases A and B come first. C and D can run in any order after that, alongside sections 2–6.

### A. Identity and theme

- [x] Answer the open decisions (recorded at the bottom of `workflow/site-plan.md`)
- [x] A1: shared theme (`theme.css`, `fx.js`): blueprint grid, reactor wave, startup pulse burst, Nulshock Bd and Oxanium fonts, cyan logo and favicon, icon tinting, look-test page
- [x] A1: Reactorcore approves the look

### B. Structure

- [x] B1: nexus rebuild: "Reactorcore's" title, six routing buttons in the hero, new copy, no stats or AAL tagging, A–Z default, square tiles, project icons, drawer removed
- [x] B1: merge `nexus-overhaul` into `main`
- [x] B2: links page and team-up page (revshare, plus joining other projects)
- [x] B3: hire-me page rewritten from scratch

### C. Content sections

- [x] C1: `tools/articles.py` built; the 16 listed articles moved onto the site with optimized images
- [x] C2: "Reactorcore's Big Projects" and "Astroneer 8th Planet" articles published
- [x] C2: the two guest articles published in full, with author credit and source links at the top
- [x] C3: AAL Universe page (one polished page) and its image spec (up to 10 Klein images)
- [x] AAL images generated

### D. The book: *Game Design Technology: The Holy Grail of Fun*

- [x] D1: audit and outline of the original, the bible and the articles
- [x] D1: Reactorcore approves the outline
- [x] D2–D6: write the book, one part per session (split set by the outline)
- [x] D7: online edition at `site/book/`
- [x] Back matter (b1–b5): needs at a glance, question kit, padding checklist, further reading, glossary
- [x] D8: offline HTML zip plus EPUB build, promo images and itch.io page text (`build_release.bat`, `book/release/`)
- [x] D8: publish the itch.io page, then set `ITCH_URL` and `ITCH_LABEL` in `tools/book.py` and rebuild the site
- [x] D9: refresh `2a-bible.md` and `2b-bible.md` from the finished book

## 2. Pilot: set the quality bar

Start after B1, so the pilot pages use the new theme. The pilot also updates the page template (fonts, icon badge, blueprint background, "free to fork" line).

- [x] Rewrite one published page and review it closely (AALSW, now AAL-Bunkerships)
- [x] Build one new page from standby and review it closely (Graviton Singularity Mecha)
- [x] Adjust `workflow/page-brief.md` with whatever the pilots taught (and `workflow/image-brief.md`)

## 3. Rewrite the published pages (37)

From here on, pages are done in hands-free batch sessions of five (the prompt is in `workflow/batch-session.md`).

The images stay, except the 5 pages marked ⚑, which also need a story image.

- [x] AAL-Stealth-Sector
- [x] AALSW (now AAL-Bunkerships, the pilot)
- [x] AALSuperweapon
- [x] ChainReactionDemolitionPunch
- [x] City Buster
- [x] Collidotron
- [x] Custom Dismount ⚑
- [x] EradicationWars
- [x] Halberd_Suit_Wars
- [x] HazardMissionTeam (2)
- [ ] Justice Will Glass Them
- [ ] Mafia_Takedown
- [ ] Megalodon
- [ ] Mosh_Pit_Mayhem ⚑
- [ ] MutantLoveQuest ⚑
- [ ] Planetary Ring Miner
- [ ] Poo Storm Janitor Powersuit
- [ ] RussiBiomonster ⚑
- [ ] Skullhead
- [ ] StardustAssault
- [ ] Underground Brawl
- [ ] Zero Space Robo Derby
- [ ] abyssal_caretaker (no design doc: the page is the design)
- [ ] admiralwars
- [ ] antigrav_deconstruction
- [ ] astro_industry
- [ ] bunkership
- [ ] colossal_devastators
- [ ] cyberdungeon
- [ ] greensteelcommander
- [ ] kickblade
- [ ] spacelancer
- [ ] starforge-legion ⚑
- [ ] thunderstrike-justice
- [ ] tile-mechs
- [ ] unhinged_lander_heist_scifi
- [ ] vectorthunder

## 4. New pages

Each one means: plan → approval → page → image spec → nexus entry → manifest updated → design file moved to `designs/done/`.

- [ ] Ukrainian Turbo Minesweeper (released; images from its own promo folder, no generation)
- [x] Graviton Singularity Mecha (Momentum Missile Mayhem 2 Redux) (pilot 2)
- [ ] Ragdoll battle royale (PUBG doc)
- [ ] Planet Warfare
- [ ] RoomSpace
- [ ] Shape Smasher
- [ ] Net Terminal (BLAME!-inspired)
- [ ] AAL Smash Droids
- [ ] Closed-room smasher (rosebud doc)
- [ ] Soldat Doom Infinite
- [ ] Space Chunks–inspired blast-em-up
- [ ] AAL Standalone
- [ ] Metroid Forever concept
- [ ] AAL Collector
- [ ] AAL Exterminator
- [ ] AAL Voyager
- [ ] AAL Inspector (decide after the trio: its own page, or folded into the trio)
- [ ] TopVerse
- [ ] AAL Trash Miner
- [ ] Temporal Shift RTS
- [ ] Type 1-X Mecha RTS
- [ ] Titanium Punk Orphans
- [ ] Metsanelaimet
- [ ] Auto chess (or fold it into another page)
- [ ] Bazooka Bomber
- [ ] Party Hard–style (its own page, or part of the Kenney anthology)
- [ ] Telekinetic Eradicator
- [ ] UNO-inspired family (decide the split: 1–3 pages)
- [ ] ETCC family (about 3 pages: v1 casual, v2 full, KMF)
- [ ] Vigilant pursuit racing
- [ ] Kenney Jam anthology page
- [ ] Human Apex
- [ ] Motherlode × Tasty Planet (pick the best variants)
- [ ] Pinball mix

## 5. Image generation (local sessions only)

Up to 70 Klein images a day. Use `python tools/images.py check`, then `gen` and `finish` (see `workflow/image-brief.md`).

- [ ] Day 1 batch
- [ ] Day 2 batch
- [ ] Day 3 batch
- [ ] Day 4 batch (if needed)
- [ ] Story images for the 5 ⚑ pages
- [ ] Optional: SDXL stand-ins for pages still waiting, later replaced with Klein images

## 6. Publish

Pages only go live once their images exist. Keep page work on a branch until its image pass is done.

- [ ] Merge to `main` and push (GitHub Pages deploys automatically)
- [ ] Spot-check both mirrors on desktop and phone
- [ ] Update the project count in `reference/outreach/` post texts and announce
