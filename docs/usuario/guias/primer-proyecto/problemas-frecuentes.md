# Problemas frecuentes

Casi siempre que algo no aparece en el visor es porque falta un enlace: un rol, un territorio o una opción activada. El visor no muestra ningún error.

| Qué pasa | Causa probable | Dónde se corrige |
| --- | --- | --- |
| La aplicación no aparece en la lista del visor | La aplicación no tiene el rol, o el usuario no tiene ese rol en ningún territorio. Si el usuario es `public`, quizá la aplicación es privada. | Aplicación → Roles; Usuario → Roles por Territorio |
| No aparece ningún mapa de fondo | La capa de fondo no está **Activo**, no tiene el rol, o sus capas no tienen el territorio. | Capas de fondo; Capas → Territorios |
| El mapa de fondo WMTS aparece en blanco | Faltan `matrixSet` o `format`. | Servicio → Parámetros de configuración |
| No se ve el panel de capas | La tarea `sitna.layerCatalog` no tiene el rol o el territorio. | Tarea básica → Roles / Territorios |
| Una capa no aparece en el árbol | La capa no está disponible para los clientes, no tiene el territorio o no está en ningún grupo con el rol. | Capas; Permisos sobre las capas |
| El árbol aparece vacío o no aparece | El árbol no tiene el rol, o ninguno de sus nodos tiene una capa que llegue al usuario. | Árboles → Roles |
| Las capas de un servicio con **Usar proxy SITMUN** no cargan | La dirección del servidor intermediario (proxy) es incorrecta. Pasa a menudo en copias de otra instalación. | Sistema → Parámetros de configuración → `proxy` |
| El nombre de una capa o aplicación no cambia en el visor | El visor muestra la traducción del idioma, no el campo original. | Sistema → Traducciones de literales |
| Después de **Cargar desde servicio** hay nodos sin capa | Algunos nodos no quedan enlazados a la capa al guardar. | Árboles → revisa cada nodo antes y después de guardar |

Si el problema continúa, prueba primero con el usuario `public` y una aplicación no privada. Es el camino con menos enlaces.
