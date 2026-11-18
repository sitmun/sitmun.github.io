# Paso 8: comprobar el resultado en el visor

El administrador no tiene ningún botón para abrir el visor. Hay que abrirlo aparte, en otra pestaña del navegador.

- **Lista de aplicaciones:** `http://<servidor>/viewer/public/dashboard`. La aplicación nueva tiene que aparecer en la lista.
- **Directo al mapa:** `.../viewer/public/map/<id aplicación>/<id territorio>`. Los identificadores (id) aparecen en las listas del administrador.

En algunas instalaciones las direcciones llevan `#/` después de `/viewer` (por ejemplo `/viewer/#/public/dashboard`).

**Lista de comprobación**

- [ ] La aplicación aparece en la lista del visor.
- [ ] El mapa se abre centrado en el territorio.
- [ ] Se ve el primer mapa de fondo, y el selector de mapas de fondo muestra el resto.
- [ ] El panel de capas muestra el árbol con las carpetas y las capas.
- [ ] Las capas marcadas con **Cargar por defecto** aparecen encendidas.
- [ ] Al hacer clic en el mapa sobre una capa consultable aparece su información.
- [ ] Están las herramientas del [paso 6](paso-6-herramientas.md).

Después de cambiar algo en el administrador, vuelve a cargar el visor. Si no ves el cambio, prueba en una ventana privada: el navegador puede tener guardada la configuración antigua.
