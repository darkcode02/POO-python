# Definición de la clase Persona
class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

    def __str__(self) -> str:
        return f"Persona(nombre={self.nombre}, edad: {self.edad})"
    
    def __repr__(self) -> str:
        return f"Persona(nombre={self.nombre}, edad: {self.edad})"

# Creación de una instancia de la clase Persona
pablo = Persona("Juan Pablo", 22)

# Imprimir la representación legible de la instancia usando el método __str__
print(pablo)

# Obtener la representación de cadena cruda (raw string) de la instancia usando el método __repr__
repre = repr(pablo)

# Evaluar la cadena cruda para crear una nueva instancia de Persona
resultado = eval(repre)

# Imprimir la edad de la nueva instancia
print(resultado.edad)
