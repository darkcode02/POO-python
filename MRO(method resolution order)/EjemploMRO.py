"""
MRO (Method Resolution Order), que significa 
"Orden de Resolución de Métodos" en español, 
se refiere a cómo Python determina el orden en el que se buscan y 
ejecutan los métodos en una jerarquía de clases durante la
 herencia múltiple en la programación orientada a objetos (POO).

En Python, una clase puede heredar de múltiples clases. 
Esto puede resultar en situaciones en las que una clase 
tiene varios ancestros con métodos del mismo nombre. 
El MRO es el algoritmo utilizado para resolver este 
tipo de conflictos y determinar el orden en que se 
deben buscar y ejecutar los métodos en la cadena de herencia.
"""
# Definición de la clase Persona
class A:
    def method(self):
        print("Method of class A")

class B(A):
    def method(self):
        print("Method of class B")

class C(A):
    def method(self):
        print("Method of class C")

class D(B, C):
    pass

d = D()
d.method()

print(D.mro())
