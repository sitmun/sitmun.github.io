"""Report the sitmun/sitmun issues cited in the docs that have been closed.

The docs carry notes about SITMUN bugs, each linked to its issue
(sitmun/sitmun#NNN or https://github.com/sitmun/sitmun/issues/NNN). When an
issue is closed, its note may need updating or removing. This lists the pages
that cite closed issues and exits 1 if there are any, except the issues listed
in .github/issue-notes-accepted.txt (closed, but the fix is not released yet
and the note already says so).

Usage: GITHUB_TOKEN=... python .github/scripts/check_issue_notes.py [docs_dir]
"""
import collections
import json
import os
import pathlib
import re
import sys
import urllib.request

docs = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "docs")
PATTERN = re.compile(r"(?:sitmun/sitmun#|github\.com/sitmun/sitmun/issues/)(\d+)")

cited = collections.defaultdict(set)
for page in sorted(docs.rglob("*.md")):
    for number in PATTERN.findall(page.read_text(encoding="utf-8")):
        cited[int(number)].add(str(page))

headers = {"Accept": "application/vnd.github+json", "User-Agent": "sitmun-docs-ci"}
if os.environ.get("GITHUB_TOKEN"):
    headers["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"

accepted = {int(line.split()[0]) for line in pathlib.Path(".github/issue-notes-accepted.txt")
            .read_text(encoding="utf-8").splitlines() if line.strip() and not line.startswith("#")}

closed = []
for number in sorted(cited):
    if number in accepted:
        continue
    request = urllib.request.Request(f"https://api.github.com/repos/sitmun/sitmun/issues/{number}", headers=headers)
    with urllib.request.urlopen(request, timeout=60) as response:
        issue = json.load(response)
    if issue["state"] == "closed":
        closed.append(number)
        for page in sorted(cited[number]):
            print(f"::warning file={page}::sitmun/sitmun#{number} is closed "
                  f"({issue['title']}); update or remove its note")

print(f"{len(cited)} issues cited, {len(closed)} closed: {closed}")
sys.exit(1 if closed else 0)
