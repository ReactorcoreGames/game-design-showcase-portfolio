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
- [ ] Rename or delete the old workspace folder `C:\ClaudeWorkspace\HTML Game Design Showcase Maker`

## 1. Nexus page overhaul (`site/index.html`)

Done first, so every page finished afterwards only needs a one-line entry.

- [ ] Project cards come from a single data list (title, subtitle, page, thumbnail, blurb, tags), not hand-written HTML
- [ ] Badges telling concepts apart from released games, and ways to browse (genre/tags, AAL universe…)
- [ ] Articles catalog subpage (`reference/outreach/article-links.md`)
- [ ] Links sidebar (articles, itch.io, Patreon, linktree, Discord, contact/hire)
- [ ] Visual refresh with Opus. The page is a showcase in its own right.
- [ ] Fix its SEO head: `og:url` points at the wrong address, and `og:image` should be an absolute URL
- [ ] Check `hire_me/hire_me.html` still says the right things

## 2. Pilot: set the quality bar

- [ ] Rewrite one published page and review it closely
- [ ] Build one new page from standby and review it closely
- [ ] Adjust `workflow/page-brief.md` with whatever the pilots taught

## 3. Rewrite the published pages (37)

The images stay, except the 5 pages marked ⚑, which also need a story image.

- [ ] AAL-Stealth-Sector
- [ ] AALSW
- [ ] AALSuperweapon
- [ ] ChainReactionDemolitionPunch
- [ ] City Buster
- [ ] Collidotron
- [ ] Custom Dismount ⚑
- [ ] EradicationWars
- [ ] Halberd_Suit_Wars
- [ ] HazardMissionTeam (2)
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
- [ ] Graviton Singularity Mecha (Momentum Missile Mayhem 2 Redux)
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
