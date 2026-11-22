# SITMUN: documentación técnica

Este repositorio contiene la documentación técnica de SITMUN (en castellano), publicada en <https://sitmun.github.io>.
El contenido tiene la licencia [EUPL 1.2](LICENSE). Los errores o discrepancias se notifican con la
[plantilla de incidencias](https://github.com/sitmun/sitmun.github.io/issues/new/choose) de este repositorio.

## Construir la web

La web se construye con [Zensical](https://zensical.org) a partir de `zensical.toml`:

```bash
python -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/zensical serve        # vista previa en http://localhost:8000
.venv/bin/zensical build --strict
.venv/bin/python .github/scripts/localize_redirects.py zensical.toml _site
```

El último paso traduce al castellano las páginas de redirección que genera Zensical (sin él, salen en inglés).
Lo ejecuta también el despliegue, así que la web publicada coincide con `_site` después de ese paso.

`requirements.txt` se genera desde `poetry.lock` con el complemento de exportación de Poetry:

```bash
poetry self add poetry-plugin-export==1.10.1
poetry export -f requirements.txt --output requirements.txt
```

La comprobación `requirements-sync` falla si `requirements.txt` no coincide con `poetry.lock`.

## Comprobaciones

Cada *pull request* a `master` ejecuta en GitHub Actions (`.github/workflows/ci.yml`):

- que `zensical build --strict` termine sin errores, lo que incluye que se pueda dibujar toda tabla de cuadrícula;
- que se traduzcan las páginas de redirección (`localize_redirects.py`);
- que se hayan dibujado todos los diagramas PlantUML (`check_diagrams.py`);
- que sigan funcionando las direcciones de páginas publicadas antes (`check_old_urls.py`);
- que ninguna página enlace a una página de redirección (`check_redirect_links.py`);
- que ninguna página cargue recursos de otros sitios (`check_external_resources.py`);
- que las etiquetas de la interfaz en negrita existan en SITMUN 1.3.0 (`check_ui_labels.py`, con `.github/label-allowlist.txt`);
- que los enlaces locales funcionen (`lychee`);
- que `requirements.txt` coincida con `poetry.lock` (`requirements-sync`).

Si el *pull request* cambia archivos Markdown, también se ejecuta `markdownlint-cli2 --fix` sobre `docs/**/*.md` y `README.md` con las
reglas de `.markdownlint-cli2.yaml`. Las correcciones se suben como un *commit* a la rama del *pull request*; lo que no se
puede corregir solo aparece como aviso y no hace fallar la comprobación. En local: `npx markdownlint-cli2@0.24.0 --fix`.

Cada lunes a las 06:00 UTC, y a mano desde la pestaña *Actions*, se ejecutan además dos flujos de trabajo:

- `links.yml` construye la web y comprueba con `lychee` todos los enlaces del resultado, también los externos;
- `issue-notes.yml` lista las incidencias cerradas que citan las páginas (`check_issue_notes.py`).
