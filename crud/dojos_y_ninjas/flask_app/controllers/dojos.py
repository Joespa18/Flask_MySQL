from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    return render_template ('index.html', all_dojos = Dojo.get_all())

@app.route('/create/dojo', methods=['POST'])
def crear():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojo/<int:id>')
def mostrar(id):
    data = {
        "id": id
    }
    return render_template('dojos.html', dojo = Dojo.get_one_with_ninjas(data))