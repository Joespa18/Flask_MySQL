from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import dojo, ninja

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html', dojos = dojo.Dojo.get_all())

@app.route('/create/ninja',methods=['POST'])
def create_ninja():
    ninja.Ninja.save(request.form)
    return redirect('/')