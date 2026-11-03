from cita import Cita


class CitaGeneral(Cita):
    def __init__(self, fecha, hora, mascota, veterinario, estado):
        super().__init__(fecha, hora, mascota, veterinario, estado)

    def mostrar_informacion(self):
        print("Tipo de cita: General")
        print(f"Fecha: {self.fecha}")
        print(f"Hora: {self.hora}")
        print(f"Mascota: {self.mascota.nombre}")
        print(f"Veterinario: {self.veterinario.nombre}")
        print(f"Estado: {self._estado}")

    def cambiar_estado(self, nuevo_estado):
        self._estado = nuevo_estado
