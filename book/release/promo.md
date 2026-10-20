# Promo: Game Design Technology on itch.io

## What to upload

- `dist/game-design-technology.zip`: the offline HTML edition (main download). On the upload's settings, leave every platform unticked: it's a document, not an executable.
- `dist/game-design-technology.epub`: the EPUB edition (bonus download).
- Cover image: `book/release/promo/thumbnail.jpg` (630x500, itch.io's "cover image" slot).
- Banner / page header: `book/release/promo/cover.jpg` (1280x720).
- Screenshots: `book/release/promo/screenshot-1.jpg` to `screenshot-5.jpg` (1920x1080), in that order.
- Classification: **Books** (not Games). Kind of project: **Downloadable**.

After the page exists, send me its URL: `ITCH_URL` and `ITCH_LABEL` in `tools/book.py` switch the online edition's "coming to itch.io" links to the real page, then `python tools/book.py build`.

## Business model

The plan is set and it fits: the full text is free online, and the offline edition is the paid download. The free edition is the marketing. Every chapter page links to the itch.io page, the book links to the designs and articles, and search engines can index all 48 pages, so the online edition brings traffic that the download converts. Keep the online edition free; putting the text behind a paywall would cut off the search traffic that the rest of the site lives on.

For the itch.io price setting, the two sensible shapes are:

- **Paid with "let people pay more than the minimum" ticked.** A clear "this is how you support the book" signal, and generous readers can pay extra. Since the text is free online anyway, nobody is locked out by the price.
- **Pay what you want with a $0 minimum.** More downloads and more people in your itch.io follower list, at the cost of most downloads being free. itch.io shows a "support the creator" prompt during the download.

The first matches the foreword's wording ("an offline edition you can buy"). If you choose the second, the foreword's sentence still reads fine. The amount is yours to set. A low starting price that rises later, as you usually do, works here too, since the page can say the online edition is free regardless.

Open source isn't the right frame for a book. The ideas are already given away in the foreword's own terms (copy, teach, build on them), which is the part of "open" that matters here.

## Where it gets found

The aim is persistent places that people browse while looking for exactly this:

1. **itch.io itself.** Tagged well, it sits in the book and game-development listings for good. Add it to a "Game design" collection on your profile, and link it from the descriptions of your other itch.io releases.
2. **Your own site.** Already done: the book is in the site nav, the articles page, the links page and the hire-me page, and every chapter links to the store page.
3. **Curated "awesome" lists on GitHub** for game design and game development resources. These are long-lived, high-traffic, and accept a pull request that adds one line. Link the free online edition there, since those lists prefer free resources; it funnels to itch.io from inside the book.
4. **Goodreads and Open Library.** Self-published ebooks can be added as books with a cover and description, and readers who look up game design books find them there.
5. **Game design communities' resource lists.** The game design subreddits and Discord servers keep pinned or wiki pages of recommended reading. I couldn't check these directly (Reddit blocks automated access), so look at their wiki/resource pages and the rules about self-promotion before posting.

## Copypastas

### itch.io

**Name**

```
Game Design Technology: The Holy Grail of Fun
```

**Subtitle (99 characters)**

```
A game design book about where fun really comes from: the human needs every game meets or violates.
```

**Description (markdown)**

```markdown
# Game Design Technology: The Holy Grail of Fun

**Where fun really comes from, and how to design for it on purpose.**

Almost every game designer makes the same mistake: they copy the final result of games they love, the mechanics and the genre and the look, instead of the root cause that made those games fun in the first place. This book is about that root cause.

Fun is the fulfillment of human needs. Every game, mechanic and menu meets some needs and violates others, whether the designer meant it to or not. Once you see games that way, a lot of design stops being guesswork: why players misbehave, why "engagement" tricks backfire, why some games are played for decades and others are forgotten in a week, and what to build first so the content you add later multiplies instead of running out.

## What's inside

- **Part I · The Common Mistake:** final result vs root cause, and why popularity is a side effect, not a goal.
- **Part II · The Mindset:** purpose, understanding human beings, and fun as the fulfillment of needs.
- **Part III · Intention Is Not Action:** when good intentions fail. Misbehaving players, money, padding and the fear that the game is too short.
- **Part IV · The Technical Side: Designing the Game:** foundations before content, building forces instead of deserts, content that multiplies, infinite metagames, pacing and progression without the scam, worlds that last.
- **Part V · The Technical Side: Building, Sharing and Growing:** what a game designer really does, the design process, working with people, handling sensitive material, and growing as a designer.
- **Back matter:** the needs at a glance, a question kit, a padding checklist, further reading and a glossary, made to keep open next to your design notes.

34 chapters in 5 parts, about 90,000 words.

## The download

- **Offline HTML edition** (zip): the whole book as a folder you open in any web browser. Contents sidebar, chapter navigation, the same look as the online edition. No internet connection, nothing to install.
- **EPUB edition:** for e-readers and phone reading apps, with a simpler layout your reader can restyle.

## Free to read online

The whole book is also free to read online: https://reactorcoregames.github.io/game-design-showcase-portfolio/book/

Buying the offline edition is how you support it. The ideas themselves are free: copy them, teach them, build games on them. A mention is appreciated.

---

Made by Reactorcore. Everything else I do: https://linktr.ee/reactorcore
```

**Tags (10)**

```
game-design, gamedev, book, ebook, epub, game-development, design, psychology, non-fiction, tutorial
```

### GitHub

Not applicable: the book has no repo of its own. Its sources live in the portfolio repo, whose description already covers the site.

### YouTube

Skipped: there's no video planned for the book.
