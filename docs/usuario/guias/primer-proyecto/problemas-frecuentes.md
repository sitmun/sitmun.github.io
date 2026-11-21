---
description: "Problemas frecuentes al montar el primer proyecto en SITMUN 3, casi siempre por un rol, territorio u opción que falta."
---

# Problemas frecuentes

Casi siempre que algo no aparece en el visor es porque falta un enlace: un rol, un territorio o una opción activada. En la mayoría de estos casos el visor no muestra ningún error; la excepción son los mapas de fondo, que impiden abrir el mapa.

| Qué pasa | Causa probable | Dónde se corrige |
| --- | --- | --- |
| La aplicación no aparece en la lista del visor | La aplicación no tiene el rol, o el usuario no tiene ese rol en ningún territorio. Si el usuario es `public`, quizá la aplicación es privada. Si la asignación tiene **Rol territorial**, la aplicación necesita **Garantizar acceso al territorio de la asignación**, y para los territorios hijos también **Garantizar acceso a territorios hijo** (en la versión 1.3.0, **Garantizar acceso a territorios hijo** sola no basta: [sitmun/sitmun#379](https://github.com/sitmun/sitmun/issues/379)). | Aplicación → Roles; Usuario → Roles por Territorio; Aplicación → Información general |
| El mapa no se abre y aparece el error «No hay capas definidas como base» | Ningún mapa de fondo llega al usuario: no está **Activo**, no tiene el rol, no está en la aplicación, o sus capas no tienen el territorio o no están disponibles para los clientes. Con **Rol territorial**, en un territorio hijo: el territorio hijo no está en las capas del mapa de fondo. | Capas de fondo; Capas → Territorios |
| El mapa muestra «Creando mapa...» y, a los 30 segundos, «Error al inicializar el mapa» | Un mapa de fondo WMTS está mal configurado: falta el parámetro `matrixSet` o el nombre de la capa del servicio es incorrecto. Basta uno para que no se abra el mapa ([sitmun/sitmun#380](https://github.com/sitmun/sitmun/issues/380)). | Servicio → Parámetros de configuración; Capas |
| En el panel de capas no aparece la sección «Capas disponibles» (el árbol) | La tarea «Catálogo de capas» (`sitna.layerCatalog`) no tiene el rol o el territorio. | Tarea básica → Roles / Territorios |
| Una capa no aparece en el árbol | La capa no está disponible para los clientes, no tiene el territorio o no está en ningún grupo con el rol. | Capas; Permisos sobre las capas |
| Una carpeta o capa añadida no aparece en el árbol | No se pulsó el icono de guardar del panel del nodo. | Árboles → Estructura del árbol |
| El árbol aparece vacío o no aparece | El árbol no tiene el rol, o ninguno de sus nodos tiene una capa que llegue al usuario. | Árboles → Roles |
| Las capas de un servicio con **Usar proxy SITMUN** no cargan | La dirección pública de SITMUN Proxy Middleware (el proxy) es incorrecta: los navegadores no llegan a `…/middleware`. Pasa a menudo tras cambiar el nombre o el puerto del servidor. Si solo fallan con un usuario registrado que ha cambiado alguna vez su contraseña, es un error de la versión 1.3.0 sin solución en la configuración ([sitmun/sitmun#387](https://github.com/sitmun/sitmun/issues/387)). | En Docker, las variables `PUBLIC_URL_SCHEME`, `PUBLIC_HOSTNAME`, `PUBLIC_PORT` y `PUBLIC_BASE_PATH` de `.env` (después, `docker compose up -d`). Sin Docker, `SITMUN_PROXY_MIDDLEWARE_URL` del backend. Si existe el parámetro `proxy` en Sistema → Parámetros de configuración, tiene prioridad sobre ellas para las capas y los servicios (no para las tareas de consulta, localizador y más información). |
| El nombre de una capa o aplicación no cambia en el visor | En el árbol, el visor muestra el **Nombre** del nodo, no el de la capa. En la lista de aplicaciones, muestra el **Título** de la aplicación. Si el campo tiene traducción, el visor muestra la del idioma elegido. | [Árboles → **Nombre** del nodo](../../manual/administrador/arboles.md#estructura-del-arbol); Aplicación → **Título**; Sistema → Traducciones de literales |
| Después de **Cargar desde servicio** hay nodos sin capa | Los nodos de capa no quedan enlazados a las capas de SITMUN al guardar. | Árboles → elige la capa en **Cartografía** en cada nodo |

Si el problema continúa, prueba primero con el usuario `public` y una aplicación no privada. Es el camino con menos enlaces.
