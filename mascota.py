class Mascota:
    def __init__(self, nombre, años, meses, tipo, propietario):
        self.nombre = nombre
        self.años = años
        self.meses = meses
        self.tipo = tipo
        self.propietario = propietario

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.años} años y {self.meses} meses")
        print(f"Tipo: {self.tipo}")
        print(f"Propietario: {self.propietario.nombre}")
