'''
Introducao a List comprehension em Python
List comprehension e uma forma rapida para criar listas a partir de iteraveis
'''

# print(list(range(10)))

lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [numero for numero in range(10)]
print(lista)

# Eu tambem posso colocar qualquer condicao ou operacao dentro dessa list comprehension

lista = [numero * 2 for numero in range(10)]
print(lista)