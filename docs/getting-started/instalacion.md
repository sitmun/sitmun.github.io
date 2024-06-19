# Instalación

=== "Docker"

      Los servicios están definidos en el archivo `docker-compose.yml`.
      Los siguientes servicios están disponibles:

      - `viewer`: aplicación del visor de SITMUN
      - `admin`: aplicación administrativa de SITMUN
      - `backend`: API de SITMUN
      - `proxy`: proxy de SITMUN
      - `postgres`: base de datos PostgreSQL

      Para fines de prueba, el uso del `proxy` está controlado por la variable de entorno `sitmun.proxy.force` en `backend`, que por defecto es `true`.

      Los datos se almacenan en el volumen `pgdata`, que es utilizado por el servicio `postgres`.

      **Pasos de instalación**

      Para instalar SITMUN, sigue estos pasos:

      1. Clona el repositorio y los proyectos anidados de SITMUN:

         ```bash
         git clone --recurse-submodules https://github.com/sitmun/sitmun-application-stack.git
         ```

      2. Cambia al directorio del repositorio:

         ```bash
         cd sitmun-application-stack
         ```

      3. Crea un nuevo archivo llamado `.env` dentro del directorio.
         Abre el archivo `.env` en un editor de texto y agrega tu token de acceso personal de GitHub (`GITHUB_TOKEN`) en el siguiente formato:

         ```properties
         GITHUB_TOKEN=tu_token_de_acceso_personal
         ```

      4. Inicia la plataforma SITMUN:

         ```bash
         docker compose up
         ```

         Este comando construirá e iniciará todos los servicios definidos en el archivo `docker-compose.yml`.

      5. Accede a la aplicación del visor de SITMUN en [http://localhost:9000/viewer](http://localhost:9000/viewer).
         Usa el acceso público que no requiere autenticación.

      6. Accede a la aplicación administrativa de SITMUN en [http://localhost:9000/admin](http://localhost:9000/admin).
         Esto requiere autenticación.
         El nombre de usuario predeterminado es `admin` y la contraseña predeterminada es `admin`.

      **Configuración**

      Las variables de entorno se definen en el archivo `.env`.

      Las siguientes variables de entorno están disponibles:

      - `GITHUB_TOKEN`: [Token de acceso personal de GitHub (clásico)](https://docs.github.com/en/packages/learn-github-packages/introduction-to-github-packages#authenticating-to-github-packages).
      El token es necesario para obtener paquetes `npm` de [GitHub Packages](https://docs.github.com/en/packages/learn-github-packages/introduction-to-github-packages#about-github-packages).

      **Desinstalación**

      Para detener y eliminar todos los servicios, volúmenes y redes definidos en el archivo `docker-compose.yml`, usa:

      ```bash
      docker compose down -v
      ```

=== "Fuente"

    !!! info "En desarrollo"
        Esta sección está siendo actualizada.
        Las instrucciones de instalación son un ejemplo de como serán en un futuro.
        Actualmente, se recomienda solo usar en modo de prueba `heroku-dev-full` que requiere de una base de datos `postgres`.

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
         2. Obtiene un [token de GitHub para trabajar con el registro de npm de GitHub Packages](https://docs.github.com/es/packages/working-with-a-github-packages-registry/working-with-the-npm-registry).
         3. Desde la consola de comandos ejecuta el siguiente comando para autenticarte en el registro de GitHub Packages de npm:

            ```shell
            npm set //npm.pkg.github.com/:_authToken <token>
            ```

            Sustituye `<token>` por el token que has obtenido en el paso anterior.
         4. Abre el proyecto descargado y modifica el parámetro `apiUrl` en el archivo `environments.ts` para que apunte
            a la URI donde está desplegado el **backend**. Ver [Configuración](../configuration.md#visor-de-mapas).
         5. Desde la consola de comandos, navega hasta el directorio raíz del proyecto y ejecuta el comando:

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
         2. Obtiene un [token de GitHub para trabajar con el registro de npm de GitHub Packages](https://docs.github.com/es/packages/working-with-a-github-packages-registry/working-with-the-npm-registry).
         3. Desde la consola de comandos ejecuta el siguiente comando para autenticarte en el registro de GitHub Packages de npm:

            ```shell
            npm set //npm.pkg.github.com/:_authToken <token>
            ```

            Sustituye `<token>` por el token que has obtenido en el paso anterior.
         4. Abre el proyecto descargado y modifica el parámetro `apiUrl` en el archivo `environments.ts` para que apunte
            a la URI donde está desplegado el **backend**. Ver [Configuración](../configuration.md#visor-de-mapas).
         5. Desde la consola de comandos, navega hasta el directorio raíz del proyecto y ejecuta el comando:

            ```shell
            npm ci
            npm build -- --configuration=<conf> --baseHref=<baseHref>
            ```

            Donde `<conf>` es la configuración y `<baseHref>` es la URI donde se va a desplegar.
            Este comando compilará el **administrador** para el entorno de producción y
            generará los archivos en la carpeta `dist/sitmun-admin-app`.

         Para desplegar el **administrador** en un servidor web, copia la carpeta `sitmun-admin-app` a tu servidor web.
