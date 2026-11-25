---
description: "Arquitectura de SITMUN 3: componentes, escenario típico de uso, diagramas de secuencia, módulos y paquetes del backend."
---

# Arquitectura de SITMUN 3

**SITMUN 3** es un sistema de código libre para poner en marcha sistemas de información territoriales donde múltiples usuarios puedan acceder a distintas aplicaciones según sus necesidades. Esto incluye:

- **Aplicaciones web de usuario final.**
  La aplicación «básica» es un visor de mapas web, pero hay otras y pueden tomar formas muy distintas si es necesario.
  En general, estas aplicaciones deben ser configuradas para resultar útiles. Esta configuración incluye indicar las herramientas específicas que van a ofrecer a sus usuarios, así como los servicios, capas o bases de datos accesibles; también incluye restricciones de acceso, basadas en usuarios, roles y territorios concretos.
  Por ejemplo, una aplicación puede ser el visor de mapas básico. Y para el usuario «público» del territorio «Municipio X», esa configuración describe cómo en el árbol de capas del mapa tienen que aparecer ciertos servicios web de mapas, y no otros, y no debe aparecer ninguna herramienta que permita modificar datos o acceder a bases de datos privadas.
  Estas aplicaciones obtienen su configuración de una API REST cada vez que arrancan.
  La configuración depende del usuario, el rol y el territorio identificados, y puede haber cambiado desde la vez anterior.
  Esta API accede a la base de datos de SITMUN y no es la misma que usa la aplicación de administración; el visor usa de la API de Administración solo unos pocos endpoints: los idiomas y los parámetros de configuración, la cuenta del usuario identificado y las plantillas de las tareas de *más información avanzada* (MIA).
  Las aplicaciones aplican la configuración obtenida antes de que los usuarios empiecen a trabajar.
- **Aplicación de administración.**
  Esta aplicación es para que los administradores de las organizaciones que instalan **SITMUN 3** configuren las aplicaciones que quieran ofrecer a sus usuarios.
  Por ejemplo, se puede añadir un nuevo servicio de mapas públicamente accesible recién encontrado al visor de mapas básico para usuarios públicos de cualquier territorio. La próxima vez que un usuario público acceda verá que hay una capa más que la vez anterior.
  Esta aplicación lee y modifica los datos en la base de datos de **SITMUN 3** a través de una API REST.
- **Componentes adicionales.** Se usan en varias aplicaciones:
    - **SITMUN Proxy Middleware**: es un proxy inverso para que se pueda dar acceso a servicios y bases de datos protegidos (bien sea porque están en una Intranet, y los usuarios están fuera de ella, o bien porque requieren credenciales de acceso y los usuarios no las deben conocer, o bien porque quiere modificarse la información que ofrecen antes de devolverla a la aplicación cliente, por ejemplo, enmascarando parte de una imagen con un mapa).
    Es un proxy inverso y, por tanto, el cliente no puede elegir usarlo o no, y esencialmente le resulta transparente.
    Lo usan el visor y las aplicaciones móviles; la aplicación de administración no.
    - **API de Autenticación** (la usan el visor, la aplicación de administración y SITMUN Mobile Editor; SITMUN Touristic no la usa, porque funciona siempre como el usuario público): permite a los usuarios y administradores identificarse utilizando distintos mecanismos que puedan estar disponibles en las distintas organizaciones: usuario y contraseña guardados en la base de datos de SITMUN, servicios LDAP (incluido Microsoft Active Directory) y proveedores OpenID Connect (OIDC).

**SITMUN 3** no tiene un conjunto de datos o servicios geográficos/territoriales predefinidos. Cada despliegue de **SITMUN 3** se hace para una organización concreta, normalmente supramunicipal, y esta organización debe decidir qué aplicaciones quiere ofrecer a sus usuarios, típicamente personal técnico de los municipios, y qué servicios y datos geográficos/territoriales van a estar accesibles en estas aplicaciones. Estos servicios y bases de datos los tendrá que tener en sus propios sistemas, o bien tendrán que estar en algún sitio al que puedan acceder.

Las aplicaciones de usuario final de **SITMUN 3** interactúan relativamente poco con las API y componentes de **SITMUN 3**:

- Con la API de Autenticación al principio, para identificar al usuario, y después cada pocos minutos, para renovar la sesión y el token de corta duración del proxy. La aplicación turística no se autentica.
- Con la API de Configuración y Autorización en el arranque.
- El visor, además, con unos pocos endpoints de la API de Administración: `GET /api/languages` y `GET /api/configuration-parameters` (idiomas y parámetros de configuración, abiertos sin sesión), `GET` y `POST /api/account` (los datos y el perfil del usuario identificado, solo con sesión) y, cuando el usuario abre una tarea MIA con plantilla, `POST /api/tasks/template/more-info-advanced/render` y `POST /api/tasks/template/export`.
- La mayor parte de las peticiones las van a hacer contra servicios de mapas y bases de datos.
    - Las que sean de intranet, protegidas, etc. irán a través del **proxy**; las demás serán directas.

Esto conviene tenerlo en cuenta al dimensionar el hardware necesario para el despliegue y al decidir cómo repartirlo.

**SITMUN 3** tiene una arquitectura de tres capas. Las aplicaciones web se desarrollan con Angular 22 (y las aplicaciones móviles con Ionic y Capacitor), Spring Boot 4.1 con Java 17 se usa en la capa web, y una base de datos relacional (PostgreSQL 12 o superior, Oracle 11g o superior, o H2 para pruebas) en la capa de datos.
Todo el código está en el repositorio [sitmun/sitmun](https://github.com/sitmun/sitmun); las versiones exactas están en su README.

## Principales componentes

```plantuml alt="Diagrama de componentes: el administrador usa la aplicación de administración y los usuarios el visor de mapas y las aplicaciones móviles; estas llaman a las API de Autenticación, administración y configuración y autorización del backend, que guarda la configuración en la base de datos de SITMUN; el proxy da acceso a servicios web y bases de datos privados tras pedir autorización al backend, y usa el servicio MBTiles para la aplicación de edición; los servicios públicos se consultan directamente."
@startuml
!include <logos/angular>
!include <logos/github>
!include <logos/javascript>
!include <logos/oracle>
!include <logos/postgresql>
!include <logos/spring>
!include <office/Concepts/application_generic>
!include <office/Concepts/globe_internet>
!include <office/Security/lock_protected>
!include <office/Security/lock_unprotected>

skinparam linetype ortho

actor Administrador
actor "Usuario SITMUN 3"

rectangle appadmin [
  <color:DarkRed><$angular> <$application_generic{scale=1.5}>

  --

  **Aplicación de administración**

  <$github{scale=0.5}>
  [[https://github.com/sitmun/sitmun/tree/main/sitmun-admin]]
]

database configdb [
  <color:Crimson><$oracle> (Oracle) / <color: RoyalBlue><$postgresql> (PostgreSQL) / <color: Green>H2 (Pruebas)

  --

  Modelo de datos de SITMUN 3.
  Es la información de configuración de
  cada aplicación:
  Usuarios, Territorios, Aplicaciones, etc.

  <$github{scale=0.5}>
  [[https://github.com/sitmun/sitmun/tree/main/sitmun-backend]]
]

note bottom of configdb
  Esto incluye autorizaciones de acceso a
  servicios y BD privados, y la información
  necesaria para conectarse a esas (URI,
  puerto, esquema de BD, credenciales…)
  así como las consultas concretas
  (parametrizadas) que se pueden hacer.
end note

rectangle visor [
  <color:DarkRed><$angular> <$application_generic{scale=1.5}>
  <color:Red>API SITNA <$javascript{scale=0.5}>

  --

  **Visor de mapas**
  <$github{scale=0.5}>
  [[https://github.com/sitmun/sitmun/tree/main/sitmun-viewer]]
]

component publicwms #PapayaWhip [
  <$lock_unprotected{scale=0.5}> <$globe_internet{scale=0.5}> OGC WMS / WFS / …

  --

  Servicio web públicamente
  accesible con información
  geográfica
]

component privatewms #PapayaWhip [
  <$lock_protected{scale=0.5}> <$globe_internet{scale=0.5}> OGC WMS / WFS / …

  --

  Servicio web no accesible
  en Internet (por ejemplo, está en la intranet)
  o que requiere usuario y contraseña
  que los usuarios no pueden conocer,
  con información geográfica
]

database territdb #PapayaWhip [
  <$lock_protected{scale=0.5}> <color:Crimson><$oracle> (Oracle 23c) / <color: RoyalBlue><$postgresql> (PostgreSQL 16)

  --

  Datos territoriales, geográficos,
  administración pública, etc.
  Son los datos que consultan o modifican
  algunas aplicaciones de SITMUN 3.

  En intranet. No accesibles públicamente.
]


component proxymiddleware [
  <color:Green><$spring> (Spring)

  --

  **SITMUN Proxy Middleware**
]

rectangle appmovil [
  <color:DarkRed><$angular> <$application_generic{scale=1.5}>
  --
  **Aplicaciones móviles**
  (edición y turística)
  <$github{scale=0.5}>
  [[https://github.com/sitmun/sitmun/tree/main/sitmun-mobile]]
]
component mbtiles [
  <color:Green><$spring> (Spring)
  --
  **MBTiles** (opcional)
  Genera paquetes de teselas
  para trabajar sin conexión
  en la aplicación de edición.
]
note right of proxymiddleware
  Da acceso transparente a
  usuarios/territorios/aplicaciones
  autorizados a servicios y BD
  no públicos (intranet, protegidos
  con contraseña…).

  Para ello solicita permiso a la
  **API de Configuración y Autorización**
  usando para ello un **token JWT**,
  territorio y aplicación
  que recibe del cliente.
end note

component backendcore {
 component apibackendcore [
  <color:Green><$spring> (Spring)

  --

  **API de Administración**
 ]

 component apiautentic [
  <color:Green><$spring> (Spring)

  --

  **API de Autenticación**
 ]

 component apiconfautoriz [
  <color:Green><$spring> (Spring)

  --

  **API de Configuración y Autorización**
 ]
}

note bottom of backendcore
<$github{scale=0.5}>
[[https://github.com/sitmun/sitmun/tree/main/sitmun-backend]]
end note


note bottom of proxymiddleware
<$github{scale=0.5}>
[[https://github.com/sitmun/sitmun/tree/main/sitmun-proxy]]
end note

note left of apibackendcore
  Acceso de grano fino a los datos de
  configuración de SITMUN 3 para uso
  desde la **aplicación de administración**.
end note

note top of apiautentic
  Autentica al usuario desde una aplicación,
  verificando que existe en la BD
  de configuración de SITMUN 3, y devuelve un
  **token JWT** para interactuar con el resto
  del sistema.

  Proveedores: base de datos de SITMUN
  (bcrypt), LDAP y OpenID Connect (OIDC),
  según los perfiles Spring activos.

end note

note bottom of apiconfautoriz
  Uso desde el **visor**: devuelve,
  para un **token JWT**
  la información necesaria
  para configurar ese visor.
  P. ej., qué capas deben aparecer en
  el árbol, qué herramientas deben estar
  habilitadas, etc.

  Solo devuelve lo que el usuario puede
  ver según sus roles y territorios.
  Sin **token JWT**, devuelve la
  configuración del usuario público.

  Uso desde el **proxy**: con
  un **token JWT**, autoriza
  (o no) a realizar ciertas peticiones a
  ciertos servicios y BD privados.

  Por seguridad, la petición debe incluir
  un secreto conocido solo por el
  **proxy** y la
  **API de Configuración y Autorización**
  (cabecera `X-SITMUN-Proxy-Key`)
  para asegurar que proviene de un proxy
  conocido.

end note

"Usuario SITMUN 3" -down-> visor
Administrador -down-> appadmin
appadmin -down-> apibackendcore
appadmin -down-> apiautentic
backendcore -down-> configdb
visor -right-> publicwms
visor -down-> apiautentic
visor -down-> proxymiddleware
visor -down-> apiconfautoriz
visor .down.> apibackendcore : idiomas, parámetros,\ncuenta y plantillas MIA
proxymiddleware -down-> privatewms
proxymiddleware -down-> territdb
proxymiddleware -left-> apiconfautoriz
appmovil -down-> apiautentic : solo edición
appmovil -down-> apiconfautoriz
appmovil -down-> proxymiddleware
proxymiddleware -down-> mbtiles
@enduml
```

## Escenario típico de uso

Un escenario típico de uso que ejemplifica la interacción de estos componentes sería:

```plantuml alt="Diagrama de secuencia del escenario típico: el visor se autentica y obtiene un token JWT, pide su configuración con el token y los identificadores de territorio y aplicación, y hace las peticiones WMS a través del proxy, que comprueba la autorización con la API de Configuración y Autorización antes de llamar al WMS restringido."
@startuml
title
    Escenario típico de uso
end title
participant "Visor de\nmapas" as Client
participant "API de\nAutenticación" as SA
participant "API de\nProxy" as SP
participant "API de\nConfiguración y Autorización" as SAC
participant "WMS\nRestringido" as Remoto

autonumber
Client->>SA: Autenticación del usuario
autonumber stop
SA-->>Client: Token JWT
autonumber resume
Client->>SAC: Configuración del visor de mapas con el token JWT\ny los identificadores de territorio y aplicación
autonumber stop
SAC-->>Client: Configuración
autonumber resume
Client->>SP: Petición WMS con el token JWT\ny los identificadores de territorio y aplicación
SP->>SAC: Comprobación de la autorización\ny petición de la configuración
autonumber stop
SAC-->>SP: Autorización y configuración
autonumber resume
SP->>Remoto: Petición
autonumber stop
Remoto-->>SP: Respuesta
SP-->Client: Respuesta
@enduml
```

1. El usuario abre una aplicación de SITMUN, por ejemplo, un visor de información territorial,
   selecciona un territorio y se autentica.
   Para ello, el visor interactúa con el [Servicio de Autenticación][servicio-de-autenticacion], obteniendo un token JWT.
2. El visor obtiene la información para su configuración para este usuario, territorio y aplicación
   interactuando directamente con el [Servicio de Configuración y Autorización][servicio-de-configuracion-y-autorizacion].
   A esta petición el visor le ha añadido el token JWT, el identificador de territorio y el identificador de aplicación.
3. El usuario interactúa con el visor y, por ejemplo, hace visible una capa que corresponde a un
   servicio WMS restringido por territorio o realiza una búsqueda entre los datos alfanuméricos del
   padrón municipal de habitantes de un municipio. Esta petición ocurrirá a través del [Servicio de Proxy][servicio-de-proxy].
   A esta petición el visor le ha añadido el token JWT, el identificador de territorio y el identificador de aplicación.
4. Con esta información, el [Servicio de Proxy][servicio-de-proxy] interactúa con el [Servicio de Configuración y Autorización][servicio-de-configuracion-y-autorizacion]
   para determinar si puede hacer la petición y, si puede hacerla, cómo debe interrogar este servicio restringido.
   En este caso, por ejemplo, qué parámetros adicionales hay que añadir a la petición para limitar la respuesta a un territorio concreto.
5. Después, el [Servicio de Proxy][servicio-de-proxy] hace la petición al servicio WMS restringido con estos parámetros adicionales y
   devuelve la respuesta al visor tras aplicar alguna transformación si fuera necesaria.

## Diagramas de secuencia

En esta sección se documentan algunas de las interacciones más relevantes del sistema en forma de diagramas de secuencia.

<a id="login"></a>

### Inicio de sesión

```plantuml alt="Diagrama de secuencia del inicio de sesión: el visor envía las credenciales a la API de Autenticación, Spring Security las comprueba en la base de datos y se devuelve el token JWT en una cookie; después el visor pide su perfil a la API de Configuración y Autorización, que valida el token y devuelve la configuración del usuario, territorio y aplicación."
@startuml

actor Usuario
participant "Visor de mapas" as Client
participant "Cadena de filtros\n(Spring Security)" as FilterChain
participant "JsonWebTokenFilter" as JsonWebTokenFilter
participant "API de\nautenticación" as AuthenticationAPI <<@RestController>>
participant "API de\nconfiguración\ny autorización" as ConfigurationAPI <<@RestController>>
participant "JsonWebTokenService" as JsonWebTokenService
participant "Authentication\nManager\n(Spring Security)" as AuthenticationManager
participant "Security Context\n(Spring Security)" as SecurityContext
database "BD SITMUN 3" as Database

Usuario ->> Client: Inicio de sesión
Client -> AuthenticationAPI: Inicio de sesión (POST /api/authenticate,\n/api/authenticate/admin para el administrador)
AuthenticationAPI -> FilterChain
FilterChain -> AuthenticationAPI: Inicio de sesión (usuario, contraseña)
AuthenticationAPI-> AuthenticationManager: Obtención de la autenticación
AuthenticationManager -> Database: ¿Existe y la contraseña es correcta?
Database-->> AuthenticationManager: Sí
AuthenticationManager -->> AuthenticationAPI: Autenticación(usuario)
AuthenticationAPI -> JsonWebTokenService: Generación del token JWT (usuario)
JsonWebTokenService -->> AuthenticationAPI: Token JWT
AuthenticationAPI -->> FilterChain: Token JWT
FilterChain -->> AuthenticationAPI: Token JWT
AuthenticationAPI -->> Client: Token JWT
note right
200 OK
Set-Cookie: viewer_access_token={tokenJWT}; HttpOnly
(admin_access_token en el administrador;
SITMUN Mobile Editor usa /api/authenticate/mobile
y recibe el token en el cuerpo de la respuesta)
end note
Client -> ConfigurationAPI: Obtención de la configuración
note right
 GET /api/config/client/profile/{appId}/{terId}
 Cookie: viewer_access_token={tokenJWT}
end note

ConfigurationAPI -> FilterChain
FilterChain -> JsonWebTokenFilter: Filtrado de la petición\n(lee el token de la cookie)
JsonWebTokenFilter -> JsonWebTokenService: Extracción del usuario del token JWT
JsonWebTokenService -->> JsonWebTokenFilter: usuario
JsonWebTokenFilter-> Database: ¿Detalles usuario?
Database -->> JsonWebTokenFilter: roles y último cambio de contraseña
note right
  Si no se encuentra el usuario, 401 Unauthorized
  Los roles pueden ser USER, o USER y ADMIN.
  PUBLIC (usuario público, sin token) y
  MOBILE_EDITION (token de la aplicación de edición)
  los asignan otros filtros
end note
JsonWebTokenFilter -> JsonWebTokenService: Validación del token JWT
JsonWebTokenService -->> JsonWebTokenFilter: Token válido
note right
  Si el token no es válido, 401 Unauthorized
end note
JsonWebTokenFilter -> SecurityContext: set(Autenticación(usuario, roles))
SecurityContext -->> JsonWebTokenFilter
JsonWebTokenFilter -->> FilterChain
FilterChain -> SecurityContext: contexto seguridad?
SecurityContext -->> FilterChain: contexto actual
FilterChain -> FilterChain: verificar contexto\nactual tiene rol USER,\nPUBLIC o MOBILE_EDITION
note right
  método asociado a /api/config/client/profile/{appId}/{terId}
  solo puede ser accedido con los roles USER,
  PUBLIC o MOBILE_EDITION por la configuración
  de seguridad. Sin token se usa el usuario
  público (rol PUBLIC).
end note
FilterChain -> ConfigurationAPI: getProfile(appId, terId)
note right
  appId y terId son variables de la ruta.
  Sin cookie, se usa el usuario público.
end note
ConfigurationAPI -> SecurityContext: ¿Usuario autenticado?
SecurityContext -->> ConfigurationAPI: username\n(fijado por JsonWebTokenFilter)
ConfigurationAPI -> Database: Recuperar configuración según\nqué hay que configurar
note right
  se busca información para
  User = username
  Territory = terId
  Application = appId

  appId y terId siempre están en la ruta. La lista de aplicaciones
  y territorios disponibles se pide con otros endpoints:
  /api/config/client/application,
  /api/config/client/application/{appId}/territories y
  /api/config/client/territory/{terId}/applications.
end note
Database -->> ConfigurationAPI: Configuración\nsin\nrefinar
ConfigurationAPI -> ConfigurationAPI: Refinar\nconfiguración
note right
  Eliminar información que no pueda ver el usuario
  dadas sus restricciones para la aplicación y territorio
  y el resto de restricciones
end note
ConfigurationAPI -->> Client: Configuración\npedida (JSON)
Client -> Client: Configuración del visor\n(JSON de configuración)
Client -->> Usuario: Visor listo para usar

@enduml
```

### Uso del proxy para acceder a un WMS privado

```plantuml alt="Diagrama de secuencia del acceso a un WMS privado: el visor pide el mapa al proxy con su token; el proxy pide la configuración al backend con su clave de proxy, el backend valida el token y devuelve la URL y los parámetros del servicio, y el proxy hace la petición al WMS y devuelve la imagen."
@startuml

actor Usuario
participant "Visor de mapas" as Client
participant "Proxy" as Proxy <<@RestController>>
participant "Configuration API" as ConfigurationAPI <<@RestController>>
participant "Cadena de filtros\n(Spring Security)" as FilterChain
participant "ProxyTokenFilter" as ProxyTokenFilter
'participant "API de\nconfiguración\ny autorización" as ConfigurationAPI
participant "JsonWebTokenService" as JsonWebTokenService
participant "Security Context\n(Spring Security)" as SecurityContext
database "BD SITMUN 3" as Database
participant "WMS Público" as PublicWMS
participant "WMS Privado" as PrivateWMS



ref over Usuario, Client, Database : Proceso de inicio de sesión y configuración inicial
note over Client, ConfigurationAPI
La info de config. devuelta incluye, para WMS públicos (y similares)
su URL pública, y para los WMS privados (y similares) una URL única
para cada servicio que pasa por el **proxy**, pero
que para el cliente es una URL de un WMS normal.
end note


Usuario ->> Client: Actualización del mapa
Client ->> Client: Carga de una capa de un WMS público
note right
 new ImageLayer({
    source: new ImageWMS({
      url: 'https://publico.es/cartography/6',
      params: {'LAYERS': 'diba1,diba2,diba3'},
      serverType: 'geoserver',
    }),
  }),

  No debe añadir los parámetros terId y appId,
  porque el servicio remoto puede no admitirlos.
  Tampoco debe enviar el token JWT en la cabecera:
  un WMS público lo ignora, pero no hace falta enviarlo.
  Solo se envía en las peticiones dirigidas al proxy.
  La API de Configuración puede indicarlo
  con un valor booleano asociado a la URL.
end note

Client ->> PublicWMS: GetMap

PublicWMS -->> Client: Imagen de mapa pedida
Client ->> Client: Carga de una capa de un WMS restringido
note right
 Por la configuración previamente recibida ya sabe que
 https://<servidor>/middleware/proxy/7/5/WMS/12/23 es el endpoint de la capa 23
 del servicio WMS 12 para una aplicación (7) y territorio (5).
 En LAYERS debe pedir las capas del servicio que forman esa capa
 de SITMUN: todas en GetMap (en GetFeatureInfo y DescribeLayer puede
 pedir solo algunas). Con otro valor, el proxy responde 403.

 Este podría ser el código
 new ImageLayer({
    source: new ImageWMS({
      url: 'https://<servidor>/middleware/proxy/7/5/WMS/12/23',
      params: {'LAYERS': 'capa1,capa2,capa3'},
      serverType: 'geoserver',
    }),
  })

  Además debe enviar el token JWT en la cabecera, porque un indicador
  de la configuración se lo ha señalado.
end note
Client ->> Proxy: GetMap
note right
 GET /proxy/{appId}/{terId}/{type}/{typeId}/{cartographyId}?{mapParams}
 Authorization: Bearer {proxyToken}
 (token de corta duración obtenido con
 POST /api/authenticate/proxy)
end note

  Proxy ->> ConfigurationAPI: GetConfiguration
  note right
  POST /api/config/proxy
  Host: backend
  X-SITMUN-Proxy-Key: MiddlewareKey
  Authorization: Bearer {proxyToken}
  {
    "type" : "{type}",
    "typeId" : {typeId},
    "cartographyId" : {cartographyId},
    "terId" : {terId},
    "appId" : {appId},
    "method" : "GET",
    "parameters" : {
        mapParams
    }
  }
  end note
  ConfigurationAPI ->> FilterChain:
  FilterChain ->> ProxyTokenFilter: Filtrado de la petición
  ProxyTokenFilter ->> ProxyTokenFilter: ¿X-SITMUN-Proxy-Key\ncorrecta?
  note right
    Si es correcta, la petición se autentica como
    proxy (rol PROXY). Si no, sigue anónima y la
    regla de seguridad del paso siguiente responde
    401 Unauthorized.
  end note
  ProxyTokenFilter ->> SecurityContext: set(Autenticación("proxy", [PROXY]))
  ProxyTokenFilter -->> FilterChain
  FilterChain ->> SecurityContext: contexto seguridad?
  SecurityContext -->> FilterChain: contexto actual
  FilterChain ->> FilterChain: verificar contexto\nactual tiene rol PROXY
  note right
    método asociado a /api/config/proxy
    solo puede ser accedido con el rol PROXY
    por la configuración de seguridad
    Si no se verifica 401 Unauthorized
  end note
  FilterChain ->> ConfigurationAPI: getServiceConfiguration(ConfigProxyRequestDto)
  note right
    ConfigProxyRequestDto: appId, terId, type, typeId,
    cartographyId, method, parameters, requestBody.
    El token del usuario llega en la cabecera Authorization.
  end note
  ConfigurationAPI ->> JsonWebTokenService: Extracción de username del token\n(cabecera Authorization)
  JsonWebTokenService -->> ConfigurationAPI: username
  ConfigurationAPI ->> Database: ¿Último cambio de contraseña?
  Database -->> ConfigurationAPI: fecha
  ConfigurationAPI ->> JsonWebTokenService: Validación del token JWT
  JsonWebTokenService -->> ConfigurationAPI: Token válido
  ConfigurationAPI ->> ConfigurationAPI: Identificar qué hay que configurar
  note right
    Se decodifica configProxyRequest.type
    en este caso es "WMS" (el tipo del servicio:
    WMS, WMTS o WFS)
  end note
  ConfigurationAPI ->> Database: Recuperar configuración según\nqué hay que configurar
  note right
    se busca información para
    User = username
    Territory = configProxyRequest.terId
    Application = configProxyRequest.appId
    Service = configProxyRequest.typeId
    Cartography = configProxyRequest.cartographyId
    Si el usuario no tiene acceso a este recurso
    en la aplicación y el territorio: 403 Forbidden
  end note
  Database -->> ConfigurationAPI: Configuración\nsin\nrefinar
  ConfigurationAPI ->> ConfigurationAPI: Refinar\nconfiguración según\nqué hay que configurar
  'ConfigurationAPI -->> FilterChain: Configuración\npedida (JSON)

  'FilterChain -->> ConfigurationAPI: Configuración\npedida (JSON)
  ConfigurationAPI -->> Proxy: Configuración (JSON)

  note right
    {
        "type": "WMS",
        "exp": 1300819380,
        "payload": {
          "type": "OgcWmsPayload",
          "uri": "http://geoserveis.icgc.cat/map/bases/service",
          "method": "GET",
          "parameters": {
            "SERVICE": "WMS",
            "REQUEST": "GetMap",
            "LAYERS": "capa1,capa2,capa3",
            "FORMAT": "image/png",
            "BBOX": "…",
            "WIDTH": "…",
            "HEIGHT": "…",
            "COD_INE": "08630"
          },
          "vary": [ "BBOX" ]
        }
    }

    "parameters" es el conjunto completo de parámetros que el proxy
    envía al servicio: los de la petición del visor más los fijos
    que añade el backend (aquí, COD_INE). LAYERS repite las capas
    pedidas; el backend no lo reescribe.
    "exp" y "vary" forman parte de la respuesta, pero el proxy
    de la versión 1.3.0 no los usa: no guarda la configuración
    y la pide al backend en cada petición.

  end note

Proxy ->> Proxy: Construcción de la petición\nal WMS con la configuración
Proxy ->> PrivateWMS: GetMap
PrivateWMS -->> Proxy: Imagen de mapa pedida
Proxy -->> Client: Imagen de mapa pedida
Client -->> Usuario: mapa


@enduml
```

### Uso del proxy para acceder a una BD en intranet

```plantuml alt="Diagrama de secuencia del acceso a una base de datos en la intranet: el visor pide una tarea al proxy con su token; el proxy pide la configuración al backend, que valida el token y devuelve la conexión y la consulta SQL; el proxy ejecuta la consulta en la base de datos protegida y devuelve el resultado en JSON."
@startuml

actor Usuario
participant "Visor de mapas" as Client
participant "Proxy" as Proxy
participant "Backend" as Backend
participant "Cadena de filtros\n(Spring Security)" as FilterChain
participant "ProxyTokenFilter" as ProxyTokenFilter
participant "API de\nconfiguración\ny autorización" as ConfigurationAPI
participant "JsonWebTokenService" as JsonWebTokenService
participant "Security Context\n(Spring Security)" as SecurityContext
database "BD SITMUN 3" as Database
participant "BD Protegida" as ProtectedDatabase

ref over Usuario, Database : Proceso de inicio de sesión y configuración inicial

Usuario ->> Client: Información privada
Client ->> Proxy: DoTask
note right
 GET /proxy/{appId}/{terId}/{type}/{typeId}?{taskParams}
 Host: proxy
 Authorization: Bearer {proxyToken}
 (token de corta duración obtenido con
 POST /api/authenticate/proxy)
end note
note over Proxy
 El proxy no guarda configuraciones:
 pide la configuración al backend
 en cada petición
end note
Proxy ->> Backend: GetConfiguration
note right
 POST /api/config/proxy
 Host: backend
 X-SITMUN-Proxy-Key: MiddlewareKey
 Authorization: Bearer {proxyToken}
 {
   "type" : "{type}",
   "typeId" : {typeId},
   "terId" : {terId},
   "appId" : {appId},
   "method" : "GET",
   "parameters" : {
       taskParams
   }
 }
end note

Backend ->> FilterChain:
FilterChain ->> ProxyTokenFilter: Filtrado de la petición
ProxyTokenFilter ->> ProxyTokenFilter: ¿X-SITMUN-Proxy-Key\ncorrecta?
note right
  Si es correcta, la petición se autentica como
  proxy (rol PROXY). Si no, sigue anónima y la
  regla de seguridad del paso siguiente responde
  401 Unauthorized.
end note
ProxyTokenFilter ->> SecurityContext: set(Autenticación("proxy", [PROXY]))
ProxyTokenFilter -->> FilterChain
FilterChain ->> SecurityContext: contexto seguridad?
SecurityContext -->> FilterChain: contexto actual
FilterChain ->> FilterChain: verificar contexto\nactual tiene rol PROXY
note right
  método asociado a /api/config/proxy
  solo puede ser accedido con el rol PROXY
  por la configuración de seguridad
  Si no se verifica 401 Unauthorized
end note
FilterChain ->> ConfigurationAPI: getServiceConfiguration(ConfigProxyRequestDto)
note right
  ConfigProxyRequestDto: appId, terId, type, typeId,
  cartographyId, method, parameters, requestBody.
  El token del usuario llega en la cabecera Authorization.
end note
ConfigurationAPI ->> JsonWebTokenService: Extracción de username del token\n(cabecera Authorization)
JsonWebTokenService -->> ConfigurationAPI: username
ConfigurationAPI ->> Database: ¿Último cambio de contraseña?
Database -->> ConfigurationAPI: fecha
ConfigurationAPI ->> JsonWebTokenService: Validación del token JWT
JsonWebTokenService -->> ConfigurationAPI: Token válido
ConfigurationAPI ->> ConfigurationAPI: Identificar qué hay que configurar
note right
  Se decodifica configProxyRequest.type
  en este caso es "SQL" (el ámbito de la tarea:
  SQL o API) y el id es el de la tarea
end note
ConfigurationAPI ->> Database: Recuperar configuración según\nqué hay que configurar
note right
  se busca información para
  User = username
  Territory = configProxyRequest.terId
  Application = configProxyRequest.appId
  Task = configProxyRequest.typeId
  Si el usuario no tiene acceso a este recurso
  en la aplicación y el territorio: 403 Forbidden
end note
Database -->> ConfigurationAPI: Configuración\nsin\nrefinar
ConfigurationAPI ->> ConfigurationAPI: Refinar\nconfiguración según\nqué hay que configurar
ConfigurationAPI -->> FilterChain: Configuración\npedida (JSON)
note right
  {
      "type": "SQL",
      "exp": 1300819380,
      "payload": {
        "type": "DatasourcePayload",
        "uri": "jdbc:postgresql://bd.intranet:5432/catastro",
        "user": "usuario",
        "password": "contraseña",
        "driver": "org.postgresql.Driver",
        "sql": "SELECT * FROM parcelas WHERE territorio = ?",
        "parameters": [ { "sqlType": 12, "value": "32" } ]
      }
  }
  Los parámetros se envían como valores tipados (sqlType de JDBC)
  y nunca se concatenan en el texto SQL.
end note
FilterChain -->> Backend: Configuración\npedida (JSON)
Backend -->> Proxy: Configuración\npedida (JSON)
Proxy ->> Proxy: Construcción de la consulta\na la base de datos\ncon la configuración
Proxy ->> ProtectedDatabase: Conexión y consulta (sqlinfo)
ProtectedDatabase -->> Proxy: Resultset
Proxy ->> Proxy: JSON = Resultset2JSON
Proxy -->> Client: JSON
Client -->> Usuario: respuesta

@enduml
```

### Diagrama de módulos

El repositorio [sitmun/sitmun](https://github.com/sitmun/sitmun) agrupa todos los componentes.
Los componentes Java se construyen con un único proyecto Gradle multimódulo (`settings.gradle`);
las aplicaciones Angular e Ionic, con un *workspace* de pnpm (`pnpm-workspace.yaml`).

```plantuml alt="Diagrama de módulos: los módulos Java (sitmun-backend, sitmun-proxy y sitmun-mbtiles) y las bibliotecas comunes sitmun-proxy-contract y sitmun-spring-upstream, y las aplicaciones Angular e Ionic (sitmun-admin, sitmun-viewer, sitmun-edition y sitmun-touristic)."
@startuml

skinparam linetype ortho

package "Java (Gradle, Spring Boot)" {
  component ":sitmun-backend" as backend
  component ":sitmun-proxy" as proxy
  component ":sitmun-mbtiles" as mbtiles
  component ":sitmun-proxy-contract" as contract <<library>>
  component ":sitmun-spring-upstream" as upstream <<library>>
}

package "Angular / Ionic (pnpm)" {
  component "sitmun-admin" as admin
  component "sitmun-viewer" as viewer
  component "sitmun-mobile/sitmun-edition" as edition
  component "sitmun-mobile/sitmun-touristic" as touristic
}

note bottom of backend
  sitmun-backend
  API de Autenticación, configuración
  y autorización, y administración
end note
note bottom of proxy
  sitmun-proxy
end note
note bottom of mbtiles
  sitmun-addons/sitmun-mbtiles
end note
note right of contract
  sitmun-common/
  Bibliotecas compartidas
end note

backend ..> contract
backend ..> upstream
proxy ..> contract
contract ..> upstream

@enduml
```

## Diagrama de paquetes

El módulo `sitmun-backend` contiene el modelo de datos de **SITMUN 3**, la API de Autenticación,
la API de Configuración y Autorización, la API de Administración y la política de seguridad.
Todos sus paquetes cuelgan de `org.sitmun`.

### Paquetes (arquitectura por capas)

En general, cada API que en despliegue quede expuesta de manera separada, es decir, con su propio endpoint HTTP, tiene un paquete.

- Paquete `authentication` que corresponde con la **API de Autenticación**.
- Paquete `authorization` que corresponde con la **API de Configuración y Autorización**.
- Paquete `administration` que corresponde con la **API de Administración**.

Cada uno de estos paquetes puede contener:

- Paquete `controller`: contiene los controladores (clases anotadas con `@Controller`) y otras cosas necesarias para implementar ese endpoint HTTP.
- Paquete `service`: contiene los servicios de aplicación específicos de la API (clases anotadas con `@Service`) y clases asociadas. Estos servicios se invocan sobre todo desde los controladores del paquete `controller` (algunos, como el de las cookies de sesión, también desde los filtros de seguridad).
- Paquete `config`: contiene la configuración específica de los componentes del endpoint definidos en los paquetes `controller` y `service`. Normalmente, son clases anotadas con `@Configuration` y parte de la configuración puede estar referida a clases de infraestructura (de biblioteca) de Spring Framework.

Además, hay dos paquetes adicionales:

- Paquete `domain` que contiene las clases y los tipos del modelo de **SITMUN 3**. Es decir, el modelo que permite definir aplicaciones **SITMUN 3**, los territorios en
los que están disponibles, a qué servicios territorios y bases de datos pueden
acceder y qué usuarios pueden utilizarlas. Los paquetes que contienen las clases de dominio están anidados, de tal forma que las clases de dominio dependientes de otra aparecen en un paquete anidado en el paquete que contiene la clase principal. Las entidades de `domain` se exponen a través de la **API de Administración** usando el framework **Spring Data REST**.
- Paquete `infrastructure` que describe los componentes de infraestructura (persistencia, seguridad, web).

El paquete `infrastructure` contiene:

- Paquete `persistence`: configuración de la persistencia (`config`), dialectos de Hibernate para Oracle (`dialect`), excepciones (`exception`), tipos y conversores que usan las entidades (`type`) y validadores (`validation`).
  Las entidades del modelo, con sus repositorios (interfaces anotadas con `@Repository`) y proyecciones, están en los paquetes de `domain`.
- Paquete `security` que contiene la configuración del framework de seguridad `Spring Security`. `Spring Security` proporciona diversas formas de aplicar seguridad en la aplicación que permite establecer políticas de acceso a controladores, servicios y repositorios en función del rol que se le asigne al usuario en función de sus credenciales: `USER`, `ADMIN`, `PUBLIC`, `MOBILE_EDITION` y `PROXY`. Además, este paquete asegura que todos los accesos anónimos sean identificados como un acceso con usuario *público*.

La relación de las API públicas con el paquete `security` es la siguiente:

- La **API de Autenticación** del paquete `authentication` usa servicios y
componentes de Spring Framework configurados por el paquete `security` para
autenticar un usuario cuando solicita un token JWT de autenticación.
- Los controladores de la **API de Configuración y Autorización** solo podrán
ser accedidos por usuarios a los que se haya determinado que tengan el rol
`USER`, `PUBLIC` (usuario público) o `MOBILE_EDITION` (SITMUN Mobile Editor) o el rol `PROXY` (proxy). Es misión del paquete
`security` establecer los filtros necesarios para interceptar las peticiones
y en función de los mecanismos de seguridad implementados (token JWT para
los clientes, con el usuario público cuando no hay token; clave de API para el rol `PROXY`) determinar si están autenticadas
y asignar la identidad y el rol correspondiente.
- Los controladores de la **API de Administración** (tanto los definidos
explícitamente como los generados dinámicamente por **Spring Data REST**)
solo podrán ser accedidos por usuarios a los que se haya determinado que
tengan el rol `ADMIN`. Las excepciones son los endpoints que usa el visor: `GET /api/languages` y
`GET /api/configuration-parameters`, abiertos sin sesión; `GET` y `POST /api/account`, para el rol `USER`; y
`POST /api/tasks/template/more-info-advanced/render` y `POST /api/tasks/template/export`, abiertos también a los roles `USER` y `PUBLIC`. Como en el caso anterior, es misión del paquete
`security` establecer los filtros necesarios para interceptar las peticiones
y en función de los mecanismos de seguridad implementados (token JWT para el
rol `ADMIN`) determinar si están autenticadas y asignar la identidad y el rol
correspondiente.

Como se puede deducir de las explicaciones anteriores:

- La **API de Autenticación** ofrece, mediante una API web, mecanismos para interactuar con el sistema de seguridad de la aplicación definido en `security`.
- La **API de Administración** ofrece, mediante una API web, mecanismos para modificar el estado de los objetos de dominio definidos en `domain` por parte de los administradores.
- La **API de Configuración y Autorización** ofrece, mediante una API web, mecanismos para obtener una configuración derivada del estado actual de los objetos de dominio definidos en `domain` en función de la identidad y rol del que solicita la información.

El diagrama muestra los paquetes principales; cada uno tiene además otros subpaquetes (por ejemplo `dto`, `event` o `mapper`).

```plantuml alt="Diagrama de los paquetes principales de org.sitmun: administration (config, controller, service), authentication (controller, dto), authorization (client, proxy, access), domain e infrastructure (persistence, security, variables, web). No muestra todos los subpaquetes."
@startuml Refactor
skinparam linetype ortho
package org.sitmun {
    package administration {
        package config {
        }
        package controller {
        }
        package service {
        }
        config-d[hidden]->controller
        controller-d[hidden]->service
    }

    package authentication {
        package controller {
        }
        package dto {
        }
        controller-d[hidden]->dto
    }
    package authorization {
        package client {
        }
        package proxy {
        }
        package access {
        }
        client-d[hidden]->proxy
        proxy-d[hidden]->access
    }
    package domain {
    }
    package infrastructure {
        package persistence {
        }
        package security {
        }
        package variables {
        }
        package web {
        }
        persistence-d[hidden]->security
        security-d[hidden]->variables
        variables-d[hidden]->web
    }
}

@enduml
```

### Clases

La descripción de los componentes y clases principales del backend, y el flujo de cada petición,
está en la sección *Architecture* de
[sitmun-backend/README.md](https://github.com/sitmun/sitmun/blob/main/sitmun-backend/README.md#architecture),
que se mantiene junto al código.
