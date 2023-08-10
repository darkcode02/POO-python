class Estudiante():
    def __init__(self,nombre,edad,grado) -> None:
        self.Nombre = nombre
        self.Edad = edad    
        self.Grado = grado

    def estudiar(self):
        print(f"El estudiante {self.Nombre} Esta estudiando")

        
nombre = input("Ingrese el nombre del estudiante: ")
edad = int(input("Ingrese la edad del estudiante: "))
grado = input("Ingrese el grado del estudiante: ")

estudiante1 = Estudiante(nombre, edad,grado)
estudiante1.estudiar()