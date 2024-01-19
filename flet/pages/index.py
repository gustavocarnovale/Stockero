from flet import *

def index():

       return View(
            "/index",
            [
                AppBar(title=Text("Index"), bgcolor=colors.SURFACE_VARIANT),

                ElevatedButton("Visit Store", on_click=lambda e: e.page.go("/stock")),

                Container(
                    alignment=alignment.center,
                ),
            ],
        )

