'''
Fatiamento de strings
 012345678
 Ola mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a funcao len retorna a qtd
de caracteres da str
'''

variavel = 'Ola mundo'
print(variavel[5])
print(variavel[:5])
print(len(variavel[5]))
print(variavel[2:6])
print(variavel[:])
print(variavel[2:])
print(variavel[0:len(variavel):2])
print(variavel[::-1])