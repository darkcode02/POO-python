class Persona:
    def __init__(self,nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad 
    def mostrar(self):
        print(f"El nombre es: {self.nombre}\nla edad es: {self.edad}")

class Estudiante(Persona):
    def __init__(self, nombre, edad,grado) -> None:
        super().__init__(nombre, edad)
        self.grado = grado

    def grado_estudiante(self):
        print(f"El grado es: {self.grado}")


estudiante1 = Estudiante("Juan Pablo", 16, "sexto de secundaria")
estudiante1.mostrar()
estudiante1.grado_estudiante()
