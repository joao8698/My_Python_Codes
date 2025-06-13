'''
Argumentos nomeados e nao nomeados em funcoes Python
Argumento nomeado tem nome com sinal de igual
Argumento nao nomeado recebe apenas o argumento (valor)
'''
def soma(x, y, z):
    # Definicao
    print(f'{x=} + y={y} + {z=}', '|', 'x + y + z =', x + y + z)

# print(soma(1, 2))

# soma(1, 2)
# soma(y=2, x=1)
# soma(1, 2, z=5)

# Se no comeco, quando voce estiver definindo os argumentos para os paramentros, e voce estiver difinindo como argumentos
# nao nomeados, a partir do momento que voce definir um argumento nomeado dentro do parenteses da chamada da funcao
# todos os argumentos que vierem a seguir depois desse tambem terao que ser nomeados!!!

# Ex.:

# soma(1, y=2, 5) vai estourar um erro logo de cara
soma(1, y=2, z=5)