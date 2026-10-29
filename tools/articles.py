"""Move the game design articles off Google Docs and onto the site.

The sources are Google Docs "Web page (.html, zipped)" exports in assets/gd articles raw/ (gitignored),
or, for articles written straight for the site, a hand-written HTML fragment in articles-src/ ("native").
site/articles.js is the catalog: titles, summaries, shelves and order all come from there, and every
entry with a slug in SOURCES below gets a page.

    python tools/articles.py build [slug ...]   unzip, clean up, write site/articles/<slug>.html + images
    python tools/articles.py list               show each catalog entry, its source zip and its page

No slug given = every article in SOURCES. A build also writes the reading time back into articles.js.

What the cleanup does: drops the Google Docs title block (the page has its own), lifts the "Summary:"
section into the page's intro panel, replaces the shared Patreon/Discord "Closing words" with the
template's closing panel, unwraps google.com/url redirects, points links to other articles' Google
Docs at their pages here, rebuilds nested lists, and keeps only bold, italic and superscript.
Images are resized to at most 800 px wide (or twice their width in the doc, if smaller) and
re-encoded as WebP into site/articles/images/<slug>/.

A native source is the finished article: an "In short" part, a line <!-- body -->, then the body, in the
same HTML the cleanup produces (h2s with ids, p, ul/ol, figure). Its images are made by hand into
site/articles/images/<slug>/ and are left alone by the build.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import zipfile
from pathlib import Path
from string import Template
from urllib.parse import parse_qs, urlparse

from bs4 import BeautifulSoup, NavigableString, Tag
from PIL import Image, ImageSequence

REPO = Path(__file__).resolve().parent.parent
SITE = REPO / "site"
OUT = SITE / "articles"
RAW = REPO / "assets" / "gd articles raw"
NATIVE = REPO / "articles-src"
WORK = REPO / "_work" / "articles"
CATALOG = SITE / "articles.js"
BASE = "https://reactorcoregames.github.io/game-design-showcase-portfolio/"

MAX_WIDTH = 800
WEBP_QUALITY = 70
WORDS_PER_MINUTE = 230
TOC_MIN_HEADINGS = 4

# slug -> source zip (without .zip) in assets/gd articles raw/
SOURCES = {
    "games-are-need-satisfiers": "Games are need satisfiers",
    "where-does-meaning-come-from": "Where Does Meaning or Motivation Come From In a Video Game How To Make a Game Worth Playing ",
    "throwaway-games-are-a-band-aid": "Throwaway games are band-aid approach",
    "future-of-games": "Future of games, the next big innovation",
    "infinite-metagame-pacing-difficulty-progression": "How To Set Up Pacing, Difficulty, And Progression Within An Infinite Metagame",
    "player-run-services": "How To Contextualize Narrative Within Infinite Metagames Player-Run Services",
    "additive-vs-multiplicative-content": "Additive vs Multiplicative Game Content And Why The Latter Is Better",
    "what-is-a-game-designer": "What Really Is a Game Designer And How To Master This Skill",
    "getting-started-in-game-development": "How To Get Started As A Complete Beginner In Game Development",
    "how-to-grow-as-a-game-designer": "How To Grow As A Game Designer. My Story and My Biggest Epiphanies",
    "evolution-of-a-game-designer": "Evolution of a Game Designer - Short 12 Steps Outline",
    "scope-creep-is-not-an-enemy": "Scope Creep Is Not An Enemy, You're Just Incompetent and Inexperienced",
    "forking-drives-innovation": "Forking Drives Innovation, Not Competition",
    "why-i-dont-play-competitive-games": "Why I Don't Play Competitive Human Vs Human Games Anymore",
    "universe-life-and-death-1": "My View On The Universe, Life And Death Pt1",
    "universe-life-and-death-2": "My View On The Universe, Life And Death Pt2",
    "ad-circus": {"native": "ad-circus.html", "written": "October 2026"},
    # C2. Options (all optional), matched against a block's text from its start:
    #   start      the first block kept (default: the first heading); blocks before it are dropped
    #   stop       the block where the article ends (not included)
    #   drop       paragraphs to leave out
    #   intro      paragraphs that go into the "In short" panel (default: the doc's "Summary:" section)
    #   skip       headings whose whole section is left out, up to the next heading at the same level
    #   strip      regex removed from heading texts
    #   shift      added to the doc's heading level (default 1: doc h1 -> page h2)
    #   toc_depth  3 to list h3s under their h2 in the contents
    #   links      heading -> page: a "See the showcase page" link under that heading
    #   written    shown in the header, for articles that are a snapshot of their time
    #   guest      guest-article header: author, author_url, site, published, note
    #   native     a hand-written source in articles-src/ instead of a zip (see the top of this file)
    "reactorcores-big-projects": {
        "zip": "!Reactorcore's Big Projects",
        "start": "General Design Tenets",
        "stop": "END OF DOCUMENT",
        "skip": ["Working Name: Sexy Neuromancy Sessions"],
        "strip": r"^Working Name:\s*",
        "toc_depth": 3,
        "links": {
            "Working Name: AAL:Superweapon": "../projects/AALSuperweapon.html",
            "Working Name: Admiral Wars Beyond": "../projects/admiralwars.html",
            "Working Name: Astro Industry Freelancer": "../projects/astro_industry.html",
        },
        "written": "January 2024",
    },
    "astroneer-8th-planet": {
        "zip": "Astroneer - 8th Planet Infinite Metagame Concept (Illustrated)",
        "start": "Document by",
        "drop": ["Document by"],
        "intro": ["Original proposal to Astroneer", "It was tailored around"],
        "stop": "Since I wrote this doc",
        "shift": 0,
    },
    "exploitative-game-design": {
        "zip": "GUEST Exploitative Game Design Beyond the F2P Debate",
        "start": "Ethics matter in game design",
        "intro": ["Ethics matter in game design"],
        "drop": ["Edward McNeill, Blogger", "August 9, 2013", "20 Min Read"],
        "shift": 0,
        "guest": {
            "author": "Edward McNeill", "author_url": "https://www.gamedeveloper.com/author/edward-mcneill",
            "site": "Game Developer (then Gamasutra)", "published": "9 August 2013",
            "note": "It's too good to vanish, so I'm keeping a copy here in case the original is lost or its site closes down. I gave it some extra love with fitting AI images to make it more fun to read.",
        },
    },
    "loopholes-in-game-design": {
        "zip": "GUEST Loopholes in Game Design",
        "start": "7 May, 2012",
        "drop": ["7 May, 2012"],
        "shift": 0,
        "guest": {
            "author": "Julian Pritchard", "author_url": "http://devmag.org.za/author/julian/",
            "site": "Devmag", "published": "7 May 2012",
            "note": "Devmag is an old site, and old sites tend to vanish, sometimes taking gems like this one with them for good. I'm keeping a copy here because it's universally useful.",
        },
    },
}

# The "Closing words" every article shared, recognised by its opening; the template's closing panel replaces it.
BOILERPLATE_CLOSING = "My hope is to spark your mind to see beyond what is currently available."
SEPARATORS = {"–", "-", "—", "--"}


def source(slug: str) -> dict:
    s = SOURCES[slug]
    return {"zip": s} if isinstance(s, str) else s


# ---------- catalog ----------

def read_catalog() -> tuple[list[dict], list[dict]]:
    """SHELVES and ARTICLES from articles.js, in order."""
    js = CATALOG.read_text(encoding="utf-8")
    shelves = [dict(id=m[0], label=json.loads(m[1]), note=json.loads(m[2]))
               for m in re.findall(r'\{ id: "(\w+)", label: ("(?:[^"\\]|\\.)*"), note: ("(?:[^"\\]|\\.)*") \}', js)]
    block = js[js.index("window.ARTICLES"):]
    articles = []
    for body in re.findall(r"\n  \{(.*?)\n  \}", block, re.S):
        entry = {}
        for key, val in re.findall(r'(\w+):\s*("(?:[^"\\]|\\.)*"|true|false|\d+|GDOC\("[^"]+"\))', body):
            if val.startswith("GDOC"):
                entry[key] = "https://docs.google.com/document/d/" + val[6:-2]
            else:
                entry[key] = json.loads(val)
        articles.append(entry)
    return shelves, articles


def write_minutes(slug: str, minutes: int) -> None:
    js = CATALOG.read_text(encoding="utf-8")
    entry = re.search(r"\n  \{(?:(?!\n  \}).)*?slug: \"" + re.escape(slug) + r"\".*?\n  \}", js, re.S)
    if not entry:
        sys.exit(f"{slug}: not in articles.js")
    new = re.sub(r"minutes: \d+", f"minutes: {minutes}", entry[0], count=1)
    CATALOG.write_text(js.replace(entry[0], new), encoding="utf-8", newline="\n")


# ---------- Google Docs HTML -> clean HTML ----------

def class_formats(doc_html: str) -> dict[str, set[str]]:
    """Google Docs puts formatting in generated classes (.c7{font-weight:700}); map each to strong/em/sup."""
    formats: dict[str, set[str]] = {}
    for name, rules in re.findall(r"\.(c\d+)\{([^}]*)\}", doc_html):
        f = set()
        if "font-weight:700" in rules:
            f.add("strong")
        if "font-style:italic" in rules:
            f.add("em")
        if "vertical-align:super" in rules:
            f.add("sup")
        if f:
            formats[name] = f
    return formats


def unwrap_href(href: str) -> str:
    if href.startswith("https://www.google.com/url?"):
        href = parse_qs(urlparse(href).query).get("q", [href])[0]
    return href


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:60] or "section"


def text_of(node: Tag) -> str:
    return re.sub(r"\s+", " ", node.get_text().replace("\xa0", " ")).strip()


class Converter:
    def __init__(self, slug: str, doc_html: str, doc_dir: Path, doc_links: dict[str, str], opts: dict):
        self.slug = slug
        self.doc_dir = doc_dir
        self.doc_links = doc_links          # Google Doc id -> local page, for links between articles
        self.opts = opts                    # this article's options from SOURCES
        self.formats = class_formats(doc_html)
        self.soup = BeautifulSoup(doc_html, "html.parser")
        self.images: dict[str, tuple[str, int, int]] = {}   # source name -> (file, width, height)
        self.ids: set[str] = set()
        self.headings: list[tuple[int, str, str]] = []     # (level, id, text) of h2s and h3s, for the contents list
        self.words = 0

    def matches(self, node: Tag, key: str) -> bool:
        """Does the block's text start with one of the option's markers?"""
        markers = self.opts.get(key, [])
        markers = [markers] if isinstance(markers, str) else markers
        text = text_of(node)
        return any(text.startswith(m) for m in markers)

    # inline

    def inline(self, node) -> str:
        if isinstance(node, NavigableString):
            text = str(node).replace("\xa0", " ")
            self.words += len(text.split())
            return html.escape(text, quote=False)
        if not isinstance(node, Tag):
            return ""
        if node.name == "br":
            return "<br>"
        if node.name == "img":
            return ""
        inner = "".join(self.inline(c) for c in node.children)
        if node.name == "a" and node.get("href"):
            href = self.link(node["href"])
            external = href.startswith("http")
            attrs = ' target="_blank" rel="noopener"' if external else ""
            return f'<a href="{html.escape(href)}"{attrs}>{inner}</a>'
        for fmt in ("sup", "em", "strong"):
            if fmt in self.fmt(node) and inner.strip():
                lead = inner[: len(inner) - len(inner.lstrip())]
                trail = inner[len(inner.rstrip()):]
                inner = f"{lead}<{fmt}>{inner.strip()}</{fmt}>{trail}"
        return inner

    def fmt(self, node: Tag) -> set[str]:
        out: set[str] = set()
        for c in node.get("class", []):
            out |= self.formats.get(c, set())
        return out

    def link(self, href: str) -> str:
        href = unwrap_href(href)
        m = re.match(r"https://docs\.google\.com/document/d/([\w-]+)", href)
        if m and m[1] in self.doc_links:
            return self.doc_links[m[1]]
        return href

    def clean_inline(self, s: str) -> str:
        s = re.sub(r"</(strong|em|sup)>(\s*)<\1>", r"\2", s)       # merge split runs: <strong>a</strong><strong>b</strong>
        s = re.sub(r"^(\s|<br>)+|(\s|<br>)+$", "", s)
        return re.sub(r"[ \t]{2,}", " ", s)

    # blocks

    def figure(self, img: Tag) -> str:
        src = img.get("src", "")
        box = img.parent if img.parent and img.parent.name == "span" else img
        m = re.search(r"width:\s*([\d.]+)px", box.get("style", ""))
        shown = round(float(m[1])) if m else MAX_WIDTH
        file, w, h = self.image(src, shown)
        alt = html.escape(img.get("alt", "") or img.get("title", ""))
        loading = "" if len(self.images) == 1 else ' loading="lazy"'
        narrow = f' class="narrow" style="max-width: {shown}px"' if shown < 560 else ""
        return f'<figure{narrow}><img src="images/{self.slug}/{file}" alt="{alt}" width="{w}" height="{h}"{loading} decoding="async"></figure>'

    def image(self, src: str, shown: int) -> tuple[str, int, int]:
        if src in self.images:
            return self.images[src]
        n = len(self.images) + 1
        im = Image.open(self.doc_dir / src)
        target = min(im.width, MAX_WIDTH, max(shown * 2, 400))
        scale = target / im.width
        size = (round(im.width * scale), round(im.height * scale))
        out_dir = OUT / "images" / self.slug
        out_dir.mkdir(parents=True, exist_ok=True)
        file = f"{n:02d}.webp"
        if getattr(im, "is_animated", False):
            frames, durations = [], []
            for frame in ImageSequence.Iterator(im):
                frames.append(frame.convert("RGBA").resize(size, Image.LANCZOS))
                durations.append(frame.info.get("duration", 100))
            frames[0].save(out_dir / file, "WEBP", save_all=True, append_images=frames[1:], duration=durations,
                           loop=0, quality=WEBP_QUALITY - 6, method=6)
        else:
            alpha = im.mode in ("RGBA", "LA") or (im.mode == "P" and "transparency" in im.info)
            im = im.convert("RGBA" if alpha else "RGB")
            if size != im.size:
                im = im.resize(size, Image.LANCZOS)
            im.save(out_dir / file, "WEBP", quality=WEBP_QUALITY, method=6)
        self.images[src] = (file, *size)
        return self.images[src]

    def paragraph(self, p: Tag) -> list[str]:
        """A paragraph, split around any images in it (each image becomes its own figure)."""
        out, run = [], []

        def flush():
            s = self.clean_inline("".join(run))
            if re.sub(r"<br>|\s", "", s) and s.strip() not in SEPARATORS:
                out.append(f"<p>{s}</p>")
            run.clear()

        for child in p.children:
            imgs = child.find_all("img") if isinstance(child, Tag) else []
            if child.name == "img" or imgs:
                flush()
                out.extend(self.figure(i) for i in ([child] if child.name == "img" else imgs))
            else:
                run.append(self.inline(child))
        flush()
        return out

    def heading(self, h: Tag) -> str | None:
        text = text_of(h)
        if not text:
            return None
        link = next((page for marker, page in self.opts.get("links", {}).items() if text.startswith(marker)), None)
        text = re.sub(r"\s*[:.]$", "", text)
        if self.opts.get("strip"):
            text = re.sub(self.opts["strip"], "", text)
        level = max(2, min(int(h.name[1]) + self.opts.get("shift", 1), 6))
        hid = base = slugify(text)
        n = 2
        while hid in self.ids:
            hid, n = f"{base}-{n}", n + 1
        self.ids.add(hid)
        if level == 2 or (level == 3 and self.opts.get("toc_depth") == 3):
            self.headings.append((level, hid, text))
        self.words += len(text.split())
        out = f'<h{level} id="{hid}">{html.escape(text, quote=False)}</h{level}>'
        if link:
            out += f'\n<p class="see-page"><a class="btn btn-sm" href="{html.escape(link)}">See the showcase page →</a></p>'
        return out

    def lists(self, run: list[Tag]) -> str:
        """Google Docs writes each list level as its own flat <ul>/<ol> (class lst-kix_<id>-<level>).
        Rebuild them into one nested list."""
        root: list = []          # a list of nodes: {"tag", "start", "items": [{"html", "children": [...]}]}
        stack: list[tuple[int, dict]] = []
        for el in run:
            m = re.search(r"lst-kix_\w+-(\d)", " ".join(el.get("class", [])))
            level = int(m[1]) if m else 0
            while stack and stack[-1][0] > level:
                stack.pop()
            if stack and stack[-1][0] == level and stack[-1][1]["tag"] == el.name and "start" not in el.get("class", []):
                node = stack[-1][1]
            else:
                if stack and stack[-1][0] == level:
                    stack.pop()
                node = {"tag": el.name, "start": el.get("start"), "items": []}
                if stack and stack[-1][1]["items"]:
                    stack[-1][1]["items"][-1]["children"].append(node)
                else:
                    root.append(node)
                stack.append((level, node))
            for li in el.find_all("li", recursive=False):
                node["items"].append({"html": self.clean_inline("".join(self.inline(c) for c in li.children)), "children": []})

        def render(node: dict) -> str:
            start = f' start="{node["start"]}"' if node["tag"] == "ol" and node["start"] not in (None, "1") else ""
            items = "".join(f"<li>{i['html']}{''.join(render(c) for c in i['children'])}</li>" for i in node["items"])
            return f"<{node['tag']}{start}>{items}</{node['tag']}>"

        return "\n".join(render(n) for n in root)

    def convert(self) -> dict:
        body = self.soup.body
        blocks = [b for b in body.children if isinstance(b, Tag)]
        summary: list[str] = []
        content: list[str] = []
        mode = "intro"           # intro (title block) -> summary -> body
        skip_level = 0           # inside a skipped section: the level of its heading
        if self.opts.get("start"):
            first = next((n for n, b in enumerate(blocks) if self.matches(b, "start")), None)
            if first is None:
                sys.exit(f"{self.slug}: start marker not found")
            blocks, mode = blocks[first:], "body"
        i = 0
        while i < len(blocks):
            b = blocks[i]
            is_heading = b.name in ("h1", "h2", "h3", "h4", "h5", "h6")
            if self.matches(b, "stop"):
                break
            if is_heading and skip_level and int(b.name[1]) <= skip_level:
                skip_level = 0
            if is_heading and self.matches(b, "skip"):
                skip_level = int(b.name[1])
            if skip_level or self.matches(b, "drop"):
                i += 1
                continue
            if b.name == "p" and self.matches(b, "intro"):
                summary.extend(self.paragraph(b))
            elif is_heading:
                title = text_of(b).rstrip(":").strip().lower()
                if title == "summary" and mode == "intro":
                    mode = "summary"
                    i += 1
                    continue
                if title == "closing words":
                    rest = " ".join(text_of(x) for x in blocks[i + 1:]).strip()
                    if rest.startswith(BOILERPLATE_CLOSING):
                        break
                mode = "body"
                h = self.heading(b)
                if h:
                    content.append(h)
            elif mode == "intro":
                pass
            elif b.name in ("ul", "ol"):
                run = []
                while i < len(blocks) and blocks[i].name in ("ul", "ol"):
                    run.append(blocks[i])
                    i += 1
                (summary if mode == "summary" else content).append(self.lists(run))
                continue
            elif b.name == "p":
                if mode == "summary" and text_of(b) in SEPARATORS:
                    mode = "body"
                else:
                    (summary if mode == "summary" else content).extend(self.paragraph(b))
            elif b.name == "hr":
                if content:
                    content.append("<hr>")
            else:
                print(f"  {self.slug}: skipped a <{b.name}> block")
            i += 1
        body = "\n".join(content)
        # An italic "(...)" paragraph right under an image is its caption.
        body = re.sub(r"(<figure[^>]*><img [^>]*>)</figure>\n<p><em>\((.*?)\)</em></p>", r"\1<figcaption>\2</figcaption></figure>", body)
        return {"summary": "\n".join(summary), "body": body}


class Native:
    """A hand-written article: already clean HTML, so only split it and collect what the page needs."""

    def __init__(self, path: Path):
        if not path.exists():
            sys.exit(f"missing source {path}")
        self.text = path.read_text(encoding="utf-8")
        self.images = re.findall(r"<img ", self.text)
        self.headings = [(2, hid, html.unescape(re.sub(r"<[^>]+>", "", t)))
                         for hid, t in re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', self.text)]
        self.words = len(re.sub(r"<!--.*?-->|<[^>]+>", " ", self.text).split())

    def convert(self) -> dict:
        if "<!-- body -->" not in self.text:
            sys.exit("native source needs a <!-- body --> line between the summary and the body")
        summary, body = self.text.split("<!-- body -->", 1)
        return {"summary": summary.strip(), "body": body.strip()}


# ---------- page ----------

PAGE = Template((Path(__file__).parent / "article_template.html").read_text(encoding="utf-8"))


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def build(slug: str, shelves: list[dict], articles: list[dict]) -> None:
    entry = next((a for a in articles if a.get("slug") == slug), None)
    if not entry:
        sys.exit(f"{slug}: no articles.js entry with this slug")
    opts = source(slug)

    doc_links = {}
    for a in articles:
        m = re.search(r"/document/d/([\w-]+)", a.get("original", ""))
        if m and a.get("slug") in SOURCES:
            doc_links[m[1]] = f"{a['slug']}.html"

    img_dir = OUT / "images" / slug
    if opts.get("native"):
        conv = Native(NATIVE / opts["native"])
    else:
        zpath = RAW / f"{opts['zip']}.zip"
        if not zpath.exists():
            sys.exit(f"{slug}: missing source {zpath}")
        work = WORK / slug
        with zipfile.ZipFile(zpath) as z:
            z.extractall(work)
        doc = next(work.glob("*.html"))
        for old in img_dir.glob("*.webp") if img_dir.exists() else []:
            old.unlink()                    # generated files only; rebuilt below
        conv = Converter(slug, doc.read_text(encoding="utf-8"), doc.parent, doc_links, opts)
    parts = conv.convert()
    minutes = max(1, round(conv.words / WORDS_PER_MINUTE))

    shelf = next(s for s in shelves if s["id"] == entry["shelf"])
    built = [a for a in articles if a.get("slug") in SOURCES]
    idx = built.index(entry)
    prev_a = built[idx - 1] if idx > 0 else None
    next_a = built[idx + 1] if idx + 1 < len(built) else None

    def neighbour(a: dict | None, label: str, cls: str) -> str:
        if not a:
            return f'<span class="pager-gap {cls}"></span>'
        return (f'<a class="pager-link {cls}" href="{a["slug"]}.html"><span class="label">{label}</span>'
                f'<span class="pager-title">{esc(a["title"])}</span></a>')

    toc = ""
    if len(conv.headings) >= TOC_MIN_HEADINGS:
        items = []
        for level, hid, text in conv.headings:
            link = f'<a href="#{hid}">{esc(text)}</a>'
            if level == 3 and items:
                items[-1][1].append(f"<li>{link}</li>")
            else:
                items.append((link, []))
        lis = "".join(f'<li>{link}{"<ol>" + "".join(subs) + "</ol>" if subs else ""}</li>' for link, subs in items)
        toc = f'<nav class="toc" aria-labelledby="toc-title"><p class="label" id="toc-title">In this article</p><ol>{lis}</ol></nav>'

    summary = ""
    if parts["summary"]:
        summary = f'<div class="summary panel bracketed"><p class="label">In short</p>{parts["summary"]}</div>'

    guest = opts.get("guest")
    original, byline, guest_panel = "", "<span>By Reactorcore</span>", ""
    if entry.get("original"):
        where = f"Original on {guest['site'].split(' (')[0]}" if guest else "Original Google Doc"
        original = f'<span><a href="{esc(entry["original"])}" target="_blank" rel="noopener">{where} ↗</a></span>'
    if guest:
        author = f'<a href="{esc(guest["author_url"])}" target="_blank" rel="noopener">{esc(guest["author"])}</a>'
        byline = f"<span>Guest article by {author}</span>"
        guest_panel = (
            f'<div class="guest panel"><p class="label">Guest article</p>'
            f'<p>Written by {author} and first published on <a href="{esc(entry["original"])}" target="_blank" rel="noopener">'
            f'{esc(guest["site"])}</a> on {esc(guest["published"])}. Reposted here with the author\'s permission; '
            f'the original is worth a visit too.</p>'
            f'<p class="guest-note"><strong>Why it\'s here:</strong> {esc(guest["note"])} <span class="faint">— Reactorcore</span></p></div>')
    written = f'<span>Written {esc(opts["written"])}</span>' if opts.get("written") else ""

    url = f"{BASE}articles/{slug}.html"
    page = PAGE.substitute(
        title=esc(entry["title"]),
        title_json=json.dumps(entry["title"], ensure_ascii=False),
        author_json=json.dumps(guest["author"] if guest else "Reactorcore", ensure_ascii=False),
        byline=byline,
        written=written,
        guest=guest_panel,
        description=esc(entry["summary"]),
        url=url,
        shelf_id=shelf["id"],
        shelf_label=esc(shelf["label"]),
        minutes=minutes,
        original=original,
        summary=summary,
        toc=toc,
        body=parts["body"],
        prev=neighbour(prev_a, "← Previous", "prev"),
        next=neighbour(next_a, "Next →", "next"),
    )
    (OUT / f"{slug}.html").write_text(page, encoding="utf-8", newline="\n")
    if entry.get("minutes") != minutes:
        write_minutes(slug, minutes)
    size = sum(p.stat().st_size for p in img_dir.glob("*")) if img_dir.exists() else 0
    print(f"{slug}: {conv.words} words, {minutes} min, {len(conv.images)} images, {size / 1e6:.1f} MB")


def cmd_build(args) -> None:
    shelves, articles = read_catalog()
    slugs = args.slugs or list(SOURCES)
    unknown = [s for s in slugs if s not in SOURCES]
    if unknown:
        sys.exit("not in SOURCES: " + ", ".join(unknown))
    OUT.mkdir(exist_ok=True)
    for slug in slugs:
        build(slug, shelves, articles)
    total = sum(p.stat().st_size for p in OUT.rglob("*") if p.is_file())
    print(f"site/articles/: {total / 1e6:.1f} MB in total")


def cmd_list(args) -> None:
    _, articles = read_catalog()
    for a in articles:
        slug = a.get("slug", "")
        opts = source(slug) if slug in SOURCES else {}
        path = NATIVE / opts["native"] if "native" in opts else RAW / f"{opts.get('zip')}.zip"
        src = "source ok" if opts and path.exists() else "no source"
        page = "page ok" if slug and (OUT / f"{slug}.html").exists() else "no page"
        print(f"{slug or '(no slug)':50} {src:10} {page:8} {a['title']}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("build")
    p.add_argument("slugs", nargs="*")
    p.set_defaults(func=cmd_build)
    p = sub.add_parser("list")
    p.set_defaults(func=cmd_list)
    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
