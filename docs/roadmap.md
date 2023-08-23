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

- **Mejora de la interficie de usuario de la página de login y dashboard de usuario**:
Mejorar la interficie de la ventana de login a los clientes SITMUN disponibles para el usuario así como el dashboard para la selección de aplicación, territorio i configuración de opciones y datos de usuario.
  
- **Edición gráfica y alfanumérica**:
Implementar herramientas en el cliente SITMUN 3 que permitan la edición gráfica (mediante servicios WFS transaccionales) 
y alfanumérica.

- **Creación dinámica de informes**:
Posiblidad de generar de forma dinámica i parametrizada un informe desde el cliente SITMUN previamente configurado en el administrador SITMUN 3. Un informe se configura en SITMUN como una tarea que integra el resultado de otras tareas (consultas, generación de imagen de mapa, etc).

- **Creación de temáticos**:
Dotar al cliente SITMUN 3 de una funcionalidad que permita al usuario modificar la simbología de una capa en función del valor de sus atributos.

- **Creación de un cliente SITMUN tipo aplicación para dispositivos móbiles (APP)**

## Detalles

### Más info avanzado
 
!!! info "Aspectos generales"

    **Estimación horas de desarrollo:** 200 horas

    **Entidad solicitante:** Comisión técnica SITMUN

    **Entidad con previsión de ejecución:** Pyrenees Orientales

    **Prioridad:** ALTA

**Objetivo:**

Esta funcionalidad busca dotar a SITMUN 3 de la capacidad de configurar, desde el administrador SITMUN 3,
el contenido de la ventana que devuelve el visor SITMUN 3 al realizar una consulta sobre el mapa para una capa determinada.

El contenido de la ventana debe poder integrar la respuesta de una o varias consultas definidas como tareas al propio administrador

**Contexto y casos de uso:**
El actual cliente SITMUN 3, al hacer clic en el area de mapa sobre un objeto de una capa determinada, presenta el resultado de la petición GetFeatureInfo sobre al servicio WMS correspondiente. 

![MASINFOAVANZADO_context1](https://github.com/sitmun/sitmun.github.io/assets/26217441/f57fee94-c4b2-44a1-a1a5-0263ebe36f22)

Con la funcionalidad 'Más info avanzado' se busca enriquecer esta ventana de respuesta con datos que provengan de otras peticiones a otros servicios o conexiones a base de datos.

Como ejemplo se puede observar el funcionamiento de SITMUN 2 en el caso del [visualizador de medio natural del Consell Insular de Menorca](https://ide.cime.es/sitmun/ambiental.jsp). En la ventana siguiente podemos observar el detalle de la ventana con distintas pestañas, cada una de ellas se corresponde con el resultado de una tarea de tipo consulta configurada en el administrador SITMUN 2. 

![MASINFOAVANZADO_context2](https://github.com/sitmun/sitmun.github.io/assets/26217441/07392c2a-c793-49ec-8f25-e833ff9e589b)

![MASINFOAVANZADO_context3](https://github.com/sitmun/sitmun.github.io/assets/26217441/c4b214fa-851f-4df7-8669-622fa5c45762)

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



### Mejora GUI de la página de login y dashboard de usuario del cliente SITMUN 3.
 
!!! info "Aspectos generales"

    **Estimación horas de desarrollo:** 40 horas

    **Entidad solicitante:** Comisión técnica SITMUN

    **Entidad con previsión de ejecución:** Pyrenees Orientales

    **Prioridad:** ALTA

**Objetivo:**

Este proyecto busca mejorar el diseño y la funcionalidad de la interficie de acceso y selección de los clientes SITMUN disponibles para un usuario concreto, dotandolas de un diseño más amigable, claro y funcional. Se busca además ampliar la funcionalidad actual.


**Contexto y casos de uso:**
En las imagenes siguientes se puede ver la actual ventana de login y selección de aplicación del actual cliente SITMUN 3.

![MejoraGUI_contexto1](https://github.com/sitmun/sitmun.github.io/assets/26217441/fa18fa8e-02c1-47a4-9ba3-a3267c141ee1)

![MejoraGUI_contexto2](https://github.com/sitmun/sitmun.github.io/assets/26217441/15929a44-00f9-4ebe-a6db-979ccb36ef87)

Se hace necesario mejorar el diseño de ambas ventanas y ampliar la funcionalidad que se ofrece al usuario.

**Requerimientos funcionales:**

_Cliente Administrador SITMUN 3_

| Funcionalidad                                                                                   | Estado actual         | Issues relacionadas |
|-------------------------------------------------------------------------------------------------|-----------------------|---------------------|
| Posibilidad de configurar tareas SITMUN de consultas a base de datos                            | Existente no testeada |                     |


_Cliente visualizador SITMUN 3 (API SITNA)_

| Funcionalidad                                                                              | Estado actual         | Issues relacionadas |
|--------------------------------------------------------------------------------------------|-----------------------|---------------------|
| Mejorar el diseño de la ventana de login, mas claro y responsive                           | nueva                 |                     |
| Mejorar el diseño de la ventana del dashboard de usuario                                   | nueva                 |                     |
| Ofrecer la opción de cambio de contraseña desde la ventana de login                        | nueva                 |                     |
| Crear lista de territorios disponibles en forma de lista. 
Al seleccionar cada territorio se presentan las aplicaciones disponibles para ese territorio | nueva                 |                     |

_API de autenticación_

No se prevén modificaciones dea este componente durante el desarrollo de esta funcionalidad.

_API de administración_

No se prevén modificaciones dea este componente durante el desarrollo de esta funcionalidad.

_API configuración y autorización_

| Funcionalidad                                                        | Estado actual         | Issues relacionadas |
|----------------------------------------------------------------------|-----------------------|---------------------|
| Posibilidad de configurar tareas SITMUN de consultas a base de datos | Existente no testeada |                     |
| Posibilidad de configurar tareas SITMUN de consulta a servicios web  | Existente no testeada |                     |

_API de proxy_

No se prevén modificaciones dea este componente durante el desarrollo de esta funcionalidad.


