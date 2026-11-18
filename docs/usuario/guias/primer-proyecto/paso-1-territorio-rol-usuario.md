# Paso 1: territorio, rol y usuario público

Este paso va primero porque casi todo lo demás (capas, mapas de fondo, árboles, tareas) se enlaza a un rol y a un territorio. El usuario `public` ya existe: solo hay que crear el territorio y el rol y asignárselos.

**1.1 Territorio** (menú **Territorios** → **Nuevo**)

- **Nombre**, **Código** y **Tipo** son obligatorios. Los tipos (Ayuntamiento, Diputación, Comarca...) ya existen; si falta alguno, se crea en **Sistema** → **Tipos de territorio**.
- Desactiva **Territorio bloqueado**. Un territorio nuevo aparece bloqueado por defecto.
- Rellena la **Extensión** (min X, max X, min Y, max Y; las cuatro juntas), el **CRS** (por ejemplo `EPSG:25831`) y, si quieres, el **Punto central** y el **Nivel de Zoom por defecto**. Estos valores mandan sobre los de la aplicación.

**1.2 Rol** (menú **Rol** → **Nuevo**)

- Solo hace falta el **Nombre**. Elígelo pensando en quién lo usará, por ejemplo «Rol público Ciutadella».

**1.3 Usuario público** (menú **Usuario**)

- Abre el usuario `public` (ya existe, no hay que crearlo), ve a la pestaña **Roles por Territorio**, pulsa **Añadir** y elige el rol del paso 1.2 y tu territorio.
- La columna **Rol territorial** hace que el rol valga también para los territorios hijos (por ejemplo, los municipios de una isla). Déjala desactivada si no lo necesitas.

Cada fila de **Roles por Territorio** es una llave: dice «esta persona, en este territorio, tiene este rol».
