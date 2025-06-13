'''
enumerate - enumera iteraveis (indices)
'''
lista = ['Joao', 'Davi', 'Hiago']
lista.append('Pedro')

lista_enumerada = enumerate(lista)

# for item in lista_enumerada:
#     print(item)

# Geralmente voce vai usar o enumerate fora de uma variavel
# e sim dentro de um for ou qualquer outro tipo de coisa
# assim, seus valores nao se esgotarao

# for item in enumerate(lista, start=1):
#     print(item)
# for item in enumerate(lista, start= 2):
#     print(item)
# for item in enumerate(lista, start=3):
#     print(item)

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)

# # OU

# for indice, nome in enumerate(lista):
#     print(indice, nome)

#######################################

for tupla_enumerada in enumerate(lista):
    print('FOR da tupla:')
    for valor in tupla_enumerada:
        print(f'\t{valor}')