# Definición de la clase Persona
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Atributo protegido (_nombre)
        self._edad = edad      # Atributo protegido (_edad)

    # Método getter para obtener el nombre
    def get_nombre(self):
        return self._nombre

    # Método setter para establecer el nombre
    def set_nombre(self, new_nombre):
        self._nombre = new_nombre

# Crear una instancia de la clase Persona
pablo = Persona("juan pablo", 22)

# Obtener y mostrar el nombre utilizando el método getter
nombre = pablo.get_nombre()
print(nombre)

# Establecer un nuevo nombre utilizando el método setter
pablo.set_nombre("lucian")

# Obtener y mostrar el nombre actualizado utilizando el método getter
nombre = pablo.get_nombre()
print(nombre)

print("=======================================")

# Definición de la clase Persona con getters y setters utilizando decoradores
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo encapsulado (__nombre)
        self.__edad = edad      # Atributo encapsulado (__edad)

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if len(nuevo_nombre) > 0:
            self.__nombre = nuevo_nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.__edad = nueva_edad

# Crear una instancia de la clase Persona
persona = Persona("Juan", 30)

# Acceder a los atributos encapsulados a través de los getters
print("Nombre:", persona.nombre)
print("Edad:", persona.edad)

# Modificar los atributos encapsulados a través de los setters
persona.nombre = "Carlos"
persona.edad = 25

# Imprimir los atributos actualizados utilizando los getters
print("Nuevo nombre:", persona.nombre)
print("Nueva edad:", persona.edad)
