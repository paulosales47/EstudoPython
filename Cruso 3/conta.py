class Conta:
    
    def __init__(self, numero, titular, saldo, limite= 1000.0):
        print("Construindo objeto.. {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Sado de {} do titular {}".format(self.__saldo, self.__titular))
    
    def deposita(self, valor):
        self.__saldo += valor
    
    def saca(self, valor):
        self.__saldo -= valor