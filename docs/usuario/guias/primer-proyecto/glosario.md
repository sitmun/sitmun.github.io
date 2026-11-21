---
description: "Glosario de los términos de SITMUN 3 que usa la guía del primer proyecto."
---

# Glosario

| Término | Significado |
| --- | --- |
| Cartografía | Otro nombre de la capa. En el administrador aparece en el **Tipo** «Grupo de cartografía» y en el campo **Cartografía** de los nodos del árbol. |
| CRS | Sistema de coordenadas del mapa, escrito como `EPSG:` + número (por ejemplo `EPSG:25831`, UTM 31N). |
| Extensión | El rectángulo de coordenadas (min X, min Y, max X, max Y) que el mapa muestra al abrirse. |
| GetCapabilities | La petición que devuelve la descripción de un servicio y la lista de sus capas. |
| GetFeatureInfo | La petición que devuelve los datos de un punto cuando el usuario hace clic en el mapa. |
| Grupo de permisos | Conjunto de capas al que se asignan roles (menú **Permisos sobre las capas**). |
| Mapa de fondo | La imagen base del mapa que el usuario elige en el selector de mapas de fondo. Se configura en el menú **Capas de fondo**. |
| Proxy | Servidor intermediario de SITMUN. El visor pasa por él para llegar a servicios protegidos. |
| Rol territorial | Opción de una asignación de usuario: el rol puede valer también para los territorios hijos. Necesita que la aplicación tenga activadas **Garantizar acceso al territorio de la asignación** (para el territorio asignado) y **Garantizar acceso a territorios hijo** (para sus territorios hijos) ([paso 7](paso-7-aplicacion.md)); en la versión 1.3.0 **Garantizar acceso a territorios hijo** por sí sola no basta (ver [sitmun/sitmun#379](https://github.com/sitmun/sitmun/issues/379)). Los territorios hijos también tienen que estar en las capas, los mapas de fondo y las tareas. |
| Tarea | Una función que se configura en el administrador. Las tareas básicas son las herramientas del visor. |
| Usuario `public` | Usuario que representa a cualquier visitante sin sesión. |
| WFS | Servicio que da los datos (geometría y atributos), no imágenes. |
| WMS | Servicio que da imágenes de mapa a demanda. |
| WMTS | Servicio que da imágenes de mapa ya cortadas en teselas. Es más rápido; se usa a menudo para los mapas de fondo. |
