import mysql.connector

class ConexionBaseDatos:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host='localhost',
            database='bdcine',
            user='root',
            password='123456'
        )

    def get_conexion(self):
        return self.conexion
