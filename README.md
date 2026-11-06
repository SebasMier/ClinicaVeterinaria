
# Sistema de Clinica Veterinaria

## Descripcion del proyecto

Este proyecto consiste en el desarrollo de un sistema de gestion de citas medicas para una clinica veterinaria utilizando Python y Programacion Orientada a Objetos (POO).

El sistema permite registrar propietarios, mascotas y veterinarios, asignar diferentes tipos de citas y guardar registros medicos de cada mascota en su historial clinico.

Ademas, usa conceptos de POO como encapsulamiento, herencia, polimorfismo, composicion y el manejo de excepciones personalizadas.

## Funcionalidades del sistema

El sistema permite:

- Registrar propietarios, mascotas y veterinarios.
- Crear citas generales, de vacunacion y de control.
- Asignar mascotas y veterinarios a las citas.
- Consultar la informacion de los propietarios, mascotas, veterinarios y citas.
- Cambiar el correo de los propietarios, la edad de las mascotas y el telefono de los veterinarios.
- Actualizar el estado de las citas.
- Guardar y consultar registros medicos en el historial clinico de cada mascota.
- Validar datos mediante excepciones personalizadas.

## Estructura del proyecto

El proyecto esta organizado en diferentes archivos Python, donde cada uno contiene una clase o una parte especifica del sistema.

- `main.py`: es el archivo principal del programa, donde se crean los objetos de propietarios, mascotas, veterinarios y diferentes tipos de citas y se encarga de hacer las pruebas y comprobar el funcionamiento del sistema.

- `propietario.py`: se define la clase Propietario, se encarga de almacenar el nombre, telefono y correo electronico de los propietarios. Permite modificar el correo mediante el metodo cambiar_correo(), el cual comprueba que el nuevo correo no sea vacio y si esta vacio lanza la excepcion personalizada CorreoInvalidoError.

- `mascota.py`: se define la clase Mascota, que almacena el nombre, la edad en años y meses, el tipo de mascota y su propietario. Permite modificar la edad mediante el metodo cambiar_edad(), que comprueba que los años no sean negativos y que los meses esten entre 0 y 11. Si los años son negativos o los meses no estan entre 0 y 11, se lanza la excepcion personalizada EdadInvalidaError. Ademas, cada mascota crea su propio historial clinico al ser registrada.

- `veterinario.py`: se define la clase Veterinario, que almacena el nombre, la identificacion, el telefono y la especialidad. Permite modificar el telefono mediante el metodo cambiar_telefono(), el cual comprueba que el nuevo telefono no sea vacio y si esta vacio lanza la excepcion personalizada TelefonoInvalidoError.

- `cita.py`: se define la clase abstracta Cita, que almacena la informacion general de las citas, como la fecha, hora, mascota, veterinario y el estado. Ademas, incluye los metodos abstractos mostrar_informacion() y cambiar_estado(), que cada tipo de cita debe implementar de acuerdo con su funcionamiento.

- `cita_general.py`: se define la clase CitaGeneral, que hereda de Cita y permite gestionar las consultas veterinarias generales. Sobrescribe los metodos mostrar_informacion() y cambiar_estado(). Cuando el estado cambia a "Completada", muestra el mensaje "Consulta general completada".

- `cita_vacunacion.py`: se define la clase CitaVacunacion, que hereda de Cita y agrega el atributo vacuna. Sobrescribe los metodos mostrar_informacion() y cambiar_estado(). Cuando el estado cambia a "Completada", muestra un mensaje con el nombre de la vacuna aplicada.

- `cita_control.py`: se define la clase CitaControl, que hereda de Cita y agrega el atributo motivo_control. Sobrescribe los metodos mostrar_informacion() y cambiar_estado(). Cuando el estado cambia a "Completada", muestra un mensaje diciendo que el control fue completado y su motivo.

- `historial_clinico.py`: se define la clase HistorialClinico, que almacena los registros medicos de cada mascota en una lista. El metodo agregar_registro() crea un objeto RegistroMedico con su fecha, diagnostico y tratamiento, y lo agrega a la lista. El metodo mostrar_informacion() recorre los registros guardados y muestra la informacion de cada uno.

- `registro_medico.py`: se define la clase RegistroMedico, se encarga de guardar la fecha, el diagnostico y el tratamiento correspondiente a cada registro medico. Ademas, cuenta con el metodo mostrar_informacion(), que muestra la informacion almacenada en el registro.

- `excepciones.py`: se definen las excepciones personalizadas CorreoInvalidoError, EdadInvalidaError y TelefonoInvalidoError, que heredan de ValueError. Se utilizan cuando se intenta establecer un correo vacio, una edad con años negativos o meses que no esten entre 0 y 11, o un telefono vacio.


## Conceptos de POO implementados

Durante el desarrollo del sistema se aplicaron diferentes conceptos de Programacion Orientada a Objetos (POO), los cuales permiten organizar el codigo mediante clases y objetos, reutilizar funcionalidades y mejorar la organizacion y el funcionamiento de las diferentes partes del sistema.


### Encapsulamiento

El encapsulamiento se utiliza en las clases Propietario, Mascota y Veterinario para controlar los cambios en algunos de sus datos.

Para esto, se utiliza un guion bajo (_) en atributos como _correo, _años, _meses y _telefono. Estos datos se pueden modificar mediante los metodos cambiar_correo(), cambiar_edad() y cambiar_telefono().

Cada metodo comprueba que los nuevos valores sean correctos. Por ejemplo, el correo y el telefono no pueden estar vacios, los años no pueden ser negativos y los meses deben estar entre 0 y 11. Si alguno de estos datos es incorrecto, el programa lanza la excepcion personalizada correspondiente.


### Herencia

La herencia se utiliza en las clases CitaGeneral, CitaVacunacion y CitaControl, las cuales heredan de la clase abstracta Cita.

Gracias a esto, las tres clases pueden utilizar los atributos de la clase Cita, como la fecha, hora, mascota, veterinario y estado, sin necesidad de definirlos nuevamente.

Ademas, cada clase cuenta con atributos especificos. Por ejemplo, CitaVacunacion agrega el atributo vacuna y CitaControl agrega el atributo motivo_control.


### Polimorfismo

El polimorfismo se aplica en las clases CitaGeneral, CitaVacunacion y CitaControl, ya que las tres utilizan los mismos metodos mostrar_informacion() y cambiar_estado(), pero cada una los ejecuta de manera diferente.

Por ejemplo, el metodo mostrar_informacion() muestra los datos correspondientes a cada tipo de cita. Por otro lado, cuando una cita cambia su estado a "Completada", el metodo cambiar_estado() muestra un mensaje diferente dependiendo de si es una cita general, de vacunacion o de control.

En main.py se demuestra el polimorfismo mediante una lista que agrupa diferentes tipos de citas y permite ejecutar sus metodos sin importar a que clase pertenece cada objeto.


### Clase abstracta

La clase Cita funciona como una clase abstracta y sirve de base para los diferentes tipos de citas veterinarias.

Esta clase define los metodos mostrar_informacion() y cambiar_estado(), pero no establece como deben funcionar en cada tipo de cita.

Por esta razon, las clases CitaGeneral, CitaVacunacion y CitaControl deben implementar estos metodos de acuerdo con sus propias necesidades. Ademas, al ser una clase abstracta, Cita no se puede utilizar para crear objetos directamente.


### Composicion

La composicion se aplica entre las clases Mascota e HistorialClinico, ya que cada mascota tiene su propio historial clinico.

Cuando se crea un objeto de la clase Mascota, tambien se crea automaticamente un objeto de la clase HistorialClinico, donde se pueden guardar los registros medicos correspondientes a esa mascota.

Ademas, la clase HistorialClinico utiliza la clase RegistroMedico para crear y almacenar los registros con su fecha, diagnostico y tratamiento.


## Instrucciones de ejecucion

Para ejecutar el sistema de clinica veterinaria, es necesario tener Python instalado en el computador.

El proyecto se puede abrir desde Visual Studio Code y ejecutar mediante la terminal, utilizando el archivo principal main.py.

### Pasos para ejecutar el programa

1. Descargar el proyecto desde el repositorio de GitHub.

2. Descomprimir el archivo descargado y abrir la carpeta ClinicaVeterinaria en Visual Studio Code.

3. Comprobar que Python este instalado ejecutando el siguiente comando en la terminal:

   `python --version`

4. Abrir la terminal de Visual Studio Code y comprobar que se encuentre en la carpeta principal del proyecto.

5. Ejecutar el archivo principal mediante el siguiente comando:

   `python main.py`

6. Cuando se ejecute el programa, la terminal mostrara la informacion de los propietarios, mascotas, veterinarios y citas creadas. Tambien se podran observar las pruebas de los metodos, los cambios de estado de las citas, las excepciones personalizadas y los registros medicos almacenados en el historial clinico.

### Requisitos

- Tener Python 3 instalado.
- Tener Visual Studio Code o un editor que permita ejecutar archivos Python.
- No es necesario instalar librerias externas, ya que el proyecto utiliza herramientas incluidas en Python.


## Diagrama de clases UML

El diagrama de clases UML muestra la estructura del sistema de clinica veterinaria, incluyendo las clases, sus atributos, metodos y las relaciones que existen entre ellas.

En el diagrama se pueden observar las relaciones de herencia entre la clase Cita y sus tres clases derivadas, asi como la composicion entre Mascota e HistorialClinico y las asociaciones entre las diferentes clases del sistema.

El diagrama de clases UML se puede ver en [draw.io](https://app.diagrams.net/#Uhttps://raw.githubusercontent.com/SebasMier/ClinicaVeterinaria/refs/heads/main/SistemaClinicoVeterinario.drawio).



## Tecnologias utilizadas

Para el desarrollo del proyecto se utilizaron las siguientes herramientas:

- **Python 3:** lenguaje de programacion utilizado para desarrollar el sistema y aplicar los conceptos de Programacion Orientada a Objetos.
- **Visual Studio Code:** editor de codigo utilizado para crear, organizar y ejecutar los archivos Python.
- **draw.io:** herramienta utilizada para elaborar el diagrama de clases UML.
- **Git:** herramienta utilizada para llevar un control de los cambios realizados durante el desarrollo del proyecto.
- **GitHub:** plataforma utilizada para almacenar el repositorio y compartir el codigo del proyecto.


## Uso de inteligencia artificial

Durante el desarrollo del proyecto se utilizo ChatGPT como herramienta de apoyo para verificar y corregir el funcionamiento del programa, resolver dudas relacionadas con Python y la Programacion Orientada a Objetos, y mejorar la presentacion visual de la informacion que se muestra en la terminal.

## Autor

Juan Sebastian Mier Acevedo


