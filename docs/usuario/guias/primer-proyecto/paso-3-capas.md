# Paso 3: crear las capas

Hay dos maneras de crear capas. La primera es la más rápida cuando el servicio es WMS.

**Opción A: desde el servicio (WMS)**

1. Abre el servicio y ve a la pestaña **Capas**.
2. Pulsa **Actualizar capas del servicio** (en un servicio que aún no has guardado, el botón se llama **Obtener capas del servicio**). Aparece la lista de capas que ofrece el servidor, marcadas como **Capa no registrada**.
3. Selecciona las que quieras, pulsa **Registrar** y después **Guarda**. Se crea una capa de SITMUN por cada una, ya disponible para los clientes.

**Opción B: a mano** (menú **Capas** → **Nuevo**)

- **Nombre**: el que verá el usuario si la capa no está en un árbol (por ejemplo, en el selector de mapas de fondo).
- **Servicio**: el del [paso 2](paso-2-servicios.md).
- **Capa o capas del servicio utilizadas**: el nombre técnico de la capa en el servidor. Si pones más de una, separadas por comas, se dibujan juntas como una sola capa.
- Opcional: **Escala mínima** y **Escala máxima**, **Transparencia** (0 = opaca), si se puede consultar (GetFeatureInfo) y el **Orden** de dibujo.

**Dos comprobaciones obligatorias para cada capa:**

- [ ] La opción **Capa disponible para su uso por parte de los clientes** está activada. En una capa creada a mano aparece desactivada, y entonces el visor no la recibe.
- [ ] En la pestaña **Territorios** está el territorio del [paso 1](paso-1-territorio-rol-usuario.md). Sin esto la capa no se muestra en ese territorio.

Esto vale también para las capas que usarás como mapa de fondo en el [paso 4](paso-4-grupos-y-fondos.md).
