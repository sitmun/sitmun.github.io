---
description: "Territorios en el administrador de SITMUN 3: datos, extensión, CRS y relaciones con usuarios, roles y otros territorios."
---

# Territorios

El territorio es el elemento para definir las características de un territorio, al que se asignan los elementos disponibles.

Con la combinación de los tres elementos, territorios, [roles](roles.md) y [usuarios](usuarios.md), se configuran los accesos y permisos a las [aplicaciones](aplicacion.md), [tareas](tareas/index.md) e información del mapa ([capas](capas.md), [capas de fondo](capas-de-fondo.md), etc.).

Un territorio necesita como mínimo estos parámetros:

- **Nombre**: nombre del territorio que permita identificar el elemento; se mostrará en las aplicaciones. Debe ser único: dos territorios no pueden llamarse igual.
- **Código**: código oficial del territorio.
- **Tipo**: se selecciona de una lista que se mantiene en [Sistema → Tipos de territorio](sistema.md#tipos-de-territorio). Una instalación nueva incluye País, Comunidad Autónoma, Ciudad Autónoma, Diputación, Consejo Insular (Baleares), Cabildo Insular (Canarias), Ayuntamiento, Comarca, Área Metropolitana, Mancomunidad, Agrupación de Municipios y Entidad de Ámbito Inferior al Municipio; cada instalación puede añadir los suyos.

La presentación inicial con la que se abre un visor en este territorio se define con estos campos:

- **Extensión** (campos *min X*, *max X*, *min Y* y *max Y*): los límites del territorio; las cuatro coordenadas se indican juntas. Es necesaria: sin extensión, el visor no abre el mapa y muestra «No se ha definido una extensión inicial válida para este mapa».
- **Punto central** (X e Y): opcional. Desplaza la vista inicial para centrarla en ese punto, que no tiene por qué ser el centro de la extensión. Sin extensión no tiene efecto.

Estos dos elementos van asociados a:

- **CRS**: el sistema de referencia en el que se expresan las coordenadas anteriores (por ejemplo, EPSG:4326).
- **Nivel de Zoom por defecto**: el nivel de zoom con el que se abre el mapa.

El CRS del territorio, si está definido, sustituye al de la aplicación. La aplicación no tiene campos de extensión ni de zoom: los del territorio son los únicos.

Complementariamente, existe la opción de definir también otros parámetros de configuración:

- **Descripción**
- **Dirección**
- **Territorio bloqueado**: según su descripción, un territorio bloqueado no aparece en las listas de territorios de los clientes ni da acceso a la configuración del visor para ese territorio. Un territorio nuevo se crea bloqueado por defecto; la opción se desactiva en los territorios que deban usarse.

    !!! warning "SITMUN 1.3.0"
        En la versión 1.3.0 esta opción no tiene efecto: un territorio bloqueado sigue apareciendo y el visor sigue recibiendo su configuración
        ([sitmun/sitmun#376](https://github.com/sitmun/sitmun/issues/376)).
- **Logo**
- **Observaciones**

En otras pestañas se detallan las relaciones con los otros elementos existentes en la plataforma:

- **Usuarios con rol**: definir la relación con los otros componentes que permitirán el acceso a este territorio. En esta relación se puede detallar si se desea transmitir los permisos entre las relaciones jerárquicas creadas entre padres e hijos.
- **Territorios padres**: indicar los territorios de un nivel superior al que se está definiendo. La pestaña no aparece si el tipo del territorio está marcado como **Tipo superior**.
- **Territorios hijos**: indicar los territorios de un nivel inferior al que se está definiendo. La pestaña no aparece si el tipo está marcado como **Tipo inferior**.
- **Cartografía**: capas de información a las que tendrá acceso este territorio.
- **Tareas**: tareas a las que tendrá acceso este territorio.
