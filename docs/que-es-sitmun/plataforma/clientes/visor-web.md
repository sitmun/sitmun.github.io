---
description: "Cliente web de SITMUN 3, basado en la API SITNA: visor de mapas en el navegador para los usuarios de SITMUN, con sus requisitos de diseño originales."
---

# Cliente web (API SITNA)

El cliente web es **el visor de mapas con el que trabajan los usuarios de SITMUN desde el navegador**. Está basado en la [API SITNA](https://github.com/sitna/api-sitna) y se publica con la instalación en `/viewer/` (código en la carpeta `sitmun-viewer` de [sitmun/sitmun](https://github.com/sitmun/sitmun)).

| | |
| --- | --- |
| **Para quién** | Usuarios de SITMUN: público general (usuario *público*, sin identificación) y personal técnico de las entidades |
| **Plataforma** | Navegador web, también en dispositivos móviles |
| **Dirección** | `/viewer/` |

## Cómo se configura

El visor no tiene una configuración fija: al arrancar la pide a la API de Configuración y Autorización, y la recibe adaptada al usuario, el territorio y la aplicación elegidos. Lo que ofrece (capas, herramientas, mapas de fondo) lo define el administrador en el [cliente de administración](administrador.md).

La mayor parte de las herramientas del visor provienen de la API SITNA y se activan como [tareas básicas](../../../usuario/manual/administrador/tareas/basicas/index.md).

## Requisitos originales

!!! note
    Este apartado recoge los requisitos con los que se diseñó el visor de mapas.
    No todos están disponibles; la lista de herramientas que se pueden activar
    está en [Tareas básicas](../../../usuario/manual/administrador/tareas/basicas/index.md).

### Aspectos globales

- **Responsivo**: para entorno web y dispositivos móviles.

- **Compatibilidad**: compatible con los navegadores más comunes.

- **Autenticación**: el cliente estará diseñado para utilizar solo HTTP sobre TLS (HTTPS).
  En caso de ser un visor público, el usuario ingresará directamente sin inicio de sesión.
  El cliente debe permitir la autenticación del usuario frente a la [API de Autenticación][api-de-autenticacion].
  La API responderá con un token JSON Web Token (JWT) en una cookie de sesión, que se utilizará para interactuar con la
  [API de Configuración y Autorización][api-de-configuracion-y-autorizacion]. Para la [API de Proxy][api-de-proxy]
  el cliente pide un token de corta duración.

- **Inicio de sesión**: botón de inicio de sesión.
  El botón de inicio de sesión inicia el proceso descrito en la funcionalidad de autenticación, seguido,
  en caso de éxito, por la funcionalidad de configuración del cliente.

- **Cierre de sesión**: botón de cierre de sesión.
  El botón de cierre de sesión borra el token de la aplicación, en caso de existir,
  seguido de la funcionalidad de configuración del cliente (en este caso, sin token).

- **Multilingüe**: visores multilingües (que puedan hacer peticiones localizadas).

- **Configuración de los clientes**: el cliente se configura mediante una petición a
  la [API de Configuración y Autorización][api-de-configuracion-y-autorizacion]. Si el usuario ha iniciado sesión,
  la petición incluye la cookie de sesión obtenida de la [API de Autenticación][api-de-autenticacion].
  En caso de ser un visor público, la petición no incluirá un token.
  A partir de los datos de configuración (gestionados por la **aplicación de administración**),
  el visor se configura para cada usuario, con los territorios y aplicaciones (capas y funcionalidades)
  a las que tiene acceso.

- **Peticiones a servicios remotos**: las peticiones a algunos servicios remotos se realizan a través de
  la [API de Proxy][api-de-proxy]. Las peticiones deben ir acompañadas de un token JWT,
  obtenido previamente de la [API de Autenticación][api-de-autenticacion], que identifica al usuario.
  La única excepción es el caso del usuario *público*, donde la autenticación es automática.
  Es decir, si no tiene una credencial, se asume que es el usuario *público*.
  Todas las peticiones enviadas a través de la [API de Proxy][api-de-proxy] deben incluir, además,
  un identificador de territorio y un identificador de aplicación.

- **Secuencia de inicio**: el cliente solicitará a la [API de Configuración y Autorización][api-de-configuracion-y-autorizacion]
  una configuración básica (territorios y aplicaciones disponibles) para mostrar al usuario lo que puede seleccionar; los idiomas
  los obtiene de la API de Administración (`GET /api/languages`).
  El usuario podrá autenticarse frente a la [API de Autenticación][api-de-autenticacion],
  lo que restringirá los territorios y aplicaciones disponibles. Una vez seleccionado el idioma, territorio y aplicación,
  se iniciará la configuración del cliente frente a la [API de Configuración y Autorización][api-de-configuracion-y-autorizacion].
  La secuencia anterior se puede modificar en función de los parámetros pasados en la petición.
  Se puede restringir a una aplicación y territorio específicos e indicar que debe comenzar como visor público.
  Si se indica que debe comenzar como visor público, solo se pedirá al usuario que seleccione el idioma antes de
  pasar a la configuración del cliente.

### Funcionalidades básicas de navegación

- **Zoom con desplazamiento**: zoom dinámico con desplazamiento del ratón. Doble clic en el mapa para acercarse.

- **Pan**: arrastrar el mapa con el ratón.

- **Barra de zoom**: barra deslizante vertical.

- **Control de escala**: selector automático de nivel de escala.

- **Zoom a ventana**: zoom a ventana (acceso rápido vía mayúsculas más ratón).

- **Zoom de extensión**: botón de Zoom de extensión.

### Funcionalidad de gestión de capas

- **Orden de capas**: posibilidad de modificar el orden de visualización de las capas.

- **Árbol de capas**: árbol de capas configurable para cada cliente a partir de la combinación de capas de diferentes servicios.

- **Clasificación de capas**: opción para que el usuario pueda elegir entre diferentes árboles de capas previamente configurados por el administrador.

- **Transparencia**: control de la transparencia de las capas.

- **Capas externas**: incorporación de capas externas (WMS, WFS, Atom, GeoJSON, KML, SHP…).

- **Metadatos**: botón con enlace a ficha de metadatos simplificados (extraídos dinámicamente del archivo XML de metadatos)
  con la opción de abrir en segunda instancia el XML completo de los metadatos.

- **Leyenda**: consulta de la leyenda de la capa.

- **Descarga**: enlace para descargar la capa (solo visible en caso de ser una capa descargable) y archivos relacionados
  (configurados en el administrador).

- **Búsqueda de capas**: opción de buscar capas por nombre y descripción, en función del idioma del visor.
  Integrado con el buscador genérico.

- **Mapa de fondo**: selección del mapa de fondo.

- **Grupos de capas**: diferenciar entre capas y grupos de capas y permitir interactuar (visualizar, descargar, metadatos, etc.)
  con ambos elementos de la misma manera tanto para capas como para grupos.

- **Capas activas**: ventana donde se presenten todas las capas activas, tanto las activadas desde el árbol como las cargadas de manera externa.

### Herramientas básicas

- **Imprimir**: impresión configurable del mapa, la leyenda, el gráfico, el título, el norte, logotipos, etc.

- **Medición y dibujo**: integración de herramientas de medición de áreas, distancias y coordenadas de un punto con las
  de dibujo de elementos sobre el mapa.

    - Modificar la simbología del elemento dibujado.
    - Imprimir los elementos dibujados al imprimir el mapa.
    - Creación de perfiles del terreno de las líneas medidas.
    - Guardar localmente los elementos dibujados en formato KML.
    - Generar enlace para compartir el mapa con los elementos dibujados.
    - Posibilidad de añadir textos sobre el mapa.

- **Obtener posición**: en caso de estar disponible en el dispositivo, botón para obtener la posición del usuario.

- **Leyenda**: ventana que muestra la leyenda construida de manera dinámica para todas las capas activas.

- **Portapapeles**: copia fácil del mapa, la leyenda o el gráfico (uno o varios) al portapapeles.

- **Pantalla completa**: posibilidad de poner el visor en modo de pantalla completa.

### Información

- **Información**: botón para solicitar información alfanumérica de los elementos gráficos de las capas activas
  (información y más información actual). Formatea la tabla de respuesta por defecto con una apariencia atractiva,
  clara y amigable para el usuario, y presentar imágenes y enlaces por defecto.
  Hay opción de organizar la información en pestañas.
  Es importante poder personalizar las ventanas de información en función de cada capa,
  más allá de especificar el tipo para cada campo (foto, texto, URL, etc.),
  tal y como permite ahora el acceso al código de cada tarea.

### Buscadores, consultas y selección espacial

- **Buscador básico**: búsqueda de topónimos básica integrada con el buscador de capas.
  Muestra candidatos a partir del tercer carácter y diferencia en la lista entre topónimos y capas.

### Herramientas avanzadas

- **Compartir**: posibilidad de compartir el mapa de diferentes maneras:

    - A través de un enlace.
    - A través de un `iframe` configurable con las capas activas en el momento de generar el `iframe` y
      en el que se pueda hacer `GetFeatureInfo` de las capas y algunas herramientas básicas (cambiar el fondo del mapa).
    - Enlace a redes sociales.
    - Generar código QR.

- **WMC**: posibilidad de guardar el WMC (vinculado a la funcionalidad anterior).

- **Operaciones espaciales**: posibilidad de realizar operaciones espaciales entre capas como la intersección espacial
  aplicando un buffer.

### Otras herramientas

- **Street View**: herramienta para agregar Street View al mapa.

[api-de-autenticacion]: ../arquitectura/api.md#api-de-autenticacion
[api-de-configuracion-y-autorizacion]: ../arquitectura/api.md#api-de-configuracion-y-autorizacion
[api-de-proxy]: ../arquitectura/api.md#api-de-proxy
