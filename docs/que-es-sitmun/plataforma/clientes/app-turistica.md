---
description: "App turística de SITMUN 3 (Android): difusión de datos turísticos, con selección de la instalación a la que conectarse."
---

# App turística

La app turística (SITMUN Touristic) es la aplicación móvil de **difusión de datos turísticos**.

| | |
| --- | --- |
| **Para quién** | Ciudadanía y visitantes |
| **Plataforma** | Solo Android |
| **Carpeta en el repositorio** | `sitmun-mobile/sitmun-touristic` |

## Instalación

La app no se publica con la instalación de SITMUN. Se compila desde su carpeta del repositorio (ver su README) y se conecta al backend de una instalación.

## Qué aplicaciones muestra

Solo muestra las aplicaciones de tipo **Aplicación turística** (código `T`) con un árbol turístico. Se configuran desde el [cliente de administración](administrador.md).

## A qué instalaciones se conecta

Las instalaciones a las que se puede conectar se indican antes de compilarla, en los archivos `src/environments/environment*.ts`:

- En `instancesUrl`, la dirección de un servicio de instancias.
- Si se deja vacío, directamente en `instancesData`.

En los dos casos es un JSON en el que cada instancia tiene:

- `name`: el texto del selector.
- `urlBackend`: la dirección del backend, por ejemplo `https://ejemplo.org/backend`.

## Más información

El contexto de esta app dentro de la hoja de ruta está en la propuesta [Cliente APP SITMUN aplicada a los recursos turísticos](../hoja-de-ruta/propuestas/app-turismo.md).
