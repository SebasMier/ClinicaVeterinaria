class RegistroMedico:
    def __init__(self, fecha, diagnostico, tratamiento):
        self.fecha = fecha
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento

    def mostrar_informacion(self):
        print(f"Fecha: {self.fecha}")
        print(f"Diagnóstico: {self.diagnostico}")
        print(f"Tratamiento: {self.tratamiento}")
