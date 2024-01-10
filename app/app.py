from flask import Flask, render_template,request, redirect, url_for
#from firebase import firebase
import firebase_admin
from firebase_admin import db, credentials


app = Flask(__name__)

#firebase = firebase.FirebaseApplication('https://stockero-40e02-default-rtdb.firebaseio.com/',None)
firebase_sdk = credentials.Certificate('stockero-40e02-firebase-adminsdk-zi40z-37e5d22f6f.json')

firebase_admin.initialize_app(firebase_sdk,{'databaseURL': 'https://stockero-40e02-default-rtdb.firebaseio.com' })

@app.route('/')
def index():

    data = {"titulo": "Hola!"}

    return render_template('index.html', data = data)

@app.route('/producto')
def producto():

    return render_template('producto.html')

@app.route('/guardar', methods =['post'])
def guardar():
    data = {
        "nombre":request.form['nombre'],
        "linea": request.form['linea'],
        "cantidad": int(request.form['cantidad'])
    }

    data_lower = {key: value.lower() if isinstance(value, str) else value for key, value in data.items()}

    return fnGuarda(data_lower)

def query():

    print(request.args.get('param1')) 

    return "Listo!"

def pag(error):
    
    return redirect(url_for('index'))

def fnGuarda(data):
    
    ruta_nodo = f'/productos/{data["linea"]}/{data["nombre"]}'
    nodo_referencia = db.reference(ruta_nodo)

    if nodo_referencia.get():

        cantidad_actual = nodo_referencia.child('cantidad').get() or 0
        nueva_cantidad = cantidad_actual + int(data["cantidad"])
        nodo_referencia.update({'cantidad': nueva_cantidad})

    else:
        nodo_referencia.set(data)

    return render_template('index.html', data=data)

if __name__ == '__main__':

    app.add_url_rule('/query', view_func = query )
    app.register_error_handler(404, pag)
    app.run(debug=True)