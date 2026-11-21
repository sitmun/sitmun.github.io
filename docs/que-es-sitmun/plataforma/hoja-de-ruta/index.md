---
description: "Hoja de ruta de SITMUN 3: proyectos en desarrollo, en cola y finalizados."
---

# Hoja de ruta

<table>
    <tr>
        <th scope="row">Última modificación</th>
        <td><strong>Noviembre 2026</strong></td>
    </tr>
    <tr>
        <th scope="row">Versión publicada</th>
        <td><strong><a href="https://github.com/sitmun/sitmun/releases/tag/v1.3.0">SITMUN 1.3.0</a> (noviembre 2026)</strong></td>
    </tr>
</table>

¡Bienvenido a la hoja de ruta de SITMUN 3! Estas son las prioridades del equipo SITMUN.

El objetivo de esta hoja de ruta es ofrecer una visión general del estado del proyecto SITMUN 3 y las próximas funcionalidades a desarrollar.

!!! info "Aspectos generales"
    **El Comité Técnico de SITMUN** es el órgano funcional encargado de revisar la descripción o,
    en su defecto, describir el alcance funcional de cada uno de los puntos.
    También de proponer la priorización de cada uno de los proyectos o funcionalidades.

    Durante la **Asamblea Ordinaria Anual de socios del proyecto SITMUN** se vota y aprueba la priorización.

## Proyectos en desarrollo

| Proyecto - Funcionalidad | Descripción | Estado |
| --- | --- | --- |
| Mejora de la **página de acceso** a la plataforma SITMUN | Mejorar la interfaz de la ventana de inicio de sesión de los clientes SITMUN disponibles para el usuario así como el panel para la selección de aplicación, territorio y configuración de opciones y datos de usuario. [Ver detalles](propuestas/mejora-ui-login-dashboard-cliente.md) | Parcialmente disponible: panel, perfil de usuario, sugerencias, cambio de idioma y cierre de sesión. Pendiente: noticias y avisos para los usuarios. |
| **Creación dinámica de informes** | Posibilidad de generar un informe de forma dinámica desde el cliente SITMUN, que haya sido previamente configurado en el administrador SITMUN 3. Un informe se configura en SITMUN como una tarea que integra el resultado de otras tareas. [Ver detalles](propuestas/informe.md) | Parcialmente disponible como tarea de **exportación documental** (PDF a partir de plantillas). |

## Cola de proyectos (sala de espera)

| Proyecto - Funcionalidad | Descripción | Prioridad |
| --- | --- | --- |
| **Creación de un cliente SITMUN - API CNIG** | Creación de un cliente SITMUN 3 basado en el [API CNIG](https://github.com/IGN-CNIG/API-CNIG) | Media |
| **Creación de temáticos** | Dotar al cliente SITMUN 3 de una funcionalidad que permita al usuario modificar la simbología de una capa en función del valor de sus atributos. | Baja |

## Proyectos finalizados

Todas las funcionalidades de esta tabla están disponibles en la versión 1.3.0, salvo la edición en el visor (ver su fila).

Algunas todavía no tienen su página en el manual del administrador: la tarea de edición, la de *más información* y la exportación documental (ver [Tareas](../../../usuario/manual/administrador/tareas/index.md)).

| Proyecto - Funcionalidad | Descripción |
| --- | --- |
| **Repositorio único y despliegue con imágenes publicadas** | Todos los componentes en [sitmun/sitmun](https://github.com/sitmun/sitmun), imágenes Docker publicadas en `ghcr.io/sitmun`, asistente de primer arranque y actualización desde 1.2.8/1.2.9. |
| **SITMUN Mobile Editor** (antes «APP SITMUN Edición») | Aplicación para dispositivos móviles (Android) que permite la edición *offline* de objetos geográficos y alfanuméricos, basada en servicios web estándar, con control de acceso de usuario y permisos, administrada desde el Administrador SITMUN 3 como un cliente más. Carpeta `sitmun-mobile/sitmun-edition`. |
| **SITMUN Touristic** (antes «APP Turismo») | Aplicación turística para dispositivos móviles común para todos los territorios que usen SITMUN, cuyo contenido y funcionalidad se gestiona desde el administrador SITMUN 3 como un cliente más. Disponible para Android. Carpeta `sitmun-mobile/sitmun-touristic`. [Ver detalles](propuestas/app-turismo.md) |
| **Edición gráfica y alfanumérica** | Herramienta de edición de la [API SITNA](https://github.com/sitna/api-sitna) que corresponde a la tarea básica [Edición WFS](../../../usuario/manual/administrador/tareas/basicas/herramientas.md#wfsedit) (control `sitna.WFSEdit`). El visor 1.3.0 desactiva ese control en su configuración, así que no edita. La edición está en la aplicación móvil de edición, con la tarea de edición. |
| **Más info y más info avanzado** | El visor interpreta y ejecuta tareas *más info* y *más info avanzado* definidas en el administrador, con plantillas de visualización. [Ver detalles](propuestas/mas-info-avanzado.md) |
| **Localizadores** | El visor interpreta y ejecuta localizadores definidos como tareas en el administrador. |
| **Consultas** | El visor ejecuta consultas (SQL, Web API, enlaces) definidas como tareas en el administrador. |
| **Autenticación LDAP y OpenID Connect** | Inicio de sesión con LDAP o con proveedores OIDC además de usuarios de la base de datos. |
| **Monitorización de servicios** | Comprobación periódica del estado de los servicios y estadísticas de uso en el administrador. |
| Publicación de **SITMUN 3 1.0.0** | Publicación de la primera versión estable de SITMUN 3 y la organización del repositorio de GitHub y la creación de un stack que facilite la instalación y creación de un entorno de desarrollo. |
| **Múltiples árboles de capas** | Extender la funcionalidad de API SITNA para poder vincular más de un árbol a un cliente SITMUN. |
| **Comparación de mapas de fondo** | Extender la funcionalidad de API SITNA para poder implementar dos mapas de fondo en la tabla de contenidos y una barra de transparencia entre ellos. |
| **Árbol de capas** | Extender la funcionalidad de API SITNA para permitir la configuración de una estructura de árbol de capas definida desde el administrador, a partir de la atomización de servicios OGC y la configuración de las distintas capas que los conforman en nodos y subnodos. |
| **Autorización por token en el cliente** | Permitir la autenticación por token en el cliente SITMUN 3 API SITNA. |
| **Actualización versión Angular** | Actualización del administrador SITMUN a la última versión de Angular y refactorización del código. |
| **Creación de página web del proyecto** (e imagen corporativa) | Creación de una página web de difusión del proyecto y actualización de la imagen corporativa. |
| **Creación de página de documentación** | Creación de una página web de documentación del proyecto SITMUN 3 que facilite el seguimiento del proyecto, la comprensión tecnológica de la plataforma y facilite el uso y la participación en los desarrollos (contribuciones de código). |
| **Desarrollo del visor SITMUN 3** (**Integración API SITNA**) | Creación de un cliente SITMUN 3 basado en la API SITNA que se configure de forma dinámica a partir de la respuesta JSON que proporciona la API REST del backend de SITMUN. |
| **Desarrollo del Administrador SITMUN 3** | Desarrollo de una herramienta de administración SITMUN que permita la configuración de múltiples visualizadores de mapas SITMUN a partir de la definición de contenidos y la gestión de permisos de usuario. |
| **Desarrollo del nivel intermedio SITMUN 3** (backend y SITMUN Proxy Middleware) | Desarrollo de las API de Configuración y Autorización, la API de Proxy, la API de Administración y la API de Autenticación. |
| **Diseño de base de datos SITMUN 3** | Revisión e internacionalización de la base de datos de SITMUN 3. |
