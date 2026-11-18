# Paso 5: construir el árbol de capas

El árbol es lo que el usuario ve en el panel de capas: carpetas que contienen capas. Una capa solo aparece en el árbol si el usuario ya tiene acceso a ella por el [paso 4](paso-4-grupos-y-fondos.md).

(menú **Árboles** → **Nuevo**)

1. **Nombre** y **Tipo** = **Cartografía**.
2. Pestaña **Estructura del árbol**:
    - Añade una carpeta de primer nivel con el botón **Carpeta**. En el primer nivel solo puede haber carpetas.
    - Dentro de una carpeta puedes añadir más carpetas o capas. Una capa no puede tener hijos.
    - En cada nodo de capa, elige en **Cartografía** la capa del [paso 3](paso-3-capas.md). El **Nombre** del nodo es lo que leerá el usuario (hasta 80 caracteres).
3. Opciones de cada nodo: **Visible**, **Cargar por defecto** (la capa aparece encendida al abrir el mapa), **Consultable (GetFeatureInfo)** (clic en el mapa para ver su información) y, en carpetas, **Modo selección única** (solo una capa encendida a la vez).
4. Pestaña **Roles**: añade el rol del [paso 1](paso-1-territorio-rol-usuario.md). Sin rol, el árbol no llega a nadie.
5. **Guarda**. Los cambios en la estructura no se guardan hasta aquí.

**Atajo:** el botón **Cargar desde servicio** de la estructura crea las carpetas y las capas a partir de la organización del servicio WMS. Revisa el resultado antes de guardar: cada nodo tiene que quedar enlazado a una capa de SITMUN.

El árbol se enlaza a la aplicación en el [paso 7](paso-7-aplicacion.md).
