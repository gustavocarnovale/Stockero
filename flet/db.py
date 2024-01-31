import firebase_admin
from firebase_admin import db, credentials

firebase_sdk = credentials.Certificate('stockero-40e02-firebase-adminsdk-zi40z-37e5d22f6f.json')
firebase_admin.initialize_app(firebase_sdk,{'databaseURL': 'https://stockero-40e02-default-rtdb.firebaseio.com' })

ruta_nodo = f'/productos/'
nodo_referencia = db.reference(ruta_nodo)

def fnCargaProductos():

    datos = nodo_referencia.get()

    return datos

def fnCargaLinea(datolinea):

    if datolinea:
        nuevaRuta = str(ruta_nodo +  datolinea)
        nuevoNodo = db.reference(nuevaRuta)    
        linea = nuevoNodo.get()
    else:
        linea = ""
        
    return linea

def fnOperacionProducto(dataLower, op):
    
    ruta_nodo = f'/productos/{dataLower["linea"]}/{dataLower["producto"]}'
    nodo_referencia = db.reference(ruta_nodo)

    datosGuardado = {
        "cantidad":dataLower['cantidad'],
        "precio": dataLower['precio']
    }
    if nodo_referencia.get():

        Cantidad_actual = nodo_referencia.child('cantidad').get() or 0
        opResta = Cantidad_actual - int(dataLower["cantidad"]) if Cantidad_actual > int(dataLower["cantidad"]) and op == 0 else 0
        opSuma = Cantidad_actual + int(dataLower["cantidad"]) if  op == 1 else opResta
        nueva_Cantidad = opSuma
        nodo_referencia.update({'cantidad': nueva_Cantidad})
        print("Hecho 1")

    else:
        nodo_referencia.set(datosGuardado)
        print("Hecho 2")
    return    
