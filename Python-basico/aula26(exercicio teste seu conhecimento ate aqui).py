"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome_input = input('Digite seu nome: ')
idade_input = input('Digite sua idade: ')

nome = nome_input
idade = idade_input

if nome and idade:
    print(f'Seu nome e {nome}')
    print(f'Seu nome invertido e {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contem espacos')
    else:
        print('Seu nome nao contem espacos')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome e {nome[:1]}')
    print(f'A ultima letra do seu nome e {nome[len(nome)-1]}')
else:
    print('Desculpe, voce deixou campos vazios!')