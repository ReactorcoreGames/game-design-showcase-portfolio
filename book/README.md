# The book: chapter sources

*Game Design Technology: The Holy Grail of Fun*, by Reactorcore. The plan, table of contents, voice guide and decisions are in `workflow/book-plan.md`. Read that first.

Each file in `chapters/` is one page of the book, written once as an HTML fragment: just the content, no `<html>`, `<head>`, navigation or styles. The online edition (`site/book/`, D7) and the offline zip and EPUB (`tools/book.py`, D8) both wrap these same files, so this folder is the only place the text lives.

After changing the text: `python tools/book.py build` for the site, and `python tools/book.py release` (or `build_release.bat`) for new itch.io downloads in `dist/`. `release/` holds the itch.io material (the zip's readme, the store page text in `promo.md`, the images); `python tools/book_promo.py` redraws the images, which only matters if the look or the chapter titles change. `fonts/` is IBM Plex Sans, which the offline edition carries because the site gets it from Google Fonts.

## Fragment conventions

- One `<article class="chapter" id="...">` per file. The `id` matches the file name without the extension.
- A `<header>` with `<p class="kicker">` (for example "Part I · Chapter 3") and the `<h1>` title.
- Sections are `<h2 id="...">` with short kebab-case ids, so the site can add anchor links. Subsections are `<h3>`; the build gives them ids where they have none. A `<section>` wrapper may carry its own id, but never the same one as its `<h2>`: every id on a page must be unique, and `tools/book.py` refuses to build otherwise.
- `<aside class="note">` for warnings and side notes the original set apart. `<blockquote>` for quotes. `<dl>` for definition lists.
- Cross-references to other chapters are `<a href="cNN-slug.html">`. D7 and D8 keep those paths working.
- Anything that needs Reactorcore's judgment gets an `<!-- Author note? ... -->` comment right where it applies. Each part's review list collects them.
- No hard-wrapped prose. One paragraph per line.

## Order

These file names are fixed: chapters already link to the later ones, so use them exactly. The number in a file name is an identifier, not the chapter number: `c30a-handle-with-care` was added in the revision pass as Chapter 31, so `c31`–`c33` are Chapters 32–34. The kickers carry the real numbers. (All of it is written: front matter, Parts I–V and the back matter.)

Front matter: `f1-foreword`, `f2-how-to-read`, `f3-definitions`.

Part I, The Common Mistake: `p1-the-common-mistake`, `c01-final-result-vs-root-cause`, `c02-three-projects-two-designers`, `c03-how-i-learned-this`, `c04-question-everything`, `c05-popularity-is-a-side-effect`, `c06-making-games-for-the-wrong-reason`, `c07-the-holy-grail`.

Part II, The Mindset: `p2-the-mindset`, `c08-purpose`, `c09-understanding-human-beings`, `c10-fun-is-the-fulfillment-of-needs`, `c11-from-inspiration-to-purpose`, `c12-game-or-interactive-tool`, `c13-purpose-as-a-compass`.

Part III, Intention Is Not Action: `p3-intention-is-not-action`, `c14-intention-and-action`, `c15-when-players-misbehave`, `c16-good-intentions-violent-methods`, `c17-money`, `c18-afraid-the-game-is-too-short`, `c19-more-ways-good-intentions-fail`.

Part IV, Designing the Game: `p4-designing-the-game`, `c20-taking-inventory`, `c21-foundations-before-content`, `c22-build-the-forces-not-the-desert`, `c23-content-that-multiplies`, `c24-infinite-metagames`, `c25-pacing-difficulty-and-progression`, `c26-worlds-that-last`.

Part V, Building, Sharing and Growing: `p5-building-sharing-and-growing`, `c27-what-a-game-designer-really-does`, `c28-the-design-process`, `c29-working-with-people`, `c30-beyond-the-game`, `c30a-handle-with-care`, `c31-putting-it-all-together`, `c32-growing-as-a-designer`, `c33-what-a-good-game-is`.

Back matter (kicker "Back matter"): `b1-needs-at-a-glance`, `b2-the-question-kit`, `b3-the-padding-checklist`, `b4-further-reading`, `b5-glossary`.
