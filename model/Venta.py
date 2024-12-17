# modelos/Venta.py
class Venta:
    def __init__(self, id_venta, fecha, asientos_reservados, tipo_pago, estado, id_cliente):
        self.id_venta = id_venta
        self.fecha = fecha
        self.asientos_reservados = asientos_reservados
        self.tipo_pago = tipo_pago
        self.estado = estado
        self.id_cliente = id_cliente

    def __str__(self):
        return f"Venta ID: {self.id_venta}, Cliente: {self.id_cliente}, Total: {self.asientos_reservados}"
