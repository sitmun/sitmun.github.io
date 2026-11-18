# Paso 6: configurar las herramientas (tareas)

Cada herramienta del visor es una **tarea básica** enlazada a un control del visor. La instalación ya trae una tarea para cada control, dentro del grupo **Básico**. Normalmente no hace falta crear ninguna: solo hay que darlas al rol y al territorio.

(menú **Tarea** → **Tarea básica** → abre cada tarea que quieras)

1. Pestaña **Roles**: añade el rol del [paso 1](paso-1-territorio-rol-usuario.md).
2. Pestaña **Territorios**: añade el territorio del [paso 1](paso-1-territorio-rol-usuario.md).
3. **Guarda**.

Si falta el rol o el territorio, la herramienta no aparece en el visor.

**Herramientas mínimas para un primer proyecto:**

| Control | Para qué sirve |
| --- | --- |
| `sitna.layerCatalog` | Panel con el árbol de capas. **Sin esta tarea no se ve el árbol.** |
| `sitna.basemapSelector` | Selector de mapas de fondo. |
| `sitna.workLayerManager` | Lista de las capas encendidas. |
| `sitna.featureInfo` | Información de un punto al hacer clic en él. |
| `sitna.overviewMap` | Mapa de situación. |

Otros controles habituales: `sitna.search` (buscador) y `sitna.printMap` (impresión). Los demás tipos de tarea del menú (consulta, localizador, edición...) son para herramientas más avanzadas y quedan fuera de esta guía.
