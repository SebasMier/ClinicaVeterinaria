from propietario import Propietario
from mascota import Mascota
from veterinario import Veterinario
from cita_general import CitaGeneral
from cita_vacunacion import CitaVacunacion
from cita_control import CitaControl

propietario1 = Propietario("Juan Alvarez", "123456789", "Juan@gmail.com")
propietario1.mostrar_informacion()
print()

propietario1.cambiar_correo("Juan123@gmail.com")
propietario1.mostrar_informacion()
print()

propietario1.cambiar_correo("")
propietario1.mostrar_informacion()
print()

mascota1 = Mascota("Luu", 3, 2, "Perro", propietario1)
mascota1.mostrar_informacion()
print()

mascota1.cambiar_edad(4, 1)
mascota1.mostrar_informacion()
print()

mascota1.cambiar_edad(3, 14)
mascota1.mostrar_informacion()
print()

mascota1.cambiar_edad(-1, 0)
mascota1.mostrar_informacion()
print()

veterinario1 = Veterinario(
    "Carlos Alberto", "987654321", "3148220936", "Cirujano")
veterinario1.mostrar_informacion()
print()

veterinario1.cambiar_telefono("3127550937")
veterinario1.mostrar_informacion()
print()

veterinario1.cambiar_telefono("")
veterinario1.mostrar_informacion()
print()

cita1 = CitaGeneral("12/11/2026", "10:00 am", mascota1,
                    veterinario1, "Pendiente")
cita1.mostrar_informacion()
print()

cita1.cambiar_estado("Completada")
cita1.mostrar_informacion()
print()

cita2 = CitaVacunacion("15/11/2026", "11:00 am", mascota1,
                       veterinario1, "Pendiente", "Rabia")
cita2.mostrar_informacion()
print()

cita2.cambiar_estado("Completada")
cita2.mostrar_informacion()
print()

cita3 = CitaControl("18/11/2026", "12:00 pm", mascota1,
                    veterinario1, "Pendiente", "Revisión despues del tratamiento")
cita3.mostrar_informacion()
print()

cita3.cambiar_estado("Completada")
cita3.mostrar_informacion()
print()

citas = [cita1, cita2, cita3]
for cita in citas:
    cita.mostrar_informacion()
    print()

for cita in citas:
    cita.cambiar_estado("Cancelada")
    cita.mostrar_informacion()
    print()
