from flet import *

def index():
    
    def btn_click(e):
        lista = {inNombre: inNombre.value,inLinea: inLinea.value,inCantidad: inCantidad.value,inPrecio: inPrecio.value}
        dictGuardad = {}
        for i, k in lista.items():
            if not k:
                i.error_text = "Ingreso erroneo"
                i.autofocus = True
            else:
                dictGuardad[i.label] = k                 
        
        print(dictGuardad) if len(dictGuardad) == 4 else dictGuardad

        vista.update()
    
    inNombre = TextField(label="Producto", autofocus=True,)
    inLinea = TextField(label="Linea")
    inCantidad = TextField(label="Cantidad", input_filter = NumbersOnlyInputFilter())
    inPrecio = TextField(label="Precio",  input_filter = NumbersOnlyInputFilter() )

    vista = View(
            "/addPrd",
            horizontal_alignment = CrossAxisAlignment.CENTER,
            auto_scroll = True,
            scroll = ScrollMode.HIDDEN,
            controls = [
                AppBar(title=Text("Agregar producto"), bgcolor=colors.SURFACE_VARIANT),
                ElevatedButton("Index", on_click=lambda e: e.page.go("/index")),
                ElevatedButton(text = "Guardar", on_click=btn_click),
                Container(),
                inNombre,
                inLinea,
                inCantidad,
                inPrecio,
            ],
        )

    return vista 

