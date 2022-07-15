from flask import Flask, render_template,redirect,request,session
from users import Usuario

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users/new')
def new_user():
    return render_template('crear.html')

@app.route('/users')
def users():
    return render_template('leer.html', users=Usuario.get_all())

@app.route('/users/create', methods=['POST'])
def create():
    print(request.form)
    Usuario.save(request.form)
    return redirect('/users')

if __name__=="__main__":
    app.run(debug=True) 