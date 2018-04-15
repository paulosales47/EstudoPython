## VARIÁVEIS / PRINT

# dia=6
# mes=4
# ano=2018
# print(dia, mes, ano, sep="/")

## TYPE

# quantidade = 10
# type(quantidade)
# valor = 7.9
# type(valor)
# texto = "Aula 01"
# type(texto)

## IF / ELIF / ELSE

# numero = 50

# if(numero > 50):
#     print("Numero maior que 50")
# elif(numero < 50):
#     print("Numero menor que 50")
# else:
#     print("Numero é igual a 50")

## WHILE

# numero = 0

# while(numero < 100):
#     print(numero)
#     numero += 1

## FOR / RANGE

# for numero in range(1, 10):
#     print(numero)

## INTERPOLAÇÃO DE STRING

# lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for numero in lista_numeros:
#     print("Numero {} de 10".format(numero))

## RANGE 2

# for numero in range (0, 1000, 10):
#     print("Numero {} de 1000".format(numero))

## CONTINUE

# for numero in range(1, 100):
#     if(numero%2 == 0):
#         continue
#     elif(numero%3 == 0):
#         continue
#     elif(numero%5 == 0):
#         continue
#     elif(numero%7 == 0):
#         continue

#     print("Numero igual a {}".format(numero))

## BREAK

# for numero in range(1, 10):
#     valor_informado = int(input("Informe um valor entre 1 e 10\n"))

#     if(valor_informado > 10 or valor_informado < 1):
#         print("O valor informado é invalido")
#         break

#     print("O numero informado é {}".format(valor_informado))

## INTERPOLAÇÃO DE STRING 2

# for tentativa in range(1, 11):
#     print("{0}° - Tentativa de {0} de {1} ".format(tentativa, 10))

# print("R$ {:f}".format(1.59))
# print("R$ {:.2f}".format(1.59))

# print("R$ {:05.2f}".format(8.45))
# print("R$ {:06.2f}".format(8.45))
# print("R$ {:07.2f}".format(8.45))
# print("R$ {:05.2f}".format(18.45))

# print("R$ {:05d}".format(58))
# print("R$ {:05d}".format(457))
# print("R$ {:05d}".format(7894))

# print("Data {:02d}/{:02d}/{:4d}".format(9,4,2018))

## RANDOM / ROUND

# import random

# print(random.random())

# numero_aleatorio = random.random() * 100

# print(int(numero_aleatorio))
# print(round(numero_aleatorio))

## RANDRANGE / SEED

# import random

# print(random.randrange(1,101)) ## 1 e 100
# print(random.randrange(101)) ## 0 e 100 

# random.seed(1,101)
# print(random.randrange(101)) 
# random.seed(1,101)
# print(random.randrange(101)) 

## ABS

# print(abs(-50))
# print(abs(50))

## ROUND 2


# print(round(3.5)) # 4
# print(round(4.5)) # 4
# sempre arredonda para o próximo valor par

## OPERAÇÃO DE DIVISÃO

print( 3 / 2) # float
print( 3 // 2) # int

## UTILIZANDO VARIOS ARQUIVOS
# import arquivoA
# import arquivoB

# arquivoA.func_a()
# arquivoB.func_b()


## FUNÇÕES 

# def soma(num_a, num_b):
#     return num_a + num_b

