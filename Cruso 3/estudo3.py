from conta import Conta

# conta = Conta()

# print(conta)


# TESTANDO CONSTRUTOR

#conta = Conta()

# conta = Conta(1, "Paulo Henrique", 1000.0, 5000.0)


# PARAMETRO OPCIONAL NO CONSTRUTOR

# conta = Conta(1, "CONTA 1", 1000.0, 5000.0)

# conta2 = Conta(1, "CONTA 2", 1200.0)

#FUNÇÕES

# conta3 = Conta(3, "CONTA 3", 500.0, 1500.0)

# conta3.extrato()
# conta3.deposita(100.0)
# conta3.extrato()

#EXERCICIO

# from datas import Data

# data = Data(1, 4, 2018)
# data.formatada()

# ENCAPSULAMENTO

# conta4 = Conta(4, "CONTA 4", 500.0, 1500.0)

# print(conta4._Conta__limite)

# conta4._Conta__limite = 1000

# # adiciona novo atributo a instancia
# conta4.novo_atributo = 50

# print(conta4._Conta__limite)

# REFERENCIA COMO PARAMETRO

# conta5 = Conta(5, "CONTA 5", 500.0, 1500.0)
# conta6 = Conta(6, "CONTA 6", 1800.0, 7500.0)

# conta6.transfere(350, conta5)
# conta5.extrato()
# conta6.extrato()

# ANOTAÇÕES PROPERTY E SETTER

# from clientes import Cliente

# cliente = Cliente("Paulo")

# print(cliente.nome)

# cliente.nome = "Paulo Henrique"

# print(cliente.nome)


# MÉTODO PRIVADO

# conta7 = Conta(7, "CONTA 7", 4500.0, 8000.0)

# print(conta7._Conta__pode_sacar(9000))

# MÉTODO ESTATICO

# print(Conta.codigo_banco())

# ATRIBUTO ESTATICO

print(Conta.NOME_BANCO)





