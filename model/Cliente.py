# modelos/Cliente.py
class Cliente:
    def __init__(self, id_cliente, nombre, apellido, tipo_doc, numero_doc, telefono, correo, genero, id_rol):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.tipo_doc = tipo_doc
        self.numero_doc = numero_doc
        self.telefono = telefono
        self.correo = correo
        self.genero = genero
        self.id_rol = id_rol

    def __str__(self):
        return f"ID: {self.id_cliente}, Nombre: {self.nombre} {self.apellido}, Correo: {self.correo}"
