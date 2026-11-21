"""Fail when a page of the site links to a redirect stub.

A redirect stub exists so that old links from outside keep working. A link
inside the site that lands on one means the linking page was written for a
page that has moved or been merged, so its context may be stale: link to the
current page instead, and check that the surrounding text still fits.

Usage: python .github/scripts/check_redirect_links.py [site_dir]
"""
import html.parser
import pathlib
import sys
import urllib.parse

site = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve()
STUB_MARK = "var anchor=window.location.hash"


def is_stub(path: pathlib.Path) -> bool:
    return STUB_MARK in path.read_text(encoding="utf-8", errors="ignore")


class Links(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            href = dict(attrs).get("href")
            if href:
                self.hrefs.append(href)


stubs = {p for p in site.rglob("*.html") if is_stub(p)}
problems = []
for page in sorted(site.rglob("*.html")):
    if page in stubs or page.name == "404.html":
        continue
    parser = Links()
    parser.feed(page.read_text(encoding="utf-8", errors="ignore"))
    for href in parser.hrefs:
        url = urllib.parse.urlsplit(href)
        if url.scheme or url.netloc or not url.path:
            continue
        target = (page.parent / urllib.parse.unquote(url.path)).resolve()
        if target.is_dir() or url.path.endswith("/"):
            target = target / "index.html"
        if target in stubs:
            problems.append((page.relative_to(site), href))

for page, href in problems:
    print(f"::error file={page}::links to the redirect stub {href}; link to the current page and check the context")
print(f"{len(stubs)} redirect stubs, {len(problems)} links to them")
sys.exit(1 if problems else 0)
