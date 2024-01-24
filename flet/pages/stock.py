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
        viewStock.controls.clear()
        viewStock.controls.append(appBarVista)
        viewStock.controls.append(botonIndexVista)
        viewStock.controls.append(confDrop)        
        viewStock.controls.append(titulosCol)        
        salida = fnCargaLinea(confDrop.value)
        for i, k in salida.items():
            viewStock.controls.append(DataTable(rows=[DataRow(cells = [DataCell(Text(value=str(i))),])],)),
            #viewStock.controls.append(Text(value=str(i)))
            for y, z in k.items():
                #viewStock.controls.append(Text(value=(f'{y}: {z}')))
                viewStock.controls.append(DataTable(rows=[DataRow(cells = [DataCell(Text(value=str(y))),DataCell(Text(value=str(z)))])],))
        viewStock.update()
        
        return salida
  
    confDrop = Dropdown(
        on_change= fnLineaElegida,
        options=items(),
    )

    appBarVista = AppBar(title=Text("Stock"), bgcolor=colors.SURFACE_VARIANT)
    botonIndexVista = ElevatedButton("Index", on_click=lambda e: e.page.go("/index"))
    titulosCol = DataTable(columns=[DataColumn(Text("Nombre")),DataColumn(Text("Cantidad")),DataColumn(Text("Precio")),])

    viewStock = View(
                    "/stock",
                    
                    controls = [
                        appBarVista,
                        botonIndexVista,
                        confDrop,
                    ],)
    
    return viewStock


            