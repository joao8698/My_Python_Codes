''' ####IMPORTANTE#### '''

frase = 'O python e uma linguagem de programacao '\
    'multiparadigma. '\
    'Python foi criado por Guido van Rossum.'

index = 0
letra_apareceu_mais_vezes = ''
quantidade_apareceu_mais_vezes = 0

while index < len(frase):
    letra_atual = frase[index]

    index += 1

    if letra_atual == ' ':
        index += 1
        continue

    quantidade_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if quantidade_apareceu_mais_vezes < quantidade_apareceu_mais_vezes_atual:
        quantidade_apareceu_mais_vezes  = quantidade_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

print(f'A letra que apareceu mais vezes foi "{letra_apareceu_mais_vezes}" que apareceu {quantidade_apareceu_mais_vezes}x')

''' ####IMPORTANTE#### '''