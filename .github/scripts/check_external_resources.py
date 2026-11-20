"""Fail when a built page loads an image, script, frame or stylesheet from another host.

The site self-hosts fonts, images and Mermaid so readers' browsers make no
third-party requests. Links to other sites are fine; resources loaded by the
page are not.

Usage: python .github/scripts/check_external_resources.py [site_dir] [site_host]
"""
import pathlib
import re
import sys

site = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "_site")
host = sys.argv[2] if len(sys.argv) > 2 else "sitmun.github.io"

TAG = re.compile(r"<(img|script|iframe|source|audio|video|embed)\b[^>]*?\bsrcs?e?t?=\"(https?://[^\"]+)\"", re.I)
STYLE = re.compile(r"<link\b[^>]*rel=\"stylesheet\"[^>]*href=\"(https?://[^\"]+)\"", re.I)

found = []
for page in sorted(site.rglob("*.html")):
    html = page.read_text(encoding="utf-8")
    urls = [m.group(2) for m in TAG.finditer(html)] + STYLE.findall(html)
    for url in urls:
        if not re.match(rf"https?://{re.escape(host)}(/|$)", url):
            found.append((page.relative_to(site), url))

for page, url in found:
    print(f"::error file={page}::loads {url}; self-host it under docs/")
print(f"{len(found)} external resources")
sys.exit(1 if found else 0)
