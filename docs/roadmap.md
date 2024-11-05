# Proyectos

<table>
    <tr>
        <td><strong>Última modificación</strong></td>
        <td><strong>Noviembre 2024</strong></td>
    </tr>
    <tr>
        <td><strong>Próxima modificación</strong></td>
        <td><strong>Marzo 2025</strong></td>
    </tr>
</table>

¡Bienvenido a la hoja de ruta de SITMUN 3! Estas son las prioridades del equipo SITMUN.

El objetivo de esta hoja de ruta es ofrecer una visión general del estado del proyecto SITMUN 3 y las próximas funcionalidades a desarrollar.

!!! info "Aspectos generales"
    [**El Comité Técnico de SITMUN**](https://sitmun.github.io/contact/) es el órgano funcional encargado de revisar la descripción o,
    en su defecto, describir el alcance funcional de cada uno de los puntos.
    También de proponer la priorización de cada uno de los proyectos o funcionalidades.

    Durante la **Asamblea Ordinaria Anual de socios del proyecto SITMUN** se vota y aprueba la priorización.

## Proyectos en desarrollo

+-----------------------------+-----------------------------------------------------------------------------+----------------------------------+
| Proyecto - Funcionalidad    | Descripción                                                                 | Estado                           |
+=============================+=============================================================================+==================================+
| Aplicación SITMUN para      | Este proyecto busca dotar a la plataforma SITMUN de una herramienta         | En desarrollo                    |
| dispositivos móviles        | para dispositivos móviles (Android) que permita la edición offline          | (inicio noviembre 2024)          |
| de edición gráfica y        | de objetos geográficos y alfanuméricos, basada en servicios web estándard,  |                                  |
| alfanumérica.               | con control de acceso de usuario, definición de permisos, que pueda ser     |                                  |
| **APP SITMUN Edición**      | administrada desde el Administrador SITMUN 3, como un cliente más.          |                                  |
|                             | [Ver detalles aquí.](roadmap/app-turismo.md)                                |                                  |
|                             |                                                                             |                                  |
+-----------------------------+-----------------------------------------------------------------------------+----------------------------------+
| Aplicación SITMUN para      | Este proyecto busca dotar a la plataforma SITMUN de la capacidad de         | En desarrollo                    |
| dispositivos móviles        | disponer de una aplicación turística para dispositivos móviles (Android e   | (inicio noviembre 2024)          |
| orientada al turismo        | iOS) común para todos los territorios que usen SITMUN como plataforma       |                                  |
| **APP Turismo**             | y cuyo contenido y funcionalidad pueda gestionarse desde el administrador   |                                  |
|                             | SITMUN 3, como un cliente más. [Ver detalles aquí.](roadmap/app-turismo.md) |                                  |
|                             |                                                                             |                                  |
+-----------------------------+-----------------------------------------------------------------------------+----------------------------------+
| Mejora de la **página de**  | Mejorar la interficie de la ventana de login a los clientes SITMUN          | En desarrollo                    |
| **acceso** a la plataforma  | disponibles para el usuario así como el dashboard para la selección de      | Análisis previo y propuesta      |
| SITMUN                      | aplicación, territorio y configuración de opciones y datos de usuario.      | técnica de implementación.       |
|                             | [Ver detalles](roadmap/mejora-ui-login-dashboard-cliente.md)                |                                  |
|                             |                                                                             |                                  |
+-----------------------------+-----------------------------------------------------------------------------+----------------------------------+
| **Creación dinámica**       | Posibilidad de generar un informe (report) de forma dinámica desde un       | En desarrollo                    |
| **de informes**             | el cliente SITMUN, que haya sido previamente configurado en el              | Análisis previo y propuesta      |
|                             | administrador SITMUN 3. Un informe se configura en SITMUN como una tarea    | técnica de implementación.       |
|                             | que integra el resultado de otras tareas.                                   |                                  |
|                             | [Ver detalles aquí](roadmap/informe.md)                                     |                                  |
|                             |                                                                             |                                  |
+-----------------------------+-----------------------------------------------------------------------------+----------------------------------+
| Publicación                 | Publicación de la primera versión estable de SITMUN 3 y la                  | Revisión de bugs y documentación |
| **SITMUN3 v1.0.0**          | organización del repositorio de Github y la creación de un stack            |                                  |
|                             | que facilite la instalación y creación de un entorno de desarrollo.         |                                  |
|                             |                                                                             |                                  |
|                             |                                                                             |                                  |
+-----------------------------+-----------------------------------------------------------------------------+----------------------------------+

## Proyectos prioritarios

+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+-------------------+
| Proyecto - Funcionalidad                                                            | Descripción                                                                                                            | Prioridad         |
+=====================================================================================+========================================================================================================================+===================+
| **Edición gráfica y alfanumérica**                                                  | Integrar en el cliente SITMUN 3 API SITNA la herramienta de edición                                                    | Alta              |
|                                                                                     | disponible en el API SITNA.  [API CNIG](https://github.com/IGN-CNIG/API-CNIG)                                          |                   |
+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+-------------------+
| **Más info avanzado**                                                               | Busca dotar a SITMUN 3 de la capacidad de configurar, desde                                                            | Alta              |
|                                                                                     | el administrador SITMUN 3, el contenido de la ventana que                                                              |                   |
|                                                                                     | devuelve el visualizador al hacer una consulta sobre una capa                                                          |                   |
|                                                                                     | visible en el área de mapa.  [Ver detalles](roadmap/mas-info-avanzado.md)                                              |                   |
+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+-------------------+
| **Más info**                                                                        | Implementar en el cliente SITMUN 3 API SITNA la capacidad de interpretar y                                             | Alta              |
|                                                                                     | ejecutar tareas más info definidas como tal en el administrador SITMUN 3.                                              |                   |
|                                                                                     | Asimilando el funcionamiento al de los actuales clientes SITMUN 2.                                                     |                   |
+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+-------------------+
| **Edición gráfica y alfanumérica**                                                  | Integrar en el cliente SITMUN 3 API SITNA la herramienta de edición                                                    | Alta              |
|                                                                                     | disponible en el API SITNA.  [API CNIG](https://github.com/IGN-CNIG/API-CNIG)                                          |                   |
+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+-------------------+


## Proyectos en espera

+------------------------------------------------+-----------------------------------------------------------------------------+-------------------+
| Proyecto - Funcionalidad                       | Descripción                                                                 | Prioridad         |
+================================================+=============================================================================+===================+
| **Creación de un cliente SITMUN - API**        | Creación de un cliente SITMUN3 basado en el                                 | Media             |
| **CNIG**                                       | [API CNIG](https://github.com/IGN-CNIG/API-CNIG)                            |                   |
+------------------------------------------------+-----------------------------------------------------------------------------+-------------------+
| **Localizadores**                              | Implementar en el cliente SITMUN 3 API SITNA la capacidad de interpretar y  | Alta              |
|                                                | ejecutar localizadores definidos como tareas en el administrador SITMUN 3.  |                   |
|                                                | Asimilando el funcionamiento al de los actuales clientes SITMUN 2.          |                   |
|                                                | Esta tarea incluye los cambios necesarios en el administrador y API SITMUN  |                   |
|                                                | para poder configurar correctamente la funcionalidad de localizadores       |                   |
|                                                | integrados genéricos existente en la API SITNA 3.                           |                   |
+------------------------------------------------+-----------------------------------------------------------------------------+-------------------+
| **Consultas**                                  | Implementar en el cliente SITMUN 3 API SITNA la capacidad de interpretar y  | Baja              |
|                                                | ejecutar consultas definidas como tareas en el administrador SITMUN 3.      |                   |
|                                                | Asimilando el funcionamiento al de los actuales clientes SITMUN 2.          |                   |
+------------------------------------------------+-----------------------------------------------------------------------------+-------------------+
| **Edición gráfica y alfanumérica**             | Implementar herramientas en el cliente SITMUN 3 que permitan la edición     | Baja              |
|                                                | gráfica (mediante servicios WFS transaccionales) y alfanumérica.            |                   |
+------------------------------------------------+-----------------------------------------------------------------------------+-------------------+
| **Creación de temáticos**                      | Dotar al cliente SITMUN 3 de una funcionalidad que permita al usuario       | Baja              |
|                                                | modificar la simbología de una capa en función del valor de sus atributos.  |                   |
+------------------------------------------------+-----------------------------------------------------------------------------+-------------------+


# Proyectos finalizados

+------------------------------------------------+-------------------------------------------------------------------------------------------------+
| Proyecto - Funcionalidad                       | Descripción                                                                                     |
+================================================+=================================================================================================+
| **Integración  API SITNA**                     | Creación de un cliente SITMUN3 basado en el API SITNA                                           |
|                                                | [API SITNA](https://github.com/IGN-CNIG/API-CNIG)                                               |
+------------------------------------------------+-------------------------------------------------------------------------------------------------+
| **Múltiples árboles de capas**                 | Extender la funcionalidad de API SITNA para poder vincular más de un árbol a un cliente         |
|                                                | SITMUN                                                                                          |
+------------------------------------------------+-------------------------------------------------------------------------------------------------+
| **Comparación de mapas de fondo**              | Extender la funcionalidad de API SITNA para poder implementar dos mapas de fondo en la          |
|                                                | tabla de contenidos y una barra de transparencia entre ellos.                                   |
+------------------------------------------------+-------------------------------------------------------------------------------------------------+
| **Arbol de capas**                             | Extender la funcionalidad de API SITNA para permitir la configuración de una estructura         |
|                                                | de árbol de capas definida desde el administrador, a partir de la atomización de servicios      |
|                                                | OGC y la configuración de las distintas capas que los conforman en nodos y subnodos.            |
+------------------------------------------------+-------------------------------------------------------------------------------------------------+
| **Autorización por token en el cliente**       | Permitir la autenticación por token en el cliente SITMUN 3 API SITNA.                           |
|                                                |                                                                                                 |
+------------------------------------------------+-------------------------------------------------------------------------------------------------+
| **Actualización versión Angular**              | Actualización del administrador SITMUN a la última versión de Ángular y refactorización         |
|                                                | del código.                                                                                     |
+------------------------------------------------+-------------------------------------------------------------------------------------------------+
