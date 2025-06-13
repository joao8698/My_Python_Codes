'''
Listas em Python
Tipo list - Mutavel
Suporta varios valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento
Metodos uteis: append, insert, pop, del, clear, extend, +
'''
#        01234
#       -54321
string = 'ABCDE'  # 5 caracteres (len)

# INDECES NA LISTA  0          1            2
#                  -3         -2           -1
jogos_favoritos = ['Warzone', 'Minecraft', 'Dayz',] # ''
print(bool(jogos_favoritos))
print(jogos_favoritos[0])
print(jogos_favoritos[1].upper())
# print(lista, type(lista))

jogos_favoritos[0] += ' Eu gosto'

print(jogos_favoritos)

jogos_favoritos[0] = 'Jogo que estressa'

print(jogos_favoritos)