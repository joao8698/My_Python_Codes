'''
for in com listas
'''

lista = ['Maria', 'Helena', 'Luiz']

for nome in lista:
    print(nome)

# Voce tambem pode passar o index do valor que voce quer interar dentro da lista
# desse jeito

for nome in lista[0]:
    print(nome)

######EXERCICIO######
'''
Exiba os indices da lista
0 Maria
1 Helena
2 Luiz
'''
for i in range(len(lista)):
    print(i, lista[i])