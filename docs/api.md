# Referencia

## API de Autenticación {#api-de-autenticacion}

La API de Autenticación expone vía una API Web mecanismos para interactuar con el sistema de seguridad de SITMUN.
Esta API se ha creado para que la **aplicación de administración** y los **visores de mapas obtengan**,
tras pasar las credenciales de usuario obtengan un token de acceso JSON web token (JWT) necesario para operar con el resto de las API.

## API de Configuración y Autorización {#api-de-configuracion-y-autorizacion}

La API de Configuración y Autorización expone vía una API Web mecanismos para obtener una configuración derivada del estado actual de los objetos de dominio
en función de la identidad y rol del que solicita la información.
Esta API se ha creado para que los **visores de mapas** y el **proxy** puedan configurarse.

La API de Configuración y Autorización se compone de dos tipos de endpoints:

- **Configuración y Autorización de Visor de mapas**.
  La petición pueden autenticarse usando un esquema de autenticación por portador (Bearer authentication)
  usando un token que se ha obtenido previamente mediante la API de Autenticación.
  Si no se autentica, se asume que la petición se ha realizado por un usuario que en el dominio de **SITMUN 3** se denomina
  *usuario público*.
- **Configuración y Autorización de Proxy**.
  La petición debe autenticarse usando una API key enviada mediante la cabecera denominada `X-SITMUN-Proxy-Key`.
  El uso de una API key específica para el endpoint **Configuración y Autorización de Proxy** es una decisión de seguridad.
  Evita que a un cliente malicioso le pueda bastar el uso del token obtenido de la API de Autenticación
  para obtener secretos vía el endpoint **Configuración y Autorización de Proxy**.

## API de Proxy {#api-de-proxy}

La API de Proxy (Proxy Middleware) permite acceder a los visores de mapas a servicios remotos y bases de datos.

Los **visores de mapas** pueden autenticarse usando un esquema de autenticación por portador (Bearer authentication)
usando un token que se ha obtenido previamente mediante la API de Autenticación.
Si no se autentica, se asume que la petición se ha realizado por un usuario que en el dominio de **SITMUN 3** se denomina
*usuario público*.

## API de Administración {#api-de-administracion}

La API de Administración expone vía una API Web mecanismos para modificar el estado de los objetos de dominio
de **SITMUN 3** por parte de la **aplicación de administración**.
La **aplicación de administración** debe autenticarse con un JSON Web Token obtenido de la API de Autenticación.
