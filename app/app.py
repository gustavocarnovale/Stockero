from flask import Flask, render_template,request, redirect, url_for
#from firebase import firebase
import firebase_admin
from firebase_admin import db, credentials
import datetime


app = Flask(__name__)

#firebase = firebase.FirebaseApplication('https://stockero-40e02-default-rtdb.firebaseio.com/',None)
firebase_sdk = credentials.Certificate('stockero-40e02-firebase-adminsdk-zi40z-37e5d22f6f.json')

firebase_admin.initialize_app(firebase_sdk,{'databaseURL': 'https://stockero-40e02-default-rtdb.firebaseio.com' })

@app.route('/')
def index():

    data = {"titulo": "Hola!"}

    return render_template('index.html', data = data)

@app.route('/stock')
def stock():

    ruta_nodo = f'/productos/'
    nodo_referencia = db.reference(ruta_nodo)
    datos = nodo_referencia.get()

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
        "cantidad": int(request.form['cantidad_vendida'])
    }

    data_lower = fnDataLower(data)
    fnOperacionProducto(data_lower, op)
    fnRegistraVenta(data_lower)

    return render_template('vender.html')

@app.route('/producto')
def producto():

    return render_template('producto.html')

@app.route('/producto', methods =['POST'])
def fnGuardaProducto():
    op = 1
    data = {
        "nombre":request.form['nombre'],
        "linea": request.form['linea'],
        "cantidad": int(request.form['cantidad'])
    }

    data_lower = fnDataLower(data)
    fnOperacionProducto(data_lower, op)


    return render_template('producto.html')

def fnRegistraVenta(data_lower):
    fecha = datetime.datetime.now()
    fecha_str = fecha.strftime("%Y-%m-%d %H:%M:%S")
    datos = {
    'cantidad': data_lower['cantidad'],
    'fecha': fecha_str,
    'precio': 0 
    }
    ruta_nodo = f'/ventas/{data_lower["linea"]}/{data_lower["nombre"]}'
    nodo_referencia = db.reference(ruta_nodo)
    
    lista_ventas = nodo_referencia.get()
    lista_ventas.append(datos)
    #nodo_referencia.set(lista_ventas)
    print(lista_ventas)

    return

def fnOperacionProducto(data_lower, op):
    
    ruta_nodo = f'/productos/{data_lower["linea"]}/{data_lower["nombre"]}'
    nodo_referencia = db.reference(ruta_nodo)

    if nodo_referencia.get():

        cantidad_actual = nodo_referencia.child('cantidad').get() or 0
        opResta = cantidad_actual - int(data_lower["cantidad"]) if cantidad_actual > int(data_lower["cantidad"]) and op == 0 else 0
        opSuma = cantidad_actual + int(data_lower["cantidad"]) if  op == 1 else opResta
        nueva_cantidad = opSuma
        nodo_referencia.update({'cantidad': nueva_cantidad})

    else:
        nodo_referencia.set(data_lower)
    return    


def fnDataLower(data):

    data =  {key: value.lower() if isinstance(value, str) else value for key, value in data.items()}

    return data

def query():

    print(request.args.get('param1')) 

    return "Listo!"

def pag(error):
    
    return redirect(url_for('index'))

if __name__ == '__main__':

    app.add_url_rule('/query', view_func = query )
    app.register_error_handler(404, pag)
    app.run(debug=True)