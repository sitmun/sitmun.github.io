---
description: "Glosario de los términos de SITMUN 3 que usa la guía del primer proyecto."
---

# Glosario

| Término | Significado |
| --- | --- |
| CRS | Sistema de coordenadas del mapa, escrito como `EPSG:` + número (por ejemplo `EPSG:25831`, UTM 31N). |
| Extensión | El rectángulo de coordenadas (min X, min Y, max X, max Y) que el mapa muestra al abrirse. |
| GetCapabilities | La petición que devuelve la descripción de un servicio y la lista de sus capas. |
| GetFeatureInfo | La petición que devuelve los datos de un punto cuando el usuario hace clic en el mapa. |
| Proxy | Servidor intermediario de SITMUN. El visor pasa por él para llegar a servicios protegidos. |
| Rol territorial | Opción de una asignación de usuario: el rol puede valer también para los territorios hijos. Necesita que la aplicación tenga activada **Garantizar acceso al territorio de la asignación** o **Garantizar acceso a territorios hijo** ([paso 7](paso-7-aplicacion.md)); sin ninguna de las dos, la aplicación no aparece. |
| Usuario `public` | Usuario que representa a cualquier visitante sin sesión. |
| WFS | Servicio que da los datos (geometría y atributos), no imágenes. |
| WMS | Servicio que da imágenes de mapa a demanda. |
| WMTS | Servicio que da imágenes de mapa ya cortadas en teselas. Es más rápido; se usa a menudo para los mapas de fondo. |
