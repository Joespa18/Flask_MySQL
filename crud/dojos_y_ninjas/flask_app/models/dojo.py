from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []


    # Crear _____________
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (nombre, created_at, updated_at) VALUES (%(nombre)s, NOW(), NOW());"
        result = connectToMySQL('dojos_y_ninjas').query_db(query,data)
        return result

    #Leer ________________

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"

        results = connectToMySQL('dojos_y_ninjas').query_db(query)
        dojos = []

        for d in results:
            dojos.append( cls(d) )
        return dojos

    @classmethod
    def get_one_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_y_ninjas').query_db(query, data)
        dojo = cls(results[0])
        for row in results:
            ninja_data = {
                "id": row['ninjas.id'],
                "nombre": row['ninjas.nombre'],
                "apellido": row['apellido'],
                "edad": row['edad'],
                "created_at": row['ninjas.created_at'],
                "updated_at": row['ninjas.updated_at']
            }
            dojo.ninjas.append( ninja.Ninja(ninja_data))
        return dojo