'''
Formatacao basica de strings
s - string
d - int
f - float
.<numero de digitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - forca o numero a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
'''

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel:.>10}') # Com esse comando ele nao preenche 10 caracteres para a esquerda, mais sim
# adiciona 7 caracteres a esquerda e como 'ABC' ja sao considerados 3 caracteres, ele so preenche pra dar
# os 10 caracteres pedidos!
print(f'{variavel:.^10}')

print(f'{1000.0325056409689468:0=+10,.1f}')
print(f'O hexadecimal de 1500 e {1500:08X}')