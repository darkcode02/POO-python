class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_informacion(self):
        print(f"Producto: {self.nombre}")
        print(f"Precio: ${self.precio}")
        print(f"Cantidad disponible: {self.cantidad}\n")

class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado a la tienda.")

    def mostrar_productos(self):
        print(f"Productos en la tienda '{self.nombre}':")
        for producto in self.productos:
            producto.mostrar_informacion()

# Ejemplo de uso
mi_tienda = Tienda("Mi Tienda")

producto1 = Producto("Camiseta", 20.0, 50)
producto2 = Producto("Pantalón", 30.0, 30)

mi_tienda.agregar_producto(producto1)
mi_tienda.agregar_producto(producto2)

mi_tienda.mostrar_productos()
