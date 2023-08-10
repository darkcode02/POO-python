#atributos

class Celular():

    #funcion iniciador
    def __init__(self,marca,modelo,camara) -> None:
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    #funcion str retorna un print(metodo)
    def __str__(self) -> str:
        return f"La marca es: {self.marca}, el modelo es: {self.modelo} y la camara es de: {self.camara} "


    def llamar(self):
        print(f"Estas haciendo un llamado desde un {self.modelo}")

    def cortar(self):
        print(f"estas cortando la llamada desde un {self.modelo}")

celular1 = Celular("Samsung","J2 Prime", "28MP")
print(celular1)
celular2 = Celular("phone","12 pro", "32MP")
print(celular2)
celular3 = Celular("Xiaomi","Poco x3 pro", "48MP")
print(celular3)
celular4 = Celular("Xiaoi","Pwdqpro", "dqwP")
print(celular4)  

celular1.llamar()
celular1.cortar()