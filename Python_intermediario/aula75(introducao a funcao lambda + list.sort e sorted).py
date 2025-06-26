# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Pedro', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Dias'},
]

# lista = [1, 3, 6, 2, 4, 46, 7, 9, 8, 10]
# lista.sort()

# ou da pra mudar a ordem

# lista.sort(reverse=True)
# print(lista)
# sorted(lista) # Cria uma nova lista a partir de outra organizada

# def ordena(item):
#     return item['nome']

lista.sort(key=lambda item: item['nome'])
l1 = sorted(lista, key=lambda item: item['nome'])

def exibir(lista):
    for item in lista:
        print(item)
    print()

exibir(lista)
exibir(l1)

# for item in lista:
#     print(item)