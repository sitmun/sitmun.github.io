# Navegación y vista

Tareas básicas para moverse por el mapa y cambiar cómo se ve.

## 3D View

Permite cambiar de una visualización 2D a una visualización 3D, siempre que la capa de fondo disponga de la configuración necesaria para permitir la representación tridimensional de la cartografía.

- Control API SITNA: `sitna.threed`

![Botón 3D del visor](../../img/basicas-3d.webp){ loading=lazy }

## Full screen

Permite activar la visualización en pantalla completa.

- Control API SITNA: `sitna.fullScreen`

![Botón de pantalla completa del visor](../../img/basicas-full-screen.webp){ loading=lazy }

## Geolocation

!!! info "En preparación"
    Este apartado todavía no está documentado.

## Navigation Bar

Son los elementos que permiten realizar las operaciones de acercar y alejar, así como volver a la escala original.

- Control API SITNA: `sitna.navBar`

![Barra de navegación del visor](../../img/basicas-navigation-bar.webp){ loading=lazy }

## Overview Map

Permite visualizar el mapa de situación. Se ubica en el icono inferior derecho.

- Control API SITNA: `sitna.overviewMap`

![Mapa de situación del visor](../../img/basicas-overview-map.webp){ loading=lazy }

## Scale

Permite visualizar la escala del mapa. Se muestra en la parte inferior derecha.

- Control API SITNA: `sitna.scale`

![Escala numérica del visor](../../img/basicas-scale.webp){ loading=lazy }

## Scale Bar

Permite visualizar la escala en formato de barra. Se muestra en la esquina inferior derecha del mapa, en el mismo lugar que el control Scale, así que conviene no activar los dos en la misma aplicación (véase la nota siguiente).

- Control API SITNA: `sitna.scaleBar`

![Barra de escala del visor](../../img/basicas-scale-bar.webp){ loading=lazy }

!!! warning "SITMUN 1.3.0"
    Si la aplicación tiene también la tarea **Scale**, la escala tapa la barra de escala
    ([sitmun/sitmun#374](https://github.com/sitmun/sitmun/issues/374)).

## Scale Selector

!!! info "En preparación"
    Este apartado todavía no está documentado.

## Street View

Permite visualizar la información de Street View de un determinado punto del mapa. Se activa arrastrando el icono hasta el mapa y se vinculará con el punto de Street View más cercano.

Es necesario disponer de una clave (*key*) de Google Maps para que esta herramienta funcione correctamente; de lo contrario, las imágenes de Street View se mostrarán con un efecto de negativo fotográfico.

- Control API SITNA: `sitna.streetView`
