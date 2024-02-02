from flask import Flask, render_template,request, redirect, url_for
#from firebase import firebase
import firebase_admin
from firebase_admin import db, credentials
import datetime


app = Flask(__name__)

#firebase = firebase.FirebaseApplication('https://stockero-40e02-default-rtdb.firebaseio.com/',None)
firebase_sdk = credentials.Certificate('stockero-40e02-firebase-adminsdk-zi40z-37e5d22f6f.json')

firebase_admin.initialize_app(firebase_sdk,{'databaseURL': 'https://stockero-40e02-default-rtdb.firebaseio.com' })

fecha = datetime.datetime.now()
fecha_str = fecha.strftime("%Y-%m-%d")
id = fecha.strftime("%H:%M:%S")

@app.route('/')
def index():

    data = {"titulo": "Hola!"}

    return render_template('index.html', data = data)

@app.route('/ventas', methods=["GET"])
def ventas():

    productos = fnCargaProductos("ekos")
    producto_seleccionado = request.args.get('producto')
    
    if producto_seleccionado:
        return mostrar_ventas(producto_seleccionado)

    return render_template('ventas.html', productos = productos)

@app.route('/ventas/<producto>', methods = ["GET"])
def mostrar_ventas(producto_seleccionado):

    ruta_nodo_ventas = f'/ventas/{producto_seleccionado}'
    nodo_referencia_ventas = db.reference(ruta_nodo_ventas)
    lista_ventas = nodo_referencia_ventas.get()

    return render_template('listaVentas.html', ventas=lista_ventas)

@app.route('/stock')
def stock():

    datos = fnCargaProductos("")

    return render_template('stock.html', datos=datos)

@app.route('/vender')
def vender():
    
    return render_template('vender.html')

@app.route('/vender', methods =['POST'])
def fnVendeProducto():
    op = 0
    data = {
        "nombre":request.form['nombre'],
        "linea": request.form['linea'],
        "cantidad": int(request.form['cantidad_vendida']),
        "precio":  float(request.form['precio'])
    }

    data_lower = fnLower(data)
    fnOperacionProducto(data_lower, op)
    fnRegistraVenta(data_lower)
    return render_template('vender.html')

#######################################################################################################################################

@app.route('/producto')
def producto():

    return render_template('producto.html')

@app.route('/producto', methods =['POST'])
def fnGuardaProducto():
    op = 1
    data = {
        "nombre":request.form['nombre'],
        "linea": request.form['linea'],
        "cantidad": int(request.form['cantidad']),
        "precio": float(request.form['precio'])
    }

    dataLower = fnLower(data)
    fnOperacionProducto(dataLower, op)

    return render_template('producto.html')

#FUNCIONES#    
#######################################################################################################################################
def fnCargaProductos(linea):
    
    ruta_nodo = f'/productos/{linea}'
    nodo_referencia = db.reference(ruta_nodo)
    datos = nodo_referencia.get()
    print(datos)
    return datos

#######################################################################################################################################
def fnRegistraVenta(dataLower):
    
    datos = {
        "cantidad": dataLower['cantidad'],
        "precio": dataLower['precio']
    }

    ruta_nodo = f'/ventas/{dataLower["nombre"]}/{id}'
    nodo_referencia = db.reference(ruta_nodo)
    dato = nodo_referencia.get()
    print(dato)
    nodo_referencia.set(datos)

    return

#######################################################################################################################################
def fnOperacionProducto(dataLower, op):
    
    ruta_nodo = f'/productos/{dataLower["linea"]}/{dataLower["nombre"]}'
    nodo_referencia = db.reference(ruta_nodo)

    datosGuardado = {
        "cantidad":dataLower['cantidad'],
        "precio": dataLower['precio']
    }
    if nodo_referencia.get():

        cantidad_actual = nodo_referencia.child('cantidad').get() or 0
        opResta = cantidad_actual - int(dataLower["cantidad"]) if cantidad_actual > int(dataLower["cantidad"]) and op == 0 else 0
        opSuma = cantidad_actual + int(dataLower["cantidad"]) if  op == 1 else opResta
        nueva_cantidad = opSuma
        nodo_referencia.update({'cantidad': nueva_cantidad})

    else:
        nodo_referencia.set(datosGuardado)
    return    

#######################################################################################################################################
def fnLower(data):

    data =  {key: value.lower() if isinstance(value, str) else value for key, value in data.items()}

    return data

#######################################################################################################################################
def pag(error):
    
    return redirect(url_for('index'))

if __name__ == '__main__':

    app.register_error_handler(404, pag)
    app.run(debug=True)