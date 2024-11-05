# Proyectos

<table>
    <tr>
        <td><strong>Última modificación</strong></td>
        <td><strong>Noviembre 2023</strong></td>
    </tr>
    <tr>
        <td><strong>Próxima modificación</strong></td>
        <td><strong>Diciembre 2023</strong></td>
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
| [Más info avanzado](roadmap/mas-info-avanzado.md)                                   | Busca dotar a SITMUN 3 de la capacidad de configurar, desde                                                            | Alta              |
|                                                                                     | el administrador SITMUN 3, el contenido de la ventana que                                                              |                   |
|                                                                                     | devuelve el visualizador al hacer una consulta sobre una capa                                                          |                   |
|                                                                                     | visible en el área de mapa.                                                                                            |                   |
+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+-------------------+
| **Más info**                                                                        | Implementar en el cliente SITMUN 3 API SITNA la capacidad de interpretar y                                             | Alta              |
|                                                                                     | ejecutar tareas más info definidas como tal en el administrador SITMUN 3.                                              |                   |
|                                                                                     | Asimilando el funcionamiento al de los actuales clientes SITMUN 2.                                                     |                   |
+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+-------------------+
| **Selector de dos mapas de fondo**                                                  | Implementar dos mapas de fondo en la tabla de contenidos y una barra de                                                | Alta              |
|                                                                                     | transparencia entre los dos. Funcionalidad desarrollada en Menorca sobre el                                            |                   |
|                                                                                     | API SITNA, falta decidir si se sobreescribe el control o se espera a que la                                            |                   |
|                                                                                     | API SITNA implemente su punto 51 de la [hora de ruta](https://github.com/sitna/api-sitna/blob/master/roadmap.es-ES.md) |                   |
+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+-------------------+
| **Autorización por token en el cliente**                                            | Autenticación por token en el cliente SITMUN 3 API SITNA                                                               | Alta              |
|                                                                                     |                                                                                                                        |                   |
+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+-------------------+
| **Cambio de arbol en aplicación cliente**                                           | Cambio de árbol del cliente SITMUN 3 API SITNA.                                                                        | Alta              |
|                                                                                     |                                                                                                                        |                   |
+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+-------------------+
| **Buscador genérico API SITNA**                                                     | Configurar los servicios WFS del buscador generico desde el administrador                                              | Alta              |
|                                                                                     |                                                                                                                        |                   |
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

+------------------------------------------------+-----------------------------------------------------------------------------+-------------------+
| Proyecto - Funcionalidad                       | Descripción                                                                 | Prioridad         |
+================================================+=============================================================================+===================+
| **Integración  API SITNA**                     | Creación de un cliente SITMUN3 basado en el API SITNA                       | Media             |
|                                                | [API SITNA](https://github.com/IGN-CNIG/API-CNIG)                           |                   |
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
| **Creación dinámica de informes**              | Posibilidad de generar de forma dinámica y parametrizada un informe desde el| Baja              |
|                                                | cliente SITMUN previamente configurado en el administrador SITMUN 3. Un     |                   |
|                                                | informe se configura en SITMUN como una tarea que integra el resultado de   |                   |
|                                                | otras tareas (consultas, generación de imagen de mapa, etc.).               |                   |
+------------------------------------------------+-----------------------------------------------------------------------------+-------------------+
| **Creación de temáticos**                      | Dotar al cliente SITMUN 3 de una funcionalidad que permita al usuario       | Baja              |
|                                                | modificar la simbología de una capa en función del valor de sus atributos.  |                   |
+------------------------------------------------+-----------------------------------------------------------------------------+-------------------+
| [Cliente APP turística](roadmap/app-turismo.md)| Esta funcionalidad busca dotar a la plataforma SITMUN de la capacidad de    | Media             |
|                                                | configurar aplicaciones móviles a través de  un primer caso de uso de una   |                   |
|                                                | APP turística.                                                              |                   |  
+------------------------------------------------+-----------------------------------------------------------------------------+-------------------+
| [Informe](roadmap/informe.md)                  | Esta funcionalidad busca dotar a SITMUN 3 de la capacidad de configurar,    | Baja              |
|                                                | desde el administrador SITMUN 3, el contenido de una ventana que devuelve el|                   |
|                                                | visor SITMUN 3 cuando el usuario busca una referencia catastral o dirección |                   | 
|                                                | del visor o como información complementaria del "Más info".                 |                   |
+------------------------------------------------+-----------------------------------------------------------------------------+-------------------+
