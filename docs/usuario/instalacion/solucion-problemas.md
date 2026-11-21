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
    `oracle` y el volumen `oradata`; las copias de seguridad se hacen con las herramientas de Oracle (por ejemplo, Data Pump).

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

- Error: "Port 9000 is already in use".
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
# Los puertos 9001-9005 se publican directamente en compose.yaml.
# Otra opción: detener el proceso que usa el puerto.
```

### Problemas de memoria

<!-- Ancla de la antigua subsección sobre la memoria de Java, que ahora forma parte de esta sección: los enlaces antiguos llegan aquí. -->
<a id="problemas-de-memoria_1"></a>

**Síntomas:**

- Los contenedores se detienen inesperadamente o la aplicación se cuelga.
- Errores de "Out of memory".

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

- Error: "Connection refused".
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

### Errores de migración de base de datos

**Síntomas:**

- Error: "Liquibase migration failed".
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

- Error: "Invalid JWT token" o 401 en peticiones que antes funcionaban.
- La sesión se cierra inesperadamente.

**Soluciones:**

- Las sesiones se firman con `SITMUN_USER_SECRET`. Si el secreto cambia (por ejemplo, al regenerar `.env`), todas las sesiones dejan de ser válidas: basta con volver a iniciar sesión. El primer intento con la cookie antigua puede responder 401 y borrarla; el segundo funciona.
- Si el navegador conserva una sesión antigua, se borran las cookies del sitio o se prueba en una ventana privada.
- En el visor, un usuario cuyo puesto en el territorio ha caducado (**Fecha de baja**) pierde la sesión al renovarla: ver [Usuarios](../manual/administrador/usuarios.md).

## Problemas del front { #problemas-de-frontend }

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

- La imagen publicada del front solo funciona en la ruta `/`. Si `PUBLIC_BASE_PATH` es otra ruta, hay que construir `front` desde el repositorio (ver [Instalación](instalacion.md)).
- En la consola del navegador (herramientas de desarrollo, pestaña *Red*) se ve qué recurso falla y a qué dirección se ha pedido.

### Errores de CORS { #problemas-de-cors }

**Síntomas:**

- Error: "CORS policy" en la consola del navegador.
- Peticiones bloqueadas desde el navegador.

**Soluciones:**

El backend de SITMUN acepta peticiones de cualquier origen, así que un error de CORS suele indicar que el navegador
llama a una dirección distinta de la que se usa para abrir la página. Se comprueba que `PUBLIC_URL_SCHEME`,
`PUBLIC_HOSTNAME` y `PUBLIC_PORT` en `.env` coinciden exactamente con la dirección del navegador (esquema, nombre y
puerto) y se vuelve a arrancar. Si el error aparece con un servicio externo, el servicio no admite peticiones del
navegador: se activa **Usar proxy SITMUN** en el servicio.

## Problemas de red

### Los servicios no se comunican { #servicios-no-se-comunican }

**Síntomas:**

- Error: "Connection refused".
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

- Error: "Name resolution failed".
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

## Contacto y soporte

Si los problemas persisten:

1. Se revisan las [incidencias abiertas](https://github.com/sitmun/sitmun/issues) del repositorio de SITMUN, por si ya están descritas.
2. Si no, se abre una [nueva incidencia](https://github.com/sitmun/sitmun/issues/new) con la información de abajo.
3. Para otras consultas, ver los [órganos de gobierno de la Red SITMUN](../../que-es-sitmun/red-sitmun/contacto.md).

!!! tip "Información útil para una incidencia"
    - Versión de SITMUN, de Docker y de Docker Compose.
    - Sistema operativo y versión.
    - Registros completos del error (`docker compose logs`).
    - Pasos para reproducir el problema.
    - Configuración de red y cortafuegos, si es relevante.
