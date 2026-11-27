---
description: "Tareas básicas de navegación en SITMUN 3: zoom, pantalla completa, vista 3D, escala y mapa de situación."
---

# Navegación y vista

Tareas básicas para moverse por el mapa y cambiar cómo se ve.

## Vista 3D (3D View) { #3d-view }

Permite cambiar de una visualización 2D a una visualización 3D, siempre que el mapa de fondo disponga de la configuración necesaria para permitir la representación tridimensional de la cartografía.

- Control API SITNA: `sitna.threed`

![Botón 3D del visor](../../img/basicas-3d.webp){ loading=lazy }

## Pantalla completa (Full Screen) { #full-screen }

Permite activar la visualización en pantalla completa.

- Control API SITNA: `sitna.fullScreen`

![Botón de pantalla completa del visor](../../img/basicas-full-screen.webp){ loading=lazy }

## Geolocalización (Geolocation) { #geolocation }

!!! info "En preparación"
    Este apartado todavía no está documentado.

## Barra de navegación (Navigation Bar) { #navigation-bar }

Son los elementos que permiten realizar las operaciones de acercar y alejar, así como volver a la escala original.

- Control API SITNA: `sitna.navBar`

![Barra de navegación del visor](../../img/basicas-navigation-bar.webp){ loading=lazy }

## Mapa de situación (Overview Map) { #overview-map }

Permite visualizar el mapa de situación. Se ubica en el icono inferior derecho.

- Control API SITNA: `sitna.overviewMap`

El mapa de situación usa la primera capa del grupo elegido en **Mapa de situación** y, si no hay grupo, la primera capa del primer mapa de fondo.

![Mapa de situación del visor](../../img/basicas-overview-map.webp){ loading=lazy }

## Escala (Scale) { #scale }

Permite visualizar la escala del mapa. Se muestra en la parte inferior derecha.

- Control API SITNA: `sitna.scale`

![Escala numérica del visor](../../img/basicas-scale.webp){ loading=lazy }

## Barra de escala (Scale Bar) { #scale-bar }

Permite visualizar la escala en formato de barra. Se muestra en la esquina inferior derecha del mapa. Si la aplicación tiene también la escala o el selector de escala, los controles se apilan en esa esquina y la barra queda encima.

- Control API SITNA: `sitna.scaleBar`

![Barra de escala del visor](../../img/basicas-scale-bar.webp){ loading=lazy }

## Selector de escala (Scale Selector) { #scale-selector }

!!! info "En preparación"
    Este apartado todavía no está documentado.

## Vista de calle (Street View) { #street-view }

Permite visualizar la información de Street View de un determinado punto del mapa. Se activa arrastrando el icono hasta el mapa y se vinculará con el punto de Street View más cercano.

Es necesario disponer de una clave (*key*) de Google Maps para que esta herramienta funcione correctamente; de lo contrario, las imágenes de Street View se mostrarán con un efecto de negativo fotográfico. La clave se indica en la pestaña **Parámetros** de la tarea, con un parámetro llamado `googleMapsKey` cuyo valor es la clave.

- Control API SITNA: `sitna.streetView`
