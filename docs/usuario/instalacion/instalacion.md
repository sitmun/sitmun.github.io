---
description: "Cómo instalar SITMUN 1.3.0 con Docker (producción, showcase o desarrollo) o compilar cada componente desde el código fuente."
---

# Instalación

Todo el código de **SITMUN 3** está en un único repositorio: [sitmun/sitmun](https://github.com/sitmun/sitmun).
Cada componente (administrador, visor, backend, proxy, MBTiles y aplicaciones móviles) es una carpeta de ese repositorio.
Los repositorios antiguos por componente (`sitmun-application-stack`, `sitmun-backend-core`, `sitmun-admin-app`, etc.) solo llegan a la versión 1.2.9.

=== "Docker"

    **Elegir cómo instalar**

    | Uso (versión) | Perfil | Base de datos |
    | --- | --- | --- |
    | *Showcase* (`v1.3.0`) | `showcase.env` | Tres aplicaciones de ejemplo |
    | Producción, PostgreSQL (`v1.3.0`) | `postgres.env` | Vacía |
    | Producción, Oracle (`v1.3.0`) | `oracle.env` | Vacía |
    | Desarrollo, PostgreSQL (`dev`) | `development-postgres.env` | Datos de ejemplo |
    | Desarrollo, Oracle (`dev`) | `development-oracle.env` | Datos de ejemplo |

    Los perfiles están en la carpeta `profiles/` del repositorio. La versión, entre paréntesis, es la etiqueta o la rama que se descarga.

    **Pasos de instalación (producción)**

    1. Se clona la versión publicada y se entra en el directorio:

        ```bash
        git clone --branch v1.3.0 https://github.com/sitmun/sitmun.git
        cd sitmun
        ```

    2. Se copia el perfil a `.env` y se generan los secretos:

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

        Para Oracle se copia `profiles/oracle.env` en lugar de `profiles/postgres.env`.

        En un servidor, antes de arrancar, se indica en `.env` la dirección por la que se accederá a SITMUN:
        `PUBLIC_URL_SCHEME`, `PUBLIC_HOSTNAME` y `PUBLIC_PORT` (por ejemplo `https`, `sitmun.ejemplo.org` y `443`).
        El front de Docker solo sirve HTTP en el puerto 9000, así que con `https` y `443` hace falta delante un proxy
        inverso con el certificado TLS que reenvíe las peticiones al puerto 9000.
        Con los valores del perfil (`http`, `localhost`, `9000`), el front redirige a `localhost` y las direcciones
        del proxy apuntan a `localhost`, así que solo funcionan desde la propia máquina.

        `setup.sh` y `setup.ps1` añaden a `.env` los tres secretos que faltan:
        `SITMUN_USER_SECRET`, `MIDDLEWARE_SECRET` y `SITMUN_MBTILES_JOB_HANDLE_SECRET`.
        Docker Compose no arranca si falta alguno.

    3. Se arranca la plataforma con las imágenes publicadas:

        ```bash
        docker compose up -d --pull always --no-build
        ```

    4. Se espera a que el backend responda con `"status":"UP"`. La primera vez tarda unos minutos, mientras crea la base de datos (con Oracle, algo más: la base de datos tarda en arrancar):

        ```bash
        curl http://localhost:9001/api/dashboard/health
        ```

        En PowerShell se usa `curl.exe` en lugar de `curl`.

    5. El administrador está en <http://localhost:9000/admin/> y el visor en <http://localhost:9000/viewer/> (o en la dirección pública configurada).
       La documentación de la API (Swagger UI) está en <http://localhost:9001/swagger-ui/index.html>.

    **Primer acceso al administrador**

    En una base de datos de producción (y en el *showcase*) el usuario `admin` no tiene contraseña.
    La primera visita a `/admin/` pide crear su contraseña y elegir el idioma por defecto.
    Cualquiera que llegue al puerto 9000 puede hacer esa primera visita, así que conviene hacerla enseguida,
    o definir `SITMUN_BOOTSTRAP_ADMIN_PASSWORD` (y, opcionalmente, `SITMUN_BOOTSTRAP_LANGUAGE`) en `.env` antes de arrancar.
    La contraseña debe tener entre 8 y 50 caracteres y no puede ser `admin`: si no cumple, el backend solo lo anota
    en su registro y la primera visita sigue pidiendo crearla.
    Esas variables se quitan de `.env` cuando `GET /api/setup/status` (puerto 9001) responde `"firstRun": false`.

    ![Primer acceso: idioma por defecto](img/primer-acceso-idioma.webp){ loading=lazy }

    ![Primer acceso: contraseña del usuario admin](img/primer-acceso-contrasena.webp){ loading=lazy }

    En una base de datos de desarrollo el usuario es `admin` y la contraseña `admin`.

    **Probar SITMUN (showcase)**

    - Linux/macOS:

        ```bash
        git clone --branch v1.3.0 https://github.com/sitmun/sitmun.git
        cd sitmun
        cp profiles/showcase.env .env
        ./setup.sh
        docker compose -p sitmun-showcase up -d --pull always --no-build
        ```

    - Windows:

        ```powershell
        git clone --branch v1.3.0 https://github.com/sitmun/sitmun.git
        cd sitmun
        Copy-Item profiles\showcase.env .env
        .\setup.ps1
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

    En Windows se usa `.\setup.ps1` en lugar de `./setup.sh`.
    Sin `.env`, `setup.sh` (o `setup.ps1`) copia `profiles/development-postgres.env`.
    `docker compose up -d` sin `--no-build` compila las imágenes a partir del código del repositorio.

    **Servicios**

    Los servicios están definidos en el archivo `compose.yaml`:

    - `front`: servidor web *nginx* en el puerto 9000. Publica el visor (`/viewer/`) y el administrador (`/admin/`) y enruta `/backend/` al `backend` y `/middleware/` al `proxy`.
    - `backend`: API de Autenticación, autorización, configuración y administración (puerto 9001).
    - `proxy`: API de Proxy-middleware, que se comunica con el `backend` (puerto 9002).
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

    - `COMPOSE_PROFILES`: `postgres` u `oracle`. Se añade `,demo` para la base de datos de ejemplo y `,mbtiles` para MBTiles.
    - `DATABASE_TYPE`, `DATABASE_URL`, `DATABASE`, `DATABASE_USERNAME`, `DATABASE_PASSWORD`.
    - `PUBLIC_URL_SCHEME`, `PUBLIC_HOSTNAME`, `PUBLIC_PORT`: dirección pública de la instalación.
    - `PUBLIC_BASE_PATH`: ruta pública (`/` por defecto). La imagen publicada del front solo funciona en `/`: para publicar
      SITMUN bajo una ruta (por ejemplo `/sitmun3/`) hay que construir `front` desde el repositorio con `PUBLIC_BASE_PATH`
      y `LOCAL_BASE_PATH`, como explica DEPLOYMENT.md (*Path prefix*).
    - `SPRING_PROFILES_ACTIVE`: perfiles del backend. Se añade `mail` (por ejemplo `prod,postgres,mail`) para que funcione
      la recuperación de contraseña del visor; sin él, «¿Contraseña olvidada?» acaba en error. El servidor de correo se configura
      con las propiedades `spring.mail.*` y `sitmun.recover-password.mail.from` en un archivo `application-mail.yml` dentro de
      la carpeta de configuración del perfil (por ejemplo `profiles/postgres/`). Los usuarios necesitan un correo electrónico.
    - `SITMUN_USER_SECRET`, `MIDDLEWARE_SECRET`, `SITMUN_MBTILES_JOB_HANDLE_SECRET`: secretos obligatorios (los genera `setup.sh`).
    - `FORCE_USE_OF_PROXY`: fuerza el uso del proxy (`false` por defecto).

    La lista completa, la conexión a una base de datos externa, las copias de seguridad y la publicación bajo una ruta
    están en [DEPLOYMENT.md](https://github.com/sitmun/sitmun/blob/main/DEPLOYMENT.md).
    La actualización desde 1.2.8 o 1.2.9 está en
    [docs/upgrade](https://github.com/sitmun/sitmun/tree/main/docs/upgrade).

    **Parar y desinstalar**

    Para parar SITMUN conservando los datos:

    ```bash
    docker compose down
    ```

    Para eliminar los contenedores, **incluida la base de datos** (no se puede deshacer; conviene hacer antes una
    [copia de seguridad](solucion-problemas.md#backup-de-base-de-datos) si se necesita):

    ```bash
    docker compose down -v
    ```

    Si se arrancó el *showcase*, se añade `-p sitmun-showcase` después de `docker compose`.
    Las imágenes descargadas, el archivo `.env` (con los secretos) y la carpeta `logs/` no se borran:
    se eliminan con `docker image rm` y borrando la carpeta del repositorio.

=== "Fuente"

    Todos los componentes se compilan desde la raíz del repositorio [sitmun/sitmun](https://github.com/sitmun/sitmun).
    Cada componente tiene su propio README con todos los detalles.

    Los comandos de esta sección son para una consola *bash* (Linux, macOS, o en Windows Git Bash o WSL). En la consola de
    Windows (`cmd`) no funcionan `export`, `envsubst`, `$(...)` ni `openssl`; para compilar el visor con
    `cmd` se usa `pnpm run build:win` en lugar de `pnpm run build`.
    Las pruebas de la versión 1.3.0 se ejecutan con PostgreSQL 12 y 16 y con Oracle 11g y 19c (en las pruebas, 19c se sustituye por 21c). La instalación con Docker usa PostgreSQL 16 u Oracle 23 Free.

    ```bash
    git clone --branch v1.3.0 https://github.com/sitmun/sitmun.git
    cd sitmun
    ```

    === "Backend"

        1. Antes del primer arranque, la base de datos tiene que existir y estar vacía, con un usuario propietario.
           En PostgreSQL, por ejemplo:

            ```bash
            psql -U postgres -c "CREATE USER sitmun3 WITH PASSWORD '<contraseña>'"
            psql -U postgres -c "CREATE DATABASE sitmun3 OWNER sitmun3"
            ```

           En Oracle, un usuario (esquema) con los privilegios `CREATE SESSION` y `CREATE TABLE` y cuota en su tablespace;
           sin cuota, Liquibase falla con `ORA-01950`. Por ejemplo, como administrador de la base de datos:

            ```sql
            CREATE USER sitmun3 IDENTIFIED BY "<contraseña>" QUOTA UNLIMITED ON USERS;
            GRANT CREATE SESSION, CREATE TABLE TO sitmun3;
            ```

           Al arrancar, el backend crea las tablas con Liquibase.

        2. Se compila con Gradle desde la raíz del repositorio:

            ```bash
            ./gradlew :sitmun-backend:build -x test
            ```

            El JAR ejecutable se genera en `sitmun-backend/build/libs/sitmun-backend-<versión>.jar`
            (no el JAR `-plain`). Con `-Ppackaging=war` se genera un WAR.

        3. Se ejecuta desde la raíz del repositorio. El JAR no incluye la configuración de cada base de datos:
           está en `profiles/postgres/` (o `profiles/oracle/`) y se carga con `--spring.config.additional-location`.
           La conexión, el *changelog* de Liquibase y los dos secretos se pasan como variables de entorno
           (son los mismos valores que usa `profiles/postgres.env` con Docker):

            ```bash
            export SPRING_DATASOURCE_URL=jdbc:postgresql://localhost:5432/sitmun3
            export SPRING_DATASOURCE_USERNAME=sitmun3
            export SPRING_DATASOURCE_PASSWORD=<contraseña>
            export SPRING_LIQUIBASE_CHANGE_LOG=file:profiles/postgres/liquibase/master.xml
            export SPRING_LIQUIBASE_CONTEXTS=
            export SPRING_JPA_HIBERNATE_DDL_AUTO=validate
            export SITMUN_USER_SECRET=$(openssl rand -hex 32)
            export SITMUN_PROXY_MIDDLEWARE_SECRET=$(openssl rand -hex 32)
            export SITMUN_PROXY_MIDDLEWARE_URL=http://localhost:8082
            java -jar sitmun-backend/build/libs/sitmun-backend-1.3.0.jar \
              --spring.profiles.active=prod,postgres \
              --spring.config.additional-location=file:profiles/postgres/
            ```

            - `SITMUN_PROXY_MIDDLEWARE_URL` es la dirección **pública** del proxy, la que usarán los navegadores
              para las capas y tareas que pasan por el proxy (por ejemplo `https://ejemplo.org/middleware`
              si un servidor web lo publica en esa ruta). El ejemplo apunta al proxy del paso siguiente,
              arrancado en el puerto 8082.
            - Los dos secretos se deben guardar: `SITMUN_PROXY_MIDDLEWARE_SECRET` debe ser el mismo que use el **proxy**
              (`SITMUN_BACKEND_CONFIG_SECRET`), y si cambia `SITMUN_USER_SECRET` se invalidan las sesiones.
            - Para Oracle se usa el perfil `prod,oracle` (u `oracle-11` para Oracle 11g), la carpeta `profiles/oracle/`,
              su `liquibase/master.xml` y una URL `jdbc:oracle:thin:@//<servidor>:1521/<servicio>`.
            - Cuando arranque, `http://localhost:8080/api/dashboard/health` responde `UP`.
              En una base de datos nueva, la primera visita al administrador pide crear la contraseña de `admin`.

        La configuración (base de datos, secretos, LDAP, OIDC…) se detalla en
        [sitmun-backend/README.md](https://github.com/sitmun/sitmun/blob/main/sitmun-backend/README.md).

        Para que el backend arranque con el sistema:

        - En Linux, como servicio *systemd*. Por ejemplo, con las variables anteriores en `/etc/sitmun/backend.env`
          (una por línea, sin `export` y con los valores ya generados, porque systemd no ejecuta `$(openssl …)`) y el repositorio en `/opt/sitmun`, el archivo
          `/etc/systemd/system/sitmun-backend.service`:

            ```ini
            [Unit]
            Description=SITMUN backend
            After=network.target

            [Service]
            User=sitmun
            WorkingDirectory=/opt/sitmun
            EnvironmentFile=/etc/sitmun/backend.env
            ExecStart=/usr/bin/java -jar sitmun-backend/build/libs/sitmun-backend-1.3.0.jar --spring.profiles.active=prod,postgres --spring.config.additional-location=file:profiles/postgres/
            Restart=on-failure

            [Install]
            WantedBy=multi-user.target
            ```

          `User=sitmun` es un usuario del sistema sin privilegios (por ejemplo, `useradd --system sitmun`); sin esa línea,
          el servicio se ejecuta como `root`. Después, `systemctl enable --now sitmun-backend`. El proxy se instala igual, con su propio archivo.
        - En Windows, como servicio con [WinSW](https://github.com/winsw/winsw): su archivo XML ejecuta el mismo
          comando `java -jar …` con las mismas variables de entorno (ver la documentación de WinSW).

    === "Proxy"

        1. Se compila con Gradle desde la raíz del repositorio:

            ```bash
            ./gradlew :sitmun-proxy:build -x test
            ```

            El JAR ejecutable se genera en `sitmun-proxy/build/libs/sitmun-proxy-<versión>.jar`.

        2. Se ejecuta desde la raíz del repositorio:

            ```bash
            export SITMUN_BACKEND_CONFIG_URL=http://localhost:8080/api/config/proxy
            export SITMUN_BACKEND_CONFIG_SECRET=<el valor de SITMUN_PROXY_MIDDLEWARE_SECRET del backend>
            java -jar sitmun-proxy/build/libs/sitmun-proxy-1.3.0.jar --spring.profiles.active=prod --server.port=8082
            ```

            - `SITMUN_BACKEND_CONFIG_URL` es la URL de la **[API de Configuración y Autorización][api-de-configuracion-y-autorizacion]**
              del backend. Si el **proxy** y el **backend** están en máquinas distintas, se usa el nombre o la dirección IP interna del **backend**.
            - `SITMUN_BACKEND_CONFIG_SECRET` debe ser idéntico al secreto del backend y tener al menos 32 caracteres.

            El backend y el proxy usan por defecto el puerto 8080. Si están en la misma máquina, el proxy se arranca
            en otro puerto (por ejemplo 8082, el mismo que `SITMUN_PROXY_MIDDLEWARE_URL` del backend).
            Cuando arranque, `http://localhost:8082/actuator/health` responde `UP`.

        La imagen Docker se construye desde la raíz con `docker/proxy/Dockerfile`.
        Más detalles en [sitmun-proxy/README.md](https://github.com/sitmun/sitmun/blob/main/sitmun-proxy/README.md).

    === "Visor de mapas"

        1. Se instalan las dependencias desde la raíz del repositorio (con Node.js y pnpm, ver [Requisitos](requisitos.md)):

            ```bash
            pnpm ci
            ```

        2. Se compila. `PUBLIC_BASE_PATH` es la ruta pública bajo la que se publica SITMUN (`/` si el visor queda en `/viewer/`).
           El visor la necesita para cargar sus módulos y registrar su *service worker* desde `/viewer/`,
           igual que hace la imagen Docker:

            ```bash
            cd sitmun-viewer
            export PUBLIC_BASE_PATH=/ APP_VERSION=1.3.0 FRONT_ENV=Production BUILD_TIMESTAMP=
            envsubst '$PUBLIC_BASE_PATH' < ../docker/front/viewer/index.html.template > src/index.html
            envsubst '$BUILD_TIMESTAMP,$APP_VERSION,$FRONT_ENV,$PUBLIC_BASE_PATH' \
              < ../docker/front/viewer/environment.prod.ts.template > src/environments/environment.prod.ts
            pnpm run build --configuration=production --base-href=${PUBLIC_BASE_PATH}viewer/
            ```

            `envsubst` forma parte de GNU gettext. Sin `PUBLIC_BASE_PATH` el visor compila, pero
            se queda en blanco: busca sus módulos en la raíz del servidor en lugar de en `/viewer/`.
            El segundo `envsubst` genera la configuración que usa la imagen Docker: la dirección del backend
            (`${PUBLIC_BASE_PATH}backend`) y las mismas opciones, por ejemplo sin el acceso con DNIe.

            Los archivos se generan en `sitmun-viewer/dist/viewer-app`.
            Esta compilación usa direcciones con `#`, por ejemplo `/viewer/#/public/dashboard`.

        El contenido de esa carpeta se copia a `/viewer/` en el servidor web (ver más abajo, *Publicar en un servidor web*).
        Para compilar después el administrador, se vuelve antes a la raíz del repositorio (`cd ..`).

        Más detalles en [sitmun-viewer/README.md](https://github.com/sitmun/sitmun/blob/main/sitmun-viewer/README.md).

    === "Administrador"

        1. Se instalan las dependencias desde la raíz del repositorio:

            ```bash
            pnpm ci
            ```

        2. Se compila. Igual que en el visor, el segundo comando genera la configuración que usa la imagen Docker:

            ```bash
            cd sitmun-admin
            export PUBLIC_BASE_PATH=/ APP_VERSION=1.3.0 FRONT_ENV=Production BUILD_TIMESTAMP=
            envsubst '$BUILD_TIMESTAMP,$APP_VERSION,$FRONT_ENV,$PUBLIC_BASE_PATH' \
              < ../docker/front/admin/environment.prod.ts.template > src/environments/environment.prod.ts
            pnpm run build --configuration=production --base-href=${PUBLIC_BASE_PATH}admin/
            ```

            Los archivos se generan en `sitmun-admin/dist/admin-app`.

        El contenido de esa carpeta se copia a `/admin/` en el servidor web (ver *Publicar en un servidor web*).
        Más detalles en [sitmun-admin/README.md](https://github.com/sitmun/sitmun/blob/main/sitmun-admin/README.md).

    **Publicar en un servidor web**

    El visor y el administrador llaman a la API en `/backend` del mismo servidor, y el visor usa el proxy
    en la dirección `SITMUN_PROXY_MIDDLEWARE_URL` del backend. El servidor web (nginx, Apache, IIS…) debe:

    - servir `dist/viewer-app` en `/viewer/` y `dist/admin-app` en `/admin/`, devolviendo el `index.html` de cada uno
      cuando el archivo pedido no existe;
    - reenviar `/backend/` al backend (`http://localhost:8080/`) y, si el proxy se publica en `/middleware/`, reenviar
      esa ruta al proxy (`http://localhost:8082/`), quitando el prefijo en ambos casos;
    - enviar al backend y al proxy las cabeceras `X-Forwarded-Proto`, `X-Forwarded-Host`, `X-Forwarded-Port` y
      `X-Forwarded-Prefix` (`/backend` o `/middleware`) con la dirección pública. Sin ellas, detrás de HTTPS
      la cookie de sesión pierde el atributo `Secure`.

    La configuración que usa la imagen Docker es un ejemplo completo:
    [docker/front/config/default.conf.template](https://github.com/sitmun/sitmun/blob/main/docker/front/config/default.conf.template).

---

Con SITMUN instalado, la guía [Primer proyecto](../guias/primer-proyecto/index.md) explica cómo crear el primer visor. Si algo no arranca, ver [Solución de problemas](solucion-problemas.md).
