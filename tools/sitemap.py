"""Rebuild site/sitemap.xml from site/projects.js.

    python tools/sitemap.py

Run it after adding a project entry. Lists the nexus, the articles, links, team-up and hire-me pages and every
project page, with URLs on the canonical GitHub Pages address.
"""
import re
from pathlib import Path
from urllib.parse import quote

REPO = Path(__file__).resolve().parent.parent
SITE = REPO / "site"
BASE = "https://reactorcoregames.github.io/game-design-showcase-portfolio/"


def main() -> None:
    data = (SITE / "projects.js").read_text(encoding="utf-8")
    pages = re.findall(r'\bpage:\s*"([^"]+)"', data)
    missing = [p for p in pages if not (SITE / "projects" / p).exists()]
    if missing:
        raise SystemExit("projects.js lists pages that don't exist: " + ", ".join(missing))

    urls = [BASE, BASE + "articles.html", BASE + "links.html", BASE + "work-with-me/", BASE + "hire_me/hire_me.html"]
    urls += [BASE + "projects/" + quote(p) for p in pages]
    body = "\n".join(f"  <url><loc>{u}</loc></url>" for u in urls)
    xml = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}\n</urlset>\n'
    (SITE / "sitemap.xml").write_text(xml, encoding="utf-8", newline="\n")
    print(f"site/sitemap.xml: {len(urls)} URLs ({len(pages)} projects)")


if __name__ == "__main__":
    main()
