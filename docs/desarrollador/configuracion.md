# Configuración

!!! info "En desarrollo"
    Esta sección está siendo actualizada.

## Backend

### API de Autenticación {#configuration-api-de-autenticacion}

Estas propiedades se utilizan para configurar el acceso al servidor LDAP para autenticar a los usuarios.

!!! info "Condición de activación"
    Estas propiedades se utilizan solo si está activado el perfil `ldap`.
    Deben almacenarse en un fichero separado denominado `application-ldap.yml`.

| Propiedad                                    | Descripción                                                               | Valor por defecto |
|----------------------------------------------|---------------------------------------------------------------------------|-------------------|
| `sitmun.authentication.ldap.url`             | Localización del servidor LDAP                                            |                   |
| `sitmun.authentication.ldap.base-dn`         | Contexto raíz para todas las operaciones LDAP                             |                   |
| `sitmun.authentication.ldap.user-dn-pattern` | Patrón que identifica el usuario                                          |                   |
| `sitmun.authentication.ldap.password`        | La contraseña a utilizar cuando se autentique con el servidor LDAP        | nulo              |

### API de Configuración y Autorización {#configuration-api-de-configuracion-y-autorizacion}

| Propiedad                                                 | Descripción                                                        | Valor por defecto |
|-----------------------------------------------------------|--------------------------------------------------------------------|-------------------|
| `sitmun.proxy-middleware.config-response-validity-in-seconds` | Duración máxima (en segundos) de validez de la respuesta de configuración | `3600`            |
| `sitmun.proxy-middleware.secret`                          | Secreto que usa el componente proxy para autenticarse               |                   |

Mediante las siguientes propiedades se puede forzar la reescritura de las URI de los servicios en las repuestas de
configuración para clientes de mapas para que apunten al componente Proxy.

| Propiedad                         | Descripción                       | Valor por defecto |
|-----------------------------------|-----------------------------------|-------------------|
| `sitmun.proxy-middleware.force`   | Fuerza el uso del proxy de SITMUN | `false`           |
| `sitmun.proxy-middleware.url`     | Localización del proxy de SITMUN  |                   |

## Proxy

| Propiedad                                 | Descripción                                                                                                                | Valor por defecto |
|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|-------------------|
| `sitmun.backend.config.url`               | Ruta al endpoint de configuración del **proxy** en la API de configuración y autorización                                  |                   |
| `sitmun.backend.config.secret`            | Secreto que usa el proxy para autenticarse (ver API de configuración y autorización)                                       |                   |

## Visor de mapas

| Propiedad | Descripción                                       | Valor por defecto               |
|-----------|---------------------------------------------------|---------------------------------|
| `apiUrl`  | La URL pública donde se despliega el **backend**. | `http://localhost:9000/backend` |

## Administrador

| Propiedad    | Descripción                                       | Valor por defecto                |
|--------------|---------------------------------------------------|----------------------------------|
| `apiBaseURL` | La URL pública donde se despliega el **backend**. | `http://localhost:9000/backend`  |
