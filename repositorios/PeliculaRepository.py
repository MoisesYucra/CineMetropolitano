class PeliculaRepository:
    def __init__(self, conexion):
        self.conexion = conexion

    def insert_pelicula(self, pelicula):
        cursor = self.conexion.cursor()
        query = "INSERT INTO peliculas (titulo, duracion, genero, clasificacion) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (pelicula.titulo, pelicula.duracion, pelicula.genero, pelicula.clasificacion))
        self.conexion.commit()

    def get_all_peliculas(self):
        cursor = self.conexion.cursor()
        query = "SELECT * FROM peliculas"
        cursor.execute(query)
        return cursor.fetchall()
