num1 = 3 
num2 = 4.4
resultado = num1 + num2
print(resultado)
print(type(resultado))#lo convierte a flotante
#puedo tener un entero o un flotante y automaticamente el tipo de dato de la suma cambia


#otro
def recorrer(elemento):
    for item in elemento:
        print(f"El elemento actual es: {item}")
lista1 = [1,2,3,4,5]
lista2 = "maquina"
recorrer(lista2)
print("-----------------")
recorrer(lista1)