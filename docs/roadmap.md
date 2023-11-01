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

El objetivo de esta hoja de ruta es ofrecer una visión general del estado del proyecto SITMUN 3 y las próximas funcionalidades a desarrollar.

!!! info "Aspectos generales"
    La [**El Comité Técnico de SITMUN**](https://sitmun.github.io/contact/) es el órgano funcional encargado de revisar la descripción o,
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
|                             | y con el layout definido para la IDE menorca                                |                                  |
+-----------------------------+-----------------------------------------------------------------------------+----------------------------------+

## Proyectos prioritarios

+--------------------------------------------+-----------------------------------------------------------------------------+-------------------+
| Proyecto - Funcionalidad                   | Descripción                                                                 | Prioridad         |
+============================================+=============================================================================+===================+
| **[Más info avanzado][mas-info-avanzado]** | Busca dotar a SITMUN 3 de la capacidad de configurar, desde                 | Alta              |
|                                            | el administrador SITMUN 3, el contenido de la ventana que                   |                   |
|                                            | devuelve el visualizador al hacer una consulta sobre una capa               |                   |
|                                            | visible en el área de mapa.                                                 |                   |
+--------------------------------------------+-----------------------------------------------------------------------------+-------------------+
| **Mejora de la interficie de usuario de**  | Mejorar la interficie de la ventana de login a los clientes SITMUN          | Media             |
| **página de login y dashboard de usuario** | disponibles para el usuario así como el dashboard para la selección de      |                   |
|                                            | aplicación, territorio y configuración de opciones y datos de usuario.      |                   |
+--------------------------------------------+-----------------------------------------------------------------------------+-------------------+
| **Más info**                               | Implementar en el cliente SITMUN 3 API SITNA la capacidad de interpretar y  | Alta              |
|                                            | ejecutar tareas más info definidas como tal en el administrador SITMUN 3.   |                   |
|                                            | Asimilando el funcionamiento al de los actuales clientes SITMUN 2.          |                   |
+--------------------------------------------+-----------------------------------------------------------------------------+-------------------+
| **Autorización por token en el cliente**   | Autenticación por token en el cliente SITMUN 3 API SITNA                    | Alta              |
|                                            |                                                                             |                   |
+--------------------------------------------+-----------------------------------------------------------------------------+-------------------+
| **Cambio de arbol en aplicación cliente**  | Cambio de árbol del cliente SITMUN 3 API SITNA.                             | Alta              |
|                                            |                                                                             |                   |
+--------------------------------------------+-----------------------------------------------------------------------------+-------------------+



## Proyectos clave en espera

+--------------------------------------------+-----------------------------------------------------------------------------+-------------------+
| Proyecto - Funcionalidad                   | Descripción                                                                 | Prioridad         |
+============================================+=============================================================================+===================+
| **Creación de un cliente SITMUN - API**    | Creación de un cliente SITMUN3 basado en el                                 | Media             |
| **CNIG**                                   | [API CNIG](https://github.com/IGN-CNIG/API-CNIG)                            |                   |
+--------------------------------------------+-----------------------------------------------------------------------------+-------------------+
| **Localizadores**                          | Implementar en el cliente SITMUN 3 API SITNA la capacidad de interpretar y  | Alta              |
|                                            | ejecutar localizadores definidos como tareas en el administrador SITMUN 3.  |                   |
|                                            | Asimilando el funcionamiento al de los actuales clientes SITMUN 2.          |                   |
|                                            |  Esta tarea incluye los cambios necesarios en el administrador y API SITMUN,|                   |
|                                            | para poder configurar correctamente la funcionalidad de localizadores       |                   |
|                                            | integrados genéricos existente en el API SITNA 3.                           |                   |
+--------------------------------------------+-----------------------------------------------------------------------------+-------------------+
| **Consultas**                              | Implementar en el cliente SITMUN 3 API SITNA la capacidad de interpretar y  | Baja              |
|                                            | ejecutar consultas definidas como tareas en el administrador SITMUN 3.      |                   |
|                                            | Asimilando el funcionamiento al de los actuales clientes SITMUN 2.          |                   |
+--------------------------------------------+-----------------------------------------------------------------------------+-------------------+
| **Edición gráfica y alfanumérica**         | Implementar herramientas en el cliente SITMUN 3 que permitan la edición     | Baja              |
|                                            | gráfica (mediante servicios WFS transaccionales) y alfanumérica.            |                   |
+--------------------------------------------+-----------------------------------------------------------------------------+-------------------+
| **Creación dinámica de informes**          | Posibilidad de generar de forma dinámica y parametrizada un informe desde el| Baja              |
|                                            | cliente SITMUN previamente configurado en el administrador SITMUN 3. Un     |                   |
|                                            | informe se configura en SITMUN como una tarea que integra el resultado de   |                   |
|                                            | otras tareas (consultas, generación de imagen de mapa, etc).                |                   |
+--------------------------------------------+-----------------------------------------------------------------------------+-------------------+
| **Creación de temáticos**                  | Dotar al cliente SITMUN 3 de una funcionalidad que permita al usuario       | Baja              |
|                                            | modificar la simbología de una capa en función del valor de sus atributos.  |                   |
+--------------------------------------------+-----------------------------------------------------------------------------+-------------------+
| **Creación de un cliente SITMUN tipo**     |                                                                             | Media             |
| **aplicación para dispositivos móbiles**   |                                                                             |                   |
| **(APP)**                                  |                                                                             |                   |
+--------------------------------------------+-----------------------------------------------------------------------------+-------------------+


## Detalles

### Más info avanzado

!!! info "Aspectos generales"

    **Estimación horas de desarrollo:** 200 horas

    **Entidad solicitante:** Comisión técnica SITMUN

    **Prioridad:** ALTA

    **Persona o entidad de referència o contacto:** Consell Insular de Menorca

**Objetivo:**

Esta funcionalidad busca dotar a SITMUN 3 de la capacidad de configurar, desde el administrador SITMUN 3,
el contenido de la ventana que devuelve el visor SITMUN 3 al realizar una consulta sobre el mapa para una capa determinada.

El contenido de la ventana debe poder integrar la respuesta de una o varias consultas definidas como tareas al propio administrador

**Contexto y casos de uso:**

El actual cliente SITMUN 3, al hacer clic en el área de mapa sobre un objeto de una capa determinada, presenta el resultado de la petición GetFeatureInfo sobre al servicio WMS correspondiente.

![MASINFOAVANZADO_context1](https://github.com/sitmun/sitmun.github.io/assets/26217441/f57fee94-c4b2-44a1-a1a5-0263ebe36f22)

Con la funcionalidad 'Más info avanzado' se busca enriquecer esta ventana de respuesta con datos que provengan de otras peticiones a otros servicios o conexiones a base de datos.

Como ejemplo se puede observar el funcionamiento de SITMUN 2 en el caso del [visualizador de medio natural del Consell Insular de Menorca](https://ide.cime.es/sitmun/ambiental.jsp). En la ventana siguiente podemos observar el detalle de la ventana con distintas pestañas, cada una de ellas se corresponde con el resultado de una tarea de tipo consulta configurada en el administrador SITMUN 2.

![MASINFOAVANZADO_context2](https://github.com/sitmun/sitmun.github.io/assets/26217441/07392c2a-c793-49ec-8f25-e833ff9e589b)

Actual ventana de ejemplo de configuración de una tarea tipo consulta en SITMUn 2.
![MASINFOAVANZADO_context3](https://github.com/sitmun/sitmun.github.io/assets/26217441/c4b214fa-851f-4df7-8669-622fa5c45762)

**Requerimientos funcionales:**

Se prevé la siguiente lógica funcional:

1. En el administrador SITMUN 3 se definirán primero las distintas tareas (que pueden ser de distintos tipos consultas a bases de datos, consultas a servicios, ...) que formaran parte de la ventana de más info avanzado.
   
    Por ejemplo, en el caso del visor medio ambiental anterior, se establecen varias consultas:

    - Una primera tarea que consiste en consulta que devuelve toda la información relativa a una ruta turística:
  
      ![MASINFOAVANZADO_context4](https://ide.cime.es/img/Captura%20de%20pantalla%202023-08-29%20105214.png)

    - Una segunda consulta que devuelve todas las fotografías de una ruta en concreto:
  
      ![MASINFOAVANZADO_context5](https://ide.cime.es/img/Captura%20de%20pantalla%202023-08-29%20105322.png)

2. Una vez definidas estas tareas, que llamaremos tareas hijas, se configurarà en el administrador SITMUN la tarea padre **más info avanzado** En la ventana de configuración de dicha tarea se podrá:

    - Establecer la relación con las distintas tareas hijas que forman parte del más info avanzado. Una tarea hija, a su vez, debe poder formar parte de varias tareas padre.
    - Establecer el tipo de más info avanzado, para establecer cómo se presentarán en la ventana las distintas tareas hijo (en tabs, en scroll...)

      ![MASINFOAVANZADO_context6](https://ide.cime.es/img/Captura%20de%20pantalla%202023-08-29%20105351.png)

    - Establecer para cada tarea hija el código HTML con la configuración o formato de renderizado (para poder definir la tabla, o cómo se muestran las imágenes, o una galeria de fotos, etc). A este código se añadirán marcas especiales con el nombre de los campos de la subconsulta que serán sustituidas en el cliente (API SITNA) por el valor de los mismos.
    Por ejemplo, a la tarea hija código 289 (primera imagen del visor de medio ambiente) le corresponde este layout, dónde los valores @@CODIGOTAREA_NOMBRECAMPO@@ deben de ser sustituidos por el valor del campo correspondiente a la consulta 289.
    
        ![MASINFOAVANZADO_context7](https://ide.cime.es/img/Captura%20de%20pantalla%202023-08-29%20105432.png)

    - Definir qué capa o capas tienen asociada esta funcionalidad.
    - Definir qué territorios y roles de usuario tienen asociada esta funcionalidad. 



3. Configurada correctamente la tarea, el API de configuración y autorización_ deberá incorporar los valores necesarios para permitir al cliente SITMUN 3 - SITNA (1) detectar qué capas tienen un *más info avanzado* definido (para el rol y territorio que se haya logeado). Así mismo, el API deberá retornar la información necesaria y suficiente para que el cliente (API SITNA u otros) puedan renderizar la información consultada de forma adecuada.
   
4. El Cliente SITMUN - API SITNA deberá configurar correctamente la ventana de info cuando se realice un clic sobre el mapa a un elemento de dicha capa, en caso que la capa tenga asociada una tarea de esta índole.

    El cliente permitirá gestionar el comportamiento en caso que el usuario haga clic a dos o más objetos sobre el mapa pertenecientes a la misma capa y/o a distintas capas, algunas de las cuales pueden tener una funcionalidad *más info avanzado** definida y otras no (con lo que presenta la ventana por defecto de respuesta GetFeatureInfo).

Se identifican los siguientes requerimientos funcionales a desarrollar para cada uno de los componentes de la arquitectura de SITMUN:

:left_speech_bubble: _Cliente Administrador SITMUN 3_

+-------------------------------------------------------------------------------------------------+---------------------------------------------+---------------------+
| Funcionalidad                                                                                   | [Commit messages](https://gitmoji.dev/)     | Issues relacionadas |
+=================================================================================================+=============================================+=====================+
| Posibilidad de configurar tareas SITMUN de consultas a base de datos                            | Existente no testeada                       |                     |
+-------------------------------------------------------------------------------------------------+---------------------------------------------+---------------------+
| Posibilidad de configurar tareas SITMUN de consulta a servicios web                             | Existente no testeada                       |                     |
+-------------------------------------------------------------------------------------------------+---------------------------------------------+---------------------+
| Creación de tipo de tareas padre que permitan seleccionar tareas hijo con una vinculación N a M | Nueva                                       |                     |
+-------------------------------------------------------------------------------------------------+---------------------------------------------+---------------------+
| Asignación de parámetros específicos a tareas padre Tab scroll                                  | Nueva                                       |                     |
+-------------------------------------------------------------------------------------------------+---------------------------------------------+---------------------+
| Asignación de una respuesta avanzada a una capa existente                                       | Nueva                                       |                     |
+-------------------------------------------------------------------------------------------------+---------------------------------------------+---------------------+

:left_speech_bubble: _Cliente visualizador SITMUN 3 (API SITNA)_

+-------------------------------------------------------------------------------------------------+-------------------------+---------------------+
| Funcionalidad                                                                                   | Estado                  | Issues relacionadas |
+=================================================================================================+=========================+=====================+
| Parsear json del API de configuración y representar los datos                                   | Existente no testeada   |                     |
+-------------------------------------------------------------------------------------------------+-------------------------+---------------------+
| Gestionar y renderizar la configuración de la respuesta avanzada para una capa concreta         | Nueva                   |                     |
+-------------------------------------------------------------------------------------------------+-------------------------+---------------------+

:left_speech_bubble: _API de autenticación_

No se prevén modificaciones dea este componente durante el desarrollo de esta funcionalidad.

:left_speech_bubble: _API de administración_

+-------------------------------------------------------------------------------------------------+-------------------------+---------------------+
| Funcionalidad                                                                                   | Estado                  | Issues relacionadas |
+=================================================================================================+=========================+=====================+
| Posibilidad de configurar tareas SITMUN de consultas a base de datos                            | Existente no testeada   |                     |
+-------------------------------------------------------------------------------------------------+-------------------------+---------------------+
| Posibilidad de configurar tareas SITMUN de consulta a servicios web                             | Existente no testeada   |                     |
+-------------------------------------------------------------------------------------------------+-------------------------+---------------------+

:left_speech_bubble: _API configuración y autorización_

No se prevén modificaciones dea este componente durante el desarrollo de esta funcionalidad.

:left_speech_bubble: _API de proxy_

No se prevén modificaciones dea este componente durante el desarrollo de esta funcionalidad.

:left_speech_bubble: _Esquema de base de datos SITMUN administrador_

No se prevén modificaciones dea este componente durante el desarrollo de esta funcionalidad.



### Mejora GUI del login y dashboard de usuario del cliente SITMUN 3.
 
!!! info "Aspectos generales"

    **Estimación horas de desarrollo:** 40 horas

    **Entidad solicitante:** Comisión técnica SITMUN

    **Prioridad:** ALTA
    
    **Persona o entidad de referència o contacto:** Consell Insular de Menorca


**Objetivo:**

Este proyecto busca mejorar el diseño y la funcionalidad de la interficie de acceso y selección de los clientes SITMUN 
disponibles para un usuario concreto, dotándolas de un diseño más amigable, claro y funcional. 
Se busca además ampliar la funcionalidad actual.


**Contexto y casos de uso:**
En las imágenes siguientes se puede ver la actual ventana de login y selección de aplicación del actual cliente SITMUN 3.

![MejoraGUI_contexto1](https://github.com/sitmun/sitmun.github.io/assets/26217441/72462a93-2403-44a8-b8df-99ecbf22130f)

En la imagen siguiente se puede ver el dashboard inicial:
![MejoraGUI_contexto2](https://github.com/sitmun/sitmun.github.io/assets/26217441/89168d4b-6873-4a60-81da-2123a337fe41)

Se hace necesario mejorar el diseño de ambas ventanas y ampliar la funcionalidad que se ofrece al usuario.


**Requerimientos funcionales:**

Se prevé la siguiente lógica funcional:

1. Acceso a SITMUN. Desde la ventana de login se permite entrar en el espacio de usuario, que ofrece acceso a las distintas combinaciones de apliación y territorio sobre las que un usuario tiene permisos. Así mismo, y de forma diferenciada en la interficie de usuario, se ofrece acceso a las aplicaciones públicas. La ventana de acceso incorpora, además del espacio de usuario/pasword una opción de acceso 'publico' permite el acceso a un espacio público que únicamente ofrece el listado de aplicaciones / territorio que són de carácter público.

2. Una vez logeado al espacio de usuario se ofrecerá al usuario de forma clara el listado de territorios y de aplicaciones. El listado de territorios se ofrece como una lista de todos los territorios a los que el usuario tiene acceso con una opción 'todos' por defecto que no realiza filtro sobre las aplicaciones. En caso que un usuario tenga acceso a muchos territorios y este hecho dificulte presentar las opciones sin filtrar por volumen, aparecerà un aviso a la pantalla principal pidiendo al usuaro que seleccione un territorio de la lista.  El listado de aplicaciones se presenta como un conjunto de elementos con características (imagen, descripción, territorio i último acceso). La ventana de usuario ofrece la siguiente funcionalidad:

    - Opción de consultar los datos de usuario en el SITMUN (territorio, rol, caducidad...) y gestionar determinados datos de usuario (cambiar el correo electrónico, el teléfono y la contraseña)
    - Informar de forma clara de: fecha del último acceso a SITMUN, fecha de último acceso para cada aplicación, fecha de caducidad de los permisos para cada aplicación/territorio,
    - Espacio de notícias y comunicados para que el administrador SITMUN pueda enviar mensajes a cada usuario en función de sus permisos de acceso. 
    - Acceso diferenciado a las aplicaciones públicas.
    - Buscador de territorios
    - Cambio de idioma
    - Logout

A continuación se presenta de forma ilustrativa el concepto de interficie. 
**Este diseño es solo demostrativo para plasmar la idea inicial de la Red SITMUN**, 
la empresa contractante deberá desarrollar esta idea y plantear una o varias propuestas de GUI. 
En la propuesta de diseño se pondrá énfasis en crear una imagen moderna, 
clara y funcional para el usuario y que sea responsiva.

![Sitmun dashboard user_conceptExample](https://github.com/sitmun/sitmun.github.io/assets/26217441/5a05eb9a-afe9-427a-b642-b12b04f12c2e)


Se identifican los siguientes requerimientos funcionales a desarrollar para cada uno de los componentes de la arquitectura de SITMUN.

:left_speech_bubble: _Cliente Administrador SITMUN 3_

+-------------------------------------------------------------------------------------------------+-------------------------+---------------------+
| Funcionalidad                                                                                   | Estado                  | Issues relacionadas |
+=================================================================================================+=========================+=====================+ 
| Añadir noticias, avisos o mensajes para todos los usuarios, para un rol o un usuario concreto.  | Nueva                   |                     |
| Cada notícia ha de tener, por lo menos, un título, texto (multiidioma), una imagen y            |                         |                     | 
| la posiblidad de agregar enlaces.                                                               |                         |                     |                   
+-------------------------------------------------------------------------------------------------+-------------------------+---------------------+
| Asociar una imagen o thumbnail a cada aplicación                                                | Existente no testeada   |                     |
+-------------------------------------------------------------------------------------------------+-------------------------+---------------------+

:left_speech_bubble: _Cliente visualizador SITMUN 3 (Dashboad de usuario)_

+-------------------------------------------------------------------------------------------------+-------------------------+---------------------+
| Funcionalidad                                                                                   | Estado                  | Issues relacionadas |
+=================================================================================================+=========================+=====================+ 
| Mejorar el diseño de la ventana de login, mas claro y responsive                                | Nueva                   |                     |
+-------------------------------------------------------------------------------------------------+-------------------------+---------------------+
| Mejorar el diseño de la ventana del dashboard de usuario                                        | Nueva                   |                     |
+-------------------------------------------------------------------------------------------------+-------------------------+---------------------+
| Ofrecer la opción de cambio de contraseña desde la ventana de login                             | Nueva                   |                     |
+-------------------------------------------------------------------------------------------------+-------------------------+---------------------+
| Presentar territorios disponibles en forma de lista, con un buscador que realice filtro         | Nueva                   |                     |
| dinámico. Si no hay territorios seleccionados se tienen que presentar todas las aplicaciones.   |                         |                     |
| Al seleccionar un territorio de la lista se presentan las aplicaciones disponibles para ese     |                         |                     |
| territorio                                                                                      |                         |                     |
+-------------------------------------------------------------------------------------------------+-------------------------+---------------------+
| Añadir espacio para consultar datos de usuario: nombre usuario, fecha última conexión, numero   | Nueva                   |                     |
| de conexiones i tiempo de conexión total del último mes, tabla de datos asociados al territorio,|                         |                     |
| con la opción de, por lo menos, poder modificar la contraseña                                   |                         |                     |
+-------------------------------------------------------------------------------------------------+-------------------------+---------------------+
| Crear un espacio en el dashboard para crear notícias y mensajes / avisos del administrador hacia| Nueva                   |                     |
| los usuarios                                                                                    |                         |                     |                                                                        
+-------------------------------------------------------------------------------------------------+-------------------------+---------------------+

:left_speech_bubble: _API de autenticación_

No se prevén modificaciones dea este componente durante el desarrollo de esta funcionalidad.

:left_speech_bubble: _API de administración_

+-------------------------------------------------------------------------------------------------+-------------------------+---------------------+
| Funcionalidad                                                                                   | Estado                  | Issues relacionadas |
+=================================================================================================+=========================+=====================+ 
| Incorporar los parámetros necesarios para configurar el listado de aplicaciones (descripción,   | Nueva                   |                     |
| imagen, título, fecha de caducidad, fecha último acceso) accesibles para el usuario en la       |                         |                     |
| aplicación de Administdración SITMUN 3                                                          |                         |                     |
+-------------------------------------------------------------------------------------------------+-------------------------+---------------------+
| Incorporar los parámetros necesarios para configurar en el dashboard las comunicaciones y       | Nueva                   |                     |
| notícias (título, descripcion, enlaces, imagen) para cada usuario desde la aplicación           |                         |                     |
| de administración SITMUN 3                                                                      |                         |                     |
+-------------------------------------------------------------------------------------------------+-------------------------+---------------------+

:left_speech_bubble: _API configuración y autorización_

No se prevén modificaciones de este componente durante el desarrollo de esta funcionalidad.

:left_speech_bubble: _API de proxy_

No se prevén modificaciones dea este componente durante el desarrollo de esta funcionalidad.

:left_speech_bubble: _Esquema de base de datos SITMUN administrador_

+-------------------------------------------------------------------------------------------------+-------------------------+---------------------+
| Funcionalidad                                                                                   | Estado                  | Issues relacionadas |
+=================================================================================================+=========================+=====================+ 
| Analizar e incorporar a la bbdd, si se requiere, los campos necesarios para permitir almacernar | Nueva                   |                     |
| los parámetros necesarios para configurar el listado de aplicaciones                            |                         |                     |
+-------------------------------------------------------------------------------------------------+-------------------------+---------------------+
| Analizar e incorporar a la bbdd si se requiere, locs campos necesarios para configurar          | Nueva                   |                     |
| en el dashboard las comunicaciones y notícias para cada usuario                                 |                         |                     |
+-------------------------------------------------------------------------------------------------+-------------------------+---------------------+
