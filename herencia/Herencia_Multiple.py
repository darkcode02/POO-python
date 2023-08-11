class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola, estoy hablando un poco")


class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        print(f"Mi habilidad es: {self.habilidad}")


class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)  # Agregamos "self" aquí
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        return super().mostrar_habilidad()  # Eliminamos el return y el f-string


EmpleadoArtista1 = EmpleadoArtista("Juan Pablo", 22, "colombiano", "dibujar", "programador", 4000000)

EmpleadoArtista1.presentarse()
