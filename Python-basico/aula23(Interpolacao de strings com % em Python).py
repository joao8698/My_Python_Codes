'''
Interpolacao basica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
'''

nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preco e R$%.2f' % (nome, preco) # Colocar entre parenteses se tiver mais de um valor
# Da pra formatar agora a string e o float, so colocar a formatacao que deseja no % que esta dentro das aspas, que nem esta ali em cima
print(variavel)

# Interpolacao e a mesma coisa que a gente fez com o metodo .format() so que de um jeito diferente

# Com numeros Hexadecimais
print('O hexadecimal de %d e %04x' % (15, 15)) # %04x pra preencher as casas no resultado!

# Os tipos e os valores tem que serem iguais na interpolacao, se nao da erro
# tipo assim, va1 = 'ola', pra fazer a interpolacao tem que usar %s, que e do tipo string