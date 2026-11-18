# Paso 2: dar de alta los servicios

Un servicio es la dirección de un servidor de mapas. Crea uno por cada servidor: uno para las capas de trabajo y otro para el mapa de fondo, si vienen de sitios distintos.

(menú **Servicio** → **Nuevo**)

1. **Título del servicio**: un nombre que reconozcas. El usuario del visor no lo ve.
2. **Tipo de servicio**: WMS, WMTS o WFS.
3. **Endpoint del servicio**: la URL base, sin parámetros (sin `?SERVICE=WMS&REQUEST=...`). Algunos servidores necesitan una barra `/` al final.
4. Si es WMS, pulsa **Obtener detalles del servicio**. El administrador pide al servidor su descripción (GetCapabilities) y rellena datos como la descripción y los metadatos. Si falla, la URL no es correcta o el servidor no responde.
5. **Método de autenticación**: deja **Ninguno** si el servicio es público. Si pide usuario y contraseña, elige **Autenticación HTTP básica** y rellénalos. La opción **Usar proxy SITMUN** se activa sola, porque el visor tiene que pasar por el servidor intermediario (proxy) de SITMUN para no exponer la contraseña.
6. Pulsa **Guarda**.

**Si el mapa de fondo es WMTS**, ve a la pestaña **Parámetros de configuración** y añade `matrixSet` y `format` (por ejemplo `image/png`). Sin estos dos valores el visor no puede dibujar el mapa de fondo.

La pestaña **Monitorización** tiene un botón **Probar acceso** para comprobar que el servidor responde.
