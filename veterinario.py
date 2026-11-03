class Veterinario:
    def __init__(self, nombre, identificacion, telefono, especialidad):
        self.nombre = nombre
        self.identificacion = identificacion
        self._telefono = telefono
        self.especialidad = especialidad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Identificación: {self.identificacion}")
        print(f"Teléfono: {self._telefono}")
        print(f"Especialidad: {self.especialidad}")

    def cambiar_telefono(self, telefono):
        if telefono == (""):
            print("El teléfono no puede estar vacío")
        else:
            self._telefono = telefono
