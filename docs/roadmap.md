# Hoja de ruta

<table>
    <tr>
        <td><strong>Última modificación</strong></td>
        <td><strong>Agosto 2023</strong></td>
    </tr>
    <tr>
        <td><strong>Próxima modificación</strong></td>
        <td><strong>Diciembre 2023</strong></td>
    </tr>
</table>

¡Bienvenido a la hoja de ruta de SITMUN 3! Estas son las prioridades del equipo SITMUN.

## Proyectos clave

El objetivo de esta hoja de ruta es brindarle una visión general. Aquí hay una lista de nuestros proyectos clave -
las cosas más importantes en las que nos enfocamos:

- **[Más info avanzado][mas-info-avanzado]**:
Busca dotar a SITMUN 3 de la capacidad de configurar, desde el administrador SITMUN 3, 
el contenido de la ventana que devuelve el visualizador al hacer una consulta sobre una capa visible en el área de mapa.

- **Mejora de la interficie de usuario de la página de login y selección de territorio/aplicación**  

- **Edición gráfica y alfanumérica**:
Implementar herramientas en el cliente SITMUN 3 que permitan la edición gráfica (mediante servicios WFS transaccionales) 
y alfanumérica.

- **Creación dinámica de informes**:
Un informe SITMUN es un documento formado por varios documentosConfiguración de informes desde el administrador de 
SITMUN 3. 

- **Creación de temáticos**:
Dotar al cliente SITMUN 3 de una funcionalidad que permita la creación de mapas temáticos.

- **Creación de un cliente SITMUN tipo aplicación para dispositivos móbiles (APP)**

## Detalles

### Más info avanzado
 
!!! info "Aspectos generales"

    **Estimación horas de desarrollo:** 80 horas

    **Entidad solicitante:** Comisión técnica SITMUN

    **Entidad con previsión de ejecución:** Pyrenees Orientales

**Objetivo:**

Esta funcionalidad busca dotar a SITMUN 3 de la capacidad de configurar, desde el administrador SITMUN 3,
el contenido de la ventana que devuelve el visor SITMUN 3 al realizar una consulta sobre el mapa para una capa determinada.

El contenido de la ventana debe poder integrar la respuesta de una o varias consultas definidas como tareas al propio administrador

**Contexto y casos de uso:**

**Requerimientos funcionales:**

_Cliente Administrador SITMUN 3_

| Funcionalidad                                                                                   | Estado actual         | Issues relacionadas |
|-------------------------------------------------------------------------------------------------|-----------------------|---------------------|
| Posibilidad de configurar tareas SITMUN de consultas a base de datos                            | Existente no testeada |                     |
| Posibilidad de configurar tareas SITMUN de consulta a servicios web                             | Existente no testeada |                     |
| Creación de tipo de tareas padre que permitan seleccionar tareas hijo con una vinculación N a M | Nueva                 |                     |
| Asignación de parámetros específicos a tareas padre Tab scroll                                  | Nueva                 |                     |

_Cliente visualizador SITMUN 3 (API SITNA)_

| Funcionalidad                                                 | Estado actual         | Issues relacionadas |
|---------------------------------------------------------------|-----------------------|---------------------|
| Parsear json del API de configuración y representar los datos | Existente no testeada |                     |

_API de autenticación_

No se prevén modificaciones dea este componente durante el desarrollo de esta funcionalidad.

_API de administración_

| Funcionalidad                                                        | Estado actual         | Issues relacionadas |
|----------------------------------------------------------------------|-----------------------|---------------------|
| Posibilidad de configurar tareas SITMUN de consultas a base de datos | Existente no testeada |                     |
| Posibilidad de configurar tareas SITMUN de consulta a servicios web  | Existente no testeada |                     |

_API configuración y autorización_

| Funcionalidad                                                        | Estado actual         | Issues relacionadas |
|----------------------------------------------------------------------|-----------------------|---------------------|
| Posibilidad de configurar tareas SITMUN de consultas a base de datos | Existente no testeada |                     |
| Posibilidad de configurar tareas SITMUN de consulta a servicios web  | Existente no testeada |                     |

_API de proxy_

No se prevén modificaciones dea este componente durante el desarrollo de esta funcionalidad.
