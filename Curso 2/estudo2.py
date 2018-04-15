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

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

numeros.add(10) # NÃO IRÁ ADICIONAR, POIS JÁ EXISTE

print(numeros)