from propietario import Propietario
from mascota import Mascota
from veterinario import Veterinario
from cita_general import CitaGeneral
from cita_vacunacion import CitaVacunacion
from cita_control import CitaControl

propietario1 = Propietario("Juan", "123456789", "Juan@gmail.com")
propietario1.mostrar_informacion()

mascota1 = Mascota("Luu", 3, 2, "Perro", propietario1)
mascota1.mostrar_informacion()

veterinario1 = Veterinario(
    "Carlos Alberto", "987654321", "3148220936", "Cirujano")
veterinario1.mostrar_informacion()

cita1 = CitaGeneral("12/11/2026", "10:00 am", mascota1,
                    veterinario1, "Pendiente")
cita1.mostrar_informacion()

cita2 = CitaVacunacion("15/11/2026", "11:00 am", mascota1,
                       veterinario1, "Pendiente", "Rabia")
cita2.mostrar_informacion()

cita3 = CitaControl("18/11/2026", "12:00 pm", mascota1,
                    veterinario1, "Pendiente", "Revisión despues del tratamiento")
cita3.mostrar_informacion()
