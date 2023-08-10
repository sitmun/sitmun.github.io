# Configuración

## Configuración de backend-core

### Seguridad

#### Autenticación vía LDAP

Estas propiedades se utilizan para configurar el acceso al servidor LDAP para autenticar a los usuarios.

!!! info "Condición de activación"
    Estas propiedades se utilizan solo si está activado el perfil `ldap`. 
    Deben almacenarse en un fichero separado denominado `application-ldap.yml`.

| Propiedad                                    | Descripción                                                               | Valor por defecto |
| -------------------------------------------- | ------------------------------------------------------------------------- | ----------------- |
| `sitmun.authentication.ldap.url`             | Localización del servidor LDAP                                            |                   |
| `sitmun.authentication.ldap.base-dn`         | Contexto raíz para todas las operaciones LDAP                             |                   |
| `sitmun.authentication.ldap.user-dn-pattern` | Patrón que identifica el usuario                                          |                   |
| `sitmum.authentication.ldap.username`        | El nombre de usuario a utilizar cuando se autentique con el servidor LDAP | nulo              |
| `sitmum.authentication.ldap.password`        | La contraseña a utilizar cuando se autentique con el servidor LDAP        | nulo              |

### Proxy

Mediante esta configuración se puede forzar el uso del [API de proxy][api-de-proxy] de SITMUN y configurar su localización.

| Propiedad            | Descripción                       | Valor por defecto |
| -------------------- | --------------------------------- | ----------------- |
| `sitmun.proxy.force` | Fuerza el uso del proxy de SITMUN | `false`           |
| `sitmun.proxy.url`   | Localización del proxy de SITMUN  |                   |

### API de configuración y autorización

| Propiedad                                         | Descripción                                           | Valor por defecto |
| ------------------------------------------------- | ----------------------------------------------------- | ----------------- |
| `sitmun.proxy.config-response-validity-in-secons` | Duración máxima del token de acceso que admite el API | `3600`            |
| `sitmun.authentication.middleware.secret`         | Token que usa el proxy para autenticarse              |                   |

## Configuración de proxy

| Propiedad                                 | Descripción                                                                           | Valor por defecto |
| ----------------------------------------- | ------------------------------------------------------------------------------------- | ----------------- |
| `sitmun.config.url`                       | Ruta al endpoint de configuración del proxy en la API de configuración y autorización |                   |
| `sitmun.authentication.middleware.secret` | Token que usa el proxy para autenticarse                                              |                   |