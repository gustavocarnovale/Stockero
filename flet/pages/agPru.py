from flet import *

def index():

    def fnContModalCerrado(e):
        contModal.open = False
        vista.update()

    contModal = AlertDialog(
        modal=True,
        title=Text("Confirmar"),
        content=Text("Do you really want to delete all those files?"),
        actions=[
            TextButton("Yes", on_click=fnContModalCerrado),
            TextButton("No", on_click=fnContModalCerrado),
        ],
        actions_alignment=MainAxisAlignment.END,
    )
    
    def fnContModalAbierto(e):
        Page.dialog = contModal
        contModal.open = True
        vista.update()

    vista = View(
            "/agPru",
            horizontal_alignment = CrossAxisAlignment.CENTER,
            auto_scroll = True,
            scroll = ScrollMode.HIDDEN,
            controls = [
                AppBar(title=Text("Pruebas"), center_title = True, bgcolor=colors.SURFACE_VARIANT, actions = [TextButton("Index", on_click=lambda e: e.page.go("/index")),]),
                #ElevatedButton("Index", on_click=lambda e: e.page.go("/index")),
                ElevatedButton("Guardar", on_click=fnContModalAbierto),
                contModal,
            ],
        )

    return vista 

