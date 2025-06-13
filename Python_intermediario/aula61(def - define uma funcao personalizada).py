'''
Introducao as funcoes (def) em Python
Funcoes sao trechos de codigo usados para
replicar determinada acao ao longo do seu codigo
Elas podem receber valores para parametros (argumentos)
e retornar um valor especifico.
Por padrao, as funcoes Python retornam None (nada)
'''
# print('Varias vezes')

# def Print():
#     print('Varias vezes!')

# Print()

# def Print(a, b, c):
#     print('Varias1')
#     print('Varias2')
#     print('Varias3')
#     print('Varias4')
#     print('Varias5')

# def imprimir(a, b, c):
#     print(a)
#     print(b)
#     print(c)

# imprimir(1, 2 ,3)
# imprimir('Maria', 'Joao', 5)

def saudacao(nome= 'Sem nome'):
    print('Bem-vindo', nome)

# user_input = input('Por favor digite seu nome: ')

# saudacao(user_input)

saudacao('Joao')
saudacao()