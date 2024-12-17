# repositorios/VentaRepository.py
class VentaRepository:
    def __init__(self, conexion):
        self.conexion = conexion

    def insert_venta(self, venta):
        cursor = self.conexion.cursor()
        query = """INSERT INTO ventas (fecha, asientos_reservados, tipo_pago, estado, id_cliente) 
                   VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(query, (venta.fecha, venta.asientos_reservados, venta.tipo_pago, venta.estado, venta.id_cliente))
        self.conexion.commit()

    def get_all_ventas(self):
        cursor = self.conexion.cursor()
        query = "SELECT * FROM ventas"
        cursor.execute(query)
        return cursor.fetchall()
