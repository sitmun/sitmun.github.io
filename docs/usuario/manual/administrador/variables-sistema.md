---
description: "Variables de sistema de SITMUN 3 que se pueden usar en consultas, plantillas y otras tareas."
---

# Anexo I: variables de sistema

Con el fin de poder interactuar con la propia aplicación de SITMUN, se ofrecen algunas variables de sistema que pueden utilizarse en la aplicación de administración de SITMUN, por ejemplo en las [consultas SQL](tareas/consulta.md#parametros-en-las-consultas-sql).

Para identificar dichas variables, en consultas, URL y parámetros de tareas se escriben con el símbolo `#` y dentro de un par de llaves `{ }`, por ejemplo `#{TERR_COD}`. En las [plantillas](tareas/plantillas.md) se escriben con otra forma, `{{#APP_NAME}}`.

El backend sustituye cada variable con datos del usuario, el territorio y la aplicación de la petición:

| Variable | Valor |
| --- | --- |
| `#{USER_ID}`, `#{USU_CODIGO}` | Identificador del usuario. |
| `#{USER_NAME}`, `#{USUARIO}` | Nombre de usuario. |
| `#{TERR_ID}`, `#{TER_CODIGO}` | Identificador del territorio. |
| `#{TERR_COD}`, `#{MUN_INE}` | Código del territorio (por ejemplo, el código INE de un municipio). |
| `#{TERR_NAME}` | Nombre del territorio. |
| `#{MUN_INES}` | Lista de códigos: el del territorio y, si la aplicación tiene **Garantizar acceso a territorios hijo**, los de sus territorios miembros. |
| `#{APP_ID}`, `#{APP_CODIGO}` | Identificador de la aplicación. |
| `#{APP_NAME}` | Nombre de la aplicación. |
| `#{PROYECCION}` | Sistema de referencia de la aplicación. |
| `#{EXTENSION_MAX_X0}`, `#{EXTENSION_MAX_Y0}`, `#{EXTENSION_MAX_X1}`, `#{EXTENSION_MAX_Y1}` | Extensión del territorio: X e Y mínimas y máximas. |
| `#{DATE}` | Fecha y hora de la petición (`dd/MM/yyyy HH:mm:ss`). |
| `#{LANG}`, `#{LANGUAGE}` | Idioma de la petición: el parámetro `lang` de la petición o, si no lo tiene, el idioma por defecto del servidor. |

Los nombres duplicados (por ejemplo `#{USUARIO}` y `#{USER_NAME}`) se mantienen por compatibilidad con SITMUN 2.

!!! warning "`#{MUN_INES}` solo dentro de `IN (...)`"
    Como es una lista, en una consulta SQL solo puede ir dentro de `IN (...)`, por ejemplo
    `WHERE codigo_ine IN (#{MUN_INES})`. En cualquier otro sitio, la prueba de la consulta se bloquea con el aviso
    «MUN_INES solo puede ir dentro de IN (...)».
