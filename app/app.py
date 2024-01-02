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

@app.route('/producto', methods =['post'])
def producto():

    data = {
        "nombre":request.form['nombre'],
        "categoria": request.form['categoria'],
        "correo": request.form['correo']
    }

    return render_template('index.html', data = data), fnGuarda(data)

def query():

    print(request.args.get('param1')) 

    return "Listo!"

#def pag(error):
#    
#    return redirect(url_for('index'))

def fnGuarda(data):

    db.reference('producto').child(data['categoria'])
    

    return render_template('producto.html')

if __name__ == '__main__':

    app.add_url_rule('/query', view_func = query )
    #app.register_error_handler(404, pag)
    app.run(debug=True)