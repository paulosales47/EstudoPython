# BOOL

# var_bool = True
# print(type(var_bool))

# print(bool(0)) # false
# print(bool("")) # false
# print(bool(None)) # false

# print(bool(1)) # true
# print(bool(-100)) # true
# print(bool(13.5)) # true
# print(bool("teste")) # true


# FIND

# palavra = "Paulo Henrique"

# index = palavra.find("H")
# print(index) # 6

# index = palavra.find("h")
# print(index) # -1

# FOR STR

# palavra = "Paulo Henrique"

# for letra in palavra:
#     print(letra)

# CAPITALIZE

# print("paulo".capitalize()) #"Paulo"

# ENDSWITH

# print("teste".endswith("te")) # true
# print("teste".endswith("ta")) # false

#UPPER / LOWER

# print("teste".upper())
# print("TESTE2".lower())

# STRIP

# print("           A              ".strip())

# LIST

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 512]

# print(type(lista))
# print(4 in lista) # true
# print(max(lista))
# print(min(lista))
# print(len(lista))


# TUPLE

# dias_semana = ('seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom') #IMUTÁVEL

# print(type(dias_semana))

# LIST PARA TUPLE

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# vat_tuple = tuple(numeros)

# TUPLE PARA LIST

# numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# vat_list = list(numeros)

# SET

# numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# numeros.add(10) # NÃO IRÁ ADICIONAR, POIS JÁ EXISTE

# print(numeros)

# LIST DENTRO DE TUPLE

# d1 = [1, "Seg"]
# d2 = [2, "Ter"]
# d3 = [3, "Qua"]

# dias_semana = (d1, d2, d3)

# print(dias_semana)


# DICTIONARY

# dias_semana = {1 : 'Seg', 2 : 'Ter', 3 : 'Qua'}

# print(type(dias_semana))


# LIST COMPREHENSION

# palavra = "Paulo Henrique"

# list_palavra = ["_" for letra in palavra]

# print(list_palavra)

# list_numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list_numero_quadrado = [pow(numero,2) for numero in list_numero]

# print(list_numero)
# print(list_numero_quadrado)

# ARQUIVOS ESCRITA

# script = open("palavras.txt", "w")
# script.write("Curso Python\n")
# name = script.name
# script.close()

#ARQUIVOS LEITURA

# script = open("palavras.txt", "r")

# print(script.read())

# for linha in script:
#     print(linha, end="")

# script.close()


#RANDOMRANGE
# import random

# arquivo = open("palavras.txt", "r")
# itens = []

# for linha in arquivo:
#     linha = linha.strip()
#     itens.append(linha)

# arquivo.close()

# numero = random.randrange(0, len(itens))
# item_aleatorio = itens[numero]

# print(item_aleatorio)

# PARAMETRO OPCIONAL

def mutiplica(num_a = 0, num_b = 0):
    return num_a * num_b

mutiplica()