"""Fail when a page links to another page by climbing two or more folders.

A link such as ../../../que-es-sitmun/plataforma/arquitectura/api.md#x depends
on where both pages sit, so moving either one breaks it, and writing it means
counting folders. Link to the heading instead with autorefs, [text][x], after
giving that heading a fixed id ({#x}); the strict build fails when the id does
not exist. Links to the same folder, a subfolder, or one folder up stay
relative. Links to images and other files are not checked: autorefs only
points to headings.

Usage: python .github/scripts/check_deep_links.py [docs_dir]
"""
import pathlib
import re
import sys

docs = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "docs")
FENCE = re.compile(r"^\s*(```|~~~)")
CODE = re.compile(r"`[^`]*`")
INLINE = re.compile(r"(?<!!)\]\(([^)\s]+)")
REFDEF = re.compile(r"^\s*\[[^\]]+\]:\s*(\S+)")
DEEP = re.compile(r"^(\.\./){2,}[^#]*\.md(#|$)")

errors = 0
for page in sorted(docs.rglob("*.md")):
    in_fence = False
    for number, line in enumerate(page.read_text(encoding="utf-8").splitlines(), 1):
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        text = CODE.sub("", line)
        targets = INLINE.findall(text) + REFDEF.findall(text)
        for target in targets:
            if DEEP.match(target):
                errors += 1
                print(f"::error file={page},line={number}::{target} climbs two or more folders; "
                      "give the target heading a fixed id ({#id}) and link with [text][id]")
print(f"{errors} links climb two or more folders")
sys.exit(1 if errors else 0)
