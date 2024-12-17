# controller/ClienteController.py
from model.Cliente import Cliente

class ClienteController:
    def __init__(self, repo):
        self.repo = repo

    def agregar_cliente(self, nombre, apellido, tipo_doc, numero_doc, telefono, correo, genero, id_rol):
        cliente = Cliente(None, nombre, apellido, tipo_doc, numero_doc, telefono, correo, genero, id_rol)
        self.repo.insert_cliente(cliente)
        print("Cliente agregado correctamente.")

    def listar_clientes(self):
        clientes = self.repo.get_all_clientes()
        print("Lista de Clientes:")
        for cliente in clientes:
            print(cliente)
