# conversao de tipos, coercao
# type convertion, typecasting, coercion
# e o ato de converter um tipo em outro
# tipos imutaveis e primitivos:
# str, int, float, bool
print(1 + 1)
print('a' + 'b')
# Isso que esta acontecendo ali em cima e chamado de polimorfismo
# ou seja, o mesmo operador (+) esta sendo usado para fazer duas coisas diferentes
print('a' + str(1))
# O codigo acima dara um erro pois nao da pra concatenar str + int
print(int('1'), type('1'))
print(str(1234234) + 'ola')

# da pra converter valores para bool (boolean)
print(bool('')) # False
print(bool(' ')) # True (porque tem um espaco!!!!!)