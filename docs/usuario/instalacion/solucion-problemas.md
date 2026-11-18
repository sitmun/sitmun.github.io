# Solución de problemas

Esta sección proporciona soluciones a los problemas más comunes que pueden surgir durante la instalación, configuración y uso de SITMUN 3.

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

# Limpiar contenedores y volúmenes
docker compose down -v
docker system prune -f

# Reiniciar Docker Desktop (si aplica)
# Reiniciar el servicio Docker en Linux
sudo systemctl restart docker
```

### Puerto ya en uso

**Síntomas:**
- Error: "Port 9000 is already in use"
- Servicios no pueden iniciarse

**Soluciones:**
```bash
# Verificar qué proceso usa el puerto
lsof -i :9000  # macOS/Linux
netstat -ano | findstr :9000  # Windows

# Cambiar puerto en docker-compose.yml
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
docker ps | grep postgres

# Verificar logs del contenedor
docker logs sitmun-application-stack-postgres-1

# Reiniciar el contenedor de PostgreSQL
docker restart sitmun-application-stack-postgres-1

# Verificar conectividad
docker exec -it sitmun-application-stack-postgres-1 psql -U sitmun3 -d sitmun3
```

### Errores de migración de base de datos

**Síntomas:**
- Error: "Liquibase migration failed"
- Tablas no se crean correctamente

**Soluciones:**
```bash
# Limpiar base de datos y volver a migrar
docker exec -it sitmun-application-stack-postgres-1 psql -U sitmun3 -d sitmun3 -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public;"

# Reiniciar el backend para ejecutar migraciones
docker restart sitmun-application-stack-backend-1
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
docker logs sitmun-application-stack-backend-1

# Usar credenciales por defecto
# Usuario: admin, Contraseña: admin
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
docker logs sitmun-application-stack-front-1

# Verificar configuración de nginx
docker exec -it sitmun-application-stack-front-1 cat /etc/nginx/conf.d/default.conf
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
docker network inspect sitmun-application-stack_default

# Verificar conectividad entre contenedores
docker exec -it sitmun-application-stack-backend-1 ping postgres
docker exec -it sitmun-application-stack-backend-1 ping proxy
```

### Problemas de DNS

**Síntomas:**
- Error: "Name resolution failed"
- Servicios no pueden resolverse

**Soluciones:**
```bash
# Verificar resolución DNS dentro de contenedores
docker exec -it sitmun-application-stack-backend-1 nslookup postgres

# Reiniciar red de Docker
docker network prune
docker compose up
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
# Aumentar heap size de Java
# Configurar variables de entorno:
# JAVA_OPTS="-Xmx2g -Xms1g"

# Monitorear uso de memoria
docker exec -it sitmun-application-stack-backend-1 jstat -gc 1
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
docker exec -it sitmun-application-stack-backend-1 bash

# Verificar configuración de Spring
docker exec -it sitmun-application-stack-backend-1 env | grep SPRING

# Verificar conectividad de base de datos
docker exec -it sitmun-application-stack-backend-1 curl http://localhost:8080/api/dashboard/health
```

## Recuperación de datos

### Backup de base de datos

```bash
# Crear backup
docker exec -it sitmun-application-stack-postgres-1 pg_dump -U sitmun3 sitmun3 > backup.sql

# Restaurar backup
docker exec -i sitmun-application-stack-postgres-1 psql -U sitmun3 sitmun3 < backup.sql
```

### Restaurar configuración

```bash
# Backup de volúmenes
docker run --rm -v sitmun-application-stack_pgdata:/data -v $(pwd):/backup alpine tar czf /backup/pgdata-backup.tar.gz -C /data .

# Restaurar volúmenes
docker run --rm -v sitmun-application-stack_pgdata:/data -v $(pwd):/backup alpine tar xzf /backup/pgdata-backup.tar.gz -C /data
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
