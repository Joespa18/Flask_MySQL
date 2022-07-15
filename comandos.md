<!-- Para crear el entorno virtual-->
python -m pipenv install flask PyMYSQL 

<!-- Activar el entorno virtual -->
python -m pipenv shell

<!-- Desactivar el entorno virtual -->
exit

<!-- Para crear el server -->
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def nombre():
    pass

if __name__=="__main__":
    app.run(debug=True) 

<!-- Pegar un style.css -->
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/style.css') }}">

<!-- Comandos para conectar a la BD -->
# un cursor es el objeto que usamos para interactuar con la base de datos
import pymysql.cursors
# esta clase nos dará una instancia de una conexión a nuestra base de datos
class MySQLConnection:
    def __init__(self, db):
        # cambiar el usuario y la contraseña según sea necesario
        connection = pymysql.connect(host = 'localhost',
                                    user = 'root', 
                                    password = 'root', 
                                    db = db,
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor,
                                    autocommit = True)
        # establecer la conexión a la base de datos
        self.connection = connection
        # el método para consultar la base de datos
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)

                cursor.execute(query, data)
                if query.lower().find("insert") >= 0:
                    # las consultas INSERT devolverán el NÚMERO DE ID de la fila insertada
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # las consultas SELECT devolverán los datos de la base de datos como una LISTA DE DICCIONARIOS
                    result = cursor.fetchall()
                    return result
                else:
                    # las consultas UPDATE y DELETE no devolverán nada
                    self.connection.commit()
            except Exception as e:
                # si la consulta falla, el método devolverá FALSE
                print("Something went wrong", e)
                return False
            finally:
                # cerrar la conexión
                self.connection.close() 
# connectToMySQL recibe la base de datos que estamos usando y la usa para crear una instancia de MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)

<!-- importar la función que devolverá una instancia de una conexión -->
from mysqlconnection import connectToMySQL