# Mejora UI del login y dashboard de usuario del cliente SITMUN 3

!!! info "Aspectos generales"

    **Estimación horas de desarrollo:** 40 horas

    **Entidad solicitante:** Comisión técnica SITMUN

    **Prioridad:** ALTA
    
    **Persona o entidad de referéncia o contacto:** Consell Insular de Menorca

## Objetivo

Este proyecto busca mejorar el diseño y la funcionalidad de la interficie de acceso y selección de los clientes SITMUN
disponibles para un usuario concreto, dotándolas de un diseño más amigable, claro y funcional.
Se busca además ampliar la funcionalidad actual.

## Contexto y casos de uso

En las imágenes siguientes se puede ver la actual ventana de login y selección de aplicación del actual cliente SITMUN 3.

![MejoraGUI_contexto1](https://github.com/sitmun/sitmun.github.io/assets/26217441/72462a93-2403-44a8-b8df-99ecbf22130f)

En la imagen siguiente se puede ver el dashboard inicial:
![MejoraGUI_contexto2](https://github.com/sitmun/sitmun.github.io/assets/26217441/89168d4b-6873-4a60-81da-2123a337fe41)

Se hace necesario mejorar el diseño de ambas ventanas y ampliar la funcionalidad que se ofrece al usuario.

## Requerimientos funcionales

Se prevé la siguiente lógica funcional:

1. Acceso a SITMUN. Desde la ventana de login se permite entrar en el espacio de usuario, que ofrece acceso a las distintas combinaciones de aplicación y territorio sobre las que un usuario tiene permisos. Así mismo, y de forma diferenciada en la interficie de usuario, se ofrece acceso a las aplicaciones públicas. La ventana de acceso incorpora, además del espacio de usuario/password una opción de acceso 'público' permite el acceso a un espacio público que únicamente ofrece el listado de aplicaciones / territorio que son de carácter público.

2. Una vez logeado al espacio de usuario se ofrecerá al usuario de forma clara el listado de territorios y de aplicaciones. El listado de territorios se ofrece como una lista de todos los territorios a los que el usuario tiene acceso con una opción 'todos' por defecto que no realiza filtro sobre las aplicaciones. En caso de que un usuario tenga acceso a muchos territorios y este hecho dificulte presentar las opciones sin filtrar por volumen, aparecerá un aviso a la pantalla principal pidiendo al usuario que seleccione un territorio de la lista.  El listado de aplicaciones se presenta como un conjunto de elementos con características (imagen, descripción, territorio i último acceso). La ventana de usuario ofrece la siguiente funcionalidad:

    - Opción de consultar los datos de usuario en el SITMUN (territorio, rol, caducidad…) y gestionar determinados datos de usuario (cambiar el correo electrónico, el teléfono y la contraseña)
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

### Cliente Administrador

+-------------------------------------------------------------------------------------------------+-------------------------+---------------------+
| Funcionalidad                                                                                   | Estado                  | Issues relacionadas |
+=================================================================================================+=========================+=====================+
| Añadir noticias, avisos o mensajes para todos los usuarios, para un rol o un usuario concreto.  | Nueva                   |                     |
| Cada noticia ha de tener, por lo menos, un título, texto (multiidioma), una imagen y            |                         |                     |
| la posibilidad de agregar enlaces.                                                              |                         |                     |
+-------------------------------------------------------------------------------------------------+-------------------------+---------------------+
| Asociar una imagen o thumbnail a cada aplicación                                                | Existente no testeada   |                     |
+-------------------------------------------------------------------------------------------------+-------------------------+---------------------+

### Cliente visualizador (Dashboard de usuario)

+--------------------------------------------------------------------------------------------------+-------------------------+---------------------+
| Funcionalidad                                                                                    | Estado                  | Issues relacionadas |
+==================================================================================================+=========================+=====================+
| Mejorar el diseño de la ventana de login, más claro y responsive                                 | Nueva                   |                     |
+--------------------------------------------------------------------------------------------------+-------------------------+---------------------+
| Mejorar el diseño de la ventana del dashboard de usuario                                         | Nueva                   |                     |
+--------------------------------------------------------------------------------------------------+-------------------------+---------------------+
| Ofrecer la opción de cambio de contraseña desde la ventana de login                              | Nueva                   |                     |
+--------------------------------------------------------------------------------------------------+-------------------------+---------------------+
| Presentar territorios disponibles en forma de lista, con un buscador que realice filtro          | Nueva                   |                     |
| dinámico. Si no hay territorios seleccionados se tienen que presentar todas las aplicaciones.    |                         |                     |
| Al seleccionar un territorio de la lista se presentan las aplicaciones disponibles para ese      |                         |                     |
| territorio                                                                                       |                         |                     |
+--------------------------------------------------------------------------------------------------+-------------------------+---------------------+
| Añadir espacio para consultar datos de usuario: nombre usuario, fecha última conexión, número    | Nueva                   |                     |
| de conexiones y tiempo de conexión total del último mes, tabla de datos asociados al territorio, |                         |                     |
| con la opción de, por lo menos, poder modificar la contraseña                                    |                         |                     |
+--------------------------------------------------------------------------------------------------+-------------------------+---------------------+
| Crear un espacio en el dashboard para crear noticias y mensajes / avisos del administrador hacia | Nueva                   |                     |
| los usuarios                                                                                     |                         |                     |
+--------------------------------------------------------------------------------------------------+-------------------------+---------------------+
| Diferenciar estilos de ventanas login, dashboard y cliente visualizador y simplificar al         | Nueva                   |                     |
| máximo el diseño de la barra para el cliente para interferir al mínimo en el diseño del          |                         |                     |
| visor (p.e. barra transparente y boton pequeño en margen superior derecho).                      |                         |                     |
+--------------------------------------------------------------------------------------------------+-------------------------+---------------------+

### API de autenticación {#roadmap-mejora-ui-api-de-autenticacion}

No se prevén modificaciones dea este componente durante el desarrollo de esta funcionalidad.

### API de administración {#roadmap-mejora-ui-api-de-administracion}

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

### API configuración y autorización {#roadmap-mejora-ui-api-de-configuracion-y-autorizacion}

No se prevén modificaciones de este componente durante el desarrollo de esta funcionalidad.

### API de proxy {#roadmap-mejora-ui-api-de-proxy}

No se prevén modificaciones dea este componente durante el desarrollo de esta funcionalidad.

### Esquema de base de datos

+------------------------------------------------------------------------------------------------+-------------------------+---------------------+
| Funcionalidad                                                                                  | Estado                  | Issues relacionadas |
+================================================================================================+=========================+=====================+
| Analizar e incorporar a la bbdd, si se requiere, los campos necesarios para permitir almacenar | Nueva                   |                     |
| los parámetros necesarios para configurar el listado de aplicaciones                           |                         |                     |
+------------------------------------------------------------------------------------------------+-------------------------+---------------------+
| Analizar e incorporar a la bbdd si se requiere, los campos necesarios para configurar          | Nueva                   |                     |
| en el dashboard las comunicaciones y noticias para cada usuario                                |                         |                     |
+------------------------------------------------------------------------------------------------+-------------------------+---------------------+
