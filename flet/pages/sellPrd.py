from flet import *
from db import fnOperacionProducto, fnLower

def index():

    dictGuardad = {}   
    
    contModal = AlertDialog(
                modal=True,
                title=Text("Confirmar"),
                actions=[],
                actions_alignment=MainAxisAlignment.END,
            )

    def fnContModalCerrado(e):
        contModal.open = False
        vista.controls.clear()
        list(map(lambda x: vista.controls.append(x),listaObj)) ### ARMA VISTA ###  
        vista.update()

    def fnGuardaProducto(e):
        datosVenta = fnLower(dictGuardad)        
        vista.controls.clear()
        contModal.open = False
        list(map(lambda x: vista.controls.append(x),listaObj)) ### ARMA VISTA ###  
        fnOperacionProducto(datosVenta, op = 0)
        vista.update()
    
    def btn_click(e):
        lista = {inNombre: inNombre.value,inLinea: inLinea.value, inPrecio: int(inPrecio.value), inCantidad: int(inCantidad.value)}

        for i, k in lista.items():
            if not k:
                i.error_text = "Ingreso erroneo"
            else:
                dictGuardad[i.label] = k
            i.value = ""

        if len(dictGuardad) == 4:
            Page.dialog = contModal.content = Text(f"{dictGuardad}")
            Page.dialog = contModal.actions.append(TextButton("Correcto", on_click = fnGuardaProducto),)
            Page.dialog = contModal.actions.append(TextButton("No", on_click = fnContModalCerrado),)
            contModal.open = True
            vista.update()
        else:
            vista.update()
        return    
   
    appBarVista = AppBar(title=Text("Vender producto"),actions = [TextButton("Index", on_click=lambda e: e.page.go("/index")),], bgcolor=colors.SURFACE_VARIANT)
    inNombre = TextField(label="producto", autofocus=True, width= WindowDragArea)
    inLinea = TextField(label="linea")
    inPrecio = TextField(label="precio", input_filter = NumbersOnlyInputFilter())
    inCantidad = TextField(label="cantidad", input_filter = NumbersOnlyInputFilter())
    btnGuardar = ElevatedButton(text = "Vender", on_click=btn_click)

    listaObj = (appBarVista,contModal,inNombre,inLinea,inCantidad,inPrecio,btnGuardar)     
    
    controles = [
                appBarVista,
                contModal,
                inNombre,
                inLinea,
                inCantidad,
                inPrecio,
                btnGuardar,
                ]

    vista = View(
            "/addPrd",
            horizontal_alignment = CrossAxisAlignment.CENTER,
            auto_scroll = True,
            scroll = ScrollMode.HIDDEN,
            controls = controles,
            )

    return vista 