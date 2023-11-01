# Más info avanzado

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


