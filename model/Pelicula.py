# modelos/Pelicula.py
class Pelicula:
    def __init__(self, id_pelicula, titulo, duracion, genero, clasificacion):
        self.id_pelicula = id_pelicula
        self.titulo = titulo
        self.duracion = duracion
        self.genero = genero
        self.clasificacion = clasificacion

    def __str__(self):
        return f"{self.titulo} - {self.genero} - {self.clasificacion}"
