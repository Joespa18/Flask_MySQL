from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.edad = data['edad']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Crear __________________
    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (nombre, apellido, edad, created_at, updated_at, dojo_id) VALUES (%(nombre)s, %(apellido)s, %(edad)s, NOW(), NOW(), %(dojo_id)s);"
        return connectToMySQL('dojos_y_ninjas').query_db(query, data)