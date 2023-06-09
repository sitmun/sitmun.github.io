# Cómo comenzar

## Instalación de la plataforma

### Requisitos

### Instalación del backend

### Instalación del administrador

### Instalación del proxy

El **proxy middleware** depende del **backend-core** para obtener, mediante la **[API de Configuración y Autorización][api-de-configuracion-y-autorizacion]**,
la configuración necesaria para realizar la petición al servicio o base de datos final.

1. **Configuración**

    En el fichero `aplication.yml` contiene varias propiedades configurables:

    - `security.authentication.middleware.secret`: API-Key para la autenticación del proxy en la **[API de Configuración y Autorización][api-de-configuracion-y-autorizacion]**.
    - `sitmun.config.url`: URL a la **[API de Configuración y Autorización][api-de-configuracion-y-autorizacion]**.

2. **Construcción**

    **Proxy middleware** es un proyecto de gradle por lo que para construirlo se debe ejecutar el siguiente comando desde la raíz del proyecto en una terminal.

    ```bash
    ./gradlew clean build
    ```

    Este comando genera el fichero Jar del proxy en la ruta `./build/libs/`.

3. **Despliegue**

    El **proxy middleware** puede ser desplegado usando Docker.
    En la raíz del proyecto se encuentra la carpeta `docker`,
    en la cual se puede encontrar el fichero `docker-compose.yml` y el fichero `Dockerfile`.

    Si se quiere desplegar únicamente el proxy, se puede hacer construyendo y arrancando la imagen del `Dockerfile`.

    ```bash
    docker build -t sitmun/proxy-middleware .
    docker run -p 8080:8080 sitmun/proxy-middleware
    ```

    Como se ha comentado anteriormente, el proxy depende de la **[API de Configuración y Autorización][api-de-configuracion-y-autorizacion]** y,
    por lo tanto, es importante tener correctamente configurada la URL a la API en el fichero de configuración (`sitmun.config.url`).

    Mediante el fichero `docker-compose.yml` se puede desplegar toda la infraestructura de SITMUN si se modifica el nombre de la imagen correspondiente al backend con el nombre de la imagen adecuada, ya sea una previamente construida o la oficial.
    En cualquiera que sea el caso el comando para levantar el servicio con Docker Compose es el siguiente:

    ```bash
    docker compose up
    ```

    Es posible desplegar el **proxy middleware** en local sin necesidad de Docker mediante JVM ejecutando el siguiente comando en la ubicación del fichero Jar generado al construir el proxy.

    ```bash
    java -jar sitmun-proxy-middleware-${version}.jar
    ```

### Instalación del visor de mapas

## Creando una aplicación

## Personalización

## Filosofía de trabajo
