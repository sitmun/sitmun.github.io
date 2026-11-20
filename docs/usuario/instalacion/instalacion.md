# Instalación

Todo el código de **SITMUN 3** está en un único repositorio: [sitmun/sitmun](https://github.com/sitmun/sitmun).
Cada componente (administrador, visor, backend, proxy, MBTiles y aplicaciones móviles) es una carpeta de ese repositorio.
Los repositorios antiguos por componente (`sitmun-application-stack`, `sitmun-backend-core`, `sitmun-admin-app`, etc.) solo llegan a la versión 1.2.9.

=== "Docker"

    **Elegir cómo instalar**

    | Uso | Rama o etiqueta | Perfil (`profiles/*.env`) | Datos |
    | --- | --- | --- | --- |
    | Probar SITMUN (*showcase*) | `main` | `showcase.env` | Tres aplicaciones de demostración |
    | Producción con PostgreSQL | `v1.3.0` | `postgres.env` | Sin datos de ejemplo |
    | Producción con Oracle | `v1.3.0` | `oracle.env` | Sin datos de ejemplo |
    | Desarrollo con PostgreSQL | `dev` | `development-postgres.env` | Datos de ejemplo |
    | Desarrollo con Oracle | `dev` | `development-oracle.env` | Datos de ejemplo |

    **Pasos de instalación (producción)**

    1. Clona la versión publicada y entra en el directorio:

        ```bash
        git clone --branch v1.3.0 https://github.com/sitmun/sitmun.git
        cd sitmun
        ```

    2. Copia el perfil a `.env` y genera los secretos:

        - Linux/macOS:

            ```bash
            cp profiles/postgres.env .env
            ./setup.sh
            ```

        - Windows:

            ```powershell
            Copy-Item profiles\postgres.env .env
            .\setup.ps1
            ```

        Para Oracle, copia `profiles/oracle.env` en lugar de `profiles/postgres.env`.

        `setup.sh` y `setup.ps1` añaden a `.env` los tres secretos que faltan:
        `SITMUN_USER_SECRET`, `MIDDLEWARE_SECRET` y `SITMUN_MBTILES_JOB_HANDLE_SECRET`.
        Docker Compose no arranca si falta alguno.

    3. Arranca la plataforma con las imágenes publicadas:

        ```bash
        docker compose up -d --pull always --no-build
        ```

    4. Verifica la instalación:

        ```bash
        docker compose ps
        curl http://localhost:9001/api/dashboard/health
        curl http://localhost:9002/actuator/health
        ```

        En PowerShell usa `curl.exe` en lugar de `curl`.

    5. Accede a las aplicaciones:

        - Visor: <http://localhost:9000/viewer/>
        - Administrador: <http://localhost:9000/admin/>
        - Backend API: <http://localhost:9000/backend/>
        - Documentación de la API (Swagger UI): <http://localhost:9001/swagger-ui/index.html>

    **Primer acceso al administrador**

    En una base de datos de producción el usuario `admin` no tiene contraseña.
    La primera visita a `/admin/` pide crear su contraseña y elegir el idioma por defecto.
    Cualquiera que llegue al puerto 9000 puede hacer esa primera visita, así que hazla enseguida,
    o define `SITMUN_BOOTSTRAP_ADMIN_PASSWORD` (y, si quieres, `SITMUN_BOOTSTRAP_LANGUAGE`) en `.env` antes de arrancar.
    Quita esas variables de `.env` cuando `GET /api/dashboard/health` responda `UP`.

    En una base de datos de desarrollo el usuario es `admin` y la contraseña `admin`.

    **Probar SITMUN (showcase)**

    ```bash
    git clone https://github.com/sitmun/sitmun.git
    cd sitmun
    cp profiles/showcase.env .env
    ./setup.sh
    docker compose -p sitmun-showcase up -d --pull always --no-build
    ```

    En el visor, el usuario `demo` con contraseña `demo` ve las tres aplicaciones de demostración.

    **Entorno de desarrollo**

    ```bash
    git clone --branch dev https://github.com/sitmun/sitmun.git
    cd sitmun
    ./setup.sh
    docker compose up -d
    ```

    Sin `.env`, `setup.sh` copia `profiles/development-postgres.env`.
    `docker compose up -d` sin `--no-build` compila las imágenes a partir del código del repositorio.

    **Servicios**

    Los servicios están definidos en el archivo `compose.yaml`:

    - `front`: servidor web *nginx* en el puerto 9000. Publica el visor (`/viewer/`) y el administrador (`/admin/`) y enruta `/backend/` al `backend` y `/middleware/` al `proxy`.
    - `backend`: API de autenticación, autorización, configuración y administración (puerto 9001).
    - `proxy`: API de proxy-middleware, que se comunica con el `backend` (puerto 9002).
    - `postgres`: base de datos PostgreSQL 16 en el volumen `pgdata` (puerto 9003, perfil `postgres`).
    - `oracle`: base de datos Oracle 23 Free (puerto 9004, perfil `oracle`).
    - `example`: base de datos PostgreSQL de ejemplo (puerto 9005, perfil `demo`).
    - `mbtiles`: servicio de exportación de teselas para la aplicación móvil de edición (perfil `mbtiles`, sin puerto publicado).

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

    Las variables de entorno se definen en el archivo `.env`. Variables clave:

    - `COMPOSE_PROFILES`: `postgres` u `oracle`. Añade `,demo` para la base de datos de ejemplo y `,mbtiles` para MBTiles.
    - `DATABASE_TYPE`, `DATABASE_URL`, `DATABASE`, `DATABASE_USERNAME`, `DATABASE_PASSWORD`.
    - `PUBLIC_URL_SCHEME`, `PUBLIC_HOSTNAME`, `PUBLIC_PORT`, `PUBLIC_BASE_PATH`: dirección pública de la instalación.
    - `SITMUN_USER_SECRET`, `MIDDLEWARE_SECRET`, `SITMUN_MBTILES_JOB_HANDLE_SECRET`: secretos obligatorios (los genera `setup.sh`).
    - `FORCE_USE_OF_PROXY`: fuerza el uso del proxy (`false` por defecto).

    La lista completa, la conexión a una base de datos externa, las copias de seguridad y la publicación bajo una ruta
    están en [DEPLOYMENT.md](https://github.com/sitmun/sitmun/blob/main/DEPLOYMENT.md).
    La actualización desde 1.2.8 o 1.2.9 está en
    [docs/upgrade](https://github.com/sitmun/sitmun/tree/main/docs/upgrade).

    **Desinstalación**

    Para detener y eliminar todos los servicios, volúmenes y redes definidos en `compose.yaml`, usa:

    ```bash
    docker compose down -v
    ```

    Añade `-p sitmun-showcase` después de `docker compose` si instalaste el *showcase*.

=== "Fuente"

    Todos los componentes se compilan desde la raíz del repositorio [sitmun/sitmun](https://github.com/sitmun/sitmun).
    Cada componente tiene su propio README con todos los detalles.

    ```bash
    git clone --branch v1.3.0 https://github.com/sitmun/sitmun.git
    cd sitmun
    ```

    === "Backend"

        1. Compila con Gradle desde la raíz del repositorio:

            ```bash
            ./gradlew :sitmun-backend:build -x test
            ```

            El JAR ejecutable se genera en `sitmun-backend/build/libs/sitmun-backend-<versión>.jar`
            (no uses el JAR `-plain`). Con `-Ppackaging=war` se genera un WAR.

        2. Ejecútalo indicando el perfil Spring de la base de datos (`postgres`, `oracle` u `oracle-11`)
           y la conexión a la base de datos:

            ```bash
            java -jar sitmun-backend/build/libs/sitmun-backend-1.3.0.jar --spring.profiles.active=postgres
            ```

        La configuración (base de datos, secretos, LDAP, OIDC…) se detalla en
        [sitmun-backend/README.md](https://github.com/sitmun/sitmun/blob/main/sitmun-backend/README.md).

        Los sistemas operativos en los que se puede desplegar el **backend** son:

        - Linux: como servicio *systemd* o mediante un script de arranque.
        - Windows: como servicio Windows usando la herramienta *WinSW* o mediante un script de arranque.

    === "Proxy"

        1. Compila con Gradle desde la raíz del repositorio:

            ```bash
            ./gradlew :sitmun-proxy:build -x test
            ```

            El JAR ejecutable se genera en `sitmun-proxy/build/libs/sitmun-proxy-<versión>.jar`.

        2. Configura las variables de entorno:

            - `SITMUN_BACKEND_CONFIG_URL`: URL de la **[API de Configuración y Autorización][api-de-configuracion-y-autorizacion]**
              del backend, por ejemplo `http://backend:8080/api/config/proxy`.
              Si el **proxy** y el **backend** están en la misma red, usa el nombre o la dirección IP interna del **backend**.
            - `SITMUN_BACKEND_CONFIG_SECRET`: el mismo secreto que el backend tiene en `SITMUN_PROXY_MIDDLEWARE_SECRET`.

        3. Ejecútalo:

            ```bash
            java -jar sitmun-proxy/build/libs/sitmun-proxy-1.3.0.jar --spring.profiles.active=prod
            ```

        La imagen Docker se construye desde la raíz con `docker/proxy/Dockerfile`.
        Más detalles en [sitmun-proxy/README.md](https://github.com/sitmun/sitmun/blob/main/sitmun-proxy/README.md).

    === "Visor de mapas"

        1. Instala las dependencias desde la raíz del repositorio (necesitas Node.js y pnpm, ver [Requisitos](requisitos.md)):

            ```bash
            pnpm ci
            ```

        2. Revisa `apiUrl` en `sitmun-viewer/src/environments/environment.prod.ts`. Por defecto es `/backend`.

        3. Compila:

            ```bash
            cd sitmun-viewer
            pnpm run build -- --configuration=production --base-href=/viewer/
            ```

            Los archivos se generan en `sitmun-viewer/dist/viewer-app`.

        Copia el contenido de esa carpeta a tu servidor web y
        configura el servidor para redirigir las solicitudes de archivos no encontrados a `index.html`.

        !!! warning "No olvides configurar la redirección a `index.html` en tu servidor"
            Si no se configura correctamente la redirección, es posible que la navegación dentro del visor de mapas
            funcione correctamente, pero al hacer clic en un enlace externo (por ejemplo, un enlace de correo electrónico),
            al introducir una URI directamente en la barra de direcciones o simplemente al refrescar la página,
            se produzca un error 404. Esto ocurre porque estas peticiones son manejadas directamente por el navegador
            y no por enrutador de Angular que gestiona la navegación dentro del visor de mapas.
            Ver [Routed apps must fall back to index.html](https://angular.dev/tools/cli/deployment#server-configuration)
            en la documentación oficial de Angular para más información.

        Más detalles en [sitmun-viewer/README.md](https://github.com/sitmun/sitmun/blob/main/sitmun-viewer/README.md).

    === "Administrador"

        1. Instala las dependencias desde la raíz del repositorio:

            ```bash
            pnpm ci
            ```

        2. Revisa `apiBaseURL` en `sitmun-admin/src/environments/environment.prod.ts`. Por defecto es `/backend`.

        3. Compila:

            ```bash
            cd sitmun-admin
            pnpm run build -- --configuration=production --base-href=/admin/
            ```

            Los archivos se generan en `sitmun-admin/dist/admin-app`.

        Copia el contenido de esa carpeta a tu servidor web.
        Más detalles en [sitmun-admin/README.md](https://github.com/sitmun/sitmun/blob/main/sitmun-admin/README.md).

---

Siguiente paso: [Primer proyecto](../guias/primer-proyecto/index.md)
