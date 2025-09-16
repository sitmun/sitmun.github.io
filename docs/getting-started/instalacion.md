# Instalación

=== "Docker"

      **Pasos de instalación**

      Para instalar SITMUN, sigue estos pasos:

      1. Clona el repositorio con submódulos y entra en el directorio:

         ```bash
         git clone --branch dev --recurse-submodules https://github.com/sitmun/sitmun-application-stack.git
         cd sitmun-application-stack
         ```

      2. Prepara el entorno:

         - Linux/macOS:

           ```bash
           ./setup.sh
           ```

         - Windows:

           ```powershell
           ./setup.ps1
           ```

      3. Arranca la plataforma SITMUN:

         ```bash
         docker compose up -d
         ```

         Nota: Por defecto se utiliza PostgreSQL. Para usar Oracle:

         ```bash
         COMPOSE_PROFILES=oracle docker compose up -d
         ```

      4. Verifica la instalación:

         ```bash
         docker compose ps
         curl http://localhost:9001/api/dashboard/health
         curl http://localhost:9002/actuator/health
         ```

      5. Accede a las aplicaciones:

         - Visor: http://localhost:9000/viewer
         - Administrador: http://localhost:9000/admin
         - Backend API: http://localhost:9000/backend

         Credenciales por defecto:

         - Usuario: `admin`
         - Contraseña: `admin`

      **Servicios**

      Los servicios están definidos en el archivo `docker-compose.yml`.
      Los siguientes servicios están disponibles:

      - `front`, un servidor web *nginx* en el puerto 9000 que publica la aplicación del visor de SITMUN (`http://localhost:9000/viewer`) y la aplicación administrativa de SITMUN (`http://localhost:9000/admin`) y enruta las solicitudes a los servicios `backend` (`http://localhost:9000/backend`) y `proxy` (`http://localhost:9000/middleware`)
      - `backend`, que expone el API de autenticación, autorización y configuración de SITMUN (puerto 9001)
      - `proxy`, que expone el API proxy-middleware de SITMUN y que se comunica con el servicio `backend` (puerto 9002)
      - `postgres`: base de datos PostgreSQL 16 que almacena los datos en el volumen `pgdata` (puerto 9003)
      - `oracle`: base de datos Oracle 23c alternativa (puerto 9004)
      - `example`: base de datos PostgreSQL de ejemplo (puerto 9005)


      ```mermaid
      block-beta
      columns 5

      space:2
      front["<b>front</b><br>nginx<br>localhost:9000"]
      space:2

      space:5

      postgres[("<b>postgres</b><br>PostgreSQL 16<br>SITMUN database")]
      space:1
      backend["<b>backend</b><br>Spring Boot<br>SITMUN backend"]
      space:1
      proxy["<b>proxy</b><br>Spring Boot<br>SITMUN proxy-middleware"]

      front -- "/middleware" --> proxy
      front -- "/backend" --> backend
      proxy -- "/api/config/proxy" --> backend
      backend -- "jdbc" --> postgres
      ```

      **Configuración**

      Las variables de entorno se definen en el archivo `.env` (si no existe, `./setup.sh` copiará `.env.example`). Variables clave:

      - `COMPOSE_PROFILES`: perfiles activos (`postgres`/`oracle`). Por defecto: `postgres`.
      - `DATABASE`, `DATABASE_URL`, `DATABASE_USERNAME`, `DATABASE_PASSWORD`.
      - `FORCE_USE_OF_PROXY`: fuerza el uso del proxy (`false` por defecto).

      **Desinstalación**

      Para detener y eliminar todos los servicios, volúmenes y redes definidos en el archivo `docker-compose.yml`, usa:

      ```bash
      docker compose down -v
      ```

=== "Fuente"

    !!! info "En desarrollo"
        Esta sección está siendo actualizada.
        Las instrucciones de instalación son un ejemplo de como serán en un futuro.
        

    === "Backend"

        Una vez completada la instalación de los prerrequisitos y la configuración, puedes proceder con la compilación del **backend** siguiendo estos pasos:

        1. Descarga el proyecto <https://github.com/sitmun/sitmun-backend-core> en tu equipo.
        2. Crea un proyecto nuevo a partir de las plantillas de la carpeta `deploy` y añádelo a `settings.gradle`.
        3. Configura el fichero `application.yml` del nuevo proyecto. Ver [Configuración](../configuration.md#administrador).
        4. Ejecutar el siguiente comando desde la raíz del proyecto en una terminal.
           ```bash
           ./gradlew clean :[proyecto]:build
           ```
           Este comando genera el fichero JAR del **proxy** en la ruta
           ```
           .[proyecto]/build/libs/[proyecto]-${version}.jar
           ```

        Los sistemas operativos en los que se pueden desplegar el **backend** son:

        - Linux: como servicio *init.d*, como servicio *systemd* o mediante un script de arranque.
        - Windows: puede ejecutarse como un servicio Windows usando la herramienta *WinSW* o mediante un script de arranque.

    === "Proxy"

         Una vez completada la instalación de los prerrequisitos y la configuración, puedes proceder con la compilación del **proxy** siguiendo estos pasos:

         1. Descarga el proyecto <https://github.com/sitmun/sitmun-proxy-middleware> en tu equipo.
         2. Abre el proyecto descargado y modifica del fichero `application.yml` las propiedades `security.authentication.middleware.secret` y `sitmun.config.url`.
            `security.authentication.middleware.secret` debe contener el token que se ha configurado en el **backend** para que el **proxy** pueda autenticarse.
            `sitmun.config.url` debe contener la URI de la **[API de Configuración y Autorización][api-de-configuracion-y-autorizacion]** del **backend**.
            Si el **proxy** y el **backend** son servicios internos de la misma red, se recomienda usar el nombre interno o la
            dirección IP interna del **backend**. Ver [Configuración](../configuration.md#proxy).
         3. Ejecutar el siguiente comando desde la raíz del proyecto en una terminal.

            ```bash
            ./gradlew clean build
            ```

            Este comando genera el fichero JAR del **proxy** en la ruta `./build/libs/` con el nombre `sitmun-proxy-middleware-[version].jar`.

         Los sistemas operativos en los que se pueden desplegar el **proxy** son:

         - Linux: como servicio *init.d*, como servicio *systemd* o mediante un script de arranque.
         - Windows: puede ejecutarse como un servicio Windows usando la herramienta *WinSW*  o mediante un script de arranque.

         El **proxy middleware** puede ser desplegado usando Docker.
         En la raíz del proyecto se encuentra la carpeta `docker`,
         en la cual se puede encontrar el fichero `docker-compose.yml` y el fichero `Dockerfile`.

         Si se quiere desplegar únicamente el proxy, se puede hacer construyendo y arrancando la imagen del `Dockerfile`.

         ```bash
         docker build -t sitmun/proxy-middleware .
         docker run -p 8080:8080 sitmun/proxy-middleware
         ```

         Como se ha comentado anteriormente,
         el proxy depende de la **[API de Configuración y Autorización][api-de-configuracion-y-autorizacion]** y,
         por lo tanto, es importante tener correctamente configurada la URL a la API en el fichero de configuración
         (`sitmun.config.url`).

         Es posible desplegar el **proxy middleware** en local sin necesidad de Docker mediante JVM ejecutando el siguiente
         comando en la ubicación del fichero JAR generado al construir el proxy.

         ```bash
         java -jar sitmun-proxy-middleware-[version].jar
         ```

    === "Visor de mapas"

         Una vez completada la instalación de los prerrequisitos puedes proceder con la compilación del **visor de mapas** siguiendo estos pasos:

         1. Descarga el proyecto <https://github.com/sitmun/sitmun-viewer-app> en tu equipo.
         2. Abre el proyecto descargado y modifica el parámetro `apiUrl` en el archivo `environments.ts` para que apunte a la URI donde está desplegado el **backend**. Ver [Configuración](../configuration.md#visor-de-mapas).
         3. Desde la consola de comandos, navega hasta el directorio raíz del proyecto y ejecuta el comando:

            ```shell
            npm ci
            npm build -- --configuration=<conf> --baseHref=<baseHref>
            ```

            Donde `<conf>` es la configuración y `<baseHref>` es la URI donde se va a desplegar.
            Este comando compilará el **visor de mapas** para el entorno de producción y
            generará los archivos en la carpeta `dist/sitmun-viewer-app`.

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

    === "Administrador"

         Una vez completada la instalación de los prerrequisitos puedes proceder con la compilación del **administrador** siguiendo estos pasos:

         1. Descarga el proyecto <https://github.com/sitmun/sitmun-admin-app> en tu equipo.
         2. Abre el proyecto descargado y modifica el parámetro `apiUrl` en el archivo `environments.ts` para que apunte
            a la URI donde está desplegado el **backend**. Ver [Configuración](../configuration.md#visor-de-mapas).
         3. Desde la consola de comandos, navega hasta el directorio raíz del proyecto y ejecuta el comando:

            ```shell
            npm ci
            npm build -- --configuration=<conf> --baseHref=<baseHref>
            ```

            Donde `<conf>` es la configuración y `<baseHref>` es la URI donde se va a desplegar.
            Este comando compilará el **administrador** para el entorno de producción y
            generará los archivos en la carpeta `dist/sitmun-admin-app`.

         Para desplegar el **administrador** en un servidor web, copia la carpeta `sitmun-admin-app` a tu servidor web.

    
---

Siguiente paso: [Creando una aplicación](creando.md)
