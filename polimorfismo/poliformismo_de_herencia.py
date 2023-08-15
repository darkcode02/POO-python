class Animal():
    def sonido(self):
        pass

class Gato(Animal):
    def sonido(self):
        return "miau"

class Perro(Animal):
    def sonido(self):
        return "guau"

def hacer_sonido(animal):
    print(animal.sonido())

gato = Gato()
perro = Perro()

print(gato.sonido())
print(perro.sonido())

hacer_sonido(perro)


#other example
class Forma():
    def area(self):
        pass

class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        import math
        return math.pi * self.radio ** 2

def calcular_area(forma):
    print("Área:", forma.area())

cuadrado = Cuadrado(5)
circulo = Circulo(3)

calcular_area(cuadrado)
calcular_area(circulo)
