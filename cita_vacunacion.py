from cita import Cita


class CitaVacunacion(Cita):
    def __init__(self, fecha, hora, mascota, veterinario, estado, vacuna):
        super().__init__(fecha, hora, mascota, veterinario, estado)
        self.vacuna = vacuna

    def mostrar_informacion(self):
        print("Tipo de cita: Vacunación")
        print(f"Fecha: {self.fecha}")
        print(f"Hora: {self.hora}")
        print(f"Mascota: {self.mascota.nombre}")
        print(f"Veterinario: {self.veterinario.nombre}")
        print(f"Estado: {self._estado}")
        print(f"Vacuna: {self.vacuna}")

    def cambiar_estado(self, nuevo_estado):
        self._estado = nuevo_estado

        if nuevo_estado == "Completada":
            print(f"Vacuna {self.vacuna} aplicada")
