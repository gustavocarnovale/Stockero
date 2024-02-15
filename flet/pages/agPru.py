from flet import *
from db import fnCargaProductos
import asyncio

productos = fnCargaProductos

def index():

    nombre = TextField(label="producto", autofocus=True, width= WindowDragArea) 
    vista = View(
        "/agPru",
        horizontal_alignment = CrossAxisAlignment.CENTER,
        auto_scroll = True,
        scroll = ScrollMode.HIDDEN,
        controls = [
            AppBar(title=Text("Pruebas"), center_title = True, bgcolor=colors.SURFACE_VARIANT, actions = [TextButton("Index", on_click=lambda e: e.page.go("/index")),]),
            nombre,
        ],
    )

    
    
    async def tarea1():
        print("1 inicia")
        await asyncio.sleep(1)
        print(productos)
    
    async def tarea2():
        print("2 inicia")
        await asyncio.sleep(3)
        print("2 terminada")

    async def tareas():
        _tarea1 = asyncio.create_task(tarea1())
        _tarea2 = asyncio.create_task(tarea2())

        await asyncio.gather(_tarea1, _tarea2)
    
    asyncio.run(tareas())

    return vista 

