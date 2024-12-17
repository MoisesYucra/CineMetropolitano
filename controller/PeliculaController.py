# controller/PeliculaController.py
from model.Pelicula import Pelicula

class PeliculaController:
    def __init__(self, repo):
        self.repo = repo

    def agregar_pelicula(self, titulo, duracion, genero, clasificacion):
        pelicula = Pelicula(None, titulo, duracion, genero, clasificacion)
        self.repo.insert_pelicula(pelicula)
        print("Película agregada correctamente.")

    def listar_peliculas(self):
        peliculas = self.repo.get_all_peliculas()
        print("Lista de Películas:")
        for pelicula in peliculas:
            print(pelicula)
