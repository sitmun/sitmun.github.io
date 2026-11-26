---
description: "App móvil de edición de SITMUN 3 (Android): edición de cartografía en trabajo de campo, online y offline, multiusuario y multiproyecto."
---

# App móvil de edición

La app móvil de edición (SITMUN Edition) permite **editar cartografía en trabajo de campo**, tanto con conexión como sin ella (online y offline). Es multiusuario y multiproyecto.

| | |
| --- | --- |
| **Para quién** | Personal de campo |
| **Plataforma** | Solo Android |
| **Funcionalidad actual** | Edición de puntos |
| **Carpeta en el repositorio** | `sitmun-mobile/sitmun-edition` |

!!! note "Alcance actual"
    En estos momentos la app solo permite la edición de **puntos**.

## Instalación

La app no se publica con la instalación de SITMUN. Se compila desde su carpeta del repositorio (ver su README) y se conecta al backend de una instalación.

## Qué aplicaciones muestra

Solo muestra las aplicaciones de tipo «Edition application» (código `ED`) a las que el usuario tiene acceso. Si no tiene ninguna, el inicio de sesión responde 403.

## Configuración en el administrador

La app usa las [tareas de edición](../../../usuario/manual/administrador/tareas/index.md), que se configuran desde el [cliente de administración](administrador.md) como el resto de tareas.
