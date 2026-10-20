"""Build the online edition of the book from its chapter fragments.

The text lives only in book/chapters/ (conventions in book/README.md). This tool wraps each fragment
in the site's page frame (tools/book_template.html) and writes site/book/: a contents page
(index.html) and one page per fragment, under the fragment's own file name, so the chapters'
cross-links (href="c12-....html") work as written. D8 extends it with the offline zip and the EPUB.

    python tools/book.py build      write site/book/*.html
    python tools/book.py check      run the checks only, write nothing

What the build does to each fragment: drops the <!-- Author note? --> comments, gives every <h3>
without an id one made from its text, adds a "#" anchor link to every h2 and h3, and counts the
words for the reading time. Styles are site/book/book.css; the green mark is site/book/book-logo.png
(tools/brand.py book-logo).

It refuses to build if an id appears twice on a page, a link points at a book page or anchor that
doesn't exist, or an Author note would reach the output. Fragments listed in ORDER that don't exist
yet (the back matter) are skipped with a notice.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from string import Template

REPO = Path(__file__).resolve().parent.parent
SRC = REPO / "book" / "chapters"
OUT = REPO / "site" / "book"
BASE = "https://reactorcoregames.github.io/game-design-showcase-portfolio/"
BOOK_URL = BASE + "book/"
WORDS_PER_MINUTE = 230               # same as tools/articles.py

TITLE = "Game Design Technology"
SUBTITLE = "The Holy Grail of Fun"
FULL_TITLE = f"{TITLE}: {SUBTITLE}"
# The offline edition's store page is made once the download exists (D8). Until then this points to
# the itch.io profile, which shows the rest of the catalog anyway.
ITCH_URL = "https://reactorcore.itch.io/"
ITCH_LABEL = "coming to itch.io"

# Reading order: (group id, group label, fragment stems). A part's label is taken from its opener
# page ("Part I · The Common Mistake"), so only front and back matter name themselves here.
ORDER = [
    ("front", "Before you start", ["f1-foreword", "f2-how-to-read", "f3-definitions"]),
    ("p1", None, ["p1-the-common-mistake", "c01-final-result-vs-root-cause", "c02-three-projects-two-designers",
                  "c03-how-i-learned-this", "c04-question-everything", "c05-popularity-is-a-side-effect",
                  "c06-making-games-for-the-wrong-reason", "c07-the-holy-grail"]),
    ("p2", None, ["p2-the-mindset", "c08-purpose", "c09-understanding-human-beings", "c10-fun-is-the-fulfillment-of-needs",
                  "c11-from-inspiration-to-purpose", "c12-game-or-interactive-tool", "c13-purpose-as-a-compass"]),
    ("p3", None, ["p3-intention-is-not-action", "c14-intention-and-action", "c15-when-players-misbehave",
                  "c16-good-intentions-violent-methods", "c17-money", "c18-afraid-the-game-is-too-short",
                  "c19-more-ways-good-intentions-fail"]),
    ("p4", None, ["p4-designing-the-game", "c20-taking-inventory", "c21-foundations-before-content",
                  "c22-build-the-forces-not-the-desert", "c23-content-that-multiplies", "c24-infinite-metagames",
                  "c25-pacing-difficulty-and-progression", "c26-worlds-that-last"]),
    ("p5", None, ["p5-building-sharing-and-growing", "c27-what-a-game-designer-really-does", "c28-the-design-process",
                  "c29-working-with-people", "c30-beyond-the-game", "c30a-handle-with-care", "c31-putting-it-all-together",
                  "c32-growing-as-a-designer", "c33-what-a-good-game-is"]),
    ("back", "Back matter", ["b1-needs-at-a-glance", "b2-the-question-kit", "b3-the-padding-checklist",
                             "b4-further-reading", "b5-glossary"]),
]

# Pages whose <h1> isn't the name they go by in the contents (the foreword's h1 is the book's title).
LABELS = {"f1-foreword": "Foreword"}

PAGE = Template((Path(__file__).parent / "book_template.html").read_text(encoding="utf-8"))

AUTHOR_NOTE = re.compile(r"[ \t]*<!--\s*Author note\?.*?-->[ \t]*\n(?:[ \t]*\n)?", re.S)
HEADING = re.compile(r'<(h[23])( id="([^"]*)")?>(.*?)</\1>', re.S)
TAG = re.compile(r"<[^>]+>")
TEMPLATE_IDS = {"book-toc", "contents-title"}   # ids the page frame uses, kept off generated heading ids


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def plain(fragment: str) -> str:
    return " ".join(html.unescape(TAG.sub(" ", fragment)).split())


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", plain(text).lower().replace("'", "").replace("’", "")).strip("-") or "section"


@dataclass
class Page:
    stem: str
    group: str
    kicker: str
    title: str
    label: str
    body: str
    words: int
    description: str
    sections: list[tuple[str, str]] = field(default_factory=list)
    ids: set[str] = field(default_factory=set)

    @property
    def href(self) -> str:
        return f"{self.stem}.html"

    @property
    def minutes(self) -> int:
        return max(1, round(self.words / WORDS_PER_MINUTE))

    @property
    def number(self) -> str | None:
        m = re.search(r"Chapter (\d+)", self.kicker)
        return m[1] if m else None

    @property
    def opener(self) -> bool:
        return re.fullmatch(r"Part [IVX]+", self.kicker) is not None


def load(stem: str, group: str) -> Page:
    path = SRC / f"{stem}.html"
    raw = path.read_text(encoding="utf-8")
    body = AUTHOR_NOTE.sub("", raw).strip() + "\n"
    if "Author note" in body:
        sys.exit(f"{stem}: an Author note survived the cleanup; check its comment syntax")

    m = re.search(r'<p class="kicker">(.*?)</p>', body)
    kicker = plain(m[1]) if m else ""
    title = plain(re.search(r"<h1>(.*?)</h1>", body, re.S)[1])

    ids = re.findall(r'\bid="([^"]+)"', body)
    dupes = sorted({i for i in ids if ids.count(i) > 1})
    if dupes:
        sys.exit(f"{stem}: duplicate ids {', '.join(dupes)} (book/README.md: a <section> never reuses its <h2>'s id)")
    taken = set(ids) | TEMPLATE_IDS
    sections = []

    def heading(m: re.Match) -> str:
        tag, hid, inner = m[1], m[3], m[4]
        if not hid:
            base = hid = slugify(inner)
            n = 2
            while hid in taken:
                hid, n = f"{base}-{n}", n + 1
            taken.add(hid)
        if tag == "h2":
            sections.append((hid, plain(inner)))
        label = esc(f"Link to this section: {plain(inner)}")
        return f'<{tag} id="{hid}">{inner}<a class="anchor" href="#{hid}" aria-label="{label}">#</a></{tag}>'

    body = HEADING.sub(heading, body)

    no_epigraph = re.sub(r'<section class="epigraph".*?</section>', "", body, flags=re.S)
    first = re.search(r"<p>(.*?)</p>", no_epigraph, re.S)
    description = plain(first[1]) if first else title
    if len(description) > 160:
        description = description[:157].rsplit(" ", 1)[0].rstrip(",;:") + "…"

    return Page(stem=stem, group=group, kicker=kicker, title=title, label=LABELS.get(stem, title), body=body,
                words=len(plain(body).split()), description=description, sections=sections, ids=taken)


def load_all() -> tuple[list[Page], list[tuple[str, str, list[Page]]]]:
    pages, groups, missing = [], [], []
    for gid, label, stems in ORDER:
        members = []
        for stem in stems:
            if (SRC / f"{stem}.html").exists():
                members.append(load(stem, gid))
            else:
                missing.append(stem)
        if not members:
            continue
        if label is None:
            opener = members[0]
            label = f"{opener.kicker} · {opener.title}"
        pages += members
        groups.append((gid, label, members))
    listed = {s for _, _, stems in ORDER for s in stems}
    strays = sorted(p.stem for p in SRC.glob("*.html") if p.stem not in listed)
    if strays:
        sys.exit("fragments not in ORDER (add them in reading order): " + ", ".join(strays))
    if missing:
        print("not written yet, skipped: " + ", ".join(missing))
    return pages, groups


def check_links(pages: list[Page]) -> None:
    by_href = {p.href: p for p in pages}
    bad = []
    for p in pages:
        for href in re.findall(r'href="([^"]+)"', p.body):
            if re.match(r"[a-z]+:", href):
                continue
            target, _, anchor = href.partition("#")
            page = by_href.get(target) if target else p
            if page is None or (anchor and anchor not in page.ids):
                bad.append(f"{p.stem} -> {href}")
    if bad:
        sys.exit("broken book links:\n  " + "\n  ".join(bad))


# ---------- page parts ----------

def book_ld(extra: dict) -> str:
    book = {"@type": "Book", "name": FULL_TITLE, "url": BOOK_URL, "inLanguage": "en", "isAccessibleForFree": True,
            "author": {"@type": "Person", "name": "Reactorcore"}}
    data = {"@context": "https://schema.org", **(book if not extra else {**extra, "isPartOf": book})}
    return "    " + json.dumps(data, ensure_ascii=False, indent=4).replace("\n", "\n    ")


def kicker_label(p: Page) -> str:
    return p.kicker or "Before you start"


def sidebar(groups, current: Page) -> str:
    out = []
    for gid, label, members in groups:
        head = esc(label)
        if members[0].opener:
            cur = ' aria-current="page"' if members[0] is current else ""
            head = f'<a href="{members[0].href}"{cur}>{head}</a>'
        items = []
        for p in members:
            if p.opener:
                continue
            num = f'<span class="n">{p.number}</span>' if p.number else '<span class="n"></span>'
            if p is current:
                secs = "".join(f'<li><a href="#{hid}">{esc(text)}</a></li>' for hid, text in p.sections)
                secs = f'<ol class="toc-secs">{secs}</ol>' if secs else ""
                items.append(f'<li><a href="{p.href}" aria-current="page">{num}{esc(p.label)}</a>{secs}</li>')
            else:
                items.append(f'<li><a href="{p.href}">{num}{esc(p.label)}</a></li>')
        out.append(f'<p class="toc-group">{head}</p><ol>{"".join(items)}</ol>')
    return f"""<nav class="book-toc" aria-label="Book contents">
            <details id="book-toc">
                <summary><span class="label">Contents</span></summary>
                <a class="toc-book" href="./"><img class="logo pixel" src="book-logo.png" alt="" width="86" height="86">{esc(TITLE)}</a>
                {"".join(out)}
                <a class="toc-itch" href="{ITCH_URL}" target="_blank" rel="noopener">Offline edition: {ITCH_LABEL} ↗</a>
            </details>
        </nav>"""


TOC_SCRIPT = """    <script>
        (function () {   // the contents list is open beside the text on wide screens, a tap-to-open box on narrow ones
            var toc = document.getElementById("book-toc"), wide = window.matchMedia("(min-width: 1140px)");
            function fit() { toc.open = wide.matches; }
            fit();
            wide.addEventListener("change", fit);
            var cur = toc.querySelector('a[aria-current="page"]'), nav = toc.parentNode;
            if (cur && wide.matches) nav.scrollTop = cur.offsetTop - nav.clientHeight / 3;
        })();
    </script>"""


def pager_link(p: Page | None, cls: str, label: str) -> str:
    if p is None:
        return (f'<a class="pager-link {cls}" href="./"><span class="label">{label}</span>'
                f'<span class="pager-title">Contents</span></a>')
    return (f'<a class="pager-link {cls}" href="{p.href}"><span class="label">{label} · {esc(kicker_label(p))}</span>'
            f'<span class="pager-title">{esc(p.label)}</span></a>')


def offline_panel() -> str:
    return f"""<aside class="offline panel" aria-label="Offline edition">
                    <span class="icon" style="--icon: url(../icons/open-book-lorc.png)" aria-hidden="true"></span>
                    <div>
                        <p class="label">Offline edition</p>
                        <p>A download of the whole book, to keep and read without a connection, is coming to itch.io. This online edition stays free to read.</p>
                    </div>
                    <a class="btn" href="{ITCH_URL}" target="_blank" rel="noopener">reactorcore.itch.io ↗</a>
                </aside>"""


def chapter_page(p: Page, prev: Page | None, nxt: Page | None, groups) -> str:
    body = "\n".join("                    " + line if line else "" for line in p.body.rstrip("\n").split("\n"))
    main = f"""    <main class="wrap sheet book-page">
        <div class="book-layout">
        {sidebar(groups, p)}

            <div class="book-main">
                <p class="book-bar"><a href="./"><img class="logo pixel" src="book-logo.png" alt="" width="86" height="86">{esc(FULL_TITLE)}</a><span>{p.minutes} min read</span></p>
                <div class="prose">
{body}
                </div>

                {offline_panel()}

                <nav class="pager" aria-label="Previous and next">
                    {pager_link(prev, "prev", "← Previous")}
                    {pager_link(nxt, "next", "Next →") if nxt else '<span class="pager-gap next"></span>'}
                </nav>
                <p class="back"><a class="btn btn-ghost" href="./"><span class="icon" style="--icon: url(../icons/open-book-lorc.png)"></span>Contents</a></p>
            </div>
        </div>
    </main>"""
    links = ""
    if prev:
        links += f'    <link rel="prev" href="{prev.href}">\n'
    if nxt:
        links += f'    <link rel="next" href="{nxt.href}">\n'
    name = p.label if not p.number else f"Chapter {p.number}: {p.label}"
    return PAGE.substitute(
        page_title=esc(f"{p.label} · {TITLE}"),
        og_title=esc(f"{name} · {FULL_TITLE}"),
        og_type="article",
        description=esc(p.description),
        url=BOOK_URL + p.href,
        ld_json=book_ld({"@type": "Chapter", "name": name, "url": BOOK_URL + p.href}),
        prev_next_links=links,
        body_class="book",
        main=main,
        itch_url=ITCH_URL,
        script=TOC_SCRIPT,
    )


def contents_page(pages: list[Page], groups) -> str:
    chapters = sum(1 for p in pages if p.number)
    parts = sum(1 for p in pages if p.opener)
    words = sum(p.words for p in pages)
    hours = round(words / WORDS_PER_MINUTE / 60)
    blocks = []
    for gid, label, members in groups:
        opener = members[0] if members[0].opener else None
        if opener:
            head = (f'<h3 class="group-head"><span class="label">{esc(opener.kicker)}</span>'
                    f'<a href="{opener.href}">{esc(opener.title)}</a></h3>')
            blurb = f'<p class="group-blurb">{esc(opener.description)}</p>'
        else:
            head, blurb = f'<h3 class="group-head"><span class="label">{esc(label)}</span></h3>', ""
        items = []
        for p in members:
            if p.opener:
                continue
            secs = " · ".join(f'<a href="{p.href}#{hid}">{esc(text)}</a>' for hid, text in p.sections)
            items.append(
                f'<li><a class="ch" href="{p.href}"><span class="n">{p.number or ""}</span>'
                f'<span class="t">{esc(p.label)}</span><span class="m">{p.minutes} min</span></a>'
                + (f'<p class="secs">{secs}</p>' if secs else "") + "</li>")
        blocks.append(f'<section class="group" id="{gid}">{head}{blurb}<ol class="chapters">{"".join(items)}</ol></section>')
    first = pages[0]
    main = f"""    <main class="wrap sheet book-page book-home">
        <section class="cover">
            <span class="bg-icon" style="--icon: url(../icons/open-book-lorc.png)" aria-hidden="true"></span>
            <img class="logo pixel lit cover-logo" src="book-logo.png" alt="" width="86" height="86">
            <div class="cover-text">
                <p class="eyebrow">A book by Reactorcore · free to read online</p>
                <h1 class="glow" data-burst-origin>{esc(TITLE)}</h1>
                <p class="subtitle">{esc(SUBTITLE)}</p>
                <p class="lead">Where fun really comes from, and how to design for it on purpose. A method for game design built on the human needs every game either meets or violates, carried from the first idea through to the finished, shared and supported game.</p>
                <p class="meta-line"><span>{chapters} chapters in {parts} parts</span><span>About {round(words, -3):,} words</span><span>About {hours} hours of reading</span></p>
                <p class="cover-actions">
                    <a class="btn btn-primary" href="{first.href}"><span class="icon" style="--icon: url(../icons/open-book-lorc.png)"></span>Start reading</a>
                    <a class="btn" href="{ITCH_URL}" target="_blank" rel="noopener">Offline edition: {ITCH_LABEL} ↗</a>
                </p>
            </div>
        </section>

        <section class="contents" aria-labelledby="contents-title">
            <h2 class="section-mark" id="contents-title"><span class="icon" style="--icon: url(../icons/scroll-unfurled-lorc.png)"></span>Contents</h2>
            {"".join(blocks)}
        </section>
    </main>"""
    return PAGE.substitute(
        page_title=esc(f"{FULL_TITLE} · Reactorcore"),
        og_title=esc(FULL_TITLE),
        og_type="book",
        description=esc("A free online book by Reactorcore on where fun really comes from and how to design games "
                        "for it on purpose: game design built on human needs, from the first idea to the finished game."),
        url=BOOK_URL,
        ld_json=book_ld({}),
        prev_next_links=f'    <link rel="next" href="{first.href}">\n',
        body_class="book",
        main=main,
        itch_url=ITCH_URL,
        script="",
    )


# ---------- commands ----------

def cmd_build(args) -> None:
    pages, groups = load_all()
    check_links(pages)
    if args.cmd == "check":
        print(f"ok: {len(pages)} pages, {sum(p.words for p in pages):,} words")
        return
    OUT.mkdir(exist_ok=True)
    keep = {p.href for p in pages} | {"index.html"}
    for old in OUT.glob("*.html"):
        if old.name not in keep:
            old.unlink()                    # a renamed or removed fragment; every page here is generated
    for i, p in enumerate(pages):
        prev = pages[i - 1] if i else None
        nxt = pages[i + 1] if i + 1 < len(pages) else None
        (OUT / p.href).write_text(chapter_page(p, prev, nxt, groups), encoding="utf-8", newline="\n")
    (OUT / "index.html").write_text(contents_page(pages, groups), encoding="utf-8", newline="\n")
    print(f"site/book/: contents + {len(pages)} pages, {sum(p.words for p in pages):,} words")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("build")
    sub.add_parser("check")
    cmd_build(ap.parse_args())


if __name__ == "__main__":
    main()
