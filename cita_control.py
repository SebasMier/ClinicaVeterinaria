from cita import Cita


class CitaControl(Cita):
    def __init__(self, fecha, hora, mascota, veterinario, estado, motivo_control):
        super().__init__(fecha, hora, mascota, veterinario, estado)
        self.motivo_control = motivo_control

    def mostrar_informacion(self):
        print("Tipo de cita: Control")
        print(f"Fecha: {self.fecha}")
        print(f"Hora: {self.hora}")
        print(f"Mascota: {self.mascota.nombre}")
        print(f"Veterinario: {self.veterinario.nombre}")
        print(f"Estado: {self.estado}")
        print(f"Motivo de control: {self.motivo_control}")
