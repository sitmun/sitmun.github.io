# Roadmap

- **Más info avanzado: enriquecimiento de datos asociados a una capa**
Funcionalidad que busca dotar a SITMUN 3 de la capacidad de configurar, desde el administrador SITMUN 3, el contenido de la ventana que devuelve el visualizador al hacer una consulta sobre una capa visible en el área de mapa.

- **Mejora del la interficie de usuario de la página de login i selección de territorio/aplicación**  

- **Edición gráfica y alfanumérica**
Implementar herramientas en el cliente SITMUN 3 que permitan la edición gráfica (mediente servicios WFS transaccionales) y alfanumérica.

- **Creación dinámica de informes**
Un informe SITMUN es un documento formado por varios documentosConfiguración de informes desde el administrador de SITMUN 3 

- **Creación de temáticos**
Dotar al cliente SITMUN 3 de una funcionalidad que permita

- **Creación de un cliente SITMUN tipo aplicación para dispositivos móbiles (APP)**




## DESCRIPCIÓN DE LAS FUNCIONALIDADES DEL ROADMAP

### **Más info avanzado: enriquecimiento de datos asociados a una capa**
 
!!! info "Aspectos generales"
     **Estimación horas de desarrollo:**  80 horas              
     **Entidad solicitante:** Comissión técnica SITMUN
     **Entidad con previsión de ejecución:** Pyrenees Orientales


**Objetivo:**
Aquesta funcionalitat busca dotar a SITMUN 3 de la capacitat de configurar, des de l’administrador SITMUN 3, el contingut de la finestra que retorna el visualitzador SITMUN 3 al fer una consulta sobre el mapa per a una capa determinada. 

El contingut de la finestra ha de poder integrar la resposta d’una o diverses consultes definides com a tasques al mateix administrador

**Contexto y casos de uso:**



**Requerimientos funcionales:**

_Cliente Administrador SITMUN 3_
| Funcionalidad | Estado actual | Issues relacionadas |
|---|---|---|
| Posibilidad de configurar tareas SITMUN de consultas a base de datos    | Existente no testeada    |  #8 |
| Posibilidad de configurar tareas SITMUN de consulta a servicios web    | Existente no testeada    | |
| Creación de tipo de tareas padre que permitan seleccionar tareas hijo con una vinculación N a M    | Nueva    | |
| Asignación de parámetros específicos a tareas padre (Tab scroll)   | Nueva    | |


_Cliente visualizador SITMUN 3 (API SITNA)_
| Funcionalidad | Estado actual | Issues relacionadas |
|---|---|---|
| Parsear json del API de configuración y representar los datos    | Existente no testeada    |  #8 |


_API de autenticación_
No se prevén modificaciones dea este componente durante el desarrollo de esta funcionalidad.
| Funcionalidad | Estado actual | Issues relacionadas |
|---|---|---|
||||


_API de administración_
| Funcionalidad | Estado actual | Issues relacionadas |
|---|---|---|
| Posibilidad de configurar tareas SITMUN de consultas a base de datos    | Existente no testeada    |  #8 |
| Posibilidad de configurar tareas SITMUN de consulta a servicios web    | Existente no testeada    | |


_API configuración y autorización_
| Funcionalidad | Estado actual | Issues relacionadas |
|---|---|---|
| Posibilidad de configurar tareas SITMUN de consultas a base de datos    | Existente no testeada    |  #8 |
| Posibilidad de configurar tareas SITMUN de consulta a servicios web    | Existente no testeada    | |


_API de proxy_
| Funcionalidad | Estado actual | Issues relacionadas |
|---|---|---|
