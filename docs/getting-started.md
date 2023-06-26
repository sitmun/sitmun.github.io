# Primeros pasos

## ¿Qué es SITMUN 3?

**SITMUN 3** es una plataforma que permite la creación y gestión de aplicaciones personalizadas en el ámbito de los sistemas de información geográfica. 
Está orientada especialmente a satisfacer las necesidades en materia de información territorial de las administraciones locales y supramunicipales.

**SITMUN 3** ha sido desarrollado con la visión de ofrecer una herramienta de gestión de información territorial a los municipios, gestionado desde una entidad supramunicipal,
de manera que permita la integración de la información territorial con la información de las corporaciones locales, independientemente del modelo de datos o del sistema de gestión de base de datos de cada municipio. 
Desde el módulo administrador se configura la información cartográfica, el territorio al que tiene acceso cada usuario para cada aplicación SIG, y las funcionalidades (consultas a base de datos, generación de informes, localizaciones, funciones de análisis espacial, etc.). 
Las funcionalidades se asignan a los usuarios a través de perfiles.

**SITMUN 3** dispone de una base de datos para administrar la plataforma. 
Entre las tablas de la base de datos se encuentran las necesarias para gestionar: 
las capas de cartografía, los usuarios con los perfiles, los territorios, las aplicaciones y las tareas (funcionalidades que se van ampliando en la plataforma).

**SITMUN 3** se basa en la utilización de servicios web estándar definidos por el **Open Geospatial Consortium** (OGC). 
Es importante tener en cuenta que en los casos en que se estime necesario a nivel de consulta, y siempre en los casos de gestión de información, 
**SITMUN 3** añade una capa de autenticación de los servicios, lo que obliga a un acceso mediante usuario/contraseña.

Todos los mensajes que se muestran en las aplicaciones **SITMUN 3** están parametrizados en un archivo de recursos, que está disponible en varios idiomas.

**SITMUN 3** tiene una arquitectura de 3 niveles:

- **Nivel de datos**: Puede estar en cualquier base de datos relacional, aunque actualmente se están utilizando **Oracle** y **PostgreSQL**. 
  El modelo de datos está documentado dentro de [la organización de SITMUN en GitHub](https://github.com/sitmun).
- **Nivel de lógica de negocio**: Desarrollado en Java con [Spring Boot](https://spring.io/projects/spring-boot), 
  tiene un modelo de Entidades de [Spring Data](https://spring.io/projects/spring-data) que refleja el esquema de la base de datos.
  El acceso a la lógica de negocio de los **visores de mapas** se realiza a través de la **[API de Configuración y Autorización][api-de-configuracion-y-autorizacion]** y de la **[API de Proxy][api-de-proxy]**.
  El acceso a la lógica de negocio de la **aplicación de administración** se realiza a través de la **[API de Administración][api-de-administracion]**. 
  En ambos casos, los usuarios se autentican mediante la **[API de Autenticación](api-de-autentiación)**.
- **Nivel cliente**: Habrá varias aplicaciones en el nivel cliente. Una para los administradores del sistema y varias para diferentes tipos de usuarios finales, 
  tanto público en general como especialistas de los ayuntamientos, etc.
  Ya está disponible la aplicación para los administradores del sistema en [GitHub](https://github.com/sitmun/sitmun-admin-app)

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

    Mediante el fichero `docker-compose.yml` se puede desplegar toda la infraestructura de **SITMUN 3** si se modifica el nombre de la imagen correspondiente al backend con el nombre de la imagen adecuada, ya sea una previamente construida o la oficial.
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
