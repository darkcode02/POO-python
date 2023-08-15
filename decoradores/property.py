# Define una clase llamada Persona
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo encapsulado (__nombre)
        self._edad = edad       # Atributo protegido (_edad)

    @property
    def nombre(self):
        return self.__nombre   # Getter para el atributo __nombre

    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre  # Setter para el atributo __nombre

    @nombre.deleter
    def nombre(self):
        del self.__nombre  # Deleter para el atributo __nombre

# Crear una instancia de la clase Persona
pablo = Persona("pablito", 22)

# Obtener y mostrar el nombre utilizando el getter
nombre = pablo.nombre
print(nombre)

# Establecer un nuevo nombre utilizando el setter
nombre = pablo.nombre = "pepe"
print(nombre)

# Usar el deleter para eliminar el atributo __nombre
del pablo.nombre  # La propiedad deleter nos permite usar 'del'
