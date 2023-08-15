# Definición de un decorador
def decorador(funcion):
    def funcion_modificada():
        print("antes de llamar a la funcion")
        funcion()  # Llama a la función original
        print("despues de llamar a la funcion")
    return funcion_modificada

# Definición de una función saludo
@decorador
def saludo():
    print("hola pablo")

# Llamada a la función saludo, que ha sido modificada por el decorador
saludo()

# Definición de otro decorador
def decorador2(funcion):
    resultado = 1 + 1
    print(f"El resultado de 1 + 1 es: {resultado}")
    funcion()

# Definición de una función restar
@decorador2
def restar():
    resultado = 1 - 1 
    print(f"El resultado de 1 - 1 es: {resultado}")

#otro ejemplos
# Definición de un decorador simple
def decorador(funcion):
    def funcion_modificada(*args, **kwargs):
        print("Ejecutando función con argumentos:", args)
        resultado = funcion(*args, **kwargs)
        print("Resultado:", resultado)
    return funcion_modificada

# Uso del decorador en una función
@decorador
def suma(a, b):
    return a + b

# Llamada a la función modificada por el decorador
suma(3, 5)
