from abc import ABC, abstractmethod


class Cita(ABC):
    def __init__(self, fecha, hora, mascota, veterinario, estado):
        self.fecha = fecha
        self.hora = hora
        self.mascota = mascota
        self.veterinario = veterinario
        self.estado = estado

    @abstractmethod
    def mostrar_informacion(self):
        pass
