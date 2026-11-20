"""Fail when a page that was ever published from master no longer resolves.

Every .md file under docs/ at any first-parent commit of master was published
as a page. Each one must still exist in the built site, as a page or as a
redirect (redirect_maps in zensical.toml), so old links and bookmarks keep
working. Needs the full git history (actions/checkout with fetch-depth: 0).

Usage: python .github/scripts/check_old_urls.py [site_dir] [branch]
"""
import pathlib
import subprocess
import sys

site = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "_site")
branch = sys.argv[2] if len(sys.argv) > 2 else "origin/master"

# Files under docs/ that were part of a bundled app, not pages.
IGNORE_PREFIXES = ("viewer-app/", "admin-app/")


def git(*args: str) -> str:
    return subprocess.run(("git",) + args, check=True, capture_output=True, text=True).stdout


paths = set()
for commit in git("rev-list", "--first-parent", branch).split():
    for name in git("ls-tree", "-r", "--name-only", commit, "--", "docs").splitlines():
        if name.endswith(".md"):
            paths.add(name.removeprefix("docs/"))

missing = []
for page in sorted(paths):
    if page.startswith(IGNORE_PREFIXES):
        continue
    if page == "index.md":
        target = site / "index.html"
    elif page.endswith("/index.md"):
        target = site / page.removesuffix("index.md") / "index.html"
    else:
        target = site / page.removesuffix(".md") / "index.html"
    if not target.is_file():
        missing.append(page)

for page in missing:
    print(f"::error::{page} was published from {branch} and no longer resolves; "
          "add it to redirect_maps in zensical.toml")
print(f"{len(paths)} published pages checked, {len(missing)} missing")
sys.exit(1 if missing else 0)
