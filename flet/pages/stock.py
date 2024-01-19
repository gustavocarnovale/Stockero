from flet import *
from db import fnCargaProductos, fnCargaLinea

dato = fnCargaProductos()
salida = ""

def index():

    def items():
        items = []
        for i in dato:
            items.append(
                dropdown.Option(f"{i}"),
            )
        return items

    def dropdown_changed(e):
        print(f"Dropdown changed to {confDrop.value}")
        salida = fnCargaLinea(confDrop.value)
        #confCont = Container(
        #content = Text(f"{salida}"))
        print(salida)
        return salida

    

    confDrop = Dropdown(
        on_change=dropdown_changed,
        options=items(),
    )

    #confCont = dropdown_changed(salida) if dropdown_changed(salida) is not None else ""

    return View(
            "/stock",
            [
                AppBar(title=Text("Stock"), bgcolor=colors.SURFACE_VARIANT),

                ElevatedButton("Index", on_click=lambda e: e.page.go("/index")),
                
                confDrop,
                
                #confCont,
            ],
        )

