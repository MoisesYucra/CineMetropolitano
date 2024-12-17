# controller/VentaController.py
from model.Venta import Venta

class VentaController:
    def __init__(self, repo):
        self.repo = repo

    def agregar_venta(self, fecha, asientos_reservados, tipo_pago, estado, id_cliente):
        venta = Venta(None, fecha, asientos_reservados, tipo_pago, estado, id_cliente)
        self.repo.insert_venta(venta)
        print("Venta agregada correctamente.")

    def listar_ventas(self):
        ventas = self.repo.get_all_ventas()
        print("Lista de Ventas:")
        for venta in ventas:
            print(venta)
