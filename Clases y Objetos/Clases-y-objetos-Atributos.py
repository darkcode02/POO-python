#atributos

class Celular():

    #funcion iniciador
    def __init__(self,marca,modelo,camara) -> None:
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    #funcion str retorna un print
    def __str__(self) -> str:
        return f"La marca es: {self.marca}, el modelo es: {self.modelo} y la camara es de: {self.camara} "

celular1 = Celular("Samsung","J2 Prime", "28MP")
print(celular1)
