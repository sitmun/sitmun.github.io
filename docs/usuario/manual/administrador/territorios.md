---
description: "Territorios en el administrador de SITMUN 3: datos, extensión, CRS y relaciones con usuarios, roles y otros territorios."
---

# Territorios

El territorio es el elemento para definir las características de un territorio, al que se asignan los elementos disponibles.

Con la combinación de los tres elementos, territorios, [roles](roles.md) y [usuarios](usuarios.md), se configuran los accesos y permisos a las [aplicaciones](aplicacion.md), [tareas](tareas/index.md) e información del mapa ([capas](capas.md), [capas de fondo](capas-de-fondo.md), etc.).

Para definir un territorio se deben definir los parámetros mínimos:

- **Nombre**: nombre del territorio que permita identificar el elemento; se mostrará en las aplicaciones.
- **Código**: código único oficial del territorio.
- **Tipo**: se selecciona de una lista que se mantiene en [Sistema → Tipos de territorio](sistema.md#tipos-de-territorio). Una instalación nueva incluye, entre otros, país, comunidad autónoma, diputación, consejo insular, comarca, área metropolitana, mancomunidad, municipio y entidad inframunicipal; cada instalación puede añadir los suyos.

Aunque no sean requisito indispensable, también es de gran importancia detallar la presentación inicial con la que se abrirá una aplicación de tipo visor con este territorio. Para ello se debe definir la ubicación del territorio con una de las dos opciones disponibles:

- **Extensión** (campos *min X*, *max X*, *min Y* y *max Y*): definir la extensión, con las cuatro coordenadas, que deben definirse juntas (minX, maxX, minY, maxY).
- **Punto central** (X e Y): se pueden definir las coordenadas de un punto concreto en el que se quiera centrar la vista inicial del visor, dando la opción de que este no sea el punto central de los límites del territorio.

Estos dos elementos van asociados a:

- **CRS**: definir el sistema de referencia en el que se expresan las coordenadas anteriores (por ejemplo, EPSG:4326).
- **Nivel de Zoom por defecto**: puede detallarse la escala del nivel de zoom.

La extensión, el CRS y el nivel de zoom inicial, si están definidos, anulan los valores de la aplicación.

Complementariamente, existe la opción de definir también otros parámetros de configuración:

- **Descripción**
- **Dirección**
- **Territorio bloqueado**: según su descripción, un territorio bloqueado no aparece en las listas de territorios de los clientes ni da acceso a perfiles. Un territorio nuevo se crea bloqueado por defecto; desactívelo para los territorios que deban usarse.

    !!! warning "SITMUN 1.3.0"
        En la versión 1.3.0 esta opción no tiene efecto: un territorio bloqueado sigue apareciendo y su perfil sigue disponible
        ([sitmun/sitmun#376](https://github.com/sitmun/sitmun/issues/376)).
- **Logo**
- **Observaciones**

En otras pestañas se detallan las relaciones con los otros elementos existentes en la plataforma:

- **Usuarios con rol**: definir la relación con los otros componentes que permitirán el acceso a este territorio. En esta relación se puede detallar si se desea transmitir los permisos entre las relaciones jerárquicas creadas entre padres e hijos.
- **Territorios padres**: indicar los territorios de un nivel superior al que se está definiendo.
- **Territorios hijos**: indicar los territorios de un nivel inferior al que se está definiendo.
- **Cartografía**: capas de información a las que tendrá acceso este territorio.
- **Tareas**: tareas a las que tendrá acceso este territorio.
