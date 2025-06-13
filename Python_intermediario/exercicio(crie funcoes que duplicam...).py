'''
Exercicio: crie funcoes que duplicam, triplicam e quadruplicam o numero recebido como parametro
'''

# def duplicar(numero):
#     return numero * 2

# def triplicar(numero):
#     return numero * 3

# def quadruplicar(numero):
#     return numero * 4

# user_input = input('Voce quer:\n' \
# '[1] duplicar\n' \
# '[2] triplicar\n' \
# '[3] quadruplicar\n' \
# 'um numero? --> ')

# if user_input == '1':
#     user_input = input('Qual numero voce deseja duplicar?: ')
#     print(duplicar(int(user_input)))

# elif user_input == '2':
#     user_input = input('Qual numero voce deseja triplicar?: ')
#     print(triplicar(int(user_input)))

# elif user_input == '3':
#     user_input = input('Qual numero voce deseja quadruplicar?: ')
#     print(quadruplicar(int(user_input)))

# da pra criar uma funcao multiplicadora que cria funcoes

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)

print(duplicar(2))