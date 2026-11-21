---
description: "Tareas básicas de SITMUN 3: los controles de la API SITNA que ofrecen la interacción básica con el mapa."
---

# Tareas básicas

Las tareas básicas son aquellas que se derivan directamente de los controles de la API SITNA. Son las tareas que ofrecen la interacción básica con el usuario en el visor.

Las tareas básicas ya vienen integradas por defecto en la instalación base de SITMUN 3.

Para que las tareas básicas puedan visualizarse en el visor, es necesario asignar a cada tarea básica un rol y un territorio. La tarea se mostrará en el visor cuando el usuario acceda con permisos que coincidan con los roles y territorios asignados.

La mayoría de las tareas básicas no necesitan nada más. Algunas sí necesitan parámetros para funcionar, por ejemplo **Vista de calle** (una clave de Google Maps) o **Buscar** (las fuentes de datos del buscador): se indican en la pestaña **Parámetros** de la tarea, como se explica en cada una.

## Parámetros

Las tareas básicas son parametrizables.

Los parámetros que pueden añadirse a estas tareas son aquellos admitidos por los controles de la API SITNA. Se añaden en la pestaña **Parámetros** de la tarea: cada parámetro tiene un nombre (el de la opción del control), un tipo y un valor; en los de tipo objeto o lista, el valor es un JSON.

## Tareas básicas incluidas

Las tareas básicas que incluye SITMUN se describen agrupadas en cuatro páginas. Cada una aparece con el nombre que muestra el administrador en castellano y, entre paréntesis, su nombre en inglés:

| Grupo | Tareas |
| --- | --- |
| [Navegación y vista](navegacion.md) | Vista 3D (3D View), Pantalla completa (Full Screen), Geolocalización (Geolocation), Barra de navegación (Navigation Bar), Mapa de situación (Overview Map), Escala (Scale), Barra de escala (Scale Bar), Selector de escala (Scale Selector), Vista de calle (Street View) |
| [Capas](capas.md) | Selector de mapa base (Basemap Selector), Cargador de datos (Data Loader), Catálogo de capas (Layer Catalog), Leyenda (Legend), Gestor de capas de trabajo (Work Layer Manager) |
| [Información](informacion.md) | Clic (Click), Coordenadas (Coordinates), Información de entidad (Feature Info), Información avanzada (More Info Advanced), Información múltiple de entidades (Multi Feature Info), Ventana emergente (Popup) |
| [Herramientas](herramientas.md) | Atribución (Attribution), Descarga (Download), Dibujar, Medir y Modificar (Draw, Measure and Modify), Indicador de carga (Loading Indicator), Medir (Measure), Creador de mapas sin conexión (Offline Map Maker), Imprimir mapa (Print Map), Buscar (Search), Compartir (Share), Consulta WFS (WFS Query), Edición WFS (WFSEdit) |
