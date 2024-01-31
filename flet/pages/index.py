from flet import *

def index():

       return View(
            "/index",
            [
                AppBar(title=Text("Index"), bgcolor=colors.SURFACE_VARIANT, actions = 
                [
                    TextButton("Stock", on_click=lambda e: e.page.go("/stock")),
                    TextButton("Agregar producto", on_click=lambda e: e.page.go("/addPrd")),
                    TextButton("Vender producto", on_click=lambda e: e.page.go("/sellPrd")),
                    TextButton("Pruebas", on_click=lambda e: e.page.go("/agPru")),
                ]),
                Container(
                    alignment=alignment.center,
                ),
            ],
        )

