"""Check that every note about a known SITMUN bug points to its issue.

A known bug is written as an admonition of type `bug`:

    !!! bug "Error conocido de SITMUN 1.3.0: <qué pasa> (sitmun/sitmun#NNN)"
        ... Seguimiento: [sitmun/sitmun#NNN](https://github.com/sitmun/sitmun/issues/NNN).

The title names the version and the issue, and the body links that issue, so the
note can be removed when the issue is fixed (check_issue_notes.py reports closed
issues every week). This fails when:
- a `bug` note has another title shape, or its body does not link its issue;
- a warning or note about a SITMUN version cites a sitmun/sitmun issue, or its title speaks of a
  known problem or error (it should be a `bug` note).

Usage: python .github/scripts/check_bug_notes.py [docs_dir]
"""
import pathlib
import re
import sys

docs = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "docs")
OPEN = re.compile(r'^(\s*)!!! (\w+)\s+"([^"]*)"\s*$')
TITLE = re.compile(r"^Error conocido de SITMUN \d+\.\d+\.\d+: .+ \(sitmun/sitmun#(\d+)\)$")
ISSUE = re.compile(r"(?:sitmun/sitmun#|github\.com/sitmun/sitmun/issues/)(\d+)")

errors = 0
notes = 0
for page in sorted(docs.rglob("*.md")):
    lines = page.read_text(encoding="utf-8").split("\n")
    for number, line in enumerate(lines, 1):
        match = OPEN.match(line)
        if not match:
            continue
        indent, kind, title = len(match.group(1)), match.group(2), match.group(3)
        body = []
        for following in lines[number:]:
            if following.strip() and len(following) - len(following.lstrip()) <= indent:
                break
            body.append(following)
        text = "\n".join(body)
        if kind == "bug":
            notes += 1
            shape = TITLE.match(title)
            if not shape:
                print(f'::error file={page},line={number}::bug note title must be '
                      f'"Error conocido de SITMUN X.Y.Z: ... (sitmun/sitmun#NNN)"')
                errors += 1
            elif f"github.com/sitmun/sitmun/issues/{shape.group(1)}" not in text:
                print(f"::error file={page},line={number}::bug note must link "
                      f"https://github.com/sitmun/sitmun/issues/{shape.group(1)} in its text")
                errors += 1
        elif re.search(r"(?i)conocid|\berror\b|problema", title) or (
                re.search(r"SITMUN \d+\.\d+|\d+\.\d+\.\d+", title) and ISSUE.search(text)):
            print(f"::error file={page},line={number}::this note is about a known bug; "
                  f"write it as a `!!! bug` note that links its issue")
            errors += 1

print(f"{notes} bug notes checked, {errors} errors")
sys.exit(1 if errors else 0)
