---
description: "Las API web de SITMUN 3: autenticación, configuración y autorización, proxy y administración."
---

# API

**SITMUN 3** expone cuatro API web. Para cada una se describe para qué sirve y qué funcionalidades ofrece.

## API de Autenticación {#api-de-autenticacion}

La API de Autenticación ofrece, mediante una API web, mecanismos para interactuar con el sistema de seguridad de SITMUN.
Esta API se ha creado para que la **aplicación de administración** y los **visores de mapas** obtengan,
tras pasar las credenciales del usuario, un token de acceso JSON Web Token (JWT) necesario para operar con el resto de las API.

### Funcionalidades {#api-de-autenticacion-funcionalidades}

- **Proporcionar token de acceso [JSON web token](https://jwt.io/) (JWT)**
  que permite al usuario acceder a los servicios de la plataforma.
  En el visor y el administrador el token se guarda en una cookie *HttpOnly*
  (`viewer_access_token` o `admin_access_token`) que se renueva con `POST /api/authenticate/refresh`
  y se borra con `POST /api/authenticate/logout`.
  La ruta del inicio de sesión decide qué cookie se crea: el visor usa `POST /api/authenticate`, que crea
  `viewer_access_token`, y el administrador usa `POST /api/authenticate/admin`, que crea `admin_access_token`.
  Iniciar sesión en `POST /api/authenticate` con la cabecera `X-SITMUN-Client: admin` crea igualmente la cookie del visor,
  y con ella la API de Administración responde 401.
  En las llamadas siguientes, la cabecera `X-SITMUN-Client` indica qué cookie se lee: el administrador envía
  `X-SITMUN-Client: admin` en todas ellas, también en `refresh` y `logout`. Sin la cabecera se lee la cookie del visor,
  así que una llamada a la API de Administración con la cookie `admin_access_token` y sin la cabecera responde 401.
  SITMUN Mobile Editor usa `POST /api/authenticate/mobile`, que devuelve el token en el cuerpo de la respuesta.
  Solo funciona si el usuario tiene acceso al menos a una aplicación de tipo «Edition application» (código `ED`); si no,
  responde 403.
  Para llamar al proxy, el cliente pide un token de corta duración con `POST /api/authenticate/proxy`.

- **Autenticación local**. SITMUN almacena las contraseñas de los usuarios en la base de datos SITMUN usando un hash
  criptográfico ([bcrypt](https://en.wikipedia.org/wiki/Bcrypt)).

- **Autenticación LDAP**. SITMUN admite la autenticación a través de un servidor LDAP (perfil Spring `ldap`).

- **Autenticación OpenID Connect (OIDC)**. SITMUN admite la autenticación con uno o varios proveedores OIDC (perfil Spring `oidc`).
  El cliente consulta los métodos activos en `GET /api/auth/enabled-methods`.

- **Verificación de usuarios**. Endpoints para verificar contraseñas y disponibilidad de correo electrónico.

- **Recuperación de contraseña**. Sistema de recuperación de contraseña por correo electrónico con tokens seguros.
  Solo está disponible con el perfil `mail` del backend y un servidor de correo configurado
  (ver [Instalación](../../../usuario/instalacion/instalacion.md)); sin él, `POST /api/password-reset/request` responde 404.

## API de Configuración y Autorización {#api-de-configuracion-y-autorizacion}

La API de Configuración y Autorización ofrece, mediante una API web, mecanismos para obtener una configuración derivada del estado actual de los objetos de dominio
en función de la identidad y rol del que solicita la información.
Esta API se ha creado para que los **visores de mapas** y el **proxy** (SITMUN Proxy Middleware) puedan configurarse.

La API de Configuración y Autorización se compone de dos tipos de endpoints:

- **Configuración y Autorización de Visor de mapas** (`/api/config/client/…`).
  La petición se autentica con la cookie de sesión obtenida previamente mediante la API de Autenticación
  (SITMUN Mobile Editor usa un token *Bearer*).
  Si no se autentica, se asume que la petición se ha realizado por un usuario que en el dominio de **SITMUN 3** se denomina
  *usuario público*.
- **Configuración y Autorización de Proxy** (`POST /api/config/proxy`).
  La petición debe autenticarse usando una clave de API (*API key*) enviada mediante la cabecera denominada `X-SITMUN-Proxy-Key`.
  El token del usuario, si lo hay, se reenvía en la cabecera `Authorization: Bearer`.
  El uso de una clave de API específica para el endpoint **Configuración y Autorización de Proxy** es una decisión de seguridad.
  Evita que a un cliente malicioso le pueda bastar el uso del token obtenido de la API de Autenticación
  para obtener secretos mediante el endpoint **Configuración y Autorización de Proxy**.

### Funcionalidades {#api-de-configuracion-y-autorizacion-funcionalidades}

- **Proporcionar configuración a clientes**. Proporciona la configuración necesaria para que el visor de mapas se configure
  para cada usuario, con los territorios y aplicaciones (capas y funcionalidades) a las que tiene acceso.

- **Proporcionar configuración al proxy**. Proporciona la configuración necesaria para que cada petición realizada
  al proxy se configure para cada usuario, en función de la aplicación y el territorio seleccionados.

- **Filtrado transparente**. Al configurar un proxy, se pueden añadir adicionalmente parámetros de filtrado
  basados en el identificador del usuario, el identificador de la aplicación, y los identificadores del territorio.
  Estos parámetros de filtrado se añaden a la petición que se realiza al servicio o base de datos final por parte del
  proxy. Estos parámetros se gestionan mediante la [API de Administración][api-de-administracion] indicando como
  valor una variable de sistema con la sintaxis `#{NOMBRE}`, por ejemplo `#{USER_ID}`, `#{APP_ID}`, `#{TERR_ID}` o `#{TERR_COD}`.
  La lista completa está en la página [Variables de sistema](../../../usuario/manual/administrador/variables-sistema.md).

## API de Proxy {#api-de-proxy}

La API de Proxy (**SITMUN Proxy Middleware**) permite a los visores de mapas acceder a servicios remotos y bases de datos.

Los **visores de mapas** pueden autenticarse usando un esquema de autenticación por portador (Bearer authentication)
usando un token de corta duración que se ha obtenido previamente mediante la [API de Autenticación][api-de-autenticacion]
(`POST /api/authenticate/proxy`).
Si no se autentica, se asume que la petición se ha realizado por un usuario que en el dominio de **SITMUN 3** se denomina
*usuario público*.

<a id="problema-token-proxy-1-3-0"></a>

!!! warning "Problema conocido en la versión 1.3.0"
    En la versión 1.3.0, el token de corta duración que el visor pide para el proxy no incluye la fecha del último cambio de contraseña.
    Por eso, los usuarios con esa fecha registrada reciben 401 en todas las capas y tareas que el visor pide a través del proxy.

    - **Usuarios afectados**: el usuario `admin` cuya contraseña se creó en el primer acceso (o con `SITMUN_BOOTSTRAP_ADMIN_PASSWORD`)
      y cualquier usuario que haya restablecido su contraseña con la recuperación de contraseña.
      Poner o cambiar la contraseña desde el formulario de usuarios no registra la fecha.
    - **Alcance**: las capas de los servicios con «Usar proxy SITMUN» activado (la opción se activa sola en los servicios con
      autenticación) y las tareas que el backend dirige al proxy: las consultas SQL, de API web (salvo las de API web sin
      proxy, de ámbito `web-api-query-no-proxy`) y sobre capas, la edición de capas, y los localizadores y las tareas de más
      información que usan SQL o una API.
    - **No afectados**: el usuario público y las capas que el visor carga directamente, sin pasar por el proxy.

    No se puede evitar con la configuración.
    La variable `FORCE_USE_OF_PROXY` de Docker Compose no tiene efecto en la versión 1.3.0
    ([sitmun/sitmun#389](https://github.com/sitmun/sitmun/issues/389)): pasan por el proxy los servicios con «Usar proxy SITMUN»
    y las tareas que el backend dirige al proxy (las de la lista anterior).
    Más información en [sitmun/sitmun#387](https://github.com/sitmun/sitmun/issues/387).

### Aspectos globales

- **Gestión de servicios transparente**: las peticiones a los servicios externos y consultas a bases de datos son
  realizadas a través del proxy sin que el usuario conozca los datos que componen la solicitud al servicio o conexión
  a base de datos.

- **Adaptación transparente**: las peticiones se adaptan en función de la aplicación, el territorio y el usuario.

- **Modificación de peticiones**: posibilidad de manipular la petición de varias formas para que se adapte a la
  configuración obtenida de la [API de Configuración y Autorización][api-de-configuracion-y-autorizacion].

<a id="servicios-soportados"></a>

### Servicios compatibles

Las peticiones tienen la forma `/proxy/{appId}/{terId}/{type}/{typeId}` (o `/proxy/{appId}/{terId}/{type}/{serviceId}/{cartographyId}`
para una capa concreta) y pueden usar los métodos HTTP GET o POST; las peticiones POST a los servicios deben llevar un cuerpo XML (por ejemplo, una petición WFS) con la cabecera `Content-Type: application/xml`; con otro tipo de contenido, también `text/xml`, el proxy responde 415. La exportación MBTiles es la excepción: sus peticiones POST (`/proxy/{appId}/{terId}/mbtiles` y `/proxy/{appId}/{terId}/mbtiles/estimate`) llevan un cuerpo JSON.

- **Servicios [OGC Web Map Service (WMS)](https://www.ogc.org/standard/wms/)**,
  que ofrecen mapas en formato imagen.

- **Servicios [OGC Web Map Tile Service (WMTS)](https://www.ogc.org/standard/wmts/)**,
  que proporcionan mapas divididos en teselas (*tiles*).

- **Servicios [OGC Web Feature Service (WFS)](https://www.ogc.org/standard/wfs/)**,
  que permiten el acceso a datos geoespaciales vectoriales.

- **Web API** usadas por las tareas de consulta de tipo *Web API*.

- **Bases de datos relacionales** accesibles con un controlador (*driver*)
  [JDBC (Java Database Connectivity)](https://es.wikipedia.org/wiki/Java_Database_Connectivity)
  incluido en el proxy (PostgreSQL, Oracle, Microsoft SQL Server y H2).
  Las respuestas de las bases de datos se devuelven en formato JSON.

- **Exportación MBTiles** (opcional): trabajos de generación de paquetes de teselas para SITMUN Mobile Editor,
  delegados al servicio `mbtiles`.

### Modificadores generales

- **Parámetros (Servicios)**: modificador encargado de añadir a la petición los parámetros proporcionados por el visor y
  la [API de Configuración y Autorización][api-de-configuracion-y-autorizacion]. La [API de Configuración y Autorización][api-de-configuracion-y-autorizacion]
  puede haber añadido parámetros a la petición que el visor no ha proporcionado (por ejemplo, parámetros de filtrado).

- **Autenticación de acceso básica (Servicios)**: modificador encargado de incluir en la cabecera de la petición HTTP un usuario y contraseña si fuese necesario ([RFC 7617](https://datatracker.ietf.org/doc/html/rfc7617)).

- **Clave de API (consultas Web API)**: modificador encargado de añadir una clave de acceso en una cabecera o en un parámetro de la consulta. Los servicios OGC (WMS, WFS, WMTS) solo admiten autenticación HTTP básica.

- **Selección (JDBC)**: modificador encargado de crear la conexión con base de datos con los datos proporcionados por la [API de Configuración y Autorización][api-de-configuracion-y-autorizacion].

- **Filtrado (JDBC)**: modificador encargado de incluir filtros en la consulta.
  Los parámetros (`${nombre}`) y las variables de sistema (`#{NOMBRE}`) se envían como valores tipados
  y nunca se concatenan en el texto SQL.

## API de Administración {#api-de-administracion}

La API de Administración ofrece, mediante una API web, mecanismos para modificar el estado de los objetos de dominio
de **SITMUN 3** por parte de la **aplicación de administración**.
El visor usa además algunos de sus endpoints: `GET /api/languages` y `GET /api/configuration-parameters`,
abiertos sin sesión, para los idiomas y los parámetros de configuración; `GET` y `POST /api/account`, para el rol `USER`,
para los datos y el perfil del usuario identificado; y `POST /api/tasks/template/more-info-advanced/render`
y `POST /api/tasks/template/export`, abiertos a los roles `USER`, `ADMIN` y `PUBLIC`, para mostrar y exportar las plantillas
de las tareas de *más información avanzada*.
La **aplicación de administración** se autentica con la cookie de sesión (`admin_access_token`) que crea `POST /api/authenticate/admin`
en la [API de Autenticación][api-de-autenticacion] y envía la cabecera `X-SITMUN-Client: admin` en cada llamada.
La documentación interactiva de todos los endpoints está en Swagger UI (`/swagger-ui/index.html` en el backend).

### Funcionalidades {#api-de-administracion-funcionalidades}

- **Gestión de usuarios**. CRUD completo de usuarios con roles y permisos.

- **Gestión de territorios**. Administración de territorios y sus configuraciones.

- **Gestión de aplicaciones**. Configuración de aplicaciones y sus funcionalidades.

- **Gestión de tareas**. Configuración de tareas y herramientas disponibles.

- **Gestión de capas**. Administración de capas cartográficas y servicios.

- **Pruebas de conexión**. Herramientas para probar conexiones a bases de datos.

- **Extracción de capacidades**. Herramientas para extraer capacidades de servicios OGC.

- **Extracción de tipos de entidad**. Herramientas para extraer información de tipos de entidad.

- **Primer arranque**. `GET /api/setup/status` y `POST /api/setup/first-run` crean la contraseña del administrador y fijan el idioma por defecto en una instalación nueva.

- **Idiomas y traducciones**. Cambio del idioma por defecto con vista previa e importación y exportación en CSV de las traducciones de literales.

- **Monitorización de servicios**. Comprobación periódica de los servicios y estadísticas de uso.

[api-de-autenticacion]: #api-de-autenticacion
[api-de-configuracion-y-autorizacion]: #api-de-configuracion-y-autorizacion
[api-de-administracion]: #api-de-administracion
