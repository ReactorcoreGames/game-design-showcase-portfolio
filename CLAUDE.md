# Reactorcore's Game Design Showcase Portfolio

A static portfolio site presenting Reactorcore's game designs. Each design gets its own showcase page with five AI-generated images, and a nexus page (`site/index.html`) links them all. This repo holds both the published site and the material it's made from: the designs, the design bible, the lore, and the workflow docs.

Live mirrors (both serve only `site/`):
- GitHub Pages: https://reactorcoregames.github.io/game-design-showcase-portfolio/
- Cloudflare Pages: https://rc-game-design-portfolio.pages.dev/

## Layout

```
site/                  THE PUBLISHED SITE. Only this folder is deployed.
  index.html           nexus page (project cards)
  styles.css           nexus styles
  hire_me/             resume / hire-me page
  projects/            one <slug>.html per project
    images/            <prefix>_<1-5>_<role>.jpg
    thumbnails/        <prefix>_2_vignette_thumb.jpg (nexus cards)
designs/
  MANIFEST.md          source of truth: which design feeds which page, slugs, status
  standby/             designs awaiting a page
  done/                designs that have a page (plus a few retired ones, see manifest)
reference/
  bible/               Reactorcore's design mentality bible (2a + 2b), read for every page
  lore/                AAL universe lore, for AAL-set projects only
  outreach/            article links, contact links, revshare/hire-me post texts
workflow/
  page-brief.md        how to write a showcase page (new or rewrite)
  image-brief.md       how to write image prompts + run the image pipeline
  cookbook.md          text-over-image legibility recipes
  legacy/              the old Sonnet-era task docs, kept for history only
image-prompts/         <slug>.json image specs (+ legacy/ old prompt txts)
tools/images.py        spec -> BAIG -> resized JPEGs + thumbnails in site/
archive/               unused alternate images
_work/                 (gitignored) raw BAIG output
```

## Doing one project

Read `workflow/page-brief.md` and follow it. In short: find the project in `designs/MANIFEST.md`, read its design file(s) and both bible parts, plan and **wait for approval**, build the page, write the image spec, add the nexus card, then update the manifest. One project per session works best.

## Images

Images are generated locally with the Batch AI Image Generator (BAIG) at `C:\ClaudeWorkspace\AI image gen batch program`, which has a CLI. Klein 4B at Standard tier, **max 70 images a day**. Full details in `workflow/image-brief.md`. Pages are written with their final image paths already in place, so the image pass only drops files into those paths.

Only `tools/images.py gen` without `--dry-run` spends anything. Run it only when the user has said to generate. Everything else in the pipeline is free.

## Publishing

- **GitHub Pages** deploys `site/` through `.github/workflows/pages.yml` on every push to `main` that touches `site/`. Pages source is set to "GitHub Actions".
- **Cloudflare Pages** deploys through `C:\14 Repos\CLOUDFLARE PAGES DEPLOYER\deploy-to-cloudflare RC GD Portfolio.bat`, which uploads `site/` with wrangler. It deploys whatever is checked out locally, so run it from an up-to-date `main`.
- Pages whose images aren't generated yet would go live with broken images. Do page work on a branch, or hold the push until the image pass is done.

## Conventions

- **Published URLs are frozen.** Never rename an existing page or its images. Untidy names like `HazardMissionTeam (2).html` stay.
- **New slugs** are lowercase kebab-case, used for both the page file and the image prefix.
- Everything outside `site/` is public in the GitHub repo by choice. Reactorcore wants people to learn from the designs and the bible. Never put credentials or copyrighted third-party assets (ripped sprites etc.) in the repo.
- Markdown prose is never hard-wrapped. One line per paragraph.
- The pages are hand-written static HTML/CSS: no build step, no framework. External scripts (mermaid) are loaded from a CDN at a pinned version.

## Status and next steps

Progress is tracked in `checklist-todo.md`, Reactorcore's own checklist. Tick items there as they're finished. The manifest records the per-project details.
