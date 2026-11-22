---
description: "Soluciones a los problemas más comunes al instalar y usar SITMUN 3 con Docker: puertos, base de datos, autenticación, red y copias de seguridad."
---

# Solución de problemas

Esta sección recoge soluciones a los problemas más comunes que pueden surgir durante la instalación, configuración y uso de SITMUN 3 con Docker.

!!! note "Comandos de Docker Compose"
    Los comandos `docker compose` se ejecutan desde la carpeta del repositorio.
    Si se arrancó el *showcase*, se añade `-p sitmun-showcase` después de `docker compose`.
    En PowerShell se usa `curl.exe` en lugar de `curl`.

!!! note "Oracle"
    Los comandos de base de datos de esta página son para PostgreSQL. Con el perfil `oracle`, el servicio se llama
    `oracle` y el volumen `oradata`; las copias de seguridad se hacen con Data Pump
    (ver [Copia de seguridad con Oracle](#backup-oracle)).

## Problemas de instalación

### Docker no se inicia

**Síntomas:**

- Error al ejecutar `docker compose up`.
- Los servicios no se levantan correctamente.

**Soluciones:**

```bash
# Comprobar que Docker está en marcha
docker --version
docker compose --version

# Parar y eliminar los contenedores (los datos se conservan)
docker compose down
docker system prune -f

# Reiniciar Docker Desktop (si se usa) o el servicio Docker en Linux
sudo systemctl restart docker
```

!!! danger "`docker compose down -v` borra la base de datos"
    La opción `-v` elimina también los volúmenes, entre ellos `pgdata` (u `oradata`), donde está la base de datos de SITMUN.
    Solo se usa para empezar desde cero y, antes, conviene hacer una [copia de seguridad](#backup-de-base-de-datos).

### Puerto ya en uso

**Síntomas:**

- Error: «Port 9000 is already in use».
- Los servicios no pueden iniciarse.

**Soluciones:**

```bash
# Comprobar qué proceso usa el puerto
lsof -i :9000  # macOS/Linux
netstat -ano | findstr :9000  # Windows

# Cambiar el puerto del front en .env (por defecto 9000). Se cambian los dos:
# LOCAL_PORT es el puerto que se abre en la máquina y PUBLIC_PORT el que
# aparece en las direcciones que genera SITMUN (por ejemplo, la del proxy):
#   LOCAL_PORT=8080
#   PUBLIC_PORT=8080
# y se vuelve a arrancar: docker compose up -d --pull always --no-build
# (si front se ha construido localmente para publicar bajo una ruta, sin --pull always:
#  docker compose pull --policy always backend proxy && docker compose up -d --no-build)
# Otra opción: detener el proceso que usa el puerto.
```

Los puertos 9001 a 9005 están fijos en `compose.yaml`. Para cambiarlos, o para publicarlos solo en `127.0.0.1`, se crea
un `compose.override.yaml` junto a `compose.yaml` con la etiqueta `!override`; sin ella, Compose añade el puerto nuevo
al antiguo en lugar de sustituirlo:

```yaml
services:
  backend:
    ports: !override
      - "127.0.0.1:9001:8080"
```

Si cambia el puerto del backend, cambian también las direcciones de comprobación (`/api/dashboard/health`) y de Swagger.

### Problemas de memoria

<!-- Ancla de la antigua subsección sobre la memoria de Java, que ahora forma parte de esta sección: los enlaces antiguos llegan aquí. -->
<a id="problemas-de-memoria_1"></a>

**Síntomas:**

- Los contenedores se detienen inesperadamente o la aplicación se cuelga.
- Errores de «Out of memory».

**Soluciones:**

```bash
# Comprobar el uso de memoria de cada contenedor
docker stats

# Aumentar la memoria disponible para Docker
# (en Docker Desktop: Settings > Resources > Memory)

# Las imágenes de backend y proxy usan por defecto
# JAVA_TOOL_OPTIONS="-XX:MaxRAMPercentage=75" (75 % de la memoria del contenedor).
# Para cambiarlo se añade JAVA_TOOL_OPTIONS al servicio en compose.yaml,
# por ejemplo JAVA_TOOL_OPTIONS="-Xmx2g -Xms1g"
```

## Problemas de base de datos

### Conexión a PostgreSQL falla

**Síntomas:**

- Error: «Connection refused».
- Error: «password authentication failed for user "sitmun3"», después de cambiar `DATABASE_PASSWORD`.
- El backend no puede conectarse a la base de datos.

**Soluciones:**

```bash
# Comprobar que PostgreSQL está en marcha
docker compose ps postgres

# Revisar el registro del contenedor
docker compose logs postgres

# Reiniciar el contenedor de PostgreSQL
docker compose restart postgres

# Comprobar la conexión
docker compose exec postgres psql -U sitmun3 -d sitmun3
```

La base de datos conserva la contraseña con la que se creó. Si `DATABASE_PASSWORD` ha cambiado después, se cambia también
en la base de datos (sin perder datos) y se vuelve a crear el contenedor del backend, para que lea el `.env` nuevo
(`restart` no lo vuelve a leer):

```bash
docker compose exec postgres psql -U sitmun3 -d sitmun3 -c "ALTER USER sitmun3 PASSWORD '<nueva contraseña>'"
docker compose up -d --no-build backend
```

En Oracle, `ALTER USER sitmun3 IDENTIFIED BY "<nueva contraseña>"`.

### Errores de migración de base de datos

**Síntomas:**

- Error: «Liquibase migration failed».
- Las tablas no se crean correctamente.

**Soluciones:**

Primero se revisa el error en `docker compose logs backend`.
Para una actualización desde la versión 1.2.8 o 1.2.9, se sigue la [guía de actualización](https://github.com/sitmun/sitmun/tree/main/docs/upgrade),
que explica `SITMUN_UPGRADE_DEFAULT_LANGUAGE`.

!!! danger "El comando siguiente borra todos los datos de SITMUN"
    `DROP SCHEMA public CASCADE` elimina todas las tablas: usuarios, territorios, servicios, capas, tareas y aplicaciones.
    Solo se usa en una instalación nueva o de pruebas y, antes, conviene hacer una [copia de seguridad](#backup-de-base-de-datos).

```bash
# Borrar la base de datos y volver a crearla desde cero (¡se pierden los datos!)
docker compose exec postgres psql -U sitmun3 -d sitmun3 -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public;"

# Reiniciar el backend para ejecutar las migraciones
docker compose restart backend
```

## Problemas de autenticación

### No se puede iniciar sesión en el administrador { #no-se-puede-acceder-al-administrador }

**Síntomas:**

- Error 401 Unauthorized.
- El inicio de sesión no funciona.

**Soluciones:**

```bash
# Comprobar que el backend está en marcha
curl http://localhost:9001/api/dashboard/health

# Revisar el registro del backend
docker compose logs backend

# En una base de datos de desarrollo: usuario admin, contraseña admin.
# En producción, la contraseña de admin se crea en la primera visita a /admin/
# (o con SITMUN_BOOTSTRAP_ADMIN_PASSWORD en .env antes de arrancar).
# "firstRun": true indica que aún no se ha hecho esa primera visita.
curl http://localhost:9001/api/setup/status
```

### La sesión se cierra o el token deja de ser válido { #token-jwt-invalido }

**Síntomas:**

- Error: «Invalid JWT token» o 401 en peticiones que antes funcionaban.
- La sesión se cierra inesperadamente.

**Soluciones:**

- Las sesiones se firman con `SITMUN_USER_SECRET`. Si el secreto cambia (por ejemplo, al regenerar `.env`), todas las sesiones dejan de ser válidas. La primera petición con la cookie antigua responde 401 y la borra; después, basta con volver a iniciar sesión.
- Si el navegador conserva una sesión antigua, se borran las cookies del sitio o se prueba en una ventana privada.
- En el visor, un usuario cuyo puesto en el territorio ha caducado (**Fecha de baja**) pierde la sesión al renovarla: ver [Usuarios](../manual/administrador/usuarios.md).

<a id="problemas-del-front"></a>

## Problemas del contenedor `front` { #problemas-de-frontend }

### El visor o el administrador no cargan { #aplicaciones-no-cargan }

**Síntomas:**

- Página en blanco.
- Errores 404 en los recursos de la página.

**Soluciones:**

```bash
# Comprobar que el front responde (debe devolver el HTML del visor)
curl -L http://localhost:9000/viewer/

# Revisar el registro del front
docker compose logs front
```

- La imagen publicada de `front` solo funciona en la ruta `/`. Si `PUBLIC_BASE_PATH` es otra ruta, hay que construir `front` desde el repositorio (ver [Instalación](instalacion.md)).
- En la consola del navegador (herramientas de desarrollo, pestaña *Red*) se ve qué recurso falla y a qué dirección se ha pedido.

### Errores de CORS { #problemas-de-cors }

**Síntomas:**

- Error: «CORS policy» en la consola del navegador.
- Peticiones bloqueadas desde el navegador.

**Soluciones:**

El backend de SITMUN acepta peticiones de cualquier origen, así que un error de CORS suele indicar que el navegador
llama a una dirección distinta de la que se usa para abrir la página. Se comprueba que `PUBLIC_URL_SCHEME`,
`PUBLIC_HOSTNAME` y `PUBLIC_PORT` en `.env` coinciden exactamente con la dirección del navegador (esquema, nombre y
puerto) y se vuelve a arrancar. Si el error aparece con un servicio externo, el servicio no admite peticiones del
navegador: se activa **Usar proxy SITMUN** en el servicio.

## Problemas de red

<a id="los-servicios-no-se-comunican"></a>

### Los servicios no se comunican { #servicios-no-se-comunican }

**Síntomas:**

- Error: «Connection refused».
- Tiempos de espera agotados en peticiones internas.

**Soluciones:**

```bash
# Revisar la red de Docker
docker network ls
# El nombre del proyecto es el de la carpeta del repositorio (p. ej. sitmun)
# o el indicado con -p (p. ej. sitmun-showcase)
docker network inspect sitmun_default

# Comprobar la conexión entre contenedores
docker compose exec backend curl -s http://proxy:8080/actuator/health
```

### Problemas de DNS

**Síntomas:**

- Error: «Name resolution failed».
- Los servicios no se encuentran por su nombre.

**Soluciones:**

```bash
# Comprobar la resolución de nombres dentro de los contenedores
docker compose exec backend getent hosts postgres

# Reiniciar la red de Docker: prune no borra las redes en uso, así que primero se paran los contenedores
docker compose down
docker network prune
# Con front construido localmente (publicación bajo una ruta), sin --pull always:
# docker compose pull --policy always backend proxy && docker compose up -d --no-build
docker compose up -d --pull always --no-build
```

## Problemas de rendimiento

### Aplicación lenta

**Síntomas:**

- Tiempos de respuesta altos.
- La interfaz no responde.

**Soluciones:**

- `docker stats` muestra si algún contenedor usa toda su CPU o memoria (ver [Problemas de memoria](#problemas-de-memoria)).
- Si la lentitud está en una capa, se comprueba la velocidad del servicio de mapas: las pestañas **Monitorización** y **Uso** del servicio en el administrador muestran su disponibilidad y su uso.
- Si está en una consulta SQL, se prueba la consulta directamente en la base de datos; las consultas se cortan a los 60 segundos (ver [Tareas de consulta](../manual/administrador/tareas/consulta.md)).

## Registros y depuración { #logs-y-debugging }

<a id="ver-los-registros-de-los-servicios"></a>

### Ver los registros de los servicios { #ver-logs-de-servicios }

```bash
# Registros de todos los servicios
docker compose logs

# Registros de un servicio
docker compose logs backend
docker compose logs postgres
docker compose logs front

# Seguir los registros en tiempo real
docker compose logs -f backend
```

El backend y el proxy escriben su registro en la salida estándar. El nivel se cambia en `.env` con `LOGGING_LEVEL_ROOT`
y `LOGGING_LEVEL_ORG_SITMUN`, y se aplica con `docker compose up -d --no-build backend proxy` (sin `--no-build`, Compose compilaría las imágenes de nuevo). Los perfiles de producción
(`profiles/postgres.env` y `profiles/oracle.env`) los ponen en `WARN` e `INFO`; sin ellos, Compose usa `INFO` y `DEBUG`.
Los registros de nginx del contenedor `front` no salen en `docker compose logs front`: van a la carpeta `logs/front/nginx`,
que contiene `access.log` y `error.log`. Nada los rota, así que conviene vaciarlos o rotarlos de vez en cuando.

### Depuración avanzada { #debugging-avanzado }

```bash
# Abrir una consola en un contenedor
docker compose exec backend bash

# Ver la configuración de Spring
docker compose exec backend env | grep SPRING

# Comprobar el estado del backend desde dentro del contenedor
docker compose exec backend curl http://localhost:8080/api/dashboard/health
```

## Recuperación de datos

### Copia de seguridad de la base de datos { #backup-de-base-de-datos }

```bash
# Crear la copia (--clean permite restaurarla sobre una base de datos que ya tiene datos)
docker compose exec -T postgres pg_dump --clean --if-exists -U sitmun3 sitmun3 > backup.sql
```

Para restaurarla, se paran el backend y el proxy, se restaura y se vuelven a arrancar:

```bash
docker compose stop backend proxy
docker compose exec -T postgres psql -v ON_ERROR_STOP=1 -U sitmun3 sitmun3 < backup.sql
docker compose start backend proxy
```

Los comandos usan el usuario y la base de datos por defecto (`sitmun3`); si se cambiaron `DATABASE_USERNAME` o `DATABASE`,
se usan esos valores. Además de la base de datos, conviene guardar `.env`, que tiene los secretos, y los archivos de
configuración propios, como `application-mail.yml`.

Con `ON_ERROR_STOP` el comando se detiene y devuelve un error si algo falla. Una copia hecha sin `--clean` solo se
puede restaurar en una base de datos vacía: antes se ejecuta el `DROP SCHEMA` de
[Errores de migración](#errores-de-migracion-de-base-de-datos), sin reiniciar el backend.

### Copia del volumen de datos { #restaurar-configuracion }

Copia completa del volumen de PostgreSQL, con todos los servicios parados:

```bash
# El volumen se llama <proyecto>_pgdata; se comprueba con: docker volume ls
docker compose stop
docker run --rm -v sitmun_pgdata:/data -v "$(pwd)":/backup alpine tar czf /backup/pgdata-backup.tar.gz -C /data .
docker compose start
```

Para restaurarla, también con los servicios parados, se vacía el volumen antes de extraer la copia:

```bash
docker compose stop
docker run --rm -v sitmun_pgdata:/data -v "$(pwd)":/backup alpine sh -c "rm -rf /data/* /data/.[!.]* && tar xzf /backup/pgdata-backup.tar.gz -C /data"
docker compose start
```

### Copia de seguridad con Oracle { #backup-oracle }

Con el perfil `oracle`, la copia es una exportación de Data Pump del esquema de la aplicación (`sitmun3` por defecto, o el
valor de `DATABASE_USERNAME`). `expdp` e `impdp` están dentro del contenedor `oracle`, que arranca con el usuario `system` y
la contraseña `password`, y el servicio de la base de datos se llama como `DATABASE` (`sitmun3` por defecto). Los comandos
siguientes se han probado con la imagen `gvenzl/oracle-free:23-slim`, también en una base de datos recién creada.

Data Pump escribe en un objeto directorio de Oracle. El primer comando crea la carpeta `/opt/oracle/oradata/dpdump`
dentro del contenedor y el objeto directorio `SITMUN_DP`, que apunta a ella. Se ejecuta antes de exportar y antes de
importar, y puede repetirse sin problema.

Para crear la copia y llevarla a un archivo del equipo:

```bash
docker compose exec oracle bash -c "mkdir -p /opt/oracle/oradata/dpdump && echo \"CREATE OR REPLACE DIRECTORY SITMUN_DP AS '/opt/oracle/oradata/dpdump';\" | sqlplus -s system/password@//localhost:1521/sitmun3"
docker compose exec oracle expdp system/password@//localhost:1521/sitmun3 schemas=sitmun3 \
  directory=SITMUN_DP dumpfile=sitmun3.dmp logfile=exp.log reuse_dumpfiles=yes
docker compose exec -T oracle cat /opt/oracle/oradata/dpdump/sitmun3.dmp > sitmun3.dmp
```

Para restaurarla, se paran el backend y el proxy, se crea el objeto directorio, se copia el archivo al contenedor, se
importa y se vuelven a arrancar:

```bash
docker compose stop backend proxy
docker compose exec oracle bash -c "mkdir -p /opt/oracle/oradata/dpdump && echo \"CREATE OR REPLACE DIRECTORY SITMUN_DP AS '/opt/oracle/oradata/dpdump';\" | sqlplus -s system/password@//localhost:1521/sitmun3"
docker compose exec -T oracle bash -c 'cat > /opt/oracle/oradata/dpdump/sitmun3.dmp' < sitmun3.dmp
docker compose exec oracle impdp system/password@//localhost:1521/sitmun3 schemas=sitmun3 \
  directory=SITMUN_DP dumpfile=sitmun3.dmp logfile=imp.log table_exists_action=replace
docker compose start backend proxy
```

`impdp` termina con un error `ORA-31684` (el usuario `sitmun3` ya existe), que es normal. La importación sustituye las
tablas que ya existen. El archivo de la copia queda en el volumen `oradata`, en `/opt/oracle/oradata/dpdump`, y puede
borrarse después. Para mover SITMUN a otro servidor, se siguen los mismos pasos en el contenedor `oracle` del servidor nuevo, con la base
de datos vacía.
Si la instalación usa otro servicio, esquema o versión de Oracle, los parámetros se ajustan según la
[documentación de Data Pump](https://docs.oracle.com/en/database/oracle/oracle-database/23/sutil/oracle-data-pump.html).

## Contacto y soporte

Si los problemas persisten:

1. Se revisan las [incidencias abiertas](https://github.com/sitmun/sitmun/issues) del repositorio de SITMUN, por si ya están descritas.
2. Si no, se abre una [nueva incidencia](https://github.com/sitmun/sitmun/issues/new/choose) con la información de abajo.
3. Para otras consultas, ver los [órganos de gobierno de la Red SITMUN](../../que-es-sitmun/red-sitmun/contacto.md).

Una vulnerabilidad de seguridad no se notifica en una incidencia pública, sino de forma privada, como indica la
[política de seguridad](https://github.com/sitmun/.github/blob/main/SECURITY.md); requiere una cuenta de GitHub.

!!! tip "Información útil para una incidencia"
    - Versión de SITMUN, de Docker y de Docker Compose.
    - Sistema operativo y versión.
    - Registros completos del error (`docker compose logs`).
    - Pasos para reproducir el problema.
    - Configuración de red y cortafuegos, si es relevante.
