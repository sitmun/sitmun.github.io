---
description: "Opciones de sistema del administrador de SITMUN 3: idiomas, traducciones, tipos de territorio y de tareas, listas de códigos y parámetros."
---

# Sistema

Las opciones de sistema permiten ajustar algunos parámetros generales de SITMUN.

## Controles de interfaz de tarea

El visor de SITMUN se basa, en su parte de frontend, en la API SITNA promovida por el Gobierno de Navarra. Esta API ofrece un conjunto de controles para realizar diversas acciones con el visor.

En este apartado podemos gestionar de manera rápida la relación entre dichos controles de la API SITNA y la tarea de SITMUN que hace uso de ellos.

## Idiomas

Permite gestionar los idiomas disponibles en SITMUN. Añadir un idioma no significa que se añadan automáticamente todas las traducciones, sino que será posible, si se desea, generar los textos en el idioma añadido.

Desde aquí también se cambia el **idioma por defecto** de SITMUN: al marcar otro idioma como idioma por defecto, el administrador muestra una vista previa de los textos afectados antes de aplicar el cambio.

Este idioma se refiere al idioma de los contenidos de SITMUN (lo que el usuario o el administrador pueden añadir), no al idioma de los propios mensajes de la aplicación, que se deberían gestionar de manera diferente en el caso de añadir un nuevo idioma.

## Traducciones de literales

Esta opción permite añadir palabras o frases del sistema en diversos idiomas. Cada literal tiene un texto original en un idioma de origen y, a partir de él, se pueden proporcionar el resto de traducciones de dicha frase.

También se puede modificar el propio texto original con el símbolo de editar situado a la derecha de cada literal.

Las traducciones se pueden exportar e importar en formato CSV.

## Tipos de territorio

Permite definir y mantener las diferentes tipologías de territorio, así como la jerarquía entre ellas.

## Tipos de tareas

Muestra la lista de tipos de tareas. Los tipos son fijos: no se pueden añadir ni borrar, solo se puede editar su título.

## Valores de listas de códigos

En general, las listas de valores que se utilizan en SITMUN provienen de un conjunto de valores y sus descriptores. Para facilitar la comprensión de la información, normalmente se muestra al administrador el valor del descriptor, que se puede editar y modificar. No así el código del descriptor, que se mantiene fijo y que SITMUN utiliza internamente para identificar los elementos en cuestión.

## Parámetros de configuración

Permite editar y añadir parámetros de configuración general de SITMUN, por ejemplo:

- `language.default`: indica el idioma por defecto de SITMUN. Es de solo lectura: se cambia desde [Idiomas](#idiomas).
- `srs.default.identifier`: indica el sistema de referencia que se utilizará por defecto.
