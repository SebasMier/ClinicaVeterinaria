class Mascota:
    def __init__(self, nombre, edad, tipo, propietario):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo
        self.propietario = propietario

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Tipo: {self.tipo}")
        print(f"Propietario: {self.propietario.nombre}")
