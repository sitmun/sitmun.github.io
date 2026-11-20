"""Fail when the built site loads a resource from another host.

The site self-hosts fonts, images and Mermaid so readers' browsers make no
third-party requests. Links to other sites are fine; resources a page loads
are not. Checked in the built site:

- HTML: src, srcset (every URL), data and poster attributes, <link> tags that
  load something (stylesheet, preload, icon...), and url() in style attributes
  and <style> blocks;
- CSS files: @import and url();
- Mermaid: every page with a diagram must load js/mermaid-local.js, or the
  theme fetches Mermaid from unpkg.com.

Usage: python .github/scripts/check_external_resources.py [site_dir] [site_host]
"""
import html.parser
import pathlib
import re
import sys

site = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "_site")
host = sys.argv[2] if len(sys.argv) > 2 else "sitmun.github.io"

LOADING_RELS = {"stylesheet", "preload", "modulepreload", "prefetch", "icon",
                "shortcut", "apple-touch-icon", "manifest"}
CSS_URL = re.compile(r"""(?:@import\s+|url\()\s*['"]?(https?:)?//([^'")\s;]+)""", re.I)


def external(url: str) -> bool:
    url = url.strip()
    if url.startswith("//"):
        url = "https:" + url
    return bool(re.match(r"https?://", url, re.I)) and not re.match(rf"https?://{re.escape(host)}(/|$)", url, re.I)


class Page(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.urls: list[str] = []
        self.in_style = False
        self.mermaid = False
        self.shim = False

    def handle_starttag(self, tag, attrs):
        a = {k: v or "" for k, v in attrs}
        for name in ("src", "data", "poster"):
            if name in a:
                self.urls.append(a[name])
        for name in ("srcset", "imagesrcset"):
            if name in a:
                self.urls += [part.strip().split(" ")[0] for part in a[name].split(",") if part.strip()]
        if tag == "link" and LOADING_RELS & set(a.get("rel", "").lower().split()):
            self.urls.append(a.get("href", ""))
        if "style" in a:
            self.urls += ["https://" + m.group(2) for m in CSS_URL.finditer(a["style"])]
        if "mermaid" in a.get("class", "").split():
            self.mermaid = True
        if tag == "script" and a.get("src", "").endswith("js/mermaid-local.js"):
            self.shim = True
        self.in_style = tag == "style"

    def handle_endtag(self, tag):
        if tag == "style":
            self.in_style = False

    def handle_data(self, data):
        if self.in_style:
            self.urls += ["https://" + m.group(2) for m in CSS_URL.finditer(data)]


found = []
for page in sorted(site.rglob("*.html")):
    parser = Page()
    parser.feed(page.read_text(encoding="utf-8"))
    for url in parser.urls:
        if external(url):
            found.append((page.relative_to(site), url))
    if parser.mermaid and not parser.shim:
        found.append((page.relative_to(site), "Mermaid from unpkg.com (js/mermaid-local.js is not loaded)"))
for sheet in sorted(site.rglob("*.css")):
    for m in CSS_URL.finditer(sheet.read_text(encoding="utf-8", errors="replace")):
        url = "https://" + m.group(2)
        if external(url):
            found.append((sheet.relative_to(site), url))

for page, url in found:
    print(f"::error file={page}::loads {url}; self-host it under docs/")
print(f"{len(found)} external resources")
sys.exit(1 if found else 0)
