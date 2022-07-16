from unittest import result
from mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def full_name(self):
        return f"{self.nombre} {self.apellido}"

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        results = connectToMySQL('db_usuarios').query_db(query)
        users = []
        for u in results:
            users.append(cls(u))
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO usuarios (nombre, apellido, email) VALUES (%(nombre)s, %(apellido)s, %(email)s);"
        result = connectToMySQL('db_usuarios').query_db(query, data)
        return result

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        result =connectToMySQL('db_usuarios').query_db(query, data)
        return cls(result[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE usuarios SET nombre=%(nombre)s, apellido=%(apellido)s, email=%(email)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('db_usuarios').query_db(query, data)

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM usuarios WHERE id = %(id)s;"
        return connectToMySQL('db_usuarios').query_db(query, data)