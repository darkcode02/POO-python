# Definición de la clase base Persona
class Persona:
    # Constructor de la clase con atributos nombre, edad y nacionalidad
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    # Método especial para representar la instancia en forma de cadena
    def __str__(self):
        return f"Tu nombre es: {self.nombre}, Tu edad: {self.edad}, Tu nacionalidad: {self.nacionalidad}"

# Definición de la clase derivada Empleado que hereda de Persona
class Empleado(Persona):
    # Constructor de la clase con atributos adicionales trabajo y salario
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        # Llamada al constructor de la clase base (Persona) usando super()
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
    
    # Método especial para representar la instancia en forma de cadena, agregando detalles de trabajo y salario
    def __str__(self):
        # Llamada al método __str__() de la clase base y luego se agrega información adicional
        return super().__str__() + f", Tu trabajo: {self.trabajo}, Tu salario: {self.salario}"

# Creación de una instancia de Persona llamada persona1
persona1 = Persona("Juan Pablo", 22, "colombiano")
# Impresión de la representación en cadena de persona1
print(persona1)

# Creación de una instancia de Empleado llamada empleado1
empleado1 = Empleado("Roberto", 21, "colombiano", "ingeniero", 1200000)
# Impresión de la representación en cadena de empleado1
print(empleado1)
