# Clientes

## Visores de mapas

### Aspectos globales

- **Responsivo**: Para entorno web y dispositivos móviles.

- **Compatibilidad**: Compatible con los navegadores más comunes.

- **Autenticación**: El cliente estará diseñado para utilizar solo HTTP sobre TLS (HTTPS).
  En caso de ser un visor público, el usuario ingresará directamente sin inicio de sesión.
  El cliente debe permitir la autenticación del usuario frente a la [API de autenticación][api-de-autenticacion].
  La API responderá con el envío de un token JSON Web Token (JWT) que se utilizará para interactuar con la
  [API de configuración y autorización][api-de-configuracion-y-autorizacion] y la [API de Proxy][api-de-proxy].

- **Inicio de sesión**: Botón de inicio de sesión.
  El botón de inicio de sesión inicia el proceso descrito en la funcionalidad de autenticación, seguido,
  en caso de éxito, por la funcionalidad de configuración del cliente.

- **Cierre de sesión**: Botón de cierre de sesión.
  El botón de cierre de sesión borra el token de la aplicación, en caso de existir,
  seguido de la funcionalidad de configuración del cliente (en este caso, sin token).

- **Multilingüe**: Visualizadores multilingües (que puedan hacer solicitudes localizadas).

- **Configuración de los clientes**: El cliente se configura mediante una solicitud a
  la [API de configuración y autorización][api-de-configuracion-y-autorizacion]. Si el usuario ha iniciado sesión,
  la solicitud debe incluir el token JWT obtenido de la [API de autenticación][api-de-autenticacion].
  En caso de ser un visualizador público, la solicitud no incluirá un token.
  A partir de los datos de configuración (gestionados por la **aplicación de administrador**),
  el visor se configura para cada usuario, con los territorios y aplicaciones (capas y funcionalidades)
  a las que tiene acceso. 

- **Solicitudes a servicios remotos**: Las solicitudes a algunos servicios remotos se realizan a través de
  la [API de Proxy][api-de-proxy]. Las solicitudes deben ir acompañadas de un token JWT,
  obtenido previamente de la [API de autenticación][api-de-autenticacion], que identifica al usuario.
  La única excepción es el caso del usuario *público*, donde la autenticación es automática.
  Es decir, si no tiene una credencial, se asume que es el usuario *público*.
  Todas las solicitudes enviadas a través de la [API de Proxy][api-de-proxy] deben incluir, además,
  un identificador de territorio y un identificador de aplicación.

- **Secuencia de inicio**: el cliente solicitará a la [API de configuración y autorización][api-de-configuracion-y-autorizacion]
  una configuración básica (idiomas, territorios, aplicaciones disponibles) para mostrar al usuario lo que puede seleccionar.
  El usuario podrá autenticarse frente a la [API de autenticación][api-de-autenticacion],
  lo que restringirá los territorios y aplicaciones disponibles. Una vez seleccionado el idioma, territorio y aplicación,
  se iniciará la configuración del cliente frente a la [API de configuración y autorización][api-de-configuracion-y-autorizacion].
  La secuencia anterior se puede modificar en función de los parámetros pasados en la petición.
  Se puede restringir a una aplicación y territorio específicos e indicar que debe comenzar como visualizador público.
  Si se indica que debe comenzar como visualizador público, solo se pedirá al usuario que seleccione el idioma antes de
  pasar a la configuración del cliente.

### Funcionalidades básicas de navegación

- **Zoom con desplazamiento**: Zoom dinámico con desplazamiento del ratón. Doble clic en el mapa para hacer Zoom-in.

- **Pan**: Botón derecho del ratón y arrastrar el botón.

- **Barra de zoom**: Barra deslizante vertical.

- **Control de escala**: Selector automático de nivel de escala.

- **Zoom a ventana**: Zoom a ventana (acceso rápido vía mayúsculas más ratón).

- **Zoom de extensión**: Botón de Zoom de extensión.

### Funcionalidad de gestión de capas

- **Orden de capas**: Posibilidad de modificar el orden de visualización de las capas.

- **Árbol de capas**: Árbol de capas configurable para cada cliente a partir de la combinación de capas de diferentes servicios.

- **Clasificación de capas**: Opción para que el usuario pueda elegir entre diferentes árboles de capas previamente configuradas por el administrador.

- **Transparencia**: Control de la transparencia de las capas.

- **Capas externas**: Incorporación de capas externas (WMS, WFS, ATOM, GEOJSON, KML, SHP, ...).

- **Metadatos**: Botón con enlace a ficha de metadatos simplificados (extraídos dinámicamente del archivo XML de metadatos)
  con la opción de abrir en segunda instancia el XML completo de los metadatos.

- **Leyenda**: Consulta de la leyenda de la capa.

- **Descarga**: Enlace para descargar la capa (solo visible en caso de ser una capa descargable) y archivos relacionados
  (configurados en el administrador).

- **Búsqueda de capas**: Opción de buscar capas por nombre y descripción, en función del idioma del visualizador.
  Integrado con el buscador genérico.

- **Mapa base**: Selección del mapa base.

- **Grupos de capas**: Diferenciar entre capas y grupos de capas y permitir interactuar (visualizar, descargar, metadatos, etc.)
  con ambos elementos de la misma manera tanto para capas como para grupos.

- **Capas activas**: Ventana donde se presenten todas las capas activas, tanto las activadas desde el árbol como las cargadas de manera externa.

### Herramientas básicas

- **Imprimir**: Impresión configurable del mapa, la leyenda, el gráfico, el título, el norte, logotipos, etc.

- **Medición y dibujo**: Integración de herramientas de medición de áreas, distancias y coordenadas de un punto con las
  de dibujo de elementos sobre el mapa.

    - Modificar la simbología del elemento dibujado.
    - Imprimir los elementos dibujados al imprimir el mapa.
    - Creación de perfiles del terreno de las líneas medidas.
    - Guardar localmente los elementos dibujados en formato KML.
    - Generar enlace para compartir el mapa con los elementos dibujados.
    - Posibilidad de añadir textos sobre el mapa.

- **Obtener posición**: En caso de estar disponible en el dispositivo, botón para obtener la posición del usuario.

- **Leyenda**: Ventana que muestra la leyenda construida de manera dinámica para todas las capas activas.

- **Portapapeles**: Copia fácil del mapa y/o la leyenda y/o el gráfico al portapapeles.

- **Pantalla completa**: Posibilidad de poner el visualizador en modo de pantalla completa.

### Información

- **Información**: Botón para solicitar información alfanumérica de los elementos gráficos de las capas activas
  (información y más información actual). Formatea la tabla de respuesta por defecto con una apariencia atractiva,
  clara y amigable para el usuario, y presentar imágenes y enlaces por defecto.
  Hay opción de organizar la información en pestañas.
  Es importante poder personalizar las ventanas de información en función de cada capa,
  más allá de especificar el tipo para cada campo (foto, texto, URL, etc.),
  tal y como permite ahora el acceso al código de cada tarea.

### Buscadores, consultas y selección espacial

- **Buscador básico**: Búsqueda de topónimos básica integrada con el buscador de capas.
  Muestra candidatos a partir del tercer carácter y diferencia en la lista entre topónimos y capas.

### Herramientas avanzadas

- **Compartir**: Posibilidad de compartir el mapa de diferentes maneras:

    - A través de un enlace.
    - A través de un IFRAME configurable con las capas activas en el momento de generar el IFRAME y
      en el que se pueda hacer `GetFeatureInfo` de las capas y algunas herramientas básicas (cambiar el fondo del mapa).
    - Enlace a redes sociales (Twitter, Facebook).
    - Generar código QR.

- **WMC**: Posibilidad de guardar el WMC (vinculado a la funcionalidad anterior).

- **Operaciones espaciales**: Posibilidad de realizar operaciones espaciales entre capas como la intersección espacial
  aplicando un buffer.

### Otras herramientas

- **Streetview**: Herramienta para agregar Street View al mapa.

## Aplicación de Administración

!!! warning "Documentación en desarrollo"

[api-de-autenticacion]: api.md#api-de-autenticacion
[api-de-configuracion-y-autorizacion]: api.md#api-de-configuracion-y-autorizacion
[api-de-proxy]: api.md#api-de-proxy

## Canonical Link References

- [API de autenticación][api-de-autenticacion]
- [API de configuración y autorización][api-de-configuracion-y-autorizacion]
- [API de Proxy][api-de-proxy]
