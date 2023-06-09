# Cómo comenzar

## Instalación de la plataforma

### Requisitos

### Instalación del backend

### Instalación del administrador

### Instalación del proxy

El **proxy middleware** depende del **backend-core** para obtener, mediante la **api de configuración y autorización**, la configuración necesaria para realizar la petición al servicio o base de datos final.

1. **Configuración**

    En el fichero `apllication.yml` contiene varias propiedades configurables:
    - `security.authentication.middleware.secret`: API-Key para la autenticación del proxy en el backend.
    - `sitmun.config.url`: url a la api de configuración y autorización.


2. **Construcción**

    **Proxy middleware** es un proyecto de gradle por lo que para construirlo se debe ejecutar el siguiente comando desde la raiz del proyecto en una terminal.
    ```bash
    ./gradlew clean build
    ```
    Este comando genera el jar del proxy en la ruta `./build/libs/`.


3. **Despliegue**
   
    El **proxy middleware** puede ser desplegado usando docker. En la raiz del proyecto se encuentra la carpeta `docker`, en la cual se puede encontrar un `docker-compose.yml` y un `Dockerfile`.
    
    Si se quiere desplegar únicamente el proxy, se puede hacer construyendo y arrancando la imagen del `Dockerfile`.
    ```bash
    $ docker build -t sitmun/proxy-middleware .
    $ docker run -p 8080:8080 sitmun/proxy-middleware
    ```
    Como se ha comentado anteriormente, el proxy depende de la **api de configuración y autorización** y por lo tanto es importante tener correctamente configurada la url a la api en el fichero de configuración.

    Con el `docker-compose.yml` se puede desplegar toda la infraestructura de SITMUN si se modifica el nombre de la imagen correspondiente al backend con la adecuada, ya sea una previamente construida o la oficial.
    En cualquiera que sea el caso el comando para levantar el servicio co docker compose es el siguiente:
    ```bash
    docker compose up
    ```

    Es posible desplegar el **proxy middleware** en local sin necesidad de docker mediante JVM ejecutando el siguiente comando en la ubicación del jar generado al construir el proxy.
    ```bash
    java -jar sitmun-proxy-middleware-${version}.jar
    ```

### Instalación del visor de mapas

## Creando una aplicación

## Personalización

## Filosofía de trabajo
