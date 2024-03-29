from flet import *
from db import fnOperacionProducto, fnCargaLinea, fnCargaProductos

def index():

    dictGuardad = {}   

    def items():
        items = ()
        items = list(map(lambda x: dropdown.Option(x),fnCargaProductos()))
        return items

    def fnLineaElegida(e):
        salida = fnCargaLinea(confDrop.value)
    
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
        vista.controls.clear()
        contModal.open = False
        list(map(lambda x: vista.controls.append(x),listaObj)) ### ARMA VISTA ###  
        fnOperacionProducto(dictGuardad, op = 1)
        vista.update()
    
    def btn_click(e):
        lista = {inNombre: inNombre.value,confDrop: confDrop.value,inCantidad: inCantidad.value,inPrecio: inPrecio.value}

        for i, k in lista.items():
            if not k:
                i.error_text = "Ingreso erroneo"
            else:
                dictGuardad[i.label] = k.lower()
            i.value = ""

        if len(dictGuardad)== 4:
            Page.dialog = contModal.content = Text(f"{dictGuardad}")
            Page.dialog = contModal.actions.append(TextButton("Correcto", on_click = fnGuardaProducto),)
            Page.dialog = contModal.actions.append(TextButton("No", on_click = fnContModalCerrado),)
            contModal.open = True
            vista.update()
        else:
            vista.update()
        return    
   
    appBarVista = AppBar(title=Text("Agregar producto"),actions = [TextButton("Index", on_click=lambda e: e.page.go("/index")),], bgcolor=colors.SURFACE_VARIANT)
    inNombre = TextField(label="producto", autofocus=True, width= WindowDragArea)
    inCantidad = TextField(label="cantidad", input_filter = NumbersOnlyInputFilter())
    inPrecio = TextField(label="precio",  input_filter = NumbersOnlyInputFilter())
    btnGuardar = ElevatedButton(text = "Guardar", on_click=btn_click)
    confDrop = Dropdown(label="linea", on_change= fnLineaElegida,options=items(),) 
    
    controles = [
                appBarVista,
                contModal,
                inNombre,
                confDrop,  
                inCantidad,
                inPrecio,
                btnGuardar,
                ]

    listaObj = (appBarVista,contModal,inNombre,confDrop,inCantidad,inPrecio,btnGuardar)    

    vista = View(
            "/addPrd",
            horizontal_alignment = CrossAxisAlignment.CENTER,
            auto_scroll = True,
            scroll = ScrollMode.HIDDEN,
            controls = controles,
            )

    return vista 