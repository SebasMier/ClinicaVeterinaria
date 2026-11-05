from propietario import Propietario
from mascota import Mascota
from veterinario import Veterinario
from cita_general import CitaGeneral
from cita_vacunacion import CitaVacunacion
from cita_control import CitaControl
from excepciones import CorreoInvalidoError, EdadInvalidaError, TelefonoInvalidoError

print("========================================")
print("       SISTEMA CLINICA VETERINARIA")
print("========================================")
print()

print("========== PROPIETARIO ==========")
print()

propietario1 = Propietario("Juan Alvarez", "123456789", "Juan@gmail.com")
propietario1.mostrar_informacion()
print()

propietario2 = Propietario("Maria Lopez", "987654321", "Maria@gmail.com")
propietario2.mostrar_informacion()
print()

print("--- PRUEBA: CAMBIO DE CORREO ---")
print()

propietario1.cambiar_correo("Juan123@gmail.com")
propietario1.mostrar_informacion()
print()

print("--- PRUEBA: CORREO VACIO ---")
print()

try:
    propietario1.cambiar_correo("")
except CorreoInvalidoError as error:
    print(error)

propietario1.mostrar_informacion()
print()


print("========== MASCOTA ==========")
print()


mascota1 = Mascota("Luu", 3, 2, "Perro", propietario1)
mascota1.mostrar_informacion()
print()

mascota2 = Mascota("Luna", 2, 5, "Gato", propietario2)
mascota2.mostrar_informacion()
print()

print("--- PRUEBA: CAMBIO DE EDAD ---")
print()

mascota1.cambiar_edad(4, 1)
mascota1.mostrar_informacion()
print()

print("--- PRUEBA: MESES INVALIDOS ---")
print()

try:
    mascota1.cambiar_edad(3, 14)
except EdadInvalidaError as error:
    print(error)

mascota1.mostrar_informacion()
print()

print("--- PRUEBA: EDAD NEGATIVA ---")
print()

try:
    mascota1.cambiar_edad(-1, 0)
except EdadInvalidaError as error:
    print(error)

mascota1.mostrar_informacion()
print()

print("========== VETERINARIO ==========")
print()

veterinario1 = Veterinario(
    "Carlos Alberto", "987654321", "3148220936", "Cirujano")
veterinario1.mostrar_informacion()
print()

veterinario2 = Veterinario(
    "Ana Martinez", "456789123", "3104567890", "Medicina general")
veterinario2.mostrar_informacion()
print()

print("--- PRUEBA: CAMBIO DE TELEFONO ---")
print()


veterinario1.cambiar_telefono("3127550937")
veterinario1.mostrar_informacion()
print()

print("--- PRUEBA: TELEFONO VACIO ---")
print()

try:
    veterinario1.cambiar_telefono("")
except TelefonoInvalidoError as error:
    print(error)

veterinario1.mostrar_informacion()
print()

print("========== CITAS VETERINARIAS ==========")
print()

cita1 = CitaGeneral("12/11/2026", "10:00 am", mascota1,
                    veterinario2, "Pendiente")
cita1.mostrar_informacion()
print()

print("--- PRUEBA: CAMBIO DE ESTADO CITA GENERAL ---")
print()

cita1.cambiar_estado("Completada")
cita1.mostrar_informacion()
print()

cita2 = CitaVacunacion("15/11/2026", "11:00 am", mascota1,
                       veterinario2, "Pendiente", "Rabia")
cita2.mostrar_informacion()
print()


print("--- PRUEBA: CAMBIO DE ESTADO CITA VACUNACION ---")
print()

cita2.cambiar_estado("Completada")
cita2.mostrar_informacion()
print()

print("--- REGISTRO MEDICO: VACUNACION DE LUU ---")
print()

mascota1.historial_clinico.agregar_registro(
    cita2.fecha, "Vacunacion contra la rabia", "Aplicacion de vacuna antirrabica"
)

mascota1.historial_clinico.mostrar_informacion()
print()

cita3 = CitaControl("18/11/2026", "12:00 pm", mascota1,
                    veterinario1, "Pendiente", "Revisión despues del tratamiento")
cita3.mostrar_informacion()
print()

print("--- PRUEBA: CAMBIO DE ESTADO CITA CONTROL ---")
print()

cita3.cambiar_estado("Completada")
cita3.mostrar_informacion()
print()

cita4 = CitaGeneral("20/11/2026", "9:00 am", mascota2,
                    veterinario2, "Pendiente")
cita4.mostrar_informacion()
print()

print("--- PRUEBA: POLIMORFISMO AL MOSTRAR CITAS ---")
print()

citas = [cita1, cita2, cita3, cita4]
for cita in citas:
    cita.mostrar_informacion()
    print()

print("--- PRUEBA DE POLIMORFISMO: SIMULACION DE CANCELACION DE CITAS ---")
print()

for cita in citas:
    cita.cambiar_estado("Cancelada")
    cita.mostrar_informacion()
    print()
