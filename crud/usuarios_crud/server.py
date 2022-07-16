from flask import Flask, render_template,redirect,request,session
from users import Usuario

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template('leer.html', users=Usuario.get_all())

@app.route('/user/new')
def new_user():
    return render_template('crear.html')

@app.route('/user/create', methods=['POST'])
def create():
    print(request.form)
    Usuario.save(request.form)
    return redirect('/users')

@app.route('/user/edit/<int:id>')
def edit(id):
    data ={
        "id":id
    }
    return render_template("editar.html", user=Usuario.get_one(data))

@app.route('/user/show/<int:id>')
def show(id):
    data ={
        "id":id
    }
    return render_template("show_user.html", user=Usuario.get_one(data))

@app.route('/user/update', methods=['POST'])
def update():
    Usuario.update(request.form)
    return redirect('/users')

@app.route('/user/destroy/<int:id>')
def destroy(id):
    data={
        'id':id
    }
    Usuario.destroy(data)
    return redirect('/users')

if __name__=="__main__":
    app.run(debug=True)