import math

# Exercício 1 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Escreva uma função que receba uma lista de números e retorne outra lista com os números ímpares.
def impares(lst):
    lista_impar = []
    for i in lst:
        if i % 2 == 1:
            lista_impar.append(i)
    return lista_impar

# Exercício 2 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Escreva uma função que receba uma lista de números e retorne outra lista com os números primos presentes.
def primos(lst):
    lst.sort()
    lista_primos = []
    for i in lst:
        if i < 2:
            continue
        flag_primo = True
        for j in range(2, math.ceil(math.sqrt(i))):
            if i % j == 0:
                flag_primo = False
                break
        if flag_primo:
            lista_primos.append(i)
    return lista_primos

# Exercício 3  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Escreva uma função que receba duas listas e retorne outra lista com os elementos que estão presentes em apenas uma das listas.
def exclusivos(lst1, lst2):
    lista = []
    for i in lst1:
        if i not in lst2:
            lista.append(i)
    for j in lst2:
        if j not in lst1:
            lista.append(j)
    lista.sort()
    return lista

# Exercício 4 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Dada uma lista de números inteiros, escreva uma função para encontrar o segundo maior valor na lista.
def segundo_maior(lst):
    exclusivos = set(lst)
    exclusivos.remove(max(exclusivos))
    return max(exclusivos)

# Exercício 5 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Crie uma função que receba uma lista de tuplas, cada uma contendo o nome e a idade de uma pessoa,
# e retorne a lista ordenada pelo nome das pessoas em ordem alfabética.
def alfabetica(lst):
    lst.sort(key=lambda x: x[0])
    return lst