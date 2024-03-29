from flet import *
from db import fnCargaProductos, fnCargaLinea

productos = fnCargaProductos()

def index():
    
    def items():
        items = ()
        items = list(map(lambda x: dropdown.Option(x),productos))
        return items

    def fnLineaElegida(e):
        salida = fnCargaLinea(confDrop.value)
        viewStock.controls.clear()
        titulosCol.rows.clear()

    ###ARMA VISTA###    
        list(map(lambda x: viewStock.controls.append(x),listaObj))

    ###CARGA DATOS DE PRODUCTOS EN LA TABLA###
        for i, k in salida.items():
            for y, z in k.items():
                if y == "cantidad":
                    cantidad = z
                elif y == "precio":
                    precio = z
             
            titulosCol.rows.append(DataRow(cells = [DataCell(Text(value=i)),DataCell(Text(value=cantidad)),DataCell(Text(value=(f"$ {precio}")))]),)
        viewStock.update()
        
        return salida
  
    confDrop = Dropdown(on_change= fnLineaElegida,options=items(),)
    appBarVista = AppBar(title=Text("Agregar producto"),actions = [TextButton("Index", on_click=lambda e: e.page.go("/index")),], bgcolor=colors.SURFACE_VARIANT)
    titulosCol = DataTable(
            columns=[DataColumn(Text(value=str("producto"))),DataColumn(Text(value=str("cantidad"))),DataColumn(Text("precio")),],
        )
    listaObj = (appBarVista,confDrop, titulosCol) 

    viewStock = View(
                    "/stock",
                    horizontal_alignment = CrossAxisAlignment.CENTER,
                    auto_scroll = True,
                    scroll = ScrollMode.HIDDEN,
                    controls = [
                        appBarVista,
                        confDrop,
                    ],
                )
    
    return viewStock


            