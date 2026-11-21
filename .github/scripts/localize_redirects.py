"""Translate the redirect pages into Spanish.

Zensical writes one small HTML page for each entry in redirect_maps. Its
template is built into Zensical and is in English (lang="en", "Redirecting...",
"You're being redirected to a new destination"), and there is no option to change
it. This script rewrites those pages after the build.

It fails when the number of redirect pages found does not match redirect_maps,
so a change to Zensical's template does not go unnoticed.

Usage: python .github/scripts/localize_redirects.py [zensical.toml] [site_dir]
"""
import pathlib
import re
import sys
import tomllib

config = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "zensical.toml")
site = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else "_site")

with config.open("rb") as f:
    redirects = tomllib.load(f)["project"]["plugins"]["redirects"]["redirect_maps"]

MESSAGE = re.compile(
    r"You're being redirected to a <a href=\"([^\"]*)\">new destination</a>\."
)
done = 0
for page in site.rglob("*.html"):
    html = page.read_text(encoding="utf-8")
    # Zensical's redirect pages carry this script; static redirect pages under
    # docs/ (copied as they are) don't, and are not counted.
    if 'http-equiv="refresh"' not in html or "var anchor=window.location.hash" not in html:
        continue
    if 'lang="es"' in html and "nueva ubicación" in html:  # already translated
        done += 1
        continue
    if not MESSAGE.search(html):
        continue
    html = html.replace('<html lang="en">', '<html lang="es">', 1)
    html = html.replace("<title>Redirecting...</title>", "<title>Redirigiendo…</title>", 1)
    html = MESSAGE.sub(r'Esta página se ha trasladado a una <a href="\1">nueva ubicación</a>.', html, 1)
    page.write_text(html, encoding="utf-8")
    done += 1

print(f"{done} redirect pages translated, {len(redirects)} in redirect_maps")
if done != len(redirects):
    print("::error::The redirect pages do not match redirect_maps; "
          "Zensical's redirect template may have changed.")
    sys.exit(1)
