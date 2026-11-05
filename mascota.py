from excepciones import EdadInvalidaError
from historial_clinico import HistorialClinico


class Mascota:
    def __init__(self, nombre, años, meses, tipo, propietario):
        self.nombre = nombre
        self._años = años
        self._meses = meses
        self.tipo = tipo
        self.propietario = propietario
        self.historial_clinico = HistorialClinico()

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self._años} años y {self._meses} meses")
        print(f"Tipo: {self.tipo}")
        print(f"Propietario: {self.propietario.nombre}")

    def cambiar_edad(self, años, meses):
        if años < 0 or meses < 0 or meses > 11:
            raise EdadInvalidaError("La edad no es valida")
        else:
            self._años = años
            self._meses = meses
