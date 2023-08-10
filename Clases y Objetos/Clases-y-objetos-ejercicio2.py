class Contacto:
    def __init__(self, nombre, apellido, telefono, email):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)
        print("Contacto agregado con éxito.")

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                print(f"Detalles del contacto '{nombre}':")
                print(f"Nombre: {contacto.nombre}")
                print(f"Apellido: {contacto.apellido}")
                print(f"Teléfono: {contacto.telefono}")
                print(f"Email: {contacto.email}")
                return
        print(f"No se encontró ningún contacto con el nombre '{nombre}'.")

    def listar_contactos(self):
        print("Lista de contactos:")
        for contacto in self.contactos:
            print(contacto.nombre)

    def eliminar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                self.contactos.remove(contacto)
                print(f"Contacto '{nombre}' eliminado.")
                return
        print(f"No se encontró ningún contacto con el nombre '{nombre}'.")

# Ejemplo de uso
agenda = Agenda()

contacto1 = Contacto("Juan", "Perez", "123456789", "juan@example.com")
contacto2 = Contacto("Maria", "Gomez", "987654321", "maria@example.com")

agenda.agregar_contacto(contacto1)
agenda.agregar_contacto(contacto2)

agenda.listar_contactos()
agenda.buscar_contacto("Juan")
agenda.eliminar_contacto("Maria")

agenda.listar_contactos()
