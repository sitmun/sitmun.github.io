# SITMUN 1.3.0 en GitHub Codespaces

Este codespace arranca SITMUN 1.3.0 con las imágenes publicadas, sin compilar nada. Hay tres variantes:

| Variante | Qué arranca | Para |
| --- | --- | --- |
| `demo` | Instalación de demostración: tres aplicaciones con datos de ejemplo | Ver SITMUN en marcha, seguir el manual |
| `vacia` | Instalación vacía | La guía «Primer proyecto» |
| `osm` | Instalación de demostración sin su mapa de fondo OpenStreetMap | La guía «Añadir OpenStreetMap como mapa de fondo» |

- La primera vez tarda unos minutos (descarga de imágenes y carga de datos). El progreso se ve en el terminal de creación del codespace.
- Cuando termina, abre la pestaña «Puertos» y usa la dirección del puerto 9000:
  - `/admin/` es el administrador. En la primera visita se eligen el idioma y la contraseña del usuario `admin`.
  - `/viewer/` es el visor.
- Los datos viven solo en este codespace. SITMUN está en `/workspaces/sitmun`; el proyecto de Docker Compose se llama
  `sitmun-showcase` en las variantes `demo` y `osm` y `sitmun` en `vacia`. Para empezar de cero, por ejemplo en `demo`:

  ```bash
  cd /workspaces/sitmun && docker compose -p sitmun-showcase down -v && rm -f .scenario-applied
  SITMUN_PROFILE=showcase SITMUN_EXTRA=demo bash /workspaces/sitmun.github.io/.devcontainer/start-sitmun.sh
  ```

- Los codespaces consumen horas de tu cuota mientras están encendidos: detén o borra el codespace desde GitHub cuando acabes.

Más información: [Instalación](https://sitmun.github.io/usuario/instalacion/instalacion/).
