# Servidores

## API de Autenticación

- **Proporcionar token de acceso [JSON web token](https://jwt.io/) (JWT)**
que permite al usuario acceder a los servicios de la plataforma. 

- **Autenticación local**. SITMUN almacena las contraseñas de los usuarios en la base de datos SITMUN usando un hash
criptográfico ([bcrypt](https://es.wikipedia.org/wiki/Bcrypt)).

- **Autenticación LDAP**. Está soportado la autenticación a través de un servidor LDAP.

## API de Configuración y Autorización

- **Proporcionar configuración a clientes**. Proporciona la configuración necesaria para que el visor de mapas se configure 
  para cada usuario, con los territorios y aplicaciones (capas y funcionalidades) a las que tiene acceso.

- **Proporcionar configuración al proxy**. Proporciona la configuración necesaria para que cada petición realizada
  al proxy se configure para cada usuario, en función de la aplicación y el territorio seleccionados.
  La petición deben autenticarse usando una API key enviada mediante la cabecera denominada `X-SITMUN-Proxy-Key`.

- **Filtrado transparente**. Al configurar un proxy, se pueden añadir adicionalmente parámetros de filtrado 
  basados en el identificador del usuario, el identificador de la aplicación, y los identificadores del territorio.
  Estos parámetros de filtrado se añaden a la petición que se realiza al servicio o base de datos final por parte del
  proxy. Estos parámetros se gestionan mediante la [API de Administración][api-de-administracion] indicando como 
  valor una de las siguientes variables: `$USER_ID`, `$APP_ID`, `$TERR_ID` y `$TERR_COD`.

## API de Administración

!!! warning "Documentación en desarrollo"

## API de Proxy

### Aspectos globales

- **Gestión de servicios transparente**: Las peticiones a los servicios externos y consultas a bases de datos son 
  realizadas a través del proxy sin que el usuario conozca los datos que componen la solicitud al servicio o conexión 
  a base de datos.

- **Adaptación transparente**. Las peticiones se adaptan en función de la aplicación, el territorio y el usuario.

- **Personalizado**. La petición pueden autenticarse usando un esquema de *autenticación por portador*
  (*[Bearer authentication](https://swagger.io/docs/specification/authentication/bearer-authentication/)*)
  usando un token que se ha obtenido previamente mediante la [API de Autenticación][api-de-autenticacion].
  Si no se autentica, se asume que la petición se ha realizado por un usuario
  que en el dominio de SITMUN se denomina *usuario público*. 

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
