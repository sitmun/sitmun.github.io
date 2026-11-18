# Añadir OpenStreetMap como mapa de fondo

Esta guía explica cómo ofrecer el mapa de [OpenStreetMap](https://www.openstreetmap.org) (OSM) como mapa de fondo en una aplicación de SITMUN. Todo se hace desde el administrador. No hace falta instalar nada ni cambiar código.

Al terminar, los usuarios del visor verán **OpenStreetMap** en la lista de mapas de fondo de la aplicación.

!!! info "Cambio de sistema de referencia"
    Los mapas de OpenStreetMap solo existen en el sistema de referencia **EPSG:3857** (Web Mercator). Si la aplicación usa otro (por ejemplo, EPSG:25831), al elegir OpenStreetMap el visor muestra el aviso *Mapa de fondo no compatible* y propone cambiar el sistema de referencia del mapa. El usuario elige **EPSG:3857** y el mapa se muestra. Al volver a un mapa de fondo de la aplicación, el visor recupera su sistema de referencia original.

??? info "Cómo funciona (detalle técnico)"
    SITMUN admite servicios WMS, WMTS y WFS. OpenStreetMap publica su mapa en otro formato (teselas XYZ), que SITMUN no admite directamente.

    El visor de SITMUN incluye un archivo que describe el mapa de OpenStreetMap como si fuera un servicio WMTS. Basta con dar de alta un servicio WMTS que apunte a ese archivo. Las teselas del mapa se descargan de los servidores de OpenStreetMap.

## Antes de empezar

Necesitas:

- Acceso al administrador de SITMUN con un usuario administrador.
- La dirección web del visor de tu instalación. Por ejemplo, `https://ejemplo.org/sitmun/viewer`.
- Saber en qué aplicaciones quieres el mapa, para qué territorios y para qué roles.

Comprueba que el archivo de OpenStreetMap está disponible. Abre en el navegador esta dirección, sustituyendo el principio por la dirección de tu visor:

```text
https://ejemplo.org/sitmun/viewer/assets/js/api-sitna/wmts/osm/1.0.0/WMTSCapabilities.xml
```

Debe mostrarse un documento XML que empieza por `<Capabilities`. Esta dirección es el **Endpoint del servicio** que usarás en el paso 1.

!!! example "Instalación local con Docker"
    En una instalación local la dirección es
    `http://localhost:9000/viewer/assets/js/api-sitna/wmts/osm/1.0.0/WMTSCapabilities.xml`.

## Paso 1. Crear el servicio

1. En el menú, abre **Servicio** y crea uno nuevo.
2. Rellena los datos principales:

    | Campo | Valor |
    |---|---|
    | **Título del servicio** | `OpenStreetMap` (solo lo ven los administradores) |
    | **Tipo de servicio** | `WMTS` |
    | **Endpoint del servicio** | La dirección del archivo que has comprobado antes |
    | **CRS soportados** | `EPSG:3857` |
    | **Usar proxy SITMUN** | Desactivado |
    | **Método de autenticación** | Ninguno |

3. En **Parámetros de configuración**, añade estos dos parámetros con el botón de añadir. En los dos, el **Tipo** es *Ajustes de teselas del visor*:

    | Nombre | Tipo | Valor |
    |---|---|---|
    | `matrixSet` | Ajustes de teselas del visor | `WorldWebMercatorQuad` |
    | `format` | Ajustes de teselas del visor | `image/png` |

4. Guarda el servicio.

!!! warning "Escribe los nombres exactamente así"
    `matrixSet` y `format` distinguen mayúsculas y minúsculas. Si están mal escritos, el visor no dibuja el mapa.

## Paso 2. Crear la capa

1. En el menú, abre **Capas** y crea una nueva.
2. Rellena los datos:

    | Campo | Valor |
    |---|---|
    | **Nombre** | `OpenStreetMap` |
    | **Capa disponible para su uso por parte de los clientes** | Activado |
    | **Servicio** (*Selecciona un servicio*) | El servicio creado en el paso 1 |
    | **Capa o capas del servicio utilizadas** | `osm` |

3. En la pestaña **Territorios**, añade los territorios donde debe estar disponible el mapa.
4. Guarda la capa.

!!! tip "El nombre de la capa es el que ven los usuarios"
    En la lista de mapas de fondo del visor aparece el **nombre de la capa**, no el del mapa de fondo. Elige un nombre claro para los usuarios, por ejemplo `OpenStreetMap`.

## Paso 3. Crear el mapa de fondo

1. En el menú, abre **Capas de fondo** y crea una nueva.
2. Rellena los datos:

    | Campo | Valor |
    |---|---|
    | **Nombre** | `OpenStreetMap` |
    | **Descripción** | Opcional |
    | **Imagen** | Miniatura que verán los usuarios. El visor incluye una: `<dirección del visor>/assets/js/api-sitna/css/img/thumb-osm.png` |
    | **Activo** | Activado |

3. En la pestaña **Capas**, añade la capa creada en el paso 2.
4. En la pestaña **Roles**, añade los roles que deben ver el mapa. Si la aplicación tiene acceso público, incluye también el rol público.
5. En la pestaña **Aplicaciones**, añade las aplicaciones donde debe aparecer el mapa.
6. Guarda.

El orden de los mapas de fondo de cada aplicación se cambia en la propia aplicación: menú **Aplicación**, pestaña **Mapas de fondo**.

## Paso 4. Comprobarlo en el visor

1. Abre la aplicación en el visor. Si ya estaba abierta, recárgala.
2. Abre el panel de capas y despliega **Mapas de fondo**. Debe aparecer **OpenStreetMap** con su miniatura.
3. Haz clic en **OpenStreetMap**. Si la aplicación no usa EPSG:3857, aparece el aviso *Mapa de fondo no compatible*: elige **EPSG:3857**.
4. Acerca el mapa hasta nivel de calle para comprobar que se ve con detalle.
5. Vuelve a un mapa de fondo de la aplicación para comprobar que el mapa recupera su sistema de referencia.

## Si no se ve

| Qué pasa | Qué revisar |
|---|---|
| OpenStreetMap no aparece en la lista de mapas de fondo | El mapa de fondo está **Activo** y tiene la aplicación (paso 3). La capa está marcada como disponible y tiene el **territorio** (paso 2). El mapa de fondo tiene el **rol** del usuario (paso 3). |
| Aparece en la lista, pero el mapa queda en blanco | Los parámetros `matrixSet` y `format` del servicio (paso 1). El campo **Capa o capas del servicio utilizadas** de la capa es `osm`, en minúsculas (paso 2). |
| Aparece con otro nombre | El nombre que se muestra es el de la **capa** (paso 2). |
| Aparece sin miniatura | La dirección del campo **Imagen** del mapa de fondo (paso 3). |
| El **Endpoint del servicio** no abre el archivo XML | La dirección del visor. Prueba primero la dirección del visor sola. |

## Condiciones de uso de OpenStreetMap

Las teselas se descargan de los servidores de la Fundación OpenStreetMap. Su uso está sujeto a la [política de uso de teselas](https://operations.osmfoundation.org/policies/tiles/):

- El mapa debe citar a OpenStreetMap: *© colaboradores de OpenStreetMap*.
- El servicio es gratuito y no tiene garantía de disponibilidad.
- No se permiten descargas masivas de teselas. No uses este mapa de fondo con herramientas de mapas sin conexión.
