# SITMUN 1.3.0 en GitHub Codespaces

Este codespace arranca el *showcase* de SITMUN 1.3.0 con las imágenes publicadas, sin compilar nada.

- El arranque tarda unos minutos la primera vez (descarga de imágenes y carga de datos de ejemplo).
  El progreso se ve en el terminal de creación del codespace.
- Cuando termina, se abre el puerto 9000. Abre la pestaña **Puertos** y usa la dirección del puerto 9000:
  - `/admin/` es el administrador. En la primera visita se elige el idioma y la contraseña del usuario `admin`.
  - `/viewer/` es el visor, con tres aplicaciones de ejemplo.
- Los datos viven solo en este codespace. Para empezar de cero:

  ```bash
  cd ~/sitmun-showcase && docker compose -p sitmun-showcase down -v
  bash /workspaces/*/.devcontainer/showcase/start.sh
  ```

- Para pararlo, detén el codespace desde GitHub; los codespaces consumen horas de tu cuota mientras están encendidos.

Más información: [Instalación](https://sitmun.github.io/usuario/instalacion/instalacion/).
