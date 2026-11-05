from registro_medico import RegistroMedico


class HistorialClinico:
    def __init__(self):
        self.registros = []

    def agregar_registro(self, fecha, diagnostico, tratamiento):
        registro = RegistroMedico(fecha, diagnostico, tratamiento)
        self.registros.append(registro)

    def mostrar_informacion(self):
        for registro in self.registros:
            registro.mostrar_informacion()
            print()
