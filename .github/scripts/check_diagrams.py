"""Fail when a PlantUML diagram did not render.

plantuml-markdown renders diagrams through a remote server at build time. When
the server cannot be reached it writes an error in place of the diagram and the
build still succeeds, even with --strict. This check compares the number of
```plantuml blocks in docs/ with the rendered diagrams in the built site.

Usage: python .github/scripts/check_diagrams.py [docs_dir] [site_dir]
"""
import pathlib
import re
import sys

docs = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "docs")
site = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else "_site")

expected = sum(
    len(re.findall(r"^```plantuml\b", p.read_text(encoding="utf-8"), re.M))
    for p in docs.rglob("*.md")
)
rendered = 0
errors = []
for page in site.rglob("*.html"):
    html = page.read_text(encoding="utf-8")
    rendered += len(re.findall(r'<img[^>]*class="uml"', html))
    if "[uml directive]" in html:
        errors.append(str(page.relative_to(site)))

for page in errors:
    print(f"::error file={page}::PlantUML diagram failed to render")
print(f"PlantUML diagrams: {rendered} rendered, {expected} expected")
if errors or rendered != expected:
    sys.exit(1)
