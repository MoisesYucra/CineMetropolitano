from model.Cartelera import Cartelera

class CarteleraController:
    def __init__(self, repo, sala_repo):
        self.repo = repo
        self.sala_repo = sala_repo  # Repositorio para verificar las salas

    def agregar_cartelera(self, hora_inicio, hora_final, fecha, id_sala):
        # Verificar si la sala existe
        if not self.sala_repo.existe_sala(id_sala):
            print(f"Error: La sala con id {id_sala} no existe.")
            return

        cartelera = Cartelera(None, hora_inicio, hora_final, fecha, id_sala)
        self.repo.insert_cartelera(cartelera)
        print("Cartelera agregada correctamente.")

    def listar_carteleras(self):
        carteleras = self.repo.get_all_carteleras()
        print("Lista de Carteleras:")
        for cartelera in carteleras:
            print(cartelera)
