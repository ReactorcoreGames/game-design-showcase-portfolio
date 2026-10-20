"""Rebuild site/sitemap.xml from site/projects.js and site/articles.js.

    python tools/sitemap.py

Run it after adding a project or an article, or after tools/book.py build. Lists the nexus, the articles catalog,
links, team-up, hire-me and AAL pages, every article page, the book's contents and chapter pages (in reading order,
from site/book/), and every project page, with URLs on the canonical GitHub Pages address.
"""
import re
from pathlib import Path
from urllib.parse import quote

REPO = Path(__file__).resolve().parent.parent
SITE = REPO / "site"
BASE = "https://reactorcoregames.github.io/game-design-showcase-portfolio/"


def book_pages() -> list[str]:
    """site/book/ in reading order: follow the rel="next" links from the contents page."""
    pages, page = [], "index.html"
    while page and (SITE / "book" / page).exists():
        pages.append(page)
        m = re.search(r'<link rel="next" href="([^"]+)">', (SITE / "book" / page).read_text(encoding="utf-8"))
        page = m[1] if m and m[1] not in pages else None
    built = {p.name for p in (SITE / "book").glob("*.html")}
    if built - set(pages):
        raise SystemExit("site/book/ has pages outside the reading chain (run tools/book.py build): "
                         + ", ".join(sorted(built - set(pages))))
    return pages


def main() -> None:
    data = (SITE / "projects.js").read_text(encoding="utf-8")
    pages = re.findall(r'\bpage:\s*"([^"]+)"', data)
    missing = [p for p in pages if not (SITE / "projects" / p).exists()]
    if missing:
        raise SystemExit("projects.js lists pages that don't exist: " + ", ".join(missing))

    articles = re.findall(r'\bslug:\s*"([^"]+)"', (SITE / "articles.js").read_text(encoding="utf-8"))
    missing = [a for a in articles if not (SITE / "articles" / f"{a}.html").exists()]
    if missing:
        raise SystemExit("articles.js lists articles without a page (run tools/articles.py build): " + ", ".join(missing))

    urls = [BASE, BASE + "articles.html", BASE + "links.html", BASE + "work-with-me/", BASE + "hire_me/hire_me.html", BASE + "aal/"]
    urls += [BASE + f"articles/{a}.html" for a in articles]
    urls += [BASE + "book/" + (p if p != "index.html" else "") for p in book_pages()]
    urls += [BASE + "projects/" + quote(p) for p in pages]
    body = "\n".join(f"  <url><loc>{u}</loc></url>" for u in urls)
    xml = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}\n</urlset>\n'
    (SITE / "sitemap.xml").write_text(xml, encoding="utf-8", newline="\n")
    print(f"site/sitemap.xml: {len(urls)} URLs ({len(articles)} articles, {len(book_pages())} book pages, {len(pages)} projects)")


if __name__ == "__main__":
    main()
