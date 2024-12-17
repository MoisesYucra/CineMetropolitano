# repositorios/ClienteRepository.py
class ClienteRepository:
    def __init__(self, conexion):
        self.conexion = conexion

    def insert_cliente(self, cliente):
        cursor = self.conexion.cursor()
        query = """INSERT INTO clientes (nombre, apellido, tipo_doc, numero_doc, telefono, correo, genero, id_rol) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, (cliente.nombre, cliente.apellido, cliente.tipo_doc, cliente.numero_doc, 
                               cliente.telefono, cliente.correo, cliente.genero, cliente.id_rol))
        self.conexion.commit()

    def get_all_clientes(self):
        cursor = self.conexion.cursor()
        query = "SELECT * FROM clientes"
        cursor.execute(query)
        return cursor.fetchall()
