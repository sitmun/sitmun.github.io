---
description: "Cliente de administración de SITMUN 3: la aplicación web con la que los administradores configuran aplicaciones, capas, tareas, territorios, roles y usuarios."
---

# Cliente de administración

El cliente de administración es **el cliente principal de las personas que administran SITMUN** en su entidad. Es una aplicación web, disponible en `/admin/` de la instalación (código en la carpeta `sitmun-admin` de [sitmun/sitmun](https://github.com/sitmun/sitmun)).

Con él se configura todo lo que luego ven los demás clientes. Permite gestionar:

- **Múltiples aplicaciones**, cada una con sus capas, árboles, mapas de fondo y herramientas.
- **Los accesos a los datos**: servicios, conexiones a bases de datos y permisos sobre las capas.
- **Los usuarios**, junto con los roles y territorios que determinan qué puede ver cada uno.

## A quién va dirigido

A los administradores de los visores de cada entidad. Los usuarios finales no lo utilizan: ellos trabajan con el [cliente web](visor-web.md), la [app de edición](app-edicion.md) o la [app turística](app-turistica.md).

## Cómo se relaciona con el resto de la plataforma

El cliente de administración lee y modifica los datos de la base de datos de SITMUN a través de la **API de Administración** del backend, y se autentica con la **API de Autenticación**. No usa la API de Configuración y Autorización, que es la que consultan los demás clientes para configurarse. Ver [API](../arquitectura/api.md).

## Documentación de uso

- Para empezar, [Primer proyecto](../../../usuario/guias/primer-proyecto/index.md) recorre ocho pasos desde la primera entrada hasta comprobar el resultado en el visor.
- Para el detalle de cada pantalla, [Manual del administrador](../../../usuario/manual/administrador/index.md).
