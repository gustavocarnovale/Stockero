from flet import *

def index():

       return View(
            "/index",
            [
                AppBar(title=Text("Index"), bgcolor=colors.SURFACE_VARIANT),
    
                ElevatedButton("Stock", on_click=lambda e: e.page.go("/stock")),
                ElevatedButton("Agregar producto", on_click=lambda e: e.page.go("/addPrd")),

                Container(
                    alignment=alignment.center,
                ),
            ],
        )

