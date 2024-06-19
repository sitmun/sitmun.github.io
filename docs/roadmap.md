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
| Cliente SITMUN3 - API SITNA | Creación de un cliente SITMUN3 genérico a partir de                         | Revisión de bugs y documentación |
|                             | la integración de                                                           |                                  |
|                             | [API SITNA](https://github.com/sitna/api-sitna/blob/master/README.es-ES.md) |                                  |
|                             | y con el layout definido para la IDE Menorca                                |                                  |
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
| [Mejora UI login y dashboard usuario](roadmap/mejora-ui-login-dashboard-cliente.md) | Mejorar la interficie de la ventana de login a los clientes SITMUN                                                     | Media             |
|                                                                                     | disponibles para el usuario así como el dashboard para la selección de                                                 |                   |
|                                                                                     | aplicación, territorio y configuración de opciones y datos de usuario.                                                 |                   |
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
