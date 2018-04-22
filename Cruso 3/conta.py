class Conta:
    
    NOME_BANCO = 'BANCO'

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

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def __pode_sacar(self, valor_saque):
        valor_disponivel = self.__saldo + self.__limite
        return valor_disponivel >= valor_saque

    @staticmethod
    def codigo_banco():
        return "001"

    @property
    def numero(self):
        return self.__numero
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.__limite
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, valor):
        self.__limite = valor
    