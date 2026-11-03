class Veterinario:
    def __init__(self, nombre, identificacion, telefono, especialidad):
        self.nombre = nombre
        self.identificacion = identificacion
        self.telefono = telefono
        self.especialidad = especialidad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Identificación: {self.identificacion}")
        print(f"Teléfono: {self.telefono}")
        print(f"Especialidad: {self.especialidad}")
