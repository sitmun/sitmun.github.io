"""Screenshot steps, in the order they run.

Steps that create example records (connection, SQL query, locator...) run
before the steps that show them, so the script needs a fresh showcase.
"""
from __future__ import annotations

import re

from lib import GUIDE_IMG, INSTALL_IMG, Ctx, shot

def before_login(c: Ctx) -> None:
    """Runs before the script logs in.

    On a fresh install without a bootstrap admin password, the admin opens a
    first-run wizard: capture it for the install page and complete it with the
    password from --password-file. Then capture the login page for the guide.
    """
    p = c.page
    p.goto(f"{c.base}/admin/")
    p.wait_for_timeout(2500)
    if "first-run" in p.url:
        card = p.locator("mat-card").first
        card.locator("button[matsteppernext]:visible").first.click()
        p.wait_for_timeout(800)
        language = card.locator("mat-select").first
        language.click()
        p.get_by_role("option", name="Castellano").or_(p.get_by_role("option", name="Español")).first.click()
        p.wait_for_timeout(500)
        c.save("primer-acceso-idioma", card, folder=INSTALL_IMG)
        card.locator("button[matsteppernext]:visible").first.click()
        p.wait_for_timeout(800)
        fields = card.locator("input[type=password]:visible")
        fields.nth(0).fill(c.password)
        fields.nth(1).fill(c.password)
        p.wait_for_timeout(300)
        c.save("primer-acceso-contrasena", card, folder=INSTALL_IMG)
        card.get_by_role("button", name=re.compile("Guardar|Guarda")).click()
        # Saving sets the database language, which takes a while.
        p.wait_for_url(lambda url: "first-run" not in url, timeout=300000)
        p.wait_for_timeout(2000)
    # The login page, in a new session (the wizard leaves the admin signed in).
    context = p.context.browser.new_context(viewport=p.viewport_size, locale="es-ES")
    login = context.new_page()
    login.goto(f"{c.base}/admin/#/login")
    login.wait_for_selector("input[formcontrolname=username]")
    login.wait_for_timeout(1500)
    Ctx(login, c.base, c.password, c.only).save(
        "primera-entrada-login", login.locator("mat-card").first, pad=40, folder=GUIDE_IMG)
    context.close()


# Example records created through the admin interface.
CONNECTION = "Base de datos de ejemplo"
QUERY = "Patrimonio UNESCO por identificador"
LOCATOR = "Localizar patrimonio UNESCO"


def fill(c: Ctx, control: str, value: str) -> None:
    c.page.locator(f"mat-sidenav-content [formcontrolname={control}]").first.fill(value)


def type_in(c: Ctx, control: str, value: str) -> None:
    """Type into a field key by key, for fields that ignore fill() (floating label stays down)."""
    field = c.page.locator(f"mat-sidenav-content [formcontrolname={control}]").first
    field.click()
    field.press_sequentially(value, delay=20)


def choose(c: Ctx, control: str, option: str) -> None:
    c.page.locator(f"mat-sidenav-content mat-select[formcontrolname={control}]").first.click(force=True)
    c.page.get_by_role("option", name=option, exact=False).first.click()
    c.page.wait_for_timeout(300)


def save_form(c: Ctx) -> None:
    button = c.page.get_by_role("button", name="Guarda").first
    if button.is_disabled():  # nothing changed
        return
    button.click()
    c.settle(1200)


# --- Conexiones ------------------------------------------------------------------

@shot
def conexiones_formulario(c: Ctx) -> None:
    c.admin("connection/-1/connectionForm")
    fill(c, "name", CONNECTION)
    choose(c, "driver", "PostgreSQL")
    fill(c, "user", "example")
    fill(c, "newPassword", "example")
    fill(c, "url", "jdbc:postgresql://example:5432/example")
    c.page.get_by_role("button", name="Probar conexión").click()
    c.settle(1500)
    c.save("conexiones-formulario", c.content, keep_toast=True)
    save_form(c)


def confirm_dialog(c: Ctx) -> None:
    """Accept the "Peligro" confirmation some actions ask for."""
    c.page.wait_for_timeout(500)
    dialog = c.page.locator("mat-dialog-container")
    if dialog.count():
        dialog.locator("button").last.click()
        c.settle(1000)


def table_rows(c: Ctx):
    return c.page.locator("mat-sidenav-content [role=row]")


def tool(c: Ctx, icon: str):
    """A table toolbar button, by its Material icon name."""
    return c.page.locator(f"mat-sidenav-content button:visible:has(mat-icon:text-is('{icon}'))").first


# --- Servicios -------------------------------------------------------------------

SERVICE_URL = "https://ideib.caib.es/geoserveis/services/public/GOIB_NATURA_ENP_IB/MapServer/WMSServer"
# The layer whose GetFeatureInfo the "capas" step enables; later steps reuse it.
QUERYABLE_LAYER: dict[str, str] = {}


@shot
def servicios(c: Ctx) -> None:
    p = c.page
    c.admin("service/-1/serviceForm")
    c.save("servicios-formulario", c.content)

    choose(c, "type", "WMS")
    fill(c, "serviceURL", SERVICE_URL)
    details = p.get_by_role("button", name="Obtener detalles del servicio")
    details.click()
    confirm_dialog(c)
    p.wait_for_timeout(3000)
    c.highlight(p.locator("mat-form-field:has([formcontrolname=name])"),
                p.locator("mat-form-field:has([formcontrolname=description])"), details)
    c.save("servicios-obtener-detalles", p.locator("mat-sidenav-content mat-card").first)

    choose(c, "authenticationMode", "básica")
    p.wait_for_timeout(500)
    auth = p.locator("mat-sidenav-content mat-card:has([formcontrolname=authenticationMode])").first
    c.highlight(p.locator("mat-form-field:has([formcontrolname=authenticationMode])"),
                p.locator("mat-slide-toggle[formcontrolname=isProxied]"))
    c.save("servicios-autenticacion", auth)
    choose(c, "authenticationMode", "Ninguno")

    # In 1.3.0, layers fetched before the service is first saved are not
    # created, so save the service first and register layers afterwards.
    save_form(c)
    p.wait_for_url("**/service/*/serviceForm", timeout=15000)
    c.tab("Capas")
    p.get_by_role("button", name="Actualizar capas del servicio").click()
    confirm_dialog(c)
    p.wait_for_timeout(4000)
    c.save("servicios-obtener-capas", c.content)

    unregistered = p.locator("mat-sidenav-content [role=row]:has([title='Capa no registrada'])")
    for i in range(3):
        unregistered.nth(i).locator("input[type=checkbox]").check()
    c.highlight(tool(c, "add_circle_outline"))
    c.save("servicios-seleccionar-capas", c.content)
    tool(c, "add_circle_outline").click()
    c.settle(800)
    c.save("servicios-capas-pendientes", c.content)
    save_form(c)
    c.tab("Capas")
    c.save("servicios-capas-registradas", c.content)

    # Remove one registered layer.
    registered = p.locator("mat-sidenav-content [role=row]:not(:has([title='Capa no registrada'])):has(input[type=checkbox])")
    registered.nth(1).locator("input[type=checkbox]").check()
    tool(c, "delete").click()
    confirm_dialog(c)
    c.page.wait_for_timeout(500)
    c.highlight(p.locator("mat-sidenav-content [role=row]:has([title='Pendiente eliminar'])"))
    c.save("servicios-quitar-capa", c.content)
    save_form(c)
    c.tab("Capas")
    c.save("servicios-capas-registradas-2", c.content)


@shot
def servicios_monitorizacion_uso(c: Ctx) -> None:
    c.admin("service/16/serviceForm")
    c.tab("Monitorización")
    c.page.wait_for_timeout(1500)
    c.save("servicios-monitorizacion", c.content)
    c.tab("Uso")
    c.page.wait_for_timeout(1500)
    c.save("servicios-uso", c.content)


def search(c: Ctx, text: str) -> None:
    box = c.page.locator("mat-sidenav-content input").first
    box.click()
    box.press_sequentially(text, delay=20)
    box.press("Enter")
    c.settle(1000)


def layer_of_new_service(c: Ctx) -> str:
    """Open the layers list filtered to the service created above; return a layer's form route."""
    c.admin("layers")
    search(c, "Zonificació PORN Paratge")
    return c.page.locator("mat-sidenav-content [role=row] a").first.get_attribute("href").lstrip("#/")


# --- Capas -----------------------------------------------------------------------

@shot
def capas(c: Ctx) -> None:
    p = c.page
    c.admin("layers")
    search(c, "Zonificació PORN")
    c.save("capas-lista", c.content)

    c.admin("layers/-1/layersForm")
    c.save("capas-formulario", c.content)

    c.admin(layer_of_new_service(c))
    QUERYABLE_LAYER["name"] = p.locator("mat-sidenav-content input[formcontrolname=name]").first.input_value()
    toggle = p.locator("mat-slide-toggle[formcontrolname=queryableFeatureEnabled]")
    toggle.scroll_into_view_if_needed()
    if toggle.locator("button[aria-checked=false]").count():
        toggle.locator("button").click()
    c.highlight(toggle)
    c.save("basicas-feature-info-capa", c.content)
    save_form(c)

    c.tab("Permisos")
    tool(c, "add_circle_outline").click()
    c.settle(800)
    dialog = p.locator("mat-dialog-container")
    dialog.locator("[role=row]:has-text('Permisos - ide_ib') input[type=checkbox]").check()
    c.save("permisos-anadir", dialog)
    dialog.locator("button:has(mat-icon:text-is('add_circle_outline'))").click()
    c.settle(800)
    c.highlight(p.locator("mat-sidenav-content [role=row]:has-text('Permisos - ide_ib')"))
    c.save("permisos-desde-capa", c.content)
    save_form(c)


@shot
def capas_de_fondo(c: Ctx) -> None:
    c.admin("backgroundLayers/1/backgroundLayersForm")
    c.highlight(c.page.locator("mat-slide-toggle[formcontrolname=active]"))
    c.save("capas-fondo-formulario", c.content)


@shot
def permisos(c: Ctx) -> None:
    c.admin("layersPermits/-1/layersPermitsForm")
    fill(c, "name", "Espacios naturales protegidos")
    choose(c, "type", "Grupo de cartografía")
    c.save("permisos-formulario", c.content)
    c.admin("layersPermits/18/layersPermitsForm")
    c.tab("Capas")
    c.save("permisos-pestana-capas", c.content)


# --- Árboles ---------------------------------------------------------------------

@shot
def arboles(c: Ctx) -> None:
    p = c.page
    c.admin("trees/-1/treesForm")
    fill(c, "name", "Espacios naturales")
    choose(c, "type", "Cartograf")
    c.save("arboles-formulario", c.content)

    c.tab("Estructura del árbol")
    folder_btn = p.locator("mat-sidenav-content button:has(mat-icon:text-is('folder'))").first
    folder_btn.click()
    c.settle(600)
    c.highlight(folder_btn)
    c.save("arboles-crear-carpeta", c.content)

    node_panel = p.locator("mat-sidenav-content mat-card:has(mat-expansion-panel)").first
    tree_panel = p.locator("mat-sidenav-content mat-card:has(mat-tree)").first
    node_panel.locator("input[formcontrolname=name]").fill("Espacios protegidos")
    node_save = node_panel.locator("button:has(mat-icon:text-is('save'))")
    c.highlight(node_save)
    c.save("arboles-guardar-carpeta", node_panel)
    node_save.click()
    c.settle(800)

    folder_row = p.locator("mat-tree-node:visible").filter(has_text="Espacios protegidos").first
    folder_row.hover()
    p.wait_for_timeout(400)
    add_layer = folder_row.locator("button[aria-label='Cartografía']")
    add_folder = folder_row.locator("button[aria-label='Carpeta']")
    c.highlight(add_layer, add_folder)
    c.save("arboles-anadir-elementos", tree_panel)
    c.clear_highlights()

    add_layer.click(force=True)
    c.settle(800)
    node_panel.locator("input[formcontrolname=name]").fill("Zonificación PORN")
    node_panel.locator("mat-expansion-panel-header:has-text('Configuración de cartografía')").click()
    p.wait_for_timeout(500)
    carto = node_panel.locator("input[formcontrolname=cartography]")
    carto.click()
    carto.press_sequentially("Zonificació", delay=30)
    p.wait_for_timeout(1500)
    c.highlight(p.locator("mat-form-field:has(input[formcontrolname=cartography])"))
    c.save("arboles-nodo-cartografia", c.content)
    p.get_by_role("option").filter(has_text=QUERYABLE_LAYER.get("name", "Zonificació")).first.click()
    p.wait_for_timeout(500)

    node_panel.locator("mat-expansion-panel-header:has-text('Opciones de visualización')").click()
    p.wait_for_timeout(600)
    queryable = node_panel.locator("mat-slide-toggle[formcontrolname=queryableActive]")
    queryable.scroll_into_view_if_needed()
    queryable.locator("button").click()
    c.highlight(queryable)
    c.save("basicas-feature-info-arbol",
           node_panel.locator("mat-expansion-panel:has-text('Opciones de visualización')"))


# Role and territory of the showcase app "Camí de Cavalls", used by the MIA below:
# a MIA and the tasks it includes must all be granted to show in the viewer.
MIA_ROLE = "Camí de cavalls - públic"
MIA_TERRITORY = "Menorca"


def grant(c: Ctx, role: str = MIA_ROLE, territory: str = MIA_TERRITORY) -> None:
    """Add a role and a territory on the Roles and Territorios tabs of a task."""
    for tab, name in (("Roles", role), ("Territorios", territory)):
        c.tab(tab)
        c.page.wait_for_timeout(600)
        tool(c, "add_circle_outline").click()
        c.settle(600)
        dialog = c.page.locator("mat-dialog-container")
        box = dialog.locator("input:not([type=checkbox])").first
        box.click()
        box.press_sequentially(name, delay=20)
        c.page.wait_for_timeout(800)
        dialog.locator("[role=row]").filter(has_text=name).first.locator("input[type=checkbox]").check()
        dialog.locator("button:has(mat-icon:text-is('add_circle_outline'))").click()
        c.settle(600)


# --- Consulta SQL ------------------------------------------------------------------

SQL = "SELECT nom_cast AS nombre, dstipus AS tipo, url, etrs89x, etrs89y\nFROM dbo.pa007his_unesco\nWHERE gid = {}"


def choose_first(c: Ctx, control: str, scope: str = "mat-sidenav-content") -> None:
    c.page.locator(f"{scope} mat-select[formcontrolname={control}]").first.click(force=True)
    options = c.page.get_by_role("option")
    options.first.click()
    c.page.wait_for_timeout(300)


def set_sql(c: Ctx, text: str) -> None:
    """Replace the text of the SQL editor (CodeMirror over a hidden textarea)."""
    editor = c.page.locator("mat-sidenav-content [data-testid=sql-editor] [contenteditable=true]").first
    editor.click()
    c.page.keyboard.press("ControlOrMeta+a")
    c.page.keyboard.press("Delete")
    c.page.keyboard.insert_text(text)
    c.page.wait_for_timeout(300)


@shot
def consulta(c: Ctx) -> None:
    p = c.page
    c.admin("taskQuery/-1/5")
    fill(c, "name", QUERY)
    choose(c, "scope", "SQL Query")
    choose_first(c, "taskGroupId")
    c.save("consulta-formulario", c.content)

    choose(c, "connectionId", CONNECTION)
    set_sql(c, SQL.format(1))
    c.highlight(p.locator("mat-form-field:has([formcontrolname=connectionId])"),
                p.locator("mat-form-field:has([formcontrolname=command])"))
    c.save("consulta-sql", c.content)

    c.tab("Parámetros")
    p.wait_for_timeout(600)
    c.highlight(tool(c, "add_circle_outline"))
    c.save("consulta-pestana-parametros", c.content)
    tool(c, "add_circle_outline").click()
    c.settle(600)
    dialog = p.locator("mat-dialog-container")
    dialog.locator("[formcontrolname=name]").fill("ID")
    dialog.locator("[formcontrolname=label]").fill("Identificador del bien")
    dialog.locator("mat-select[formcontrolname=dataType]").click(force=True)
    p.get_by_role("option", name="integer", exact=True).click()
    p.wait_for_timeout(300)
    c.save("consulta-anadir-parametro", dialog)
    dialog.locator("button:has(mat-icon:text-is('add_circle_outline'))").click()
    c.settle(600)

    c.tab("Información general")
    set_sql(c, SQL.format("${ID}"))
    c.highlight(p.locator("mat-form-field:has([formcontrolname=command])"))
    c.save("consulta-sql-parametro", c.content)
    grant(c)
    save_form(c)


@shot
def conexiones_pestana_tareas(c: Ctx) -> None:
    c.admin("connection")
    search(c, CONNECTION)
    c.page.locator("mat-sidenav-content [role=row] a").first.click()
    c.settle()
    c.tab("Tareas")
    c.page.wait_for_timeout(1000)
    c.save("conexiones-pestana-tareas", c.content)


# --- Localizador ---------------------------------------------------------------------

@shot
def localizador(c: Ctx) -> None:
    p = c.page
    c.admin("tasks/-1/4")
    fill(c, "name", LOCATOR)
    choose(c, "taskGroupId", "Básico")
    query = p.locator("mat-sidenav-content input[aria-autocomplete]").first
    query.click()
    query.press_sequentially(QUERY[:10], delay=30)
    p.get_by_role("option", name=QUERY).first.click()
    p.wait_for_timeout(500)
    c.save("localizador-general", c.content)

    c.tab("Configuración del geocodificador")
    p.wait_for_timeout(600)
    fill(c, "geocoderLabelField", "nombre")
    fill(c, "geocoderSrs", "EPSG:4326")
    fill(c, "geocoderLatField", "etrs89y")
    fill(c, "geocoderLonField", "etrs89x")
    c.highlight(*[p.locator(f"mat-form-field:has([formcontrolname={name}])") for name in
                  ("geocoderLabelField", "geocoderSrs", "geocoderLatField", "geocoderLonField")])
    c.save("localizador-configuracion", c.content)
    save_form(c)


# --- Plantillas ------------------------------------------------------------------------

TEMPLATE = "Ficha de patrimonio UNESCO"
TEMPLATE_HTML = """<h3>Patrimonio de la Humanidad</h3>
<table data-sitmun-each="patrimonio.rows">
  <tbody>
    <tr>
      <th>Nombre</th>
      <th>Tipo</th>
      <th>Más información</th>
    </tr>
    <tr>
      <td>{{nombre}}</td>
      <td>{{tipo}}</td>
      <td><a href="{{url}}">{{url}}</a></td>
    </tr>
  </tbody>
</table>"""


@shot
def plantillas(c: Ctx) -> None:
    p = c.page
    c.admin("tasks/-1/15")
    fill(c, "name", TEMPLATE)
    choose(c, "taskGroupId", "Básico")
    c.save("plantilla-general", c.content)

    c.tab("Fuentes")
    p.wait_for_timeout(600)
    body = p.locator("mat-sidenav-content mat-tab-body.mat-mdc-tab-body-active")
    sources = body.locator("mat-card").first
    add = body.locator("input").first
    add.click()
    add.press_sequentially(QUERY[:10], delay=30)
    p.wait_for_timeout(1200)
    c.save("plantilla-seleccionar-consulta", c.content)
    p.get_by_role("option").filter(has_text=QUERY).filter(has_text="Consulta SQL").last.click()
    p.wait_for_timeout(1200)

    reference = sources.locator("[role=row], tr").filter(has_text=QUERY).locator("input").first
    reference.fill("patrimonio")
    sources.locator("button:has(mat-icon:text-is('check'))").first.click()
    p.wait_for_timeout(600)
    c.highlight(reference.locator("xpath=ancestor::mat-form-field[1]"))
    c.save("plantilla-referencia", sources)

    card = body.locator("mat-card").filter(has_text="Referencia HTML").first
    card.locator("input").last.fill("1")
    card.get_by_role("button", name="Ejecutar").click()
    p.wait_for_timeout(3000)
    c.save("plantilla-probar-consulta", card)

    c.tab("Plantilla")
    p.wait_for_timeout(800)
    p.locator("mat-sidenav-content button:has(mat-icon:text-is('code'))").first.click()
    p.wait_for_timeout(500)
    p.locator("mat-sidenav-content textarea.template-editor-source").fill(TEMPLATE_HTML)
    p.wait_for_timeout(500)
    c.save("plantilla-editor-html", c.content)
    p.locator("mat-sidenav-content button:has(mat-icon:text-is('wysiwyg'))").first.click()
    p.wait_for_timeout(800)
    c.save("plantilla-editor-visual", c.content)

    c.tab("Parámetros")
    p.wait_for_timeout(600)
    tool(c, "add_circle_outline").click()
    c.settle(600)
    dialog = p.locator("mat-dialog-container")
    dialog.locator("[formcontrolname=name]").fill("ID")
    dialog.locator("[formcontrolname=value]").fill("1")
    dialog.locator("button:has(mat-icon:text-is('add_circle_outline'))").click()
    c.settle(600)
    c.save("plantilla-parametros", c.content)
    grant(c)
    save_form(c)


# --- Más información avanzada (MIA) --------------------------------------------------

# The showcase app "Camí de Cavalls" already shows this layer as queryable, so a
# MIA with its role and territory appears in that app's viewer.
MIA = "Patrimonio UNESCO"
MIA_LAYER = "Monumentos de la Menorca Talayótica (UNESCO)"


def add_task(c: Ctx, name: str, kind: str):
    """Pick a task in the "Añadir tarea" field of a MIA; returns the field."""
    add = c.page.locator("mat-sidenav-content mat-form-field:has-text('Añadir tarea') input").first
    add.click()
    add.press_sequentially(name[:10], delay=30)
    c.page.wait_for_timeout(1500)
    return add


def map_parameter(c: Ctx, mia_param: str, child_param: str) -> None:
    c.page.locator("mat-sidenav-content button:has-text('Añadir')").first.click()
    c.page.wait_for_timeout(500)
    selects = c.page.locator("mat-sidenav-content mat-select:not([formcontrolname])")
    for select, option in ((selects.nth(0), mia_param), (selects.nth(1), child_param)):
        select.click(force=True)
        c.page.get_by_role("option", name=option, exact=True).click()
        c.page.wait_for_timeout(300)
    c.page.keyboard.press("Escape")


@shot
def visor_mia_campos_gfi(c: Ctx) -> None:
    """The layer's GetFeatureInfo fields, before a MIA takes over the click."""
    click_monument(c)
    popup = c.page.locator(".tc-ctl-popup.tc-visible").first
    c.mark(popup.locator("tr").filter(has_text="gid").first)
    box = popup.bounding_box()
    c.save("mia-campos-gfi", clip={"x": box["x"], "y": box["y"], "width": box["width"],
                                   "height": min(box["height"], 300)})


@shot
def mia(c: Ctx) -> None:
    p = c.page
    c.admin("tasks/-1/16")
    fill(c, "name", MIA)
    choose(c, "taskGroupId", "Básico")
    carto = p.locator("mat-sidenav-content mat-form-field:has-text('Cartografía utilizada') input").first
    carto.click()
    carto.press_sequentially("UNESCO", delay=30)
    p.get_by_role("option", name=MIA_LAYER).click()
    p.wait_for_timeout(500)
    c.highlight(carto.locator("xpath=ancestor::mat-form-field[1]"))
    c.save("mia-general", c.content)

    # In 1.3.0 the mapping only offers MIA parameters that are already saved.
    c.tab("Parámetros")
    p.wait_for_timeout(600)
    tool(c, "add_circle_outline").click()
    c.settle(600)
    dialog = p.locator("mat-dialog-container")
    dialog.locator("[formcontrolname=label]").fill("Identificador")
    dialog.locator("[formcontrolname=value]").fill("gid")
    dialog.locator("[formcontrolname=description]").fill("Atributo gid del GetFeatureInfo")
    dialog.locator("button:has(mat-icon:text-is('add_circle_outline'))").click()
    c.settle(600)
    c.save("mia-parametros", c.content)
    save_form(c)

    c.tab("Información general")
    p.wait_for_timeout(600)
    add_task(c, QUERY, "query")
    c.save("mia-anadir-tarea", c.content)
    p.get_by_role("option").filter(has_text=QUERY).filter(has_text="query").last.click()
    p.wait_for_timeout(1000)

    map_parameter(c, "Identificador", "Identificador del bien")
    c.highlight(p.locator("mat-sidenav-content mat-select:not([formcontrolname])").nth(0),
                p.locator("mat-sidenav-content mat-select:not([formcontrolname])").nth(1))
    c.save("mia-mapeo", c.content)
    grant(c)
    save_form(c)


# --- Visor: tareas básicas -------------------------------------------------------------

# The SDI Viewer ("Visualizador IDE") of the showcase, territory Islas Baleares.
SDI_APP, SDI_TERRITORY = 1, 2
SDI_ROLE = "Visualitzador IDE - Illes Balears"
SDI_TERRITORY_NAME = "Islas Baleares"
# Seeded basic tasks that no showcase role grants; the manual shows them all.
# Names are in Spanish because the first-run wizard sets Castellano as the
# database language (before_login).
UNGRANTED_CONTROLS = ("Descarga", "Medir", "Barra de escala", "Buscar", "Vista 3D")


@shot
def visor_controles(c: Ctx) -> None:
    """Grant the remaining seeded controls to the SDI Viewer (setup, no images)."""
    for name in UNGRANTED_CONTROLS:
        c.admin("tasksBasic")
        search(c, name)
        c.page.locator("mat-sidenav-content [role=row]").get_by_role("link", name=name, exact=True).first.click()
        c.settle()
        grant(c, SDI_ROLE, SDI_TERRITORY_NAME)
        save_form(c)


LEFT_BAR = {"x": 0, "y": 116, "width": 420, "height": 510}
PALMA = (2.6502, 39.5696)
BOTTOM_RIGHT = {"x": 1000, "y": 780, "width": 440, "height": 220}


def panel(c: Ctx, button_title: str) -> None:
    """Open a side panel of the viewer from its toolbar button."""
    c.page.locator(f"[title='{button_title}']:visible").first.click()
    c.page.wait_for_timeout(1200)


def expand(c: Ctx, ctl: str):
    """Expand a collapsible SITNA control by clicking its header; return the control."""
    control = c.page.locator(f".{ctl}:visible").first
    header = control.locator("h2").first
    if "tc-collapsed" in (control.get_attribute("class") or ""):
        header.click()
        c.page.wait_for_timeout(800)
    return control


@shot
def visor_basicas(c: Ctx) -> None:
    p = c.page
    c.map(SDI_APP, SDI_TERRITORY)
    c.center(*PALMA, 20)

    c.mark(p.locator(".tc-ctl-nav").first)
    c.save("basicas-navigation-bar", clip=LEFT_BAR)
    c.mark(p.locator(".tc-ctl-fscreen-btn").first)
    c.save("basicas-full-screen", clip=LEFT_BAR)
    c.mark(p.locator(".tc-ctl-3d-btn").first)
    c.save("basicas-3d", clip=LEFT_BAR)
    c.mark(p.locator(".tc-ctl-scl").first)
    c.save("basicas-scale", clip=BOTTOM_RIGHT)
    # In 1.3.0 the scale covers the scale bar when an app has both controls;
    # hide the scale to show what an app with only the scale bar displays.
    p.evaluate("document.querySelector('.tc-ctl-scl').style.visibility = 'hidden'")
    c.mark(p.locator(".tc-ctl-sb").first)
    c.save("basicas-scale-bar", clip=BOTTOM_RIGHT)
    p.evaluate("document.querySelector('.tc-ctl-scl').style.visibility = ''")

    c.center(2.95, 39.62, 150)
    p.locator("h1[title='Mapa situación']").click()
    p.wait_for_timeout(8000)
    c.mark(p.locator(".tc-ctl-ovmap").first)
    c.save("basicas-overview-map", clip={"x": 900, "y": 560, "width": 540, "height": 440})


RIGHT_PANEL = {"x": 900, "y": 64, "width": 540, "height": 600}


def open_section(c: Ctx, ctl: str) -> None:
    """Expand a section of the layers panel (background maps, loaded layers...)."""
    section = c.page.locator(f".tc-right-panel .{ctl}").first
    if "tc-collapsed" in (section.get_attribute("class") or ""):
        section.locator("h2").first.click()
        c.page.wait_for_timeout(1500)


def load_first_layer(c: Ctx, folder_name: str) -> None:
    """Expand a catalog folder down to its first layer and load that layer."""
    folder = c.page.locator(".tc-ctl-lcat li.tc-ctl-lcat-node").filter(has_text=folder_name).first
    leaf = folder.locator("li.tc-ctl-lcat-leaf:visible")
    for _ in range(6):
        if leaf.count():
            break
        folder.locator("li.tc-collapsed:visible > button.tc-ctl-lcat-collapse-btn, "
                       ":scope.tc-collapsed > button.tc-ctl-lcat-collapse-btn").first.click()
        c.page.wait_for_timeout(600)
    leaf.first.locator("input.sitmun-lcat-leaf-load").click()
    c.page.wait_for_timeout(4000)


@shot
def visor_capas(c: Ctx) -> None:
    p = c.page
    c.map(SDI_APP, SDI_TERRITORY)
    c.center(*PALMA, 20)
    p.locator("h1.tc-panel-tab[title='Capas']").click()
    p.wait_for_timeout(1500)

    open_section(c, "tc-ctl-bms")
    c.save("aplicacion-selector-fondos", p.locator(".tc-right-panel .tc-ctl-bms").first)
    c.mark(p.locator(".tc-right-panel .tc-ctl-bms").first)
    c.save("basicas-basemap-selector", clip=RIGHT_PANEL)
    p.locator(".tc-right-panel .tc-ctl-bms h2").first.click()
    p.wait_for_timeout(800)

    c.mark(p.locator(".tc-right-panel .tc-ctl-lcat").first)
    c.save("basicas-layer-catalog", clip=RIGHT_PANEL)

    load_first_layer(c, "Espacios de relevancia ambiental")
    open_section(c, "tc-ctl-wlm")
    c.mark(p.locator(".tc-right-panel .tc-ctl-wlm").first)
    c.save("basicas-work-layer-manager", clip=RIGHT_PANEL)

    c.mark(p.locator(".tc-right-panel .tc-ctl-tctr-datldr").first)
    c.save("basicas-data-loader", clip={"x": 900, "y": 740, "width": 540, "height": 260})

    # basicas-legend: not retaken; the 1.3.0 legend panel stays empty (sitmun/sitmun#375).


LEFT_PANEL = {"x": 0, "y": 64, "width": 620, "height": 560}


def tool_panel(c: Ctx, ctl: str):
    """Expand one tool of the left tools panel; return it."""
    tool = c.page.locator(f".tc-left-panel .{ctl}").first
    if "tc-collapsed" in (tool.get_attribute("class") or ""):
        tool.locator("h2").first.click()
        c.page.wait_for_timeout(1200)
    return tool


def collapse(c: Ctx, tool) -> None:
    if "tc-collapsed" not in (tool.get_attribute("class") or ""):
        tool.locator("h2").first.click()
        c.page.wait_for_timeout(600)


@shot
def visor_herramientas(c: Ctx) -> None:
    p = c.page
    c.map(SDI_APP, SDI_TERRITORY)
    c.center(*PALMA, 20)
    p.mouse.click(40, 148)  # tools button
    p.wait_for_timeout(1500)

    for ctl, name in (("tc-ctl-download", "basicas-download"),
                      ("tc-ctl-dmm", "basicas-draw-measure"),
                      ("tc-ctl-share", "basicas-share"),
                      ("tc-ctl-prnmap", "basicas-print-dialogo")):
        tool = tool_panel(c, ctl)
        if ctl == "tc-ctl-download":
            tool.get_by_text("Imagen del mapa").click()
            p.wait_for_timeout(800)
        c.mark(tool)
        c.save(name, clip=LEFT_PANEL)
        if ctl == "tc-ctl-prnmap":
            tool.get_by_role("button", name="Imprimir").click()
            p.wait_for_timeout(10000)
            c.save("basicas-print-vista", clip={"x": 180, "y": 64, "width": 1080, "height": 730})
            p.keyboard.press("Escape")
            p.locator(".tc-modal-close:visible, [title='Cerrar']:visible").first.click()
            p.wait_for_timeout(800)
        collapse(c, tool)

    measure = tool_panel(c, "tc-ctl-meas")
    measure.get_by_text("Longitud").first.click()
    p.wait_for_timeout(500)
    for x, y in ((560, 420), (760, 520)):
        p.mouse.click(x, y)
        p.wait_for_timeout(400)
    p.mouse.dblclick(900, 470)
    p.wait_for_timeout(1000)
    c.mark(measure)
    c.save("basicas-measure", clip={"x": 0, "y": 64, "width": 1100, "height": 700})


@shot
def visor_informacion(c: Ctx) -> None:
    # basicas-search: not retaken; search finds nothing in 1.3.0 (sitmun/sitmun#352).
    p = c.page
    c.map(SDI_APP, SDI_TERRITORY)
    p.locator("h1.tc-panel-tab[title='Capas']").click()
    p.wait_for_timeout(1500)
    load_first_layer(c, "Cubiertas del suelo")
    p.locator("h1.tc-panel-tab[title='Capas']").click()  # close the panel
    p.wait_for_timeout(800)
    point = c.center(2.70, 39.62, 10)
    p.mouse.click(point["x"], point["y"])
    p.wait_for_timeout(5000)
    popup = p.locator(".tc-ctl-finfo:visible, .tc-ctl-popup:visible").first
    c.mark(popup)
    box = popup.bounding_box()
    c.save("basicas-feature-info-resultado",
           clip={"x": max(box["x"] - 200, 0), "y": max(box["y"] - 120, 64),
                 "width": box["width"] + 400, "height": box["height"] + 320})


# --- Visor: resultado del MIA -----------------------------------------------------------

MIA_APP, MIA_APP_TERRITORY = 2, 3
TORRE_GALMES = (4.1158390045166, 39.9029197130127)  # gid 1 in dbo.pa007his_unesco


def click_monument(c: Ctx) -> None:
    p = c.page
    c.map(MIA_APP, MIA_APP_TERRITORY)
    p.locator("h1.tc-panel-tab[title='Capas']").click()
    p.wait_for_timeout(1500)
    folder = p.locator(".tc-ctl-lcat li.tc-ctl-lcat-node").filter(has_text="Puntos de interés").first
    folder.locator(":scope > button.tc-ctl-lcat-collapse-btn").click()
    p.wait_for_timeout(800)
    folder.locator("li.tc-ctl-lcat-leaf").filter(has_text="Talayótica").locator("input.sitmun-lcat-leaf-load").click()
    p.wait_for_timeout(3000)
    p.locator("h1.tc-panel-tab[title='Capas']").click()
    p.wait_for_timeout(800)
    point = c.center(*TORRE_GALMES, 2)
    p.mouse.click(point["x"], point["y"])
    p.wait_for_timeout(8000)


MIA_PANEL = ".sitmun-mia-popup-overlay.sitmun-mia-popup-visible"


@shot
def visor_mia(c: Ctx) -> None:
    click_monument(c)
    c.save("mia-resultado-tabla", clip={"x": 560, "y": 64, "width": 880, "height": 560})


@shot
def mia_plantilla(c: Ctx) -> None:
    """Replace the MIA's query with the template that formats its result."""
    p = c.page
    # Open it from the list: after the first save the form's URL keeps the "-1"
    # of a new task, so it does not give the new id.
    c.admin("tasksMoreInfoAdvanced")
    search(c, MIA)
    p.locator("mat-sidenav-content [role=row]").get_by_role("link", name=MIA, exact=True).last.click()
    c.settle()
    p.locator("mat-sidenav-content button:has(mat-icon:text-is('delete')):visible").first.click()
    confirm_dialog(c)
    add_task(c, TEMPLATE, "template")
    p.get_by_role("option").filter(has_text=TEMPLATE).filter(has_text="template").last.click()
    p.wait_for_timeout(1000)
    map_parameter(c, "Identificador", "ID")
    selects = p.locator("mat-sidenav-content mat-select:not([formcontrolname])")
    c.highlight(selects.nth(0), selects.nth(1))
    c.save("mia-mapeo-plantilla", c.content)
    save_form(c)


@shot
def visor_mia_plantilla(c: Ctx) -> None:
    click_monument(c)
    c.save("mia-resultado-plantilla", clip={"x": 560, "y": 64, "width": 880, "height": 560})


# --- General y aplicaciones ----------------------------------------------------------------

@shot
def general_traducciones(c: Ctx) -> None:
    p = c.page
    c.admin(f"application/{MIA_APP}/applicationForm")
    button = p.locator("mat-sidenav-content mat-form-field:has(input[formcontrolname=name]) mat-icon.iconTranslate").first
    c.save("general-icono-traducciones", button, pad=12)
    button.click()
    c.settle(800)
    c.save("general-formulario-traducciones", p.locator("mat-dialog-container").first)
    p.keyboard.press("Escape")
    p.wait_for_timeout(500)


@shot
def general_visor_idiomas(c: Ctx) -> None:
    for language, name in (("ca", "general-visor-catalan"), ("es", "general-visor-castellano")):
        c.viewer("public/dashboard", language)
        c.page.wait_for_timeout(1500)
        c.save(name, clip={"x": 0, "y": 0, "width": 1440, "height": 560})


@shot
def aplicacion_mantenimiento(c: Ctx) -> None:
    """Put the SDI Viewer in maintenance, show its card, and take it out again."""
    p = c.page

    def set_maintenance(on: bool) -> None:
        c.admin(f"application/{SDI_APP}/applicationForm")
        toggle = p.locator("mat-slide-toggle[formcontrolname=isUnavailable]")
        if (toggle.locator("button").get_attribute("aria-checked") == "true") != on:
            toggle.locator("button").click()
            save_form(c)

    set_maintenance(True)
    try:
        c.viewer("public/dashboard")
        p.wait_for_timeout(1500)
        card = p.locator("mat-card").filter(has_text="Visualizador IDE").first
        c.save("aplicacion-mantenimiento", card, pad=8)
    finally:
        set_maintenance(False)


# --- Guía "Primer proyecto" ---------------------------------------------------------------
# Steps that only show existing forms reuse the manual's images; these are the rest.

@shot
def guia_primer_proyecto(c: Ctx) -> None:
    p = c.page
    c.admin("dashboard")
    c.save("primera-entrada-cuadro-mando", folder=GUIDE_IMG)

    c.admin("territory/-1/territoryForm")
    type_in(c, "name", "Ayuntamiento de ejemplo")
    type_in(c, "code", "99999")
    choose(c, "typeId", "Ayuntamiento")
    c.save("paso-1-territorio", c.content, folder=GUIDE_IMG)

    c.admin("role/-1/roleForm")
    type_in(c, "name", "Visor público")
    c.save("paso-1-rol", c.content, folder=GUIDE_IMG)

    c.admin("user/2/userForm")  # the seeded "public" user
    c.save("paso-1-usuario-public", c.content, folder=GUIDE_IMG)

    c.admin("tasksBasic")
    search(c, "Pantalla completa")
    p.locator("mat-sidenav-content [role=row]").get_by_role("link", name="Pantalla completa", exact=True).first.click()
    c.settle()
    c.tab("Roles")
    p.wait_for_timeout(800)
    c.save("paso-6-tarea-roles", c.content, folder=GUIDE_IMG)

    c.admin(f"application/{SDI_APP}/applicationForm")
    c.save("paso-7-aplicacion", c.content, folder=GUIDE_IMG)
    c.tab("Mapas de fondo")
    p.wait_for_timeout(800)
    c.save("paso-7-aplicacion-fondos", c.content, folder=GUIDE_IMG)

    c.map(SDI_APP, SDI_TERRITORY)
    c.save("paso-8-visor", folder=GUIDE_IMG)
