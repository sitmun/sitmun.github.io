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
poetry self add poetry-plugin-export
poetry export -f requirements.txt --output requirements.txt
```

La comprobación `requirements-sync` falla si `requirements.txt` no coincide con `poetry.lock`.

## Comprobaciones

Cada *pull request* a `master` ejecuta en GitHub Actions (`.github/workflows/ci.yml`):

- `zensical build --strict`, que además falla si alguna tabla de cuadrícula no se puede dibujar;
- la traducción de las páginas de redirección (`localize_redirects.py`);
- que todos los diagramas PlantUML se hayan dibujado (`check_diagrams.py`);
- que las direcciones de páginas publicadas antes sigan funcionando (`check_old_urls.py`);
- que ninguna página enlace a una página de redirección (`check_redirect_links.py`);
- que ninguna página cargue recursos de otros sitios (`check_external_resources.py`);
- que las etiquetas de la interfaz en negrita existan en SITMUN 1.3.0 (`check_ui_labels.py`, con `.github/label-allowlist.txt`);
- una comprobación de enlaces locales con `lychee`;
- que `requirements.txt` coincida con `poetry.lock` (`requirements-sync`).

Si el *pull request* cambia archivos Markdown, también se ejecuta `markdownlint-cli2 --fix` sobre `docs/**/*.md` con las
reglas de `.markdownlint-cli2.yaml`. Las correcciones se suben como un *commit* a la rama del *pull request*; lo que no se
puede corregir solo aparece como aviso y no hace fallar la comprobación. En local: `npx markdownlint-cli2@0.24.0 --fix`.
