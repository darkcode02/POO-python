class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.__titular = titular
        self.__saldo = saldo_inicial

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, nuevo_saldo):
        if nuevo_saldo >= 0:
            self.__saldo = nuevo_saldocd
        else:
            print("Saldo no válido")

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito de {cantidad} realizado. Saldo actual: {self.__saldo}")
        else:
            print("Cantidad no válida para depósito")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.__saldo:
        #if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro de {cantidad} realizado. Saldo actual: {self.__saldo}")
        else:
            print("Cantidad no válida para retiro o saldo insuficiente")

# Crear una instancia de la clase CuentaBancaria
mi_cuenta = CuentaBancaria("Juan", 1000)

# Consultar el titular y el saldo utilizando los getters
print("Titular:", mi_cuenta.titular)
print("Saldo actual:", mi_cuenta.saldo)

# Modificar el saldo utilizando el setter
mi_cuenta.saldo = 1500

# Realizar operaciones de depósito y retiro
mi_cuenta.depositar(500)
mi_cuenta.retirar(200)

# Consultar el saldo actualizado
print("Saldo actual:", mi_cuenta.saldo)
