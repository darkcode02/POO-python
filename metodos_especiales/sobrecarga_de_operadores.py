# Definición de la clase Persona
class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
        
    # Método para mostrar una representación legible del objeto
    def __str__(self) -> str:
        return f"Persona(nombre={self.nombre}, edad: {self.edad})"
    
    # Método para generar una representación cruda del objeto
    def __repr__(self) -> str:
        return f'Persona("{self.nombre}", {self.edad})'
    
    # Método especial para la operación de suma entre dos objetos Persona
    def __add__(self, otro):
        nuevo_valor = self.edad + otro.edad
        nuevo_nombre = self.nombre + " " + otro.nombre
        return Persona(nuevo_nombre, nuevo_valor)

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

# Crear otra instancia de Persona
pedro = Persona("Pedro", 21)

# Realizar una operación de suma entre dos objetos Persona usando el método __add__
resultado = pablo + pedro

# Imprimir el resultado de la operación de suma
print(resultado)
