"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra_secreta = 'abacaxi'
palavras_acertadas = ''
tentativas = 15

print('Bem-vindo ao jogo da palavra secreta\n' \
'voce tem que acertar qual e a palavra em 15 tentativas!\n' \
'digite apenas uma letra na tela, ou... se ja\n' \
'souber qual e a palavra, apenas digite ela inteira e pressione\n' \
'enter!')

while tentativas >= 1:
    user_input = input('Qual a letra? --> ')

    if user_input not in palavra_secreta:
        tentativas -= 1
        print(f'Errou, menos uma tentativa, voce tem {tentativas} tentativas!')
        continue

    if user_input == palavra_secreta:
        print(f'A palavra era {palavra_secreta}. Voce acertou a palavra, parabens!')
        break

    if user_input in palavra_secreta:
        palavras_acertadas += user_input

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in palavras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    if palavra_formada == palavra_secreta:
        print(f'A palavra era {palavra_secreta}. Voce acertou a palavra, parabens!')
        break
        
    print(palavra_formada)
else:
    print('Acabou suas tentativas!')