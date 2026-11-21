// Listas de comprobación interactivas: se pueden marcar y se recuerdan
// mientras la pestaña del navegador siga abierta (sessionStorage).
function initChecklists() {
  var key = "checklist:" + location.pathname;
  var saved = {};
  try {
    saved = JSON.parse(sessionStorage.getItem(key) || "{}");
  } catch (e) {
    saved = {};
  }

  var boxes = document.querySelectorAll(".md-typeset .task-list-item input[type=checkbox]");
  boxes.forEach(function (box, i) {
    box.disabled = false;
    // El texto del paso queda fuera de la etiqueta de la casilla: se lo damos como nombre accesible.
    var item = box.closest(".task-list-item");
    if (item && !box.hasAttribute("aria-label")) {
      var text = Array.prototype.filter.call(item.childNodes, function (node) {
        return !(node.nodeType === 1 && (node.matches("label.task-list-control") || node.matches("ul, ol")));
      }).map(function (node) { return node.textContent; }).join("").replace(/\s+/g, " ").trim();
      if (text) box.setAttribute("aria-label", text);
    }
    if (Object.prototype.hasOwnProperty.call(saved, i)) {
      box.checked = saved[i];
    }
    box.addEventListener("change", function () {
      saved[i] = box.checked;
      try {
        sessionStorage.setItem(key, JSON.stringify(saved));
      } catch (e) {
        // Sin almacenamiento disponible: la marca funciona igual, pero no se recuerda.
      }
    });
  });
}

// Con navigation.instant, Material avisa de cada cambio de página mediante document$
if (typeof document$ !== "undefined") {
  document$.subscribe(initChecklists);
} else {
  document.addEventListener("DOMContentLoaded", initChecklists);
}
