#realizar una interfaz simple que internamente cumple una funcion compleja
class Auto():
    def __init__(self) -> None:
        self.estado = "Apagado"
    def encender(self):
        self.estado = "Prendido"
    
    def conducir(self):
        if self.estado == "Prendido":
            print("Conduciendo")
        else: 
            print("debe encender el auto para conducir")


auto1 = Auto()
auto1.encender()
auto1.conducir()

#como podemos observar las personas o los desarrolladores que miren este sencillo programa
#solo tienen que utilizar los metodos, esto genera la abstraccion por que ellos
# no saben que funcionamiento hay detras de todo esto

