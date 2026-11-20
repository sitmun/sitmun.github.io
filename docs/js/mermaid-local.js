/*
 * Mermaid alojado en este sitio (sin peticiones a unpkg.com).
 *
 * El tema de Zensical carga https://unpkg.com/mermaid@12/... solo si no existe
 * una variable global `mermaid`, y después llama a mermaid.initialize(config) y
 * a mermaid.render(id, texto). Este sustituto define esas dos funciones y, la
 * primera vez que se dibuja un diagrama, carga la copia local de
 * js/vendor/mermaid-12.3.0/mermaid.min.js (5,5 MB), así que las páginas sin
 * diagramas no la descargan.
 *
 * Para actualizar Mermaid: sustituye la carpeta vendor y cambia VERSION.
 */
(function () {
  var VERSION = "12.3.0";
  var src = new URL("vendor/mermaid-" + VERSION + "/mermaid.min.js",
                    document.currentScript.src).href;
  var config = null;
  var loading = null;

  function load() {
    if (!loading) {
      loading = new Promise(function (resolve, reject) {
        var script = document.createElement("script");
        script.src = src;
        script.onload = function () {
          // La copia local sustituye a este objeto en window.mermaid
          var real = window.mermaid;
          if (config) real.initialize(config);
          resolve(real);
        };
        script.onerror = reject;
        document.head.appendChild(script);
      });
    }
    return loading;
  }

  window.mermaid = {
    initialize: function (options) { config = options; },
    render: function (id, text) {
      return load().then(function (real) { return real.render(id, text); });
    }
  };
})();
