# Documentation screenshots

`shots.py` takes the screenshots of the administrator manual, the "Primer
proyecto" guide and the installation page from a running SITMUN showcase. Run it
for each release so the images match the screens readers see.

It drives the admin and the viewer with Playwright, in Spanish, at 1440×1000. On
the way it creates the example records the manual describes: a connection to the
example database, a WMS service and its layers, a tree, an SQL query, a locator,
a template and a MIA. It also grants a few seeded controls (Download, Measure,
Scale Bar, Search, 3D View) to the SDI Viewer role so the viewer shows them.

## Requirements

- Python 3.11+ and the packages in `requirements.txt`:

  ```bash
  python -m venv .venv
  .venv/bin/pip install -r tools/screenshots/requirements.txt
  .venv/bin/playwright install chromium
  ```

- A **fresh** showcase started from the `sitmun/sitmun` release tag, with the
  example database. The script creates its records through the UI, so a second
  run on the same database fails on records that already exist.
- Internet access: the showcase uses public WMS services (IDEIB, IDE Menorca, IGN).

## Start a fresh showcase

From a checkout of `sitmun/sitmun` at the release tag:

```bash
cp profiles/showcase.env .env && ./setup.sh
COMPOSE_PROFILES=postgres,demo SITMUN_BOOTSTRAP_ADMIN_PASSWORD= \
    docker compose up -d --pull always --no-build
```

The `demo` profile starts the example database that the query, template and
MIA images use; `showcase.env` alone does not include it. If the connection test
to it fails, the script stops rather than take error screens.

Leaving `SITMUN_BOOTSTRAP_ADMIN_PASSWORD` empty keeps the first-run wizard, which
the script captures for the installation page and completes with the password
you give it, choosing Castellano as the database language. The script looks for
the showcase records by their Spanish names, so it needs that language. If the admin password is already set, the script skips the wizard
and those two images keep their previous version.

To run it next to another SITMUN stack, use another project name
(`docker compose -p sitmun-shots ...`) and a `compose.override.yaml` that
publishes other ports.

## Run

Put the admin password (8 to 50 characters) in a file outside the repository:

```bash
.venv/bin/python tools/screenshots/shots.py --base http://localhost:9000 \
    --password-file ~/sitmun-admin-password
```

- `--list` prints the steps in the order they run.
- `--only STEP ...` runs some steps. Later steps use records created by earlier
  ones, so use it to retake images while working on the script, not on a fresh
  showcase.
- If the script cannot sign in (wrong address or password), it says so and
  exits with status 1 without taking any image.
- A failed step does not stop the run. Its last screen goes to
  `/tmp/shot-fail-<step>.png`, and the script exits with status 1.

Then check the images (`git diff --stat docs/`), build the site
(`zensical build --strict`), and stop the showcase
(`docker compose down -v`).

## Images the script does not take

- `basicas-search` and `basicas-legend`: in 1.3.0 the search finds nothing
  (sitmun/sitmun#352) and the legend stays empty (sitmun/sitmun#375). Take them
  again once a release fixes those issues.
