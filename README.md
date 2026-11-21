# SITMUN Documentation

Este repositorio contiene la documentación del proyecto SITMUN.

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

`requirements.txt` se genera desde `poetry.lock` con `poetry export -f requirements.txt --output requirements.txt`.

## Comprobaciones

Cada *pull request* hacia `master` ejecuta en GitHub Actions:

- `markdownlint-cli2 --fix` sobre `docs/**/*.md` con las reglas de `.markdownlint-cli2.yaml`.
  Las correcciones se suben como un *commit* a la rama del *pull request*; lo que no se puede corregir
  solo aparece como aviso y no hace fallar la comprobación.
  En local: `npx markdownlint-cli2@0.24.0 --fix`.
- `zensical build --strict` y una comprobación de enlaces locales con `lychee`.
