from abc import ABC, abstractclassmethod

# Definición de la clase abstracta Persona
class Persona(ABC):
    # Constructor abstracto de la clase Persona
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, actividad) -> None:
        self.nombre = nombre
        self.edad = edad   
        self.sexo = sexo
        self.actividad = actividad

    # Método abstracto para realizar una actividad
    @abstractclassmethod
    def realizar_actividad(self):
        print("Estoy realizando una actividad")

    # Método concreto para presentar a la persona
    def presentarse(self):
        print(f"Hola me llamo: {self.nombre} y tengo {self.edad} años")

# Definición de la subclase Estudiante
class Estudiante(Persona):
    # Constructor de la subclase Estudiante
    def __init__(self, nombre, edad, sexo, actividad) -> None:
        super().__init__(nombre, edad, sexo, actividad)

    # Implementación del método realizar_actividad para Estudiante
    def realizar_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")

# Definición de la subclase Trabajador
class Trabajador(Persona):
    # Constructor de la subclase Trabajador
    def __init__(self, nombre, edad, sexo, actividad) -> None:
        super().__init__(nombre, edad, sexo, actividad)

    # Implementación del método realizar_actividad para Trabajador
    def realizar_actividad(self):
        print(f"Estoy trabajando como: {self.actividad}")

# Ejemplo para Estudiante
pablo = Estudiante("Juan Pablo", 22, "Masculino", "Programación")
pablo.realizar_actividad()

# Ejemplo para Trabajador
javier = Trabajador("Javier Velázquez", 38, "Masculino", "Obrero")
javier.realizar_actividad()

# Crear una instancia de Persona directamente (esto dará un error ya que Persona es abstracta)
# persona = Persona("Ana", 30, "Femenino", "Ninguna")

# Crear un estudiante y usar sus métodos
ana = Estudiante("Ana", 20, "Femenino", "Ingeniería")
ana.presentarse()  # Imprime: "Hola me llamo: Ana y tengo 20 años"
ana.realizar_actividad()  # Imprime: "Estoy estudiando: Ingeniería"

# Crear un trabajador y usar sus métodos
juan = Trabajador("Juan", 28, "Masculino", "Carpintero")
juan.presentarse()  # Imprime: "Hola me llamo: Juan y tengo 28 años"
juan.realizar_actividad()  # Imprime: "Estoy trabajando como: Carpintero"

# Utilizar polimorfismo: almacenar diferentes tipos de personas en una lista
personas = [ana, juan]

for persona in personas:
    persona.presentarse()
    persona.realizar_actividad()

# Salida esperada:
# Hola me llamo: Ana y tengo 20 años
# Estoy estudiando: Ingeniería
# Hola me llamo: Juan y tengo 28 años
# Estoy trabajando como: Carpintero
