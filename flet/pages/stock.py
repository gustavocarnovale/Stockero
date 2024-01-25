from flet import *
from db import fnCargaProductos, fnCargaLinea

productos = fnCargaProductos()

def index():
    
    def items():
        items = []
        for i in productos:
            items.append(
                dropdown.Option(f"{i}"),
            )
        return items

    def fnLineaElegida(e):
        salida = fnCargaLinea(confDrop.value)
        viewStock.controls.clear()
        titulosCol.rows.clear()

    ###ARMA VISTA###    
        for objetos in listaObj:
            viewStock.controls.append(objetos)

    ###CARGA DATOS DE PRODUCTOS EN LA TABLA###
        for i, k in salida.items():
            for y, z in k.items():
                if y == "cantidad":
                    cantidad = z
                elif y == "precio":
                    precio = z
                else:
                    pass
             
            titulosCol.rows.append(DataRow(cells = [DataCell(Text(value=i)),DataCell(Text(value=cantidad)),DataCell(Text(value=(f"$ {precio}")))]),)
        viewStock.update()
        
        return salida
  
    confDrop = Dropdown(on_change= fnLineaElegida,options=items(),)
    appBarVista = AppBar(title=Text("Stock"), bgcolor=colors.SURFACE_VARIANT)
    botonIndexVista = ElevatedButton("Index", on_click=lambda e: e.page.go("/index"))
    titulosCol = DataTable(
            columns=[DataColumn(Text(value=str("producto"))),DataColumn(Text(value=str("cantidad"))),DataColumn(Text("precio")),],
        )
    listaObj = (appBarVista,botonIndexVista,confDrop, titulosCol) 

    viewStock = View(
                    "/stock",
                    horizontal_alignment = CrossAxisAlignment.CENTER,
                    auto_scroll = True,
                    scroll = ScrollMode.HIDDEN,
                    controls = [
                        appBarVista,
                        botonIndexVista,
                        confDrop,
                    ],
                )
    
    return viewStock


            