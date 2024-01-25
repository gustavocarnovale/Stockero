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
