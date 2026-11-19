# API

**SITMUN 3** expone cuatro API web. Para cada una se describe para qué sirve y qué funcionalidades ofrece.

## API de Autenticación {#api-de-autenticacion}

La API de Autenticación expone vía una API Web mecanismos para interactuar con el sistema de seguridad de SITMUN.
Esta API se ha creado para que la **aplicación de administración** y los **visores de mapas** obtengan,
tras pasar las credenciales del usuario, un token de acceso JSON Web Token (JWT) necesario para operar con el resto de las API.

### Funcionalidades {#api-de-autenticacion-funcionalidades}

- **Proporcionar token de acceso [JSON web token](https://jwt.io/) (JWT)**
  que permite al usuario acceder a los servicios de la plataforma.

- **Autenticación local**. SITMUN almacena las contraseñas de los usuarios en la base de datos SITMUN usando un hash
  criptográfico ([bcrypt](https://en.wikipedia.org/wiki/Bcrypt)).

- **Autenticación LDAP**. Está soportada la autenticación a través de un servidor LDAP.

- **Verificación de usuarios**. Endpoints para verificar contraseñas y disponibilidad de email.

- **Recuperación de contraseña**. Sistema de recuperación de contraseña por email con tokens seguros.

## API de Configuración y Autorización {#api-de-configuracion-y-autorizacion}

La API de Configuración y Autorización expone vía una API Web mecanismos para obtener una configuración derivada del estado actual de los objetos de dominio
en función de la identidad y rol del que solicita la información.
Esta API se ha creado para que los **visores de mapas** y el **proxy** puedan configurarse.

La API de Configuración y Autorización se compone de dos tipos de endpoints:

- **Configuración y Autorización de Visor de mapas**.
  La petición puede autenticarse usando un esquema de autenticación por portador (Bearer authentication)
  usando un token que se ha obtenido previamente mediante la API de Autenticación.
  Si no se autentica, se asume que la petición se ha realizado por un usuario que en el dominio de **SITMUN 3** se denomina
  *usuario público*.
- **Configuración y Autorización de Proxy**.
  La petición debe autenticarse usando una API key enviada mediante la cabecera denominada `X-SITMUN-Proxy-Key`.
  El uso de una API key específica para el endpoint **Configuración y Autorización de Proxy** es una decisión de seguridad.
  Evita que a un cliente malicioso le pueda bastar el uso del token obtenido de la API de Autenticación
  para obtener secretos vía el endpoint **Configuración y Autorización de Proxy**.

### Funcionalidades {#api-de-configuracion-y-autorizacion-funcionalidades}

- **Proporcionar configuración a clientes**. Proporciona la configuración necesaria para que el visor de mapas se configure
  para cada usuario, con los territorios y aplicaciones (capas y funcionalidades) a las que tiene acceso.

- **Proporcionar configuración al proxy**. Proporciona la configuración necesaria para que cada petición realizada
  al proxy se configure para cada usuario, en función de la aplicación y el territorio seleccionados.

- **Filtrado transparente**. Al configurar un proxy, se pueden añadir adicionalmente parámetros de filtrado
  basados en el identificador del usuario, el identificador de la aplicación, y los identificadores del territorio.
  Estos parámetros de filtrado se añaden a la petición que se realiza al servicio o base de datos final por parte del
  proxy. Estos parámetros se gestionan mediante la [API de Administración][api-de-administracion] indicando como
  valor una de las siguientes variables: `$USER_ID`, `$APP_ID`, `$TERR_ID` y `$TERR_COD`.

## API de Proxy {#api-de-proxy}

La API de Proxy (Proxy Middleware) permite acceder a los visores de mapas a servicios remotos y bases de datos.

Los **visores de mapas** pueden autenticarse usando un esquema de autenticación por portador (Bearer authentication)
usando un token que se ha obtenido previamente mediante la [API de Autenticación][api-de-autenticacion].
Si no se autentica, se asume que la petición se ha realizado por un usuario que en el dominio de **SITMUN 3** se denomina
*usuario público*.

### Aspectos globales

- **Gestión de servicios transparente**: Las peticiones a los servicios externos y consultas a bases de datos son
  realizadas a través del proxy sin que el usuario conozca los datos que componen la solicitud al servicio o conexión
  a base de datos.

- **Adaptación transparente**. Las peticiones se adaptan en función de la aplicación, el territorio y el usuario.

- **Modificación de peticiones**: Posibilidad de manipular la petición de varias formas para que se adapte a la
  configuración obtenida de la [API de configuración y autorización][api-de-configuracion-y-autorizacion].

### Servicios soportados

- **Servicios [OGC Web Map Service (WMS)](https://www.ogc.org/standard/wms/)**,
  que ofrecen mapas en formato imagen usando peticiones HTTP GET.

- **Servicios [OGC Web Map Tile Service (WMTS)](https://www.ogc.org/standard/wmts/)**,
  que proporcionan mapas divididos en teselas (*tiles*) usando peticiones HTTP GET (codificación KVP).

- **Servicios [OGC Web Feature Service (WFS)](https://www.ogc.org/standard/wfs/)**,
  que permiten el acceso a datos geoespaciales vectoriales usando peticiones HTTP GET (codificación KVP).

- **Bases de datos relacionales que dispongan de un controlador (*driver*)
  [JDBC (Java Database Connectivity)](https://es.wikipedia.org/wiki/Java_Database_Connectivity)**.
  Las respuestas de las bases de datos se devuelven en formato JSON usando peticiones HTTP GET.

### Modificadores generales

- **Parámetros (Servicios)**: Modificador encargado de añadir a la petición los parámetros proporcionados por el visor y
  la [API de configuración y autorización][api-de-configuracion-y-autorizacion]. La [API de configuración y autorización][api-de-configuracion-y-autorizacion]
  puede haber añadido parámetros a la petición que el visor no ha proporcionado (por ejemplo, parámetros de filtrado).

- **Autenticación de acceso básica (Servicios)**: Modificador encargado de incluir en la cabecera de la petición HTTP un usuario y contraseña si fuese necesario ([RFC 7617](https://datatracker.ietf.org/doc/html/rfc7617)).

- **Selección (JDBC)**: Modificador encargado de crear la conexión con base de datos con los datos proporcionados por la [API de configuración y autorización][api-de-configuracion-y-autorizacion].

- **Filtrado (JDBC)**: Modificador encargado de incluir filtros en la consulta.

## API de Administración {#api-de-administracion}

La API de Administración expone vía una API Web mecanismos para modificar el estado de los objetos de dominio
de **SITMUN 3** por parte de la **aplicación de administración**.
La **aplicación de administración** debe autenticarse con un JSON Web Token obtenido de la [API de Autenticación][api-de-autenticacion].

### Funcionalidades {#api-de-administracion-funcionalidades}

- **Gestión de usuarios**. CRUD completo de usuarios con roles y permisos.

- **Gestión de territorios**. Administración de territorios y sus configuraciones.

- **Gestión de aplicaciones**. Configuración de aplicaciones y sus funcionalidades.

- **Gestión de tareas**. Configuración de tareas y herramientas disponibles.

- **Gestión de capas**. Administración de capas cartográficas y servicios.

- **Pruebas de conexión**. Herramientas para probar conexiones a bases de datos.

- **Extracción de capacidades**. Herramientas para extraer capacidades de servicios OGC.

- **Extracción de tipos de entidad**. Herramientas para extraer información de tipos de entidad.

[api-de-autenticacion]: #api-de-autenticacion
[api-de-configuracion-y-autorizacion]: #api-de-configuracion-y-autorizacion
[api-de-administracion]: #api-de-administracion
