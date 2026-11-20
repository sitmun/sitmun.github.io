"""Take the documentation screenshots from a running SITMUN showcase.

The script drives the admin and viewer of a *fresh* showcase (see README.md)
with Playwright, creates the few example records the manual needs (a
connection to the example database, an SQL query, a locator...) through the
admin interface, and writes WebP images into docs/.

Usage:
    python tools/screenshots/shots.py --base http://localhost:9000 \
        --password-file <file with the admin password> [--only NAME ...]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from playwright.sync_api import sync_playwright  # noqa: E402

from lib import SHOTS, VIEWPORT, Abort, Ctx, login_admin  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", default="http://localhost:9000")
    ap.add_argument("--password-file", help="file with the admin password (required unless --list)")
    ap.add_argument("--only", nargs="*", default=[])
    ap.add_argument("--list", action="store_true", help="list the steps and exit")
    args = ap.parse_args()

    import steps  # noqa: F401  (registers the @shot steps)

    if args.list:
        print("before_login  (first-run wizard and login page, before signing in)")
        print("\n".join(SHOTS))
        return 0
    if not args.password_file:
        ap.error("--password-file is required")
    password = Path(args.password_file).read_text().strip()
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(viewport=VIEWPORT, locale="es-ES", device_scale_factor=1)
        page = context.new_page()
        ctx = Ctx(page, args.base, password, set(args.only))
        failed = []
        try:
            if not ctx.only or "before_login" in ctx.only:
                steps.before_login(ctx)
            login_admin(page, args.base, password)
        except Exception as exc:
            failed.append("login")
            print(f"Could not sign in to the admin at {args.base} (address or password?): {exc}")
            page.screenshot(path="/tmp/shot-fail-login.png")
        for name, step in SHOTS.items():
            if failed == ["login"] or (ctx.only and name not in ctx.only):
                continue
            print(f"- {name}")
            try:
                step(ctx)
            except Abort as exc:  # later images would be wrong: stop here
                failed.append(name)
                print(f"  STOPPED: {exc}")
                break
            except Exception as exc:  # keep going; report at the end
                failed.append(name)
                print(f"  FAILED: {exc}")
                page.screenshot(path=f"/tmp/shot-fail-{name}.png")
        browser.close()
    print(f"{len(ctx.written)} images written, {len(failed)} steps failed: {failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
