---
description: "Roles en el administrador de SITMUN 3: nombre del rol y su relación con usuarios por territorio, tareas y aplicaciones."
---

# Roles

El rol es el elemento para definir las características de un rol de comportamiento; en él se detallan los accesos a otros elementos.

Con la combinación de los tres elementos, [territorios](territorios.md), roles y [usuarios](usuarios.md), se configuran los accesos y permisos a las [aplicaciones](aplicacion.md), [tareas](tareas/index.md) e información del mapa ([capas](capas.md), [capas de fondo](capas-de-fondo.md), etc.).

Para definir un rol, únicamente hace falta definir un parámetro mínimo:

- **Nombre**: nombre del rol que permita identificar el elemento. Solo se usa en el administrador: no se envía a las aplicaciones.

Opcionalmente, una **Descripción** (hasta 500 caracteres) explica para qué sirve el rol.

En otras pestañas se detallan las relaciones de acceso con los otros elementos existentes en la plataforma:

- **Usuarios por territorio**: definir la relación con los otros componentes que permitirán el acceso a este rol.
- **Tiene acceso a Tareas**: tareas a las que tendrá acceso este rol.
- **Tiene acceso a Aplicaciones**: aplicaciones a las que este rol tiene acceso.
