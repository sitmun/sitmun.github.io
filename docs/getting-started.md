# Primeros pasos

## ¿Qué es SITMUN 3?

**SITMUN 3** es una plataforma que permite la creación y gestión de aplicaciones personalizadas en el ámbito de los [Sistemas de Información Geográfica](https://es.wikipedia.org/wiki/Sistema_de_informaci%C3%B3n_geogr%C3%A1fica) (SIG). 
Está diseñada específicamente para satisfacer las necesidades de información territorial de las administraciones locales y supramunicipales.

**SITMUN 3** ha sido desarrollado con la visión de proporcionar una herramienta de gestión de información territorial a los municipios, gestionada desde una entidad supramunicipal.
Permite la integración de la información territorial con los datos de las corporaciones locales, independientemente del modelo de datos o del sistema de gestión de base de datos utilizado por cada municipio.
Es importante destacar que **SITMUN 3** agrega una capa de autenticación al acceso a los servicios cuando sea necesario, especialmente en consultas y siempre en los casos de gestión de información. 
Esta medida contribuye a la seguridad y privacidad de los datos, asegurando que solo usuarios autorizados puedan acceder y gestionar la información territorial

**SITMUN 3** se presenta al usuario en forma de aplicaciones accesibles a través de **visores de mapas**, que se pueden configurar para que se adapten a las necesidades de cada municipio.

**SITMUN 3** tiene una **aplicación de administración** que configura la información cartográfica, el territorio y las tareas que cada usuario tiene acceso para cada aplicación.
Estas tareas ofrecen una amplia gama de funcionalidades, como consultas a bases de datos, generación de informes, buscadores, funciones de análisis espacial, entre otras.

**SITMUN 3** dispone de una base de datos para administrar la plataforma. 
El modelo de datos permite la definición de información cartográfica, territorios, aplicaciones, tareas, usuarios, roles y permisos de acceso.

**SITMUN 3** se basa en la utilización de servicios web estándar definidos por el **[Open Geospatial Consortium](https://www.ogc.org/)** (OGC). 

Todos los mensajes que se muestran en las aplicaciones de **SITMUN 3** están parametrizados en un archivo de recursos disponible en varios idiomas.

**SITMUN 3** tiene una arquitectura de 3 niveles:

- **Nivel de datos**: Puede estar en cualquier base de datos relacional, aunque actualmente se utilizan **Oracle** y **PostgreSQL**. 
  El modelo de datos está documentado en [la organización de SITMUN en GitHub](https://github.com/sitmun).
- **Nivel de lógica de negocio**: Desarrollado en Java con [Spring Boot](https://spring.io/projects/spring-boot), 
  tiene un modelo de entidades de [Spring Data](https://spring.io/projects/spring-data) que refleja el esquema de la base de datos.
  El acceso a la lógica de negocio de los **visores de mapas** se realiza a través de la **[API de Configuración y Autorización][api-de-configuracion-y-autorizacion]** y de la **[API de Proxy][api-de-proxy]**.
  El acceso a la lógica de negocio de la **aplicación de administración** se realiza a través de la **[API de Administración][api-de-administracion]**. 
  En ambos casos, los usuarios se autentican mediante la **[API de Autenticación][api-de-autenticacion]**.
- **Nivel cliente**: Actualmente, existen una **[aplicación de administración](https://github.com/sitmun/sitmun-admin-app)** para los administradores
  y un **[visor de mapas](https://github.com/sitmun/sitmun-viewer-app)** basado en la [API SITNA](https://github.com/sitna/api-sitna)
  que es utilizado por los diferentes tipos de usuarios finales, tanto al público en general como a especialistas de los ayuntamientos, entre otros.

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

#### Prerrequisitos

Antes de proceder con la compilación del visor de mapas, 
asegúrate de tener los siguientes prerrequisitos en tu sistema:

- **Node.js**: El visor de mapas requiere **Node.js** con una versión compatible con **Angular 16**,
  que puede ser `^16.14.0 || ^18.10.0`. Puedes descargar **Node.js** desde el sitio oficial: https://nodejs.org/
- **npm**: El visor de mapas depende de paquetes gestionados por **npm**. 
  Puedes instalar **npm** siguiendo la guía oficial: https://docs.npmjs.com/cli/install

Una vez que hayas cumplido con los prerrequisitos mencionados anteriormente, 
procede a instalar el Cliente Angular (**Angular CLI**) de la siguiente manera:

```shell
npm install -g @angular/cli
```

!!! warning "No olvides activar la ejecución de scripts de PowerShell en Windows"
    Si estás utilizando un sistema operativo Windows, será necesario permitir la [ejecución de scripts de PowerShell](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies). 
    Para hacerlo, abre una consola de PowerShell con privilegios de administrador y ejecuta el siguiente comando:

    ```shell
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```

#### Compilación

Una vez completada la instalación de los prerrequisitos, puedes proceder con la compilación del visor de mapas siguiendo estos pasos:

1. Descarga el proyecto https://github.com/sitmun/sitmun-viewer-app en tu equipo.
2. Abre el proyecto descargado y modifica el parámetro `apiUrl` en el archivo `environments.ts` para que apunte 
   a la URI donde estará desplegado.
3. Desde la consola de comandos, navega hasta el directorio raíz del proyecto y ejecuta el comando `ng build`.
4. Este comando compilará el visor de mapas para el entorno de producción y 
   generará los archivos en la carpeta `dist/sitmun-viewer-app`.

#### Despliegue

Para desplegar el visor de mapas en un servidor web, copia la carpeta `sitmun-viewer-app` a tu servidor web.

Configura tu servidor para redirigir las solicitudes de archivos no encontrados a `index.html`
Es fundamental configurar correctamente esta redirección para el correcto funcionamiento del visor de mapas.

!!! warning "No olvides configurar la redirección a `index.html` en tu servidor"
    Si no se configura correctamente la redirección, es posible que la navegación dentro del visor de mapas 
    funcione correctamente, pero al hacer clic en un enlace externo (por ejemplo, un enlace de correo electrónico),
    al introducir una URI directamente en la barra de direcciones o simplemente al refrescar la página, 
    se produzca un error 404. Esto ocurre porque estas peticiones son manejadas directamente por el navegador 
    y no por enrutador de Angular que gestiona la navegación dentro del visor de mapas. 
    Ver [Routed apps must fall back to index.html](https://angular.io/guide/deployment#fallback) en la documentación
    oficial de Angular para más información.

## Creando una aplicación

## Personalización

## Filosofía de trabajo
