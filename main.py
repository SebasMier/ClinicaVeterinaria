from propietario import Propietario
from mascota import Mascota

propietario1 = Propietario("Juan", "123456789", "Juan@gmail.com")
propietario1.mostrar_informacion()

mascota1 = Mascota("Luu", 3, "Perro", propietario1)
mascota1.mostrar_informacion()
