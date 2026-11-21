"""Helpers and step registry for the documentation screenshots (see shots.py)."""
from __future__ import annotations

import io
import re
from pathlib import Path
from typing import Callable

from PIL import Image
from playwright.sync_api import Locator, Page

ROOT = Path(__file__).resolve().parents[2]
MANUAL_IMG = ROOT / "docs/usuario/manual/administrador/img"
GUIDE_IMG = ROOT / "docs/usuario/guias/primer-proyecto/img"
INSTALL_IMG = ROOT / "docs/usuario/instalacion/img"

VIEWPORT = {"width": 1440, "height": 1000}
HIGHLIGHT = "3px dashed #e53935"

SHOTS: dict[str, Callable[["Ctx"], None]] = {}


class Abort(Exception):
    """A step found the showcase unusable; later images would show errors, so stop."""


def shot(func: Callable[["Ctx"], None]) -> Callable[["Ctx"], None]:
    """Register a screenshot step. Steps run in definition order."""
    SHOTS[func.__name__] = func
    return func


class Ctx:
    def __init__(self, page: Page, base: str, password: str, only: set[str]):
        self.page = page
        self.base = base.rstrip("/")
        self.password = password
        self.only = only
        self.written: list[Path] = []

    # --- navigation -----------------------------------------------------------
    def admin(self, route: str) -> None:
        if self.page.url.endswith(f"#/{route}"):
            # Same address: the hash router would not reload the form.
            self._leave_to("dashboard")
        self._leave_to(route)
        self.settle()

    def _leave_to(self, route: str) -> None:
        self.page.goto(f"{self.base}/admin/#/{route}")
        self.page.wait_for_timeout(400)
        # Leaving a form with unsaved changes asks for confirmation.
        dialog = self.page.locator("mat-dialog-container")
        if dialog.count():
            dialog.locator("button").last.click()
            self.page.wait_for_timeout(400)
            self.page.goto(f"{self.base}/admin/#/{route}")
            self.page.wait_for_timeout(400)

    def viewer(self, route: str, language: str = "es") -> None:
        """Open a viewer page in the given language (the viewer keeps it in localStorage)."""
        self.page.goto(f"{self.base}/viewer/")
        self.page.evaluate("lang => localStorage.setItem('language', lang)", language)
        self.page.goto(f"{self.base}/viewer/#/{route}")
        self.page.reload()
        self.settle(1500)

    def map(self, app: int, territory: int, language: str = "es") -> None:
        """Open an application's map and wait until SITNA has loaded it."""
        self.viewer(f"public/map/{app}/{territory}", language)
        self.page.wait_for_function(
            "() => { const el = document.querySelector('.tc-map');"
            " const m = el && window.TC && TC.Map.get(el); return !!(m && m.isLoaded); }",
            timeout=90000,
        )
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(2500)

    def center(self, lon: float, lat: float, resolution: float) -> dict:
        """Center the map on a WGS84 point; return its pixel position on the page."""
        return self.page.evaluate(
            """async ([lon, lat, res]) => {
              const m = TC.Map.get(document.querySelector('.tc-map'));
              const c = TC.Util.reproject([lon, lat], 'EPSG:4326', m.crs);
              const view = m.wrap.map.getView();
              view.setCenter(c); view.setResolution(res);
              await new Promise(r => setTimeout(r, 3000));
              const px = m.wrap.map.getPixelFromCoordinate(c);
              const rect = m.wrap.map.getTargetElement().getBoundingClientRect();
              return {x: rect.left + px[0], y: rect.top + px[1]};
            }""",
            [lon, lat, resolution],
        )

    def settle(self, ms: int = 800) -> None:
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(ms)

    def tab(self, label: str) -> None:
        self.page.get_by_role("tab", name=label, exact=True).click()
        self.settle(500)

    # --- capture --------------------------------------------------------------
    @property
    def content(self) -> Locator:
        """Admin page content, without the toolbar and side menu."""
        return self.page.locator("mat-sidenav-content")

    def highlight(self, *targets: Locator) -> None:
        for t in targets:
            t.first.evaluate(
                "(e, s) => { e.style.outline = s; e.style.outlineOffset = '3px'; }",
                HIGHLIGHT,
            )

    def mark(self, *targets: Locator, pad: int = 3) -> None:
        """Highlight with a box drawn over the page, for elements an outline can't
        show (the viewer's SITNA controls, custom elements, clipped panels)."""
        for t in targets:
            box = t.first.bounding_box()
            assert box, "mark: target not visible"
            self.page.evaluate(
                """([b, s, pad]) => {
                  const d = document.createElement('div');
                  d.className = 'shot-mark';
                  Object.assign(d.style, {position: 'fixed', zIndex: 2147483647, pointerEvents: 'none',
                    left: (b.x - pad) + 'px', top: (b.y - pad) + 'px',
                    width: (b.width + 2 * pad) + 'px', height: (b.height + 2 * pad) + 'px',
                    border: s, boxSizing: 'border-box'});
                  document.body.appendChild(d);
                }""",
                [box, HIGHLIGHT, pad],
            )

    def clear_highlights(self) -> None:
        self.page.evaluate(
            "() => { document.querySelectorAll('[style*=outline]').forEach(e => e.style.outline = '');"
            " document.querySelectorAll('.shot-mark').forEach(e => e.remove()); }"
        )

    def save(self, name: str, target: Locator | None = None, folder: Path = MANUAL_IMG,
             pad: int = 0, full: bool = False, keep_toast: bool = False,
             clip: dict | None = None) -> None:
        if not keep_toast:
            self.page.evaluate(
                "() => document.querySelectorAll('.mat-mdc-snack-bar-container, mat-snack-bar-container')"
                ".forEach(e => e.style.visibility = 'hidden')"
            )
        if clip is not None:
            png = self.page.screenshot(clip=clip)
        elif target is None:
            png = self.page.screenshot(full_page=full)
        elif pad:
            box = target.first.bounding_box()
            assert box, f"{name}: target not visible"
            clip = {
                "x": max(box["x"] - pad, 0),
                "y": max(box["y"] - pad, 0),
                "width": box["width"] + 2 * pad,
                "height": box["height"] + 2 * pad,
            }
            png = self.page.screenshot(clip=clip, full_page=True)
        else:
            png = target.first.screenshot()
        folder.mkdir(parents=True, exist_ok=True)
        out = folder / f"{name}.webp"
        trim_bottom(Image.open(io.BytesIO(png)).convert("RGB")).save(out, "WEBP", quality=85, method=6)
        self.written.append(out)
        self.clear_highlights()
        self.page.evaluate(
            "() => document.querySelectorAll('.mat-mdc-snack-bar-container, mat-snack-bar-container')"
            ".forEach(e => e.style.visibility = '')"
        )
        print(f"  wrote {out.relative_to(ROOT)}")


def trim_bottom(img: Image.Image, margin: int = 16) -> Image.Image:
    """Drop empty rows at the bottom (the page background below the content)."""
    w, h = img.size
    bg = img.getpixel((4, h - 2))
    px = img.load()
    last = h - 1
    scan = range(0, max(w - 24, 1), 4)  # skip the scrollbar strip on the right
    while last > 0:
        row_empty = all(
            sum(abs(a - b) for a, b in zip(px[x, last], bg)) < 12 for x in scan
        )
        if not row_empty:
            break
        last -= 1
    return img.crop((0, 0, w, min(h, last + 1 + margin)))


def login_admin(page: Page, base: str, password: str) -> None:
    page.goto(f"{base}/admin/")
    page.wait_for_timeout(2000)
    if "/dashboard" in page.url:  # already signed in (after the first-run wizard)
        return
    page.fill("input[formcontrolname=username]", "admin")
    page.fill("input[formcontrolname=password]", password)
    page.click("button[type=submit]")
    page.wait_for_url(re.compile(r".*/dashboard.*"), timeout=30000)
