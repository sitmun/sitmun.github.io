# Creando una aplicación

Esta sección describe cómo crear y configurar una nueva aplicación en SITMUN 3.

## Configuración básica

Para crear una nueva aplicación en SITMUN 3, sigue estos pasos:

1. **Accede al administrador** de SITMUN en `http://localhost:9000/admin`
2. **Autentícate** con las credenciales de administrador (usuario: `admin`, contraseña: `admin`)
3. **Navega a la sección de Aplicaciones** en el menú principal
4. **Crea una nueva aplicación** haciendo clic en el botón "Nueva aplicación"

## Configuración de la aplicación

### Información básica

- **Nombre**: Nombre descriptivo de la aplicación
- **Descripción**: Descripción detallada de la funcionalidad
- **Tipo**: Tipo de aplicación. En SITMUN están soportados tipos internos, externos y turísticos.
- **Estado**: Activa/Inactiva

### Ajustes avanzados (opcionales)

- **Privacidad**: Marcar la aplicación como privada para restringir el acceso público (propiedad `appPrivate`).
- **Parámetros de cabecera**: Definir parámetros HTTP por defecto para las peticiones de la aplicación ("header parameters").
- **SRS**: Sistema de referencia espacial por defecto (`srs`).
- **Escalas**: Lista de escalas por defecto (`scales`).
- **Mapa de situación**: Grupo de cartografías de situación (`situationMap`).
- **Autorefresco del árbol**: Refrescar automáticamente el árbol de contenidos (`treeAutoRefresh`).
- **Acceso por territorio**: Habilitar acceso a territorios padre/hijo según necesidad (`accessParentTerritory`, `accessChildrenTerritory`).

### Configuración de territorios

- **Territorios disponibles**: Selecciona los territorios donde estará disponible la aplicación
- **Territorio por defecto**: Establece el territorio por defecto para nuevos usuarios

### Configuración de usuarios

- **Roles permitidos**: Define qué roles de usuario pueden acceder a la aplicación
- **Usuarios específicos**: Asigna usuarios específicos si es necesario

## Configuración de capas

1. **Añade capas cartográficas** que estarán disponibles en la aplicación
2. **Configura el orden** de visualización de las capas
3. **Establece la visibilidad** por defecto de cada capa
4. **Configura estilos** y transparencias

## Configuración de herramientas

1. **Selecciona las herramientas** disponibles en la aplicación
2. **Configura parámetros** específicos para cada herramienta
3. **Establece permisos** de acceso por rol de usuario

## Pruebas y validación

1. **Prueba la aplicación** accediendo desde el visor en `http://localhost:9000/viewer`
2. **Verifica la configuración** de capas y herramientas
3. **Comprueba los permisos** con diferentes usuarios y roles

## Despliegue

Una vez configurada y probada:

1. **Activa la aplicación** en el administrador
2. **Notifica a los usuarios** sobre la disponibilidad
3. **Proporciona documentación** de uso si es necesario

!!! tip "Consejos"
    - Comienza con una configuración simple y añade complejidad gradualmente
    - Prueba siempre con usuarios de prueba antes del despliegue
    - Mantén documentación actualizada de la configuración

---

Siguiente paso: [Personalización](personalizando.md)
