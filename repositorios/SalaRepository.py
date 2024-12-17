class SalaRepository:
    def __init__(self, conexion):
        self.conexion = conexion

    def existe_sala(self, id_sala):
        query = "SELECT COUNT(*) FROM salas WHERE id_sala = %s"
        cursor = self.conexion.cursor()
        cursor.execute(query, (id_sala,))
        result = cursor.fetchone()
        return result[0] > 0  # Retorna True si la sala existe, de lo contrario False
