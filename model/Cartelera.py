class Cartelera:
    def __init__(self, id_cartelera, hora_inicio, hora_final, fecha, id_sala):
        self.id_cartelera = id_cartelera
        self.hora_inicio = hora_inicio
        self.hora_final = hora_final
        self.fecha = fecha
        self.id_sala = id_sala

    def __str__(self):
        return f"Cartelera ID: {self.id_cartelera}, Hora Inicio: {self.hora_inicio}, Hora Final: {self.hora_final}, Fecha: {self.fecha}, Sala: {self.id_sala}"
