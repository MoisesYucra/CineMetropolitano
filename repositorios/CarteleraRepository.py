class CarteleraRepository:
    def __init__(self, conexion):
        self.conexion = conexion

    def insert_cartelera(self, cartelera):
        query = "INSERT INTO cartelera (hora_inicio, hora_final, fecha, id_sala) VALUES (%s, %s, %s, %s)"
        cursor = self.conexion.cursor()
        cursor.execute(query, (cartelera.hora_inicio, cartelera.hora_final, cartelera.fecha, cartelera.id_sala))
        self.conexion.commit()

    def get_all_carteleras(self):
        query = "SELECT * FROM cartelera"
        cursor = self.conexion.cursor()
        cursor.execute(query)
        return cursor.fetchall()
