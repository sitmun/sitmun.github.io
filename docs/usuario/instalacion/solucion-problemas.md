---
description: "Soluciones a los problemas más comunes al instalar y usar SITMUN 3 con Docker: puertos, base de datos, autenticación, red y copias de seguridad."
---

# Solución de problemas

Esta sección proporciona soluciones a los problemas más comunes que pueden surgir durante la instalación, configuración y uso de SITMUN 3.

!!! note "Comandos de Docker Compose"
    Ejecuta los comandos `docker compose` desde la carpeta del repositorio.
    Si instalaste el *showcase*, añade `-p sitmun-showcase` después de `docker compose`.
    En PowerShell usa `curl.exe` en lugar de `curl`.

## Problemas de instalación

### Docker no se inicia

**Síntomas:**

- Error al ejecutar `docker compose up`
- Servicios no se levantan correctamente

**Soluciones:**

```bash
# Verificar que Docker esté ejecutándose
docker --version
docker compose --version

# Parar y eliminar los contenedores (los datos se conservan)
docker compose down
docker system prune -f

# Reiniciar Docker Desktop (si aplica)
# Reiniciar el servicio Docker en Linux
sudo systemctl restart docker
```

!!! danger "`docker compose down -v` borra la base de datos"
    La opción `-v` elimina también los volúmenes, entre ellos `pgdata` (u `oradata`), donde está la base de datos de SITMUN.
    Úsala solo si quieres empezar desde cero y, antes, haz una [copia de seguridad](#backup-de-base-de-datos).

### Puerto ya en uso

**Síntomas:**

- Error: "Port 9000 is already in use"
- Servicios no pueden iniciarse

**Soluciones:**

```bash
# Verificar qué proceso usa el puerto
lsof -i :9000  # macOS/Linux
netstat -ano | findstr :9000  # Windows

# Cambiar el puerto del front en .env (por defecto 9000). Cambia los dos:
# LOCAL_PORT es el puerto que se abre en la máquina y PUBLIC_PORT el que
# aparece en las direcciones que genera SITMUN (por ejemplo, la del proxy):
#   LOCAL_PORT=8080
#   PUBLIC_PORT=8080
# y vuelve a arrancar: docker compose up -d
# Los puertos 9001-9005 se publican directamente en compose.yaml
# O detener el proceso que usa el puerto
```

### Problemas de memoria

**Síntomas:**

- Contenedores se detienen inesperadamente
- Errores de "Out of memory"

**Soluciones:**

```bash
# Aumentar memoria disponible para Docker
# En Docker Desktop: Settings > Resources > Memory

# Verificar uso de memoria
docker stats

# Limpiar recursos no utilizados
docker system prune -a
```

## Problemas de base de datos

### Conexión a PostgreSQL falla

**Síntomas:**

- Error: "Connection refused"
- Backend no puede conectarse a la base de datos

**Soluciones:**

```bash
# Verificar que PostgreSQL esté ejecutándose
docker compose ps postgres

# Verificar logs del contenedor
docker compose logs postgres

# Reiniciar el contenedor de PostgreSQL
docker compose restart postgres

# Verificar conectividad
docker compose exec postgres psql -U sitmun3 -d sitmun3
```

### Errores de migración de base de datos

**Síntomas:**

- Error: "Liquibase migration failed"
- Tablas no se crean correctamente

**Soluciones:**

Revisa primero el error en `docker compose logs backend`.
Si vienes de la versión 1.2.8 o 1.2.9, sigue la [guía de actualización](https://github.com/sitmun/sitmun/tree/main/docs/upgrade),
que explica `SITMUN_UPGRADE_DEFAULT_LANGUAGE`.

!!! danger "El comando siguiente borra todos los datos de SITMUN"
    `DROP SCHEMA public CASCADE` elimina todas las tablas: usuarios, territorios, servicios, capas, tareas y aplicaciones.
    Úsalo solo en una instalación nueva o de pruebas y, antes, haz una [copia de seguridad](#backup-de-base-de-datos).

```bash
# Borrar la base de datos y volver a crearla desde cero (¡se pierden los datos!)
docker compose exec postgres psql -U sitmun3 -d sitmun3 -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public;"

# Reiniciar el backend para ejecutar migraciones
docker compose restart backend
```

## Problemas de autenticación

### No se puede acceder al administrador

**Síntomas:**

- Error 401 Unauthorized
- No se puede hacer login

**Soluciones:**

```bash
# Verificar que el backend esté ejecutándose
curl http://localhost:9001/api/dashboard/health

# Verificar logs del backend
docker compose logs backend

# En una base de datos de desarrollo: usuario admin, contraseña admin
# En producción, la contraseña de admin se crea en la primera visita a /admin/
# (o con SITMUN_BOOTSTRAP_ADMIN_PASSWORD en .env antes de arrancar)
curl http://localhost:9001/api/setup/status
```

### Token JWT inválido

**Síntomas:**

- Error: "Invalid JWT token"
- Sesión expira inesperadamente

**Soluciones:**

```bash
# Limpiar cookies del navegador
# O usar modo incógnito

# Verificar configuración de JWT en el backend
# Revisar logs para errores de validación
```

## Problemas de frontend

### Aplicaciones no cargan

**Síntomas:**

- Página en blanco
- Errores 404 en recursos estáticos

**Soluciones:**

```bash
# Verificar que el frontend esté ejecutándose
curl http://localhost:9000

# Verificar logs del frontend
docker compose logs front

# Verificar configuración de nginx
docker compose exec front cat /etc/nginx/conf.d/default.conf
```

### Problemas de CORS

**Síntomas:**

- Error: "CORS policy"
- Requests bloqueados desde el navegador

**Soluciones:**

```bash
# Verificar configuración CORS en el backend
# Revisar headers en las respuestas HTTP

# Verificar configuración de nginx
# Asegurar que los headers CORS estén configurados
```

## Problemas de red

### Servicios no se comunican

**Síntomas:**

- Error: "Connection refused"
- Timeouts en requests internos

**Soluciones:**

```bash
# Verificar red de Docker
docker network ls
# El nombre del proyecto es el de la carpeta del repositorio (p. ej. sitmun)
# o el indicado con -p (p. ej. sitmun-showcase)
docker network inspect sitmun_default

# Verificar conectividad entre contenedores
docker compose exec backend curl -s http://proxy:8080/actuator/health
```

### Problemas de DNS

**Síntomas:**

- Error: "Name resolution failed"
- Servicios no pueden resolverse

**Soluciones:**

```bash
# Verificar resolución DNS dentro de contenedores
docker compose exec backend getent hosts postgres

# Reiniciar red de Docker
docker network prune
docker compose up -d
```

## Problemas de rendimiento

### Aplicación lenta

**Síntomas:**

- Tiempos de respuesta altos
- Interfaz no responde

**Soluciones:**

```bash
# Verificar uso de recursos
docker stats

# Aumentar memoria disponible
# Optimizar consultas de base de datos
# Configurar índices apropiados
```

### Problemas de memoria

**Síntomas:**

- Aplicación se cuelga
- Errores de "Out of memory"

**Soluciones:**

```bash
# Las imágenes de backend y proxy usan por defecto
# JAVA_TOOL_OPTIONS="-XX:MaxRAMPercentage=75" (75 % de la memoria del contenedor).
# Para cambiarlo, añade JAVA_TOOL_OPTIONS al servicio en compose.yaml,
# por ejemplo JAVA_TOOL_OPTIONS="-Xmx2g -Xms1g"

# Monitorear uso de memoria
docker stats
```

## Logs y debugging

### Ver logs de servicios

```bash
# Logs de todos los servicios
docker compose logs

# Logs de un servicio específico
docker compose logs backend
docker compose logs postgres
docker compose logs front

# Seguir logs en tiempo real
docker compose logs -f backend
```

### Debugging avanzado

```bash
# Acceder a contenedor para debugging
docker compose exec backend bash

# Verificar configuración de Spring
docker compose exec backend env | grep SPRING

# Verificar conectividad de base de datos
docker compose exec backend curl http://localhost:8080/api/dashboard/health
```

## Recuperación de datos

### Backup de base de datos

```bash
# Crear backup
docker compose exec -T postgres pg_dump -U sitmun3 sitmun3 > backup.sql

# Restaurar backup
docker compose exec -T postgres psql -U sitmun3 sitmun3 < backup.sql
```

### Restaurar configuración

```bash
# Backup de volúmenes (con los servicios parados: docker compose stop)
# El volumen se llama <proyecto>_pgdata; compruébalo con: docker volume ls
docker run --rm -v sitmun_pgdata:/data -v $(pwd):/backup alpine tar czf /backup/pgdata-backup.tar.gz -C /data .

# Restaurar volúmenes
docker run --rm -v sitmun_pgdata:/data -v $(pwd):/backup alpine tar xzf /backup/pgdata-backup.tar.gz -C /data
```

## Contacto y soporte

Si los problemas persisten:

1. **Revisar la documentación** oficial de SITMUN
2. **Consultar los issues** en GitHub
3. **Contactar al equipo** de soporte técnico
4. **Proporcionar logs** detallados del problema

!!! tip "Información útil para soporte"
    - Versión de Docker y Docker Compose
    - Sistema operativo y versión
    - Logs completos del error
    - Pasos para reproducir el problema
    - Configuración de red y firewall
