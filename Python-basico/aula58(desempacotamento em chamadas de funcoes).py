# Desempacotamento em chamadas
# de metodos e funcoes
string = 'ABCD'
lista = ['Maria', 'Helena', 'Eduarda']
tupla = 'Python', 'e', 'legal'
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1         2
    ['Luiz', 'Joao', 'Eduarda', (0, 10, 20, 30, 40)],  # 2
]

# a, b, c = lista
# print(a, b)

# p, b, *_, ap, u = lista
# print(p, u, ap)

# for nome in lista:
#     print(nome, end=' ')

# print('Maria', 'Helena', 'Eduarda')
# print(*lista) # Fazer isso e a mesma coisa que fazer o print da linha acima
# print(*string)
# print(*tupla)

print(*salas, sep='\n',end='\n')