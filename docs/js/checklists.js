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
