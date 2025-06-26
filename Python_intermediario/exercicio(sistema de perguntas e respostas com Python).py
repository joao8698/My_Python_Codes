# Exercicio - sistema de perguntas e respostas

import os, time

perguntas = [
    {
        'pergunta': 'Qual e a raiz quadrada de 4?',
        'opcoes': ['4', '2', '6', '3'],
        'resposta': '2',
    },
    {
        'pergunta': 'Qual e o satelite natural da Terra?',
        'opcoes': ['Sol', 'Lua', 'Netuno', 'Saturno'],
        'resposta': 'Lua',
    },
    {
        'pergunta': 'Qual e a cor da mistura entre azul e amarelo?',
        'opcoes': ['Laranja', 'Lilas', 'Verde', 'Magenta'],
        'resposta': 'Verde'
    },
]
for pergunta in perguntas:
    print(pergunta['pergunta'])
    i = 0
    for valor, opcao in enumerate(pergunta['opcoes']):
        print(f'{valor}) {opcao}')
    user_input = input('Qual a escolha certa? --> ')
    if user_input in pergunta['resposta']:
        print('Voce acertou!!!')
        t = 3
        while t > 0:
            os.system('cls')
            print(f'Voce acertou!!!😍😎😋😎 Proxima pergunta em:')
            print(t)
            time.sleep(1)
            t -= 1
        os.system('cls')
        continue
    else:
        print('Voce errou!!!😭😭😢')
        exit()

print('Voce acertou todas as perguntas!! parabens.')