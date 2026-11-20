---
description: "Arquitectura de SITMUN 3: componentes, escenario típico de uso, diagramas de secuencia, módulos y paquetes del backend."
---

# Arquitectura de SITMUN 3

**SITMUN 3** es un sistema de código libre para poner en marcha sistemas de información territoriales donde múltiples usuarios puedan acceder a distintas aplicaciones según sus necesidades. Esto incluye:

- **Aplicaciones web de usuario final.**
  La aplicación “básica” es un visor de mapas web, pero hay otras y pueden tomar formas muy distintas si es necesario.
  En general, estas aplicaciones deben ser configuradas para resultar útiles. Esta configuración incluye indicar las herramientas específicas que van a ofrecer a sus usuarios, así como los servicios, capas o bases de datos accesibles; también incluye restricciones de acceso, basadas en usuarios, roles y territorios concretos.
  P. ej., una aplicación puede ser el visor de mapas básico. Y si te identificas como usuario “público” del territorio “Municipio X” esa configuración describe cómo en el árbol de capas del mapa tienen que aparecer ciertos servicios web de mapas, y no otros, y no debe aparecer ninguna herramienta que permita modificar datos o acceder a BD privadas.
  Estas aplicaciones obtienen su configuración cada vez que arrancan (porque depende del usuario, rol y territorio que se haya identificado, y porque puede haber cambiado desde la vez anterior) de una API REST. Esta API accede a la BD de SITMUN y no es la misma que usa la aplicación web de administración. Y finalmente aplican la configuración obtenida antes de permitir a los usuarios ponerse a trabajar.
- **Aplicación web de administración.**
  Esta aplicación es para que los administradores de las organizaciones que instalan **SITMUN 3** configuren las aplicaciones que quieran ofrecer a sus usuarios.
  P. ej., podemos añadir un nuevo servicio de mapas públicamente accesible que acabamos de encontrar al visor de mapas básico para usuarios públicos de cualquier territorio. La próxima vez que un usuario público acceda verá que hay una capa más que la vez anterior.
  Esta aplicación lee y modifica los datos en la BD de **SITMUN 3** a través de una API REST.
- **Componentes adicionales.** Se usan en varias aplicaciones, (tanto en la de administración como en las de usuario final):
    - **Proxy**: es un proxy inverso para que se pueda dar acceso a servicios y bases de datos protegidos (bien sea porque están en una Intranet, y los usuarios están fuera de ella, o bien porque requieren credenciales de acceso y los usuarios no las deben conocer, o bien porque quiere modificarse la información que ofrecen antes de devolverla a la aplicación cliente, por ejemplo, enmascarando parte de una imagen con un mapa).
    Es un proxy inverso y, por tanto, el cliente no puede elegir usarlo o no, y esencialmente le resulta transparente.
    - **API de autenticación**: permite a los usuarios y administradores identificarse utilizando distintos mecanismos que puedan estar disponibles en las distintas organizaciones: usuario y contraseña guardados en la base de datos de SITMUN, servicios LDAP (incluido Microsoft Active Directory) y proveedores OpenID Connect (OIDC).

**SITMUN 3** no tiene un conjunto de datos o servicios geográficos/territoriales predefinidos. Cada despliegue de **SITMUN 3** se hace para una organización concreta, normalmente supramunicipal, y esta organización debe decidir qué aplicaciones quiere ofrecer a sus usuarios, típicamente personal técnico de los municipios, y qué servicios y datos geográficos/territoriales van a estar accesibles en estas aplicaciones. Estos servicios y bases de datos los tendrá que tener en sus propios sistemas, o bien tendrán que estar en algún sitio al que puedan acceder.

Las aplicaciones de usuario final de **SITMUN 3** interactúan relativamente poco con las API y componentes de **SITMUN 3**:

- Con la API de autenticación solo al principio, para identificar al usuario.
- Con la API de configuración solo en el arranque.
- La mayor parte de las peticiones las van a hacer contra servicios de mapas y bases de datos.
    - Las que sean intranet, protegidas etc. irán a través del **proxy**, las demás serán directas.

Esto conviene tenerlo en cuenta cuando estemos dimensionando el hardware que necesitamos para el despliegue, y cómo lo vamos a repartir.

**SITMUN 3** tiene una arquitectura de 3-tiers. Las aplicaciones web se desarrollan con Angular 22 (y las aplicaciones móviles con Ionic y Capacitor), Spring Boot 4.1 con Java 17 se usa en el tier web, y una base de datos relacional (PostgreSQL 12 o superior, Oracle 11g o superior, o H2 para pruebas) en el tier de datos.
Todo el código está en el repositorio [sitmun/sitmun](https://github.com/sitmun/sitmun); las versiones exactas están en su README.

## Principales componentes

```plantuml alt="Diagrama de componentes: el administrador usa la aplicación de administración y los usuarios el visor de mapas y las aplicaciones móviles; estas llaman a las API de autenticación, administración y configuración y autorización del backend, que guarda la configuración en la base de datos de SITMUN; el proxy middleware da acceso a servicios web y bases de datos privados tras pedir autorización al backend, y usa el servicio MBTiles para la aplicación de edición; los servicios públicos se consultan directamente."
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
  
  **Aplicación de Administración**
  
  <$github{scale=0.5}>
  [[https://github.com/sitmun/sitmun/tree/main/sitmun-admin]] 
]

database configdb [
  <color:Crimson><$oracle> (Oracle) / <color: RoyalBlue><$postgresql> (PostgreSQL) / <color: Green>H2 (Pruebas)
  
  --
  
  Modelo de datos de SITMUN 3.
  Es la información de configuración de 
  cada aplicación:
  Usuarios, Territorios, Aplicaciones etc.
  
  <$github{scale=0.5}>
  [[https://github.com/sitmun/sitmun/tree/main/sitmun-backend]]
]

note bottom of configdb
  Esto incluye autorizaciones de acceso a 
  servicios y BD privados, y la información
  necesaria para conectarse a esas (URI,
  puerto, esquema de BD, credenciales...)
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
  <$lock_unprotected{scale=0.5}> <$globe_internet{scale=0.5}> OGC WMS / WFS / ...
  
  --
  
  Servicio web públicamente
  accesible con información 
  geográfica
]

component privatewms #PapayaWhip [
  <$lock_protected{scale=0.5}> <$globe_internet{scale=0.5}> OGC WMS / WFS / ...
  
  --
  
  Servicio web no accesible 
  en Internet (p.ej., está en intranet)
  o que requiere usuario y contraseña
  que los usuarios no pueden conocer,
  con información geográfica
]

database territdb #PapayaWhip [
  <$lock_protected{scale=0.5}> <color:Crimson><$oracle> (Oracle 23c) / <color: RoyalBlue><$postgresql> (PostgreSQL 16)
  
  --
  
  Datos territoriales, geográficos,
  administración pública, etc. 
  Son los datos que consultan y/o modifican
  algunas aplicaciones de SITMUN 3.
  
  En intranet. No accesibles públicamente.
]


component proxymiddleware [
  <color:Green><$spring> (Spring)
  
  --
  
  **Proxy "Middleware"**
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
  con contraseña...).
  
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
  desde la **Aplicación de Administración**.
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
  P.ej., qué capas deben aparecer en
  el árbol, qué herramientas deben estar
  habilitadas, etc.
  
  Solo devuelve lo que el usuario puede
  ver según sus roles y territorios.
  Sin **token JWT**, devuelve la
  configuración del usuario público.

  Uso desde el **proxy "middleware"**: con
  un **token JWT**, autoriza
  (o no) a realizar ciertas peticiones a 
  ciertos servicios y BD privados.

  Por seguridad, la petición debe incluir
  un secreto conocido solo por el 
  **proxy "middleware"** y el 
  **API de configuración y autorización**
  (cabecera `X-SITMUN-Proxy-Key`)
  para asegurar que proviene de un proxy
  conocido.

end note

"Usuario SITMUN 3" -down-> visor
Administrador -down-> appadmin
appadmin -down-> apibackendcore
backendcore -down-> configdb
visor -right-> publicwms
visor -down-> apiautentic
visor -down-> proxymiddleware
visor -down-> apiconfautoriz
proxymiddleware -down-> privatewms
proxymiddleware -down-> territdb
proxymiddleware -left-> apiconfautoriz
appmovil -down-> apiautentic
appmovil -down-> apiconfautoriz
appmovil -down-> proxymiddleware
proxymiddleware -down-> mbtiles
@enduml
```

## Escenario típico de uso

Un escenario típico de uso que ejemplifica la interacción de estos componentes sería:

```plantuml alt="Diagrama de secuencia del escenario típico: el visor se autentica y obtiene un token JWT, pide su configuración con el token y los identificadores de territorio y aplicación, y hace las peticiones WMS a través del proxy, que comprueba la autorización con la API de configuración y autorización antes de llamar al WMS restringido."
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
Client->>SA: Autentica usuario
autonumber stop
SA-->>Client: Token JWT
autonumber resume
Client->>SAC: Configura visor de mapas usando token JWT\ne identificadores territorio y aplicación
autonumber stop
SAC-->>Client: Configuración
autonumber resume
Client->>SP: Petición WMS usando token JWT\ne identificadores territorio y aplicación
SP->>SAC: Comprueba autorización\ny dame configuración
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
   padrón municipal de habitantes de un municipio. Esta petición ocurrirá a través del [Servicio de proxy][servicio-de-proxy].
   A esta petición el visor le ha añadido el token JWT, el identificador de territorio y el identificador de aplicación.
4. Con esta información, el [Servicio de proxy][servicio-de-proxy] interactúa con el [Servicio de Configuración y Autorización][servicio-de-configuracion-y-autorizacion]
   para determinar si puede hacer la petición y, si puede hacerla, cómo debe interrogar este servicio restringido.
   En este caso, por ejemplo, qué parámetros adicionales hay que añadir a la petición para limitar la respuesta a un territorio concreto.
5. Después, el [Servicio de proxy][servicio-de-proxy] hace la petición al servicio WMS restringido con estos parámetros adicionales y
   devuelve la respuesta al visor tras aplicar alguna transformación si fuera necesaria.

## Diagramas de secuencia

En esta sección se documentan algunas de las interacciones más relevantes del sistema en forma de diagramas de secuencia.

### Login

```plantuml alt="Diagrama de secuencia del inicio de sesión: el visor envía las credenciales a la API de autenticación, Spring Security las comprueba en la base de datos y se devuelve el token JWT en una cookie; después el visor pide su perfil a la API de configuración y autorización, que valida el token y devuelve la configuración del usuario, territorio y aplicación."
@startuml

actor Usuario
participant "Visor de mapas" as Client
participant "Authentication\nEntry Point\n(Spring Security)" as AuthenticationEntryPoint
participant "Filtro token\nautenticación" as AuthTokenFilter
participant "API de\nautenticación" as AuthenticationAPI <<@RestController>>
participant "API de\nconfiguración\ny autorización" as ConfigurationAPI <<@RestController>>
participant "Utilidades\nJWT" as JWTUtils
participant "Authentication\nManager\n(Spring Security)" as AuthenticationManager
participant "Security Context\n(Spring Security)" as SecurityContext
database "BD SITMUN 3" as Database

Usuario ->> Client: Login
Client -> AuthenticationAPI: Login (POST /api/authenticate,\n/api/authenticate/admin para el administrador)
AuthenticationAPI -> AuthenticationEntryPoint
AuthenticationEntryPoint -> AuthenticationAPI: Login(usuario, password)
AuthenticationAPI-> AuthenticationManager: Obtener Autenticación
AuthenticationManager -> Database: ¿Existe y pwd OK?
Database-->> AuthenticationManager: Sí
AuthenticationManager -->> AuthenticationAPI: Autenticación(usuario)
AuthenticationAPI -> SecurityContext: set(Autenticación)
SecurityContext -->> AuthenticationAPI
AuthenticationAPI -> JWTUtils: Generar Token JWT(usuario)
JWTUtils -->> AuthenticationAPI: Token JWT
AuthenticationAPI -->> AuthenticationEntryPoint: Token JWT
AuthenticationEntryPoint -->> AuthenticationAPI: Token JWT
AuthenticationAPI -->> Client: Token JWT
note right
200 Ok
Set-Cookie: viewer_access_token={tokenJWT}; HttpOnly
(admin_access_token en el administrador;
la app móvil de edición usa /api/authenticate/mobile
y recibe el token en el cuerpo de la respuesta)
end note
Client -> ConfigurationAPI: Obtener configuración 
note right
 GET /api/config/client/profile/{appId}/{terId}
 Cookie: viewer_access_token={tokenJWT}
end note

ConfigurationAPI -> AuthenticationEntryPoint
AuthenticationEntryPoint -> AuthTokenFilter: Filtra petición\n(lee el token de la cookie)
AuthTokenFilter -> JWTUtils: Validar token JWT
JWTUtils -->> AuthTokenFilter: Token OK
AuthTokenFilter -> JWTUtils: Extraer usuario del token JWT
JWTUtils -->> AuthTokenFilter: usuario
AuthTokenFilter-> Database: ¿Detalles usuario?
Database -->> AuthTokenFilter: roles
note right
  Si no se encuentra 401 Unauthorized
  Los roles pueden ser USER y/o ADMIN.
  PUBLIC (usuario público, sin token) y
  MOBILE_EDITION (token de la app de edición)
  los asignan otros filtros
end note
AuthTokenFilter -> SecurityContext: set(Autenticación(usuario, roles))
SecurityContext -->> AuthTokenFilter
AuthTokenFilter -->> AuthenticationEntryPoint
AuthenticationEntryPoint -> SecurityContext: contexto seguridad?
SecurityContext -->> AuthenticationEntryPoint: contexto actual
AuthenticationEntryPoint -> AuthenticationEntryPoint: verificar contexto\nactual tiene rol USER,\nPUBLIC o MOBILE_EDITION
note right
  método asociado a "/api/config/client/profile/{appId}/{terId}"
  solo puede ser accedido con los roles USER,
  PUBLIC o MOBILE_EDITION por la configuración
  de seguridad. Sin token se usa el usuario
  público (rol PUBLIC).
end note
AuthenticationEntryPoint -> ConfigurationAPI: getProfile(appId, terId)
note right
  appId y terId son variables de la ruta.
  Sin cookie, se usa el usuario público.
end note
ConfigurationAPI -> JWTUtils: Validar token JWT
JWTUtils -->> ConfigurationAPI: Token OK
ConfigurationAPI -> JWTUtils: Extraer "username" del token\n(cabecera Authorization)
JWTUtils -->> ConfigurationAPI: "username"
ConfigurationAPI -> Database: Recuperar configuración según\nqué hay que configurar
note right
  buscamos información para 
  User = username
  Territory = terId
  Application = appId

  Si no hay territorio, estamos configurando la aplicación 
  para que pueda seleccionar el territorio. 
  No hay acceso a información de tareas o capas.
  
  Si no hay aplicación, nos está pidiendo todas las aplicaciones
  para el territorio indicado.
  No hay acceso a información de tareas o capas.


  Si no hay territorio y ni aplicación, nos pide saber todas 
  las aplicaciones y territorios que puede combinar
  No hay acceso a información de tareas o capas.

end note
Database -->> ConfigurationAPI: Configuración\nsin\nrefinar
ConfigurationAPI -> ConfigurationAPI: Refinar\nconfiguración 
note right
  Eliminar información que no pueda ver el usuario 
  dadas sus restricciones para la aplicación y territorio
  y el resto de restricciones
end note
ConfigurationAPI -->> AuthenticationEntryPoint: Configuración\npedida (JSON)
AuthenticationEntryPoint -->> AuthenticationAPI: Configuración\npedida (JSON)
AuthenticationAPI -->> Client: Configuración\npedida (JSON)
Client -> Client: Configurar visor\n(Config JSON)
Client -->> Usuario: Visor listo para usar

@enduml
```

### Uso del proxy para acceder a un WMS privado

```plantuml alt="Diagrama de secuencia del acceso a un WMS privado: el visor pide el mapa al proxy con su token; si no hay una configuración válida en caché, el proxy la pide al backend con su clave de proxy, el backend valida el token y devuelve la URL y los parámetros del servicio, y el proxy hace la petición al WMS y devuelve la imagen."
@startuml

actor Usuario
participant "Visor de mapas" as Client
participant "Proxy" as Proxy <<@RestController>>
participant "Configuration API" as ConfigurationAPI <<@RestController>>
participant "Authentication\nEntry Point\n(Spring Security)" as AuthenticationEntryPoint
participant "Filtro \nmiddleware" as MiddlewareFilter
'participant "API de\nconfiguración\ny autorización" as ConfigurationAPI
participant "Utilidades\nJWT" as JWTUtils
participant "Security Context\n(Spring Security)" as SecurityContext
database "BD SITMUN 3" as Database
participant "WMS Público" as PublicWMS
participant "WMS Privado" as PrivateWMS



ref over Usuario, Client, Database : Proceso de login y config. inicial
note over Client, ConfigurationAPI
La info de config. devuelta incluye, para WMS públicos (y similares)
su URL pública, y para los WMS privados (y similares) una URL única 
para cada servicio que pasa por el **proxy middleware**, pero
que para el cliente es una URL de un WMS normal.
end note


Usuario ->> Client: Refresca mapa
Client ->> Client: Carga una capa de un WMS público
note right
 new ImageLayer({
    source: new ImageWMS({
      url: 'https://publico.es/cartography/6',
      params: {'LAYERS': 'diba1,diba2,diba3'},
      serverType: 'geoserver',
    }),
  }),

  No debe añadir los parámetros 'terrId' y 'appId' 
  ya que pueden no estar soportados por el servicio remoto.
  Tampoco debe añadir en la cabecera el TokenJWT
  El token será ignorado en un WMS público, pero para evitar problemas
  el token no tiene que ir siempre. 
  Se puede añadir solo si las peticiones están dirigidas al proxy
  Esta información puede ser proporcionada por el API de configuración
  mediante un valor booleano asociado a la URL. 
end note

Client ->> PublicWMS: GetMap

PublicWMS -->> Client: Imagen de mapa pedida
Client ->> Client: Carga una capa de un WMS restringido
note right
 Por la configuración previamente recibida ya sabe que 
 https://<servidor>/middleware/proxy/7/5/WMS/12/23 es el endpoint de la capa 23
 del servicio WMS 12 para una aplicación (7) y territorio (5). 
 Debe además usar LAYERS=default para obtenerla. 

 Este podría ser el código
 new ImageLayer({
    source: new ImageWMS({
      url: 'https://<servidor>/middleware/proxy/7/5/WMS/12/23',
      params: {'LAYERS': 'default},
      serverType: 'geoserver',
    }),
  })
 
  Además debe añadir en la cabecera el TokenJWT porque una bandera se lo ha indicado. 
end note
Client ->> Proxy: GetMap
note right
 GET /proxy/{appId}/{terId}/{type}/{typeId}?{mapParams}
 Authorization: Bearer {proxyToken}
 (token de corta duración obtenido con
 POST /api/authenticate/proxy)
end note

Proxy -> Proxy: Configuración en cache?

alt Hay una configuración válida reusable en la cache
  Proxy -> Proxy: Configuración (JSON) = Sacar de cache()

else No hay configuración reusable en la cache

  Proxy ->> ConfigurationAPI: GetConfiguration
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
        mapParams
    }
  }
  end note
  ConfigurationAPI ->> AuthenticationEntryPoint: 
  AuthenticationEntryPoint ->> MiddlewareFilter: Filtra petición
  MiddlewareFilter ->> MiddlewareFilter: MiddlewareKey\nconocida?
  note right
    Si no se verifica 401 Unauthorized
  end note
  MiddlewareFilter ->> SecurityContext: set(Autenticación("proxy", [PROXY]))
  MiddlewareFilter -->> AuthenticationEntryPoint
  AuthenticationEntryPoint ->> SecurityContext: contexto seguridad?
  SecurityContext -->> AuthenticationEntryPoint: contexto actual
  AuthenticationEntryPoint ->> AuthenticationEntryPoint: verificar contexto\nactual tiene rol PROXY
  note right
    método asociado a "/api/config/proxy" 
    solo puede ser accedido con el rol PROXY
    por la configuración de seguridad
    Si no se verifica 401 Unauthorized
  end note
  AuthenticationEntryPoint ->> ConfigurationAPI: getServiceConfiguration(ConfigProxyRequestDto)
  note right
    ConfigProxyRequestDto: appId, terId, type, typeId,
    cartographyId, method, parameters, requestBody.
    El token del usuario llega en la cabecera Authorization.
  end note
  ConfigurationAPI ->> JWTUtils: Validar token JWT
  JWTUtils -->> ConfigurationAPI: Token OK
  ConfigurationAPI ->> JWTUtils: Extraer "username" del token\n(cabecera Authorization)
  JWTUtils -->> ConfigurationAPI: "username"
  ConfigurationAPI ->> ConfigurationAPI: Identificar qué hay que configurar 
  note right
    Decodificamos configProxyRequest.type
    en este caso es "WMS" (el tipo del servicio:
    WMS, WMTS o WFS)
  end note
  ConfigurationAPI ->> Database: Recuperar configuración según\nqué hay que configurar
  note right
    buscamos información para 
    User = username
    Territory = configProxyRequest.terId
    Application = configProxyRequest.appId
    Cartography = configProxyRequest.typeId
  end note
  Database -->> ConfigurationAPI: Configuración\nsin\nrefinar
  ConfigurationAPI ->> ConfigurationAPI: Refinar\nconfiguración según\nqué hay que configurar
  'ConfigurationAPI -->> AuthenticationEntryPoint: Configuración\npedida (JSON)
  
  'AuthenticationEntryPoint -->> ConfigurationAPI: Configuración\npedida (JSON)
  ConfigurationAPI -->> Proxy: Configuración (JSON)

  note right
    {
        "type": "WMS",
        "exp": 1300819380,
        "payload": {
          "type": "OgcWmsPayload",
          "uri": "http://geoserveis.icgc.cat/map/bases/service",
          "method": "GET",
          "parameters": { "LAYERS": "topogris", "COD_INE": "08630" },
          "vary": [ "BBOX" ]
        }
    }

    "parameters" son los parámetros que el proxy añade a la petición
    o sustituye en ella.
    "exp" es el momento hasta el que el proxy puede reutilizar
    (cachear) esta configuración.
    "vary" indica al proxy que puede usar esta respuesta cacheada
    si el único cambio es en el parámetro BBOX

  end note

end

Proxy ->> Proxy: Interpreta la respuesta\ncomo una pregunta\na un WMS OGC
Proxy ->> PrivateWMS: GetMap
PrivateWMS -->> Proxy: Imagen de mapa pedida
Proxy -->> Client: Imagen de mapa pedida
Client -->> Usuario: mapa


@enduml
```

### Uso del proxy para acceder a una BD en Intranet

```plantuml alt="Diagrama de secuencia del acceso a una base de datos en la intranet: el visor pide una tarea al proxy con su token; el proxy pide la configuración al backend, que valida el token y devuelve la conexión y la consulta SQL; el proxy ejecuta la consulta en la base de datos protegida y devuelve el resultado en JSON."
@startuml

actor Usuario
participant "Visor de mapas" as Client
participant "Proxy" as Proxy
participant "Backend" as Backend
participant "Authentication\nEntry Point\n(Spring Security)" as AuthenticationEntryPoint
participant "Filtro \nmiddleware" as MiddlewareFilter
participant "API de\nconfiguración\ny autorización" as ConfigurationAPI
participant "Utilidades\nJWT" as JWTUtils
participant "Security Context\n(Spring Security)" as SecurityContext
database "BD SITMUN 3" as Database
participant "BD Protegida" as ProtectedDatabase

ref over Usuario, Database : Proceso de login y config. inicial

Usuario ->> Client: Información privada
Client ->> Proxy: DoTask
note right
 GET /proxy/{appId}/{terId}/{type}/{typeId}?{taskParams}
 Host: proxy
 Authorization: Bearer {proxyToken}
 (token de corta duración obtenido con
 POST /api/authenticate/proxy)
end note
Proxy ->> Proxy: Comprueba cache
note right
 Se comprueba primero que no hay en la cache
 una respuesta anterior del backend que sea 
 válida y que se pueda usar para configurar
 la petición
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

Backend ->> AuthenticationEntryPoint: 
AuthenticationEntryPoint ->> MiddlewareFilter: Filtra petición
MiddlewareFilter ->> MiddlewareFilter: MiddlewareKey\nconocida?
note right
  Si no se verifica 401 Unauthorized
end note
MiddlewareFilter ->> SecurityContext: set(Autenticación("proxy", [PROXY]))
MiddlewareFilter -->> AuthenticationEntryPoint
AuthenticationEntryPoint ->> SecurityContext: contexto seguridad?
SecurityContext -->> AuthenticationEntryPoint: contexto actual
AuthenticationEntryPoint ->> AuthenticationEntryPoint: verificar contexto\nactual tiene rol PROXY
note right
  método asociado a "/api/config/proxy" 
  solo puede ser accedido con el rol PROXY
  por la configuración de seguridad
  Si no se verifica 401 Unauthorized
end note
AuthenticationEntryPoint ->> ConfigurationAPI: getServiceConfiguration(ConfigProxyRequestDto)
note right
  ConfigProxyRequestDto: appId, terId, type, typeId,
  cartographyId, method, parameters, requestBody.
  El token del usuario llega en la cabecera Authorization.
end note
ConfigurationAPI ->> JWTUtils: Validar token JWT
JWTUtils -->> ConfigurationAPI: Token OK
ConfigurationAPI ->> JWTUtils: Extraer "username" del token\n(cabecera Authorization)
JWTUtils -->> ConfigurationAPI: "username"
ConfigurationAPI ->> ConfigurationAPI: Identificar qué hay que configurar 
note right
  Decodificamos configProxyRequest.type
  en este caso es "SQL" (el ámbito de la tarea:
  SQL, API o URL) y el id es el de la tarea
end note
ConfigurationAPI ->> Database: Recuperar configuración según\nqué hay que configurar
note right
  buscamos información para 
  User = username
  Territory = configProxyRequest.terId
  Application = configProxyRequest.appId
  Task = configProxyRequest.typeId
end note
Database -->> ConfigurationAPI: Configuración\nsin\nrefinar
ConfigurationAPI ->> ConfigurationAPI: Refinar\nconfiguración según\nqué hay que configurar
ConfigurationAPI -->> AuthenticationEntryPoint: Configuración\npedida (JSON)
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
AuthenticationEntryPoint -->> Backend: Configuración\npedida (JSON)
Backend -->> Proxy: Configuración\npedida (JSON)
Proxy ->> Proxy: Interpreta la respuesta\ncomo una pregunta\na base de datos
Proxy ->> ProtectedDatabase: Connect and Query (sqlinfo)
ProtectedDatabase -->> Proxy: Resultset
Proxy ->> Proxy: JSON = Resulset2JSON
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
  API de autenticación, configuración
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

El módulo `sitmun-backend` contiene el modelo de datos de **SITMUN 3**, la API de autenticación,
la API de configuración y autorización, la API de administración y la política de seguridad.
Todos sus paquetes cuelgan de `org.sitmun`.

### Paquetes (Arquitectura por Capas)

En general, cada API que en despliegue quede expuesta de manera separada, es decir, con su propio endpoint HTTP, tiene un paquete.

- Paquete `authentication` que corresponde con la **API de Autenticación**.
- Paquete `authorization` que corresponde con la **API de Configuración y Autorización**.
- Paquete `administration` que corresponde con la **API de Administración**.

Cada uno de estos paquetes puede contener:

- Paquete `controller`: contiene los controladores (clases anotadas con `@Controller`) y otras cosas necesarias para implementar ese endpoint HTTP.
- Paquete `service`: contiene los servicios de aplicación específicos del API (clases anotadas con `@Service`) y clases asociadas. Estos servicios solo se invocarán desde los controladores del paquete `controller`.
- Paquete `config`: contiene la configuración específica de los componentes del endpoint definidos en los paquetes `controller` y `service`. Normalmente, son clases anotadas con `@Configuration` y parte de la configuración puede estar referida a clases de infraestructura (de biblioteca) de Spring Framework.

Además, hay dos paquetes adicionales:

- Paquete `domain` que contiene las clases y los tipos del modelo de **SITMUN 3**. Es decir, el modelo que permite definir aplicaciones **SITMUN 3**, los territorios en
los que están disponibles, a qué servicios territorios y bases de datos pueden
acceder y qué usuarios pueden utilizarlas.  Los paquetes que contienen las clases de dominio están anidados, de tal forma que las clases de dominio dependientes de otra aparecen en un paquete anidado en el paquete que contiene la clase principal. Las entidades de `domain` se exponen a través de la **API de Administración** usando el framework **Spring Data REST**.
- Paquete `infrastructure` que describe los componentes de infraestructura (persistencia, seguridad, web).

El paquete `infrastructure` contiene:

- Paquete `persistence`: configuración de la persistencia (`config`), dialectos de Hibernate para Oracle (`dialect`), excepciones (`exception`), tipos y conversores que usan las entidades (`type`) y validadores (`validation`).
  Las entidades del modelo, con sus repositorios (interfaces anotadas con `@Repository`) y proyecciones, están en los paquetes de `domain`.
- Paquete `security` que contiene la configuración del framework de seguridad `Spring Security`. `Spring Security` proporciona diversas formas de aplicar seguridad a nivel de la aplicación que permite establecer políticas de acceso a controladores, servicios y repositorios en función del rol que se le asigne al usuario en función de sus credenciales: `USER`, `ADMIN`, `PROXY`. Además, este paquete asegura que todos los accesos anónimos sean identificados como un acceso con usuario *público*.

La relación de las API públicas con el paquete `security`es la siguiente:

- La **API de Autenticación** del paquete `authentication` usa servicios y
componentes de Spring Framework configurados por el paquete `security` para
autenticar un usuario cuando solicita un token JWT de autenticación.  
- Los controladores de la **API de Configuración y Autorización** solo podrán
ser accedidos por usuarios a los se haya determinado que tengan el rol
`USER`, `PUBLIC` (usuario público) o `MOBILE_EDITION` (clientes **SITMUN 3**) o el rol `PROXY` (proxy). Es misión del paquete
`security` establecer los filtros necesarios para interceptar las peticiones
y en función de los mecanismos de seguridad implementados (token JWT para
los clientes, con el usuario público cuando no hay token; API key para el rol `PROXY`) determinar si están autenticadas
y asignar la identidad y el rol correspondiente.
- Los controladores de la **API de Administración** (tanto los definidos
explícitamente como los generados dinámicamente por **Spring Data REST**)
solo podrán ser accedidos por usuarios a los que se haya determinado que
tengan el rol `ADMIN`. Como en el caso anterior, es misión del paquete
`security` establecer los filtros necesarios para interceptar las peticiones
y en función de los mecanismos de seguridad implementados (token JWT para el
rol `ADMIN`) determinar si están autenticadas y asignar la identidad y el rol
correspondiente.

Como se puede deducir de las explicaciones anteriores:

- La **API de Autenticación** expone vía una API Web mecanismos para interactuar con el sistema de seguridad de la aplicación definido en `security`.
- La **API de Administración** expone vía una API Web mecanismos para modificar el estado de los objetos de dominio definidos en `domain` por parte de los administradores.
- La **API de Configuración y Autorización** expone vía una API Web mecanismos para obtener una configuración derivada del estado actual de los objetos de dominio definidos en `domain` en función de la identidad y rol del que solicita la información.

```plantuml alt="Diagrama de paquetes de org.sitmun: administration (config, controller, service), authentication (controller, dto), authorization (client, proxy, access), domain e infrastructure (persistence, security, variables, web)."
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
