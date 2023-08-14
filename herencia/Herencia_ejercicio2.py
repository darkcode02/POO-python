class Animal:
    def comer(self):
        print("El animal esta comiendo")
class Ave(Animal):
    def volar(self):
        print("El animal esta Volando")
class Mamifero(Animal):
    def correr(self):
        print("El animal esta corriendo")
        
class Murcielago(Mamifero, Ave):
    pass

murcielago = Murcielago()
murcielago.comer
murcielago.volar
murcielago.correr

print(Murcielago.mro())