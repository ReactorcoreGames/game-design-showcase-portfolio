"""Build the book's editions from its chapter fragments.

The text lives only in book/chapters/ (conventions in book/README.md). This tool wraps each fragment
in the site's page frame (tools/book_template.html) and writes site/book/: a contents page
(index.html) and one page per fragment, under the fragment's own file name, so the chapters'
cross-links (href="c12-....html") work as written.

    python tools/book.py build      write site/book/*.html (the online edition)
    python tools/book.py check      run the checks only, write nothing
    python tools/book.py release    write the itch.io downloads into dist/ (gitignored):
                                    game-design-technology.zip and game-design-technology.epub

What the build does to each fragment: drops the <!-- Author note? --> comments, gives every <h3>
without an id one made from its text, adds a "#" anchor link to every h2 and h3, and counts the
words for the reading time. Styles are site/book/book.css; the green mark is site/book/book-logo.png
(tools/brand.py book-logo).

It refuses to build if an id appears twice on a page, a link points at a book page or anchor that
doesn't exist, or an Author note would reach the output. Fragments listed in ORDER that don't exist
yet are skipped with a notice.

The offline edition (the zip) is the online one built a second time with a different Edition: the
same pages in a book/ folder beside a "Read the book.html" launcher and book/release/readme.md. It
has to work from file://, where Chrome and Edge refuse web fonts and CSS mask images loaded from
other files, so the theme, the fonts and the icons are packed into one stylesheet
(book/assets/book.css) as data URIs. Header and footer links go to the live site.

The EPUB is EPUB 3 (plus an EPUB 2 toc.ncx for older readers): every page as XHTML with a plain
e-reader stylesheet (EPUB_CSS), and book/release/epub-cover.jpg as the cover (tools/book_promo.py).
"""

from __future__ import annotations

import argparse
import base64
import html
import json
import re
import shutil
import sys
import uuid
import xml.etree.ElementTree as ET
import zipfile
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from string import Template

REPO = Path(__file__).resolve().parent.parent
SRC = REPO / "book" / "chapters"
SITE = REPO / "site"
OUT = SITE / "book"
FONTS = REPO / "book" / "fonts"             # IBM Plex Sans for the offline edition (the site loads it from Google)
RELEASE_SRC = REPO / "book" / "release"     # the zip's readme.md, the EPUB cover, the itch.io material
DIST = REPO / "dist"
RELEASE_NAME = "game-design-technology"
ZIP_FOLDER = "Game Design Technology"       # the folder the buyer gets when they unzip
BASE = "https://reactorcoregames.github.io/game-design-showcase-portfolio/"
BOOK_URL = BASE + "book/"
WORDS_PER_MINUTE = 230               # same as tools/articles.py

TITLE = "Game Design Technology"
SUBTITLE = "The Holy Grail of Fun"
FULL_TITLE = f"{TITLE}: {SUBTITLE}"
# The offline edition's store page.
ITCH_URL = "https://reactorcore.itch.io/game-design-technology-the-holy-grail-of-fun"
ITCH_LABEL = "on itch.io"

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

# The game-icons the pages draw; the offline stylesheet packs exactly these.
ICONS = ["open-book-lorc", "scroll-unfurled-lorc"]

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


@dataclass(frozen=True)
class Edition:
    """What differs between the online pages and the offline download's."""
    offline: bool
    site: str           # where the header and footer's links to the rest of the site point
    assets: str         # prefix of the site's shared files (logo, icons)
    book_assets: str    # prefix of the book's own files (book-logo.png)
    home: str           # the contents page

    def icon(self, name: str) -> str:
        return f"var(--icon-{name})" if self.offline else f"url({self.assets}icons/{name}.png)"


ONLINE = Edition(offline=False, site="../", assets="../", book_assets="", home="./")
OFFLINE = Edition(offline=True, site=BASE, assets="assets/", book_assets="assets/", home="index.html")

ONLINE_META = Template("""    <meta name="robots" content="index, follow">
    <link rel="canonical" href="$url">

    <meta property="og:type" content="$og_type">
    <meta property="og:site_name" content="Reactorcore Games">
    <meta property="og:title" content="$og_title">
    <meta property="og:description" content="$description">
    <meta property="og:url" content="$url">
    <meta property="og:image" content="https://reactorcoregames.github.io/game-design-showcase-portfolio/og-image.jpg">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">

    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:site" content="@ReactorcoreDev">
    <meta name="twitter:title" content="$og_title">
    <meta name="twitter:description" content="$description">
    <meta name="twitter:image" content="https://reactorcoregames.github.io/game-design-showcase-portfolio/og-image.jpg">

    <script type="application/ld+json">
$ld_json
    </script>
""")

ONLINE_HEAD = """    <link rel="icon" href="../favicon.svg" type="image/svg+xml">
    <link rel="icon" href="../favicon.ico" sizes="32x32">
    <link rel="apple-touch-icon" href="../apple-touch-icon.png">
    <link rel="manifest" href="../site.webmanifest">
    <meta name="theme-color" content="#040b16">
{links}
    <link rel="preload" href="../fonts/rc-display-black.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../theme.css">
    <link rel="stylesheet" href="book.css">
    <script src="../fx.js" defer></script>"""

OFFLINE_HEAD = """    <link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
    <link rel="icon" href="assets/favicon.ico" sizes="32x32">
    <meta name="theme-color" content="#040b16">
{links}
    <link rel="stylesheet" href="assets/book.css">
    <script src="assets/fx.js" defer></script>"""


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


def other_edition_link(ed: Edition, cls: str) -> str:
    """The online pages point to the offline edition, the offline pages to the online one."""
    if ed.offline:
        return f'<a class="{cls}" href="{BOOK_URL}" target="_blank" rel="noopener">Online edition ↗</a>'
    return f'<a class="{cls}" href="{ITCH_URL}" target="_blank" rel="noopener">Offline edition: {ITCH_LABEL} ↗</a>'


def sidebar(groups, current: Page, ed: Edition) -> str:
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
                <a class="toc-book" href="{ed.home}"><img class="logo pixel" src="{ed.book_assets}book-logo.png" alt="" width="86" height="86">{esc(TITLE)}</a>
                {"".join(out)}
                {other_edition_link(ed, "toc-itch")}
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


def pager_link(p: Page | None, cls: str, label: str, ed: Edition) -> str:
    if p is None:
        return (f'<a class="pager-link {cls}" href="{ed.home}"><span class="label">{label}</span>'
                f'<span class="pager-title">Contents</span></a>')
    return (f'<a class="pager-link {cls}" href="{p.href}"><span class="label">{label} · {esc(kicker_label(p))}</span>'
            f'<span class="pager-title">{esc(p.label)}</span></a>')


def edition_panel(ed: Edition) -> str:
    if ed.offline:
        return f"""<aside class="offline panel" aria-label="Thank you">
                    <span class="icon" style="--icon: {ed.icon("open-book-lorc")}" aria-hidden="true"></span>
                    <div>
                        <p class="label">Thank you</p>
                        <p>for getting the offline edition. It's how you support the book. The rest of my designs, articles and games are one click away.</p>
                    </div>
                    <a class="btn" href="{BASE}links.html" target="_blank" rel="noopener">All my links ↗</a>
                </aside>"""
    return f"""<aside class="offline panel" aria-label="Offline edition">
                    <span class="icon" style="--icon: {ed.icon("open-book-lorc")}" aria-hidden="true"></span>
                    <div>
                        <p class="label">Offline edition</p>
                        <p>A download of the whole book, to keep and read without a connection, is on itch.io. This online edition stays free to read.</p>
                    </div>
                    <a class="btn" href="{ITCH_URL}" target="_blank" rel="noopener">Get it on itch.io ↗</a>
                </aside>"""


def frame(ed: Edition, *, page_title, og_title, og_type, description, url, ld, links, main, script) -> str:
    """Wrap a page's <main> in the template, with the edition's head and footer."""
    if ed.offline:
        meta, head = "", OFFLINE_HEAD.format(links=links)
        footer = f'Online edition: <a href="{BOOK_URL}" target="_blank" rel="noopener">free to read on the web</a>'
    else:
        meta = ONLINE_META.substitute(og_type=og_type, og_title=esc(og_title), description=esc(description), url=url,
                                      ld_json=ld)
        head = ONLINE_HEAD.format(links=links)
        footer = f'Offline edition: <a href="{ITCH_URL}" target="_blank" rel="noopener">{ITCH_LABEL}</a>'
    return PAGE.substitute(page_title=esc(page_title), description=esc(description), meta=meta, head_assets=head,
                           site=ed.site, assets=ed.assets, home=ed.home, body_class="book", main=main,
                           footer_edition=footer, script=script)


def chapter_page(p: Page, prev: Page | None, nxt: Page | None, groups, ed: Edition) -> str:
    body = "\n".join("                    " + line if line else "" for line in p.body.rstrip("\n").split("\n"))
    main = f"""    <main class="wrap sheet book-page">
        <div class="book-layout">
        {sidebar(groups, p, ed)}

            <div class="book-main">
                <p class="book-bar"><a href="{ed.home}"><img class="logo pixel" src="{ed.book_assets}book-logo.png" alt="" width="86" height="86">{esc(FULL_TITLE)}</a><span>{p.minutes} min read</span></p>
                <div class="prose">
{body}
                </div>

                {edition_panel(ed)}

                <nav class="pager" aria-label="Previous and next">
                    {pager_link(prev, "prev", "← Previous", ed)}
                    {pager_link(nxt, "next", "Next →", ed) if nxt else '<span class="pager-gap next"></span>'}
                </nav>
                <p class="back"><a class="btn btn-ghost" href="{ed.home}"><span class="icon" style="--icon: {ed.icon("open-book-lorc")}"></span>Contents</a></p>
            </div>
        </div>
    </main>"""
    links = ""
    if prev:
        links += f'    <link rel="prev" href="{prev.href}">\n'
    if nxt:
        links += f'    <link rel="next" href="{nxt.href}">\n'
    name = p.label if not p.number else f"Chapter {p.number}: {p.label}"
    return frame(ed, page_title=f"{p.label} · {TITLE}", og_title=f"{name} · {FULL_TITLE}", og_type="article",
                 description=p.description, url=BOOK_URL + p.href,
                 ld=book_ld({"@type": "Chapter", "name": name, "url": BOOK_URL + p.href}),
                 links=links, main=main, script=TOC_SCRIPT)


def contents_page(pages: list[Page], groups, ed: Edition) -> str:
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
            <span class="bg-icon" style="--icon: {ed.icon("open-book-lorc")}" aria-hidden="true"></span>
            <img class="logo pixel lit cover-logo" src="{ed.book_assets}book-logo.png" alt="" width="86" height="86">
            <div class="cover-text">
                <p class="eyebrow">A book by Reactorcore · {"offline edition" if ed.offline else "free to read online"}</p>
                <h1 class="glow" data-burst-origin>{esc(TITLE)}</h1>
                <p class="subtitle">{esc(SUBTITLE)}</p>
                <p class="lead">Where fun really comes from, and how to design for it on purpose. A method for game design built on the human needs every game either meets or violates, carried from the first idea through to the finished, shared and supported game.</p>
                <p class="meta-line"><span>{chapters} chapters in {parts} parts</span><span>About {round(words, -3):,} words</span><span>About {hours} hours of reading</span></p>
                <p class="cover-actions">
                    <a class="btn btn-primary" href="{first.href}"><span class="icon" style="--icon: {ed.icon("open-book-lorc")}"></span>Start reading</a>
                    {other_edition_link(ed, "btn")}
                </p>
            </div>
        </section>

        <section class="contents" aria-labelledby="contents-title">
            <h2 class="section-mark" id="contents-title"><span class="icon" style="--icon: {ed.icon("scroll-unfurled-lorc")}"></span>Contents</h2>
            {"".join(blocks)}
        </section>
    </main>"""
    return frame(ed, page_title=f"{FULL_TITLE} · Reactorcore", og_title=FULL_TITLE, og_type="book",
                 description="A free online book by Reactorcore on where fun really comes from and how to design games "
                             "for it on purpose: game design built on human needs, from the first idea to the finished game.",
                 url=BOOK_URL, ld=book_ld({}), links=f'    <link rel="next" href="{first.href}">\n', main=main, script="")


def write_pages(pages: list[Page], groups, ed: Edition, out: Path) -> None:
    for i, p in enumerate(pages):
        prev = pages[i - 1] if i else None
        nxt = pages[i + 1] if i + 1 < len(pages) else None
        (out / p.href).write_text(chapter_page(p, prev, nxt, groups, ed), encoding="utf-8", newline="\n")
    (out / "index.html").write_text(contents_page(pages, groups, ed), encoding="utf-8", newline="\n")


# ---------- the offline edition ----------

def data_uri(path: Path, mime: str) -> str:
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode('ascii')}"


def offline_css() -> str:
    """theme.css and book.css in one file, with every font and icon inside it as a data URI."""
    theme, n = re.subn(r'url\("fonts/([^"]+)"\)', lambda m: f'url("{data_uri(SITE / "fonts" / m[1], "font/woff2")}")',
                       (SITE / "theme.css").read_text(encoding="utf-8"))
    if n != 3:
        sys.exit(f"theme.css: expected 3 font urls to pack, found {n}")
    plex = data_uri(FONTS / "ibm-plex-sans.woff2", "font/woff2")
    plex_italic = data_uri(FONTS / "ibm-plex-sans-italic.woff2", "font/woff2")
    icons = "\n".join(f'    --icon-{name}: url("{data_uri(SITE / "icons" / f"{name}.png", "image/png")}");' for name in ICONS)
    return f"""/* The offline edition's stylesheet, built by tools/book.py release: site/theme.css and site/book/book.css,
   with the fonts and icons packed in as data URIs so the book works when opened from a folder. */

/* ---------- IBM Plex Sans (the site loads it from Google Fonts) ---------- */
@font-face {{
    font-family: "IBM Plex Sans";
    src: url("{plex}") format("woff2");
    font-weight: 400 600; font-style: normal; font-display: swap;
}}
@font-face {{
    font-family: "IBM Plex Sans";
    src: url("{plex_italic}") format("woff2");
    font-weight: 400; font-style: italic; font-display: swap;
}}
:root {{
{icons}
}}

/* ---------- site/theme.css ---------- */
{theme}
/* ---------- site/book/book.css ---------- */
{(OUT / "book.css").read_text(encoding="utf-8")}"""


LAUNCHER = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{esc(FULL_TITLE)}</title>
    <meta http-equiv="refresh" content="0; url=book/index.html">
    <style>body {{ background: #040b16; color: #e6f0fa; font: 1.1rem/1.6 "Segoe UI", sans-serif; padding: 3rem; }} a {{ color: #39ff5a; }}</style>
</head>
<body>
    <p>Opening the book… If nothing happens, <a href="book/index.html">open the contents page</a>.</p>
</body>
</html>
"""


def build_offline(pages, groups, root: Path) -> None:
    book = root / "book"
    assets = book / "assets"
    assets.mkdir(parents=True)
    write_pages(pages, groups, OFFLINE, book)
    (assets / "book.css").write_text(offline_css(), encoding="utf-8", newline="\n")
    for src in [SITE / "fx.js", SITE / "logo.png", SITE / "favicon.svg", SITE / "favicon.ico", OUT / "book-logo.png"]:
        shutil.copy2(src, assets / src.name)
    licenses = assets / "font-licenses"
    licenses.mkdir()
    for src in [*(SITE / "fonts").glob("OFL-*.txt"), FONTS / "OFL-ibm-plex.txt"]:
        shutil.copy2(src, licenses / src.name)
    (root / "Read the book.html").write_text(LAUNCHER, encoding="utf-8", newline="\n")
    shutil.copy2(RELEASE_SRC / "readme.md", root / "readme.md")

    # Nothing in the download may load from the network, and every local link must land on a file in it.
    bad = []
    for f in book.glob("*.html"):
        text = f.read_text(encoding="utf-8")
        bad += [f"{f.name}: loads {m}" for m in re.findall(r'(?:src="|url\()(https?:[^")]+)', text)]
        bad += [f"{f.name}: loads {m}" for m in re.findall(r'<link [^>]*href="(https?:[^"]+)"', text)]
        for ref in re.findall(r'(?:src|href)="([^"#]+)', text):
            if ":" not in ref and not (book / ref).exists():
                bad.append(f"{f.name}: missing {ref}")
    if bad:
        sys.exit("offline edition:\n  " + "\n  ".join(sorted(set(bad))))


# ---------- the EPUB ----------

EPUB_CSS = """/* E-readers bring their own fonts and margins; this only gives the book's structure a shape. */
body { line-height: 1.5; }
h1, h2, h3 { line-height: 1.25; page-break-after: avoid; break-after: avoid; }
h1 { font-size: 1.6em; margin: 0.3em 0 1em; }
h2 { font-size: 1.25em; margin: 1.6em 0 0.5em; }
h3 { font-size: 1.05em; margin: 1.3em 0 0.4em; color: #1d6b2c; }
.kicker { font-size: 0.8em; letter-spacing: 0.12em; text-transform: uppercase; color: #1d6b2c; margin: 2em 0 0.3em; }
.part-opener .kicker { margin-top: 30%; }
.part-opener h1 { font-size: 2em; }
p { margin: 0 0 0.8em; }
blockquote { margin: 1em 0 1em 0.5em; padding-left: 1em; border-left: 3px solid #1d6b2c; font-style: italic; }
aside.note { margin: 1.2em 0; padding: 0.6em 0.9em; border: 1px solid #999; border-left: 4px solid #1d6b2c; }
.epigraph { margin: 1em 0 2.5em; padding-left: 1em; border-left: 2px solid #1d6b2c; }
.epigraph p { margin: 0.2em 0; }
dt { font-weight: bold; margin-top: 0.8em; }
dd { margin: 0.2em 0 0 1.2em; }
table { border-collapse: collapse; width: 100%; margin: 1em 0 1.4em; font-size: 0.9em; }
th, td { border: 1px solid #999; padding: 0.35em 0.5em; text-align: left; vertical-align: top; }
th { background: #e8f2ea; }
nav ol { list-style: none; padding-left: 1em; }
nav > ol { padding-left: 0; }
nav li { margin: 0.25em 0; }
.cover { margin: 0; padding: 0; text-align: center; }
.cover img { max-width: 100%; max-height: 100%; }
"""


def xhtml(title: str, body: str, cls: str = "") -> str:
    attr = f' class="{cls}"' if cls else ""
    return f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en" xml:lang="en">
<head>
<meta charset="utf-8"/>
<title>{esc(title)}</title>
<link rel="stylesheet" type="text/css" href="style.css"/>
</head>
<body{attr}>
{body}
</body>
</html>
"""


def epub_body(p: Page) -> str:
    body = re.sub(r'<a class="anchor"[^>]*>#</a>', "", p.body)
    body = re.sub(r'href="([a-z0-9-]+)\.html(#[^"]*)?"', r'href="\1.xhtml\2"', body)
    return re.sub(r"<(br|wbr|hr|img)\b([^>]*?)\s*/?>", r"<\1\2/>", body)


def epub_nav(groups) -> str:
    items = []
    for gid, label, members in groups:
        head = f'<a href="{members[0].stem}.xhtml">{esc(label)}</a>' if members[0].opener else f"<span>{esc(label)}</span>"
        subs = "".join(f'<li><a href="{p.stem}.xhtml">{esc((p.number + ". ") if p.number else "")}{esc(p.label)}</a></li>'
                       for p in members if not p.opener)
        items.append(f"<li>{head}<ol>{subs}</ol></li>")
    return xhtml("Contents", f"""<nav epub:type="toc" id="toc"><h1>Contents</h1><ol>{"".join(items)}</ol></nav>
<nav epub:type="landmarks" hidden="hidden"><ol>
<li><a epub:type="cover" href="cover.xhtml">Cover</a></li>
<li><a epub:type="toc" href="nav.xhtml">Contents</a></li>
<li><a epub:type="bodymatter" href="{groups[0][2][0].stem}.xhtml">Start reading</a></li>
</ol></nav>""")


def epub_ncx(pages, book_id: str) -> str:
    """The EPUB 2 contents, for old readers only: a flat list of the pages."""
    points = []
    for n, p in enumerate(pages, 1):
        name = f"{p.number}. {p.label}" if p.number else (f"{p.kicker}: {p.title}" if p.opener else p.label)
        points.append(f'<navPoint id="np{n}" playOrder="{n}"><navLabel><text>{esc(name)}</text></navLabel>'
                      f'<content src="{p.stem}.xhtml"/></navPoint>')
    return f"""<?xml version="1.0" encoding="utf-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
<head><meta name="dtb:uid" content="{book_id}"/><meta name="dtb:depth" content="1"/></head>
<docTitle><text>{esc(FULL_TITLE)}</text></docTitle>
<navMap>{"".join(points)}</navMap>
</ncx>
"""


def build_epub(pages, groups, target: Path) -> None:
    book_id = f"urn:uuid:{uuid.uuid5(uuid.NAMESPACE_URL, BOOK_URL)}"
    files: dict[str, str | bytes] = {"style.css": EPUB_CSS, "nav.xhtml": epub_nav(groups), "toc.ncx": epub_ncx(pages, book_id)}
    cover = RELEASE_SRC / "epub-cover.jpg"
    if cover.exists():
        files["cover.jpg"] = cover.read_bytes()
        files["cover.xhtml"] = xhtml(FULL_TITLE, f'<img src="cover.jpg" alt="{esc(FULL_TITLE)}, by Reactorcore"/>', "cover")
    else:
        print("no book/release/epub-cover.jpg yet (python tools/book_promo.py), so the EPUB has no cover")
    for p in pages:
        files[f"{p.stem}.xhtml"] = xhtml(p.label, epub_body(p))

    for name, text in files.items():
        if name.endswith((".xhtml", ".ncx")):
            try:
                ET.fromstring(text.encode("utf-8"))
            except ET.ParseError as e:
                sys.exit(f"EPUB: {name} is not well-formed XML: {e}")

    def item(name: str) -> str:
        mime = {"xhtml": "application/xhtml+xml", "css": "text/css", "jpg": "image/jpeg", "ncx": "application/x-dtbncx+xml"}
        props = {"nav.xhtml": ' properties="nav"', "cover.jpg": ' properties="cover-image"'}.get(name, "")
        return f'<item id="{re.sub(r"[^a-zA-Z0-9]", "_", "f_" + name)}" href="{name}" media-type="{mime[name.rsplit(".", 1)[1]]}"{props}/>'

    spine = (["cover.xhtml"] if "cover.xhtml" in files else []) + ["nav.xhtml"] + [f"{p.stem}.xhtml" for p in pages]
    modified = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    opf = f"""<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="book-id" xml:lang="en">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="book-id">{book_id}</dc:identifier>
<dc:title>{esc(FULL_TITLE)}</dc:title>
<dc:creator>Reactorcore</dc:creator>
<dc:publisher>Reactorcore Games</dc:publisher>
<dc:language>en</dc:language>
<dc:description>Where fun really comes from, and how to design for it on purpose: game design built on human needs, from the first idea to the finished game.</dc:description>
<dc:source>{BOOK_URL}</dc:source>
<meta property="dcterms:modified">{modified}</meta>
{'<meta name="cover" content="f_cover_jpg"/>' if "cover.jpg" in files else ""}
</metadata>
<manifest>
{chr(10).join(item(n) for n in files)}
</manifest>
<spine toc="f_toc_ncx">
{chr(10).join(f'<itemref idref="{re.sub(r"[^a-zA-Z0-9]", "_", "f_" + n)}"/>' for n in spine)}
</spine>
</package>
"""
    ET.fromstring(opf.encode("utf-8"))
    container = """<?xml version="1.0" encoding="utf-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
<rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles>
</container>
"""
    with zipfile.ZipFile(target, "w") as z:
        z.writestr(zipfile.ZipInfo("mimetype"), "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        z.writestr("META-INF/container.xml", container, compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/content.opf", opf, compress_type=zipfile.ZIP_DEFLATED)
        for name, data in files.items():
            z.writestr(f"OEBPS/{name}", data, compress_type=zipfile.ZIP_STORED if name.endswith(".jpg") else zipfile.ZIP_DEFLATED)


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
    write_pages(pages, groups, ONLINE, OUT)
    print(f"site/book/: contents + {len(pages)} pages, {sum(p.words for p in pages):,} words")


def cmd_release(args) -> None:
    pages, groups = load_all()
    check_links(pages)
    DIST.mkdir(exist_ok=True)
    root = DIST / ZIP_FOLDER
    if root.exists():
        shutil.rmtree(root)                 # dist/ is all generated
    build_offline(pages, groups, root)
    archive = DIST / f"{RELEASE_NAME}.zip"
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for f in sorted(root.rglob("*")):
            if f.is_file():
                z.write(f, f.relative_to(DIST).as_posix())
    epub = DIST / f"{RELEASE_NAME}.epub"
    build_epub(pages, groups, epub)
    for f in (archive, epub):
        print(f"{f.relative_to(REPO).as_posix()}: {f.stat().st_size / 1024:,.0f} KB")
    print(f"unzipped copy to test with: dist/{ZIP_FOLDER}/Read the book.html")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("build")
    sub.add_parser("check")
    sub.add_parser("release")
    args = ap.parse_args()
    cmd_release(args) if args.cmd == "release" else cmd_build(args)


if __name__ == "__main__":
    main()
