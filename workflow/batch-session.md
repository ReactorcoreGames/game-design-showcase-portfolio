# Batch session: five pages, hands-free

How to run one session of the remaining project pages (checklist sections 3 and 4). Reactorcore starts each session with a one-line prompt pointing here and is mostly away while it runs, so this file holds the rules that would otherwise need asking.

## Before starting

Read `CLAUDE.md`, `workflow/page-brief.md`, `workflow/image-brief.md`, both bible parts in full (`reference/bible/2a-bible.md`, `2b-bible.md`), `workflow/cookbook.md`, and the two reference pages (`site/projects/AAL-Bunkerships.html`, `site/projects/graviton-mayhem.html`) with `site/projects/project.css` and `project.js`. Check that you're on `dev` with a clean tree, and run `git log --oneline -10` to see where the last session stopped.

## Which five

The next five unticked projects in `checklist-todo.md`: first the rewrites in section 3, in list order, then the new pages in section 4, in list order. If a project can't be done in this session (its design is missing, or it's blocked on something outside the repo), skip it, say why in the manifest notes, and take the next one.

## Hands-free means you decide

Don't stop to ask. Make every design call yourself from the design files, the bible and the lore, the way the pilots did: titles for unnamed games, stand-in names for outside IP, how to split a file that holds several games (the UNO, ETCC, Terrene and Motherlode families), which variants of a vague doc are strongest, what to fill where the design is silent, whether a published image still fits. Record each non-obvious decision in that project's manifest notes, in a sentence or two, so Reactorcore can review it afterwards.

Stop and ask only for something that can't be undone or reaches outside the repo: renaming a published page, deleting anything, spending beyond the limits below, or pushing.

## Spending

- **Klein** (`klein4b`): allowed, within the daily allowance of 70 images across all of today's sessions. Five pages need about 25, plus rerolls. If unsure what today has already used, check `python cli.py status` in the BAIG folder.
- **SDXL**: free, use as needed for the mini images.
- **Nano Banana 2 Lite**: up to 3 rerolls per session (about $0.03 each), only for an image Klein clearly can't manage after two tries (complex structured scenes, flagged outputs). Beyond that, keep the best Klein result and note the image in the manifest for a later reroll.

## Per project

Follow the page brief's process from start to finish: build, images, checks (desktop and 390px phone), catalog, sitemap, manifest, checklist. Then commit on `dev`, one commit per project, before starting the next. Don't push or merge.

If a page shows a gap in the template (`project.css`, `project.js`), fix it in the template rather than in the page, then re-check the other template pages at phone width. If you learn something every later page should know, add it to `workflow/page-brief.md` or `workflow/image-brief.md` in the same commit.

## Ending the session

Finish with a short report to Reactorcore:

- the five pages, each with its file name and one line on what it argues
- the decisions worth a second look (they're also in the manifest)
- the images: anything kept that's weaker than it should be, any Nano Banana use, and roughly what Klein used today
- template or brief changes
- what's next in the checklist
