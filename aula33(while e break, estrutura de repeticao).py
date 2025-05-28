'''
Repeticoes
while (enquanto)
Executa uma acao enquanto uma condicao for True
Loop infinito --> quando um codigo nao tem fim
'''
condicao = True

while condicao:
    nome = input('Qual seu nome? --> ')

    if nome == 'sair':
        break # Procura o laco mais proximo e faz ele "sair" (para de executar o while)

    print(f'Seu nome e {nome}')

print('Voce saiu!')

# Texto de codigo unreachable
# e quando um trecho de codigo nunca e executado, devido a um loop infinito que vem antes dele
# exemplo

'''
while True:
    print('Ola')
print('saiu') ----> esse trecho de codigo nunca vai ser executado porque o while nunca vai acabar!
'''

contador = 0

while contador < 10:
    contador = contador + 1
    print(contador)