primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor:')

if primeiro_valor > segundo_valor:
    print(f'O primeiro valor e maior que o segundo valor ({primeiro_valor} e {segundo_valor})')
elif primeiro_valor < segundo_valor:
    print(f'O primeiro valor e menor que o segundo valor ({primeiro_valor} e {segundo_valor})')
else:
    print(f'Os dois valores sao iguais ({primeiro_valor} e {segundo_valor})')