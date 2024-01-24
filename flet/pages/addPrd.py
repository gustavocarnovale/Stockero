from flet import *

def index():

    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Please enter your name"
            vista.update()
        else:
            name = txt_name.value
            vista.controls.append(Text(value=str(name)))
            vista.update()
            print(name)

    txt_name = TextField(label="Producto")

    vista = View(
            "/addPrd",
            controls = [
                AppBar(title=Text("Agregar producto"), bgcolor=colors.SURFACE_VARIANT),
                Container(),
                txt_name,
                Text(value=str("name")),
                ElevatedButton("Say hello!", on_click=btn_click),
                ElevatedButton("Index", on_click=lambda e: e.page.go("/index")),
            ],
        )

    return vista 

