"""Fail when a page that was ever published from docs/ on master no longer resolves.

Every .md file under docs/ at any first-parent commit of master was published
as a page, and so was every .html file (the 2023 Sphinx pages). Each one must
still exist in the built site, as a page or a redirect (redirect_maps in
zensical.toml, or a static redirect page under docs/), so old links and
bookmarks keep working. Pages from before the site was built from docs/ (2021)
are out of scope. Needs the full git history (actions/checkout with
fetch-depth: 0).

Usage: python .github/scripts/check_old_urls.py [site_dir] [branch]
"""
import pathlib
import subprocess
import sys

site = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "_site")
branch = sys.argv[2] if len(sys.argv) > 2 else "origin/master"

# Files under docs/ that were part of a bundled app or theme templates, not pages.
IGNORE_PREFIXES = ("viewer-app/", "admin-app/")
IGNORE_PARTS = ("/_static/",)


def git(*args: str) -> str:
    return subprocess.run(("git",) + args, check=True, capture_output=True, text=True).stdout


paths = set()
for commit in git("rev-list", "--first-parent", branch).split():
    for name in git("ls-tree", "-r", "--name-only", commit, "--", "docs").splitlines():
        if name.endswith((".md", ".html")):
            paths.add(name.removeprefix("docs/"))

missing = []
checked = 0
for page in sorted(paths):
    if page.startswith(IGNORE_PREFIXES) or any(part in "/" + page for part in IGNORE_PARTS):
        continue
    if page.endswith(".html"):
        target = site / page
    elif page == "index.md":
        target = site / "index.html"
    elif page.endswith("/index.md"):
        target = site / page.removesuffix("index.md") / "index.html"
    else:
        target = site / page.removesuffix(".md") / "index.html"
    checked += 1
    if not target.is_file():
        missing.append(page)

for page in missing:
    print(f"::error::{page} was published from {branch} and no longer resolves; "
          "add it to redirect_maps in zensical.toml")
print(f"{checked} published pages checked, {len(missing)} missing")
sys.exit(1 if missing else 0)
