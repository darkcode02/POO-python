# Definición de la clase Persona
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola, estoy hablando un poco")

# Definición de la clase Artista
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        print(f"Mi habilidad es: {self.habilidad}")

# Definición de la clase EmpleadoArtista que hereda de Persona y Artista
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        # Llamamos a los constructores de Persona y Artista para inicializar atributos de ambas clases
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        # Llamamos al método mostrar_habilidad() de la clase Artista usando super()
        return super().mostrar_habilidad()

# Creación de una instancia de EmpleadoArtista
EmpleadoArtista1 = EmpleadoArtista("Juan Pablo", 22, "colombiano", "dibujar", 4000000, "miEmpresa")

# Llamada al método presentarse() en la instancia EmpleadoArtista1
EmpleadoArtista1.presentarse()

#saber si esta clase hereda de otra
herencia = issubclass(EmpleadoArtista, Artista)
print(herencia)

#saber si una variable es una instancia de una clase en especifico
instancia = isinstance(EmpleadoArtista1,EmpleadoArtista)
print(instancia)