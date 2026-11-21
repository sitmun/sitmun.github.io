---
description: "Tareas de SITMUN 3: qué son y qué tipos de tarea ofrece el administrador."
---

# Tareas

Las tareas de SITMUN 3 son un conjunto de elementos que permiten realizar determinadas acciones de interacción con el usuario.

La base de la mayoría de las tareas son los controles de la API SITNA. Esta API permite realizar determinadas acciones de interacción con el usuario, y SITMUN 3 aprovecha estas funcionalidades para implementar nuevas tareas más adaptadas a las necesidades y requisitos de SITMUN 3.

Las tareas se clasifican en [grupos de tareas](../grupos-de-tareas.md). Los tipos de tarea son:

- [Tareas básicas](basicas/index.md): las herramientas básicas del visor (selector de mapas de fondo, leyenda, impresión, medición…).
- [Tareas de consulta](consulta.md): consultas a bases de datos y otras fuentes, que utilizan otras tareas.
- [Tarea de localizador](localizador.md): sitúa un elemento en el mapa del visor.
- [Plantillas](plantillas.md): dan formato a la información obtenida con las consultas.
- [Tarea de más información avanzada](mas-informacion-avanzada.md): amplía la información de un elemento seleccionado en el mapa.

Estos tipos de tarea también existen en SITMUN 1.3.0 y aparecen en el menú **Tarea** del administrador,
pero su documentación todavía no está escrita. Lo esencial de cada una:

- **Tarea de imagen de mapa**: genera una imagen del mapa para usarla en [plantillas](plantillas.md); el visor no la muestra directamente.
- **Exportación documental**: genera documentos PDF a partir de [plantillas](plantillas.md). Se configuran el motor, la salida,
  el tamaño y la orientación de la página. No es una tarea hija: se asigna a roles y territorios
  como cualquier tarea, y entonces las ventanas de [más información avanzada](mas-informacion-avanzada.md) del visor muestran el botón para exportar el PDF.
- **Tarea de edición**: edición de datos, en base de datos o en servicios WFS. En la versión 1.3.0 solo la usa la aplicación
  móvil de edición; el visor web no la muestra.
- **Tarea de más información**: necesita una capa, una tarea de consulta y la correspondencia entre los parámetros de la
  consulta y los campos de la capa. El resultado aparece dentro de la ventana de información (GetFeatureInfo) de esa capa.
