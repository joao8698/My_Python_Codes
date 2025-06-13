# Exercicio com funcoes

# Crie uma funcao que multiplica todos os argumentos
# nao nomeados recebidos
# Retorne o total para uma variavel e mostre o valor
# da variavel

# Crie uma funcao que fala se um numero e par ou impar.
# Retorne se o numero e par ou impar.

# Exercicio 1:

def multiplicador(*args):
    resultado = 1
    for valor in args:
        resultado *= valor
    return resultado

total = multiplicador(1, 2, 3, 4, 5)

print(total)

# Exercicio 2:

def par_ou_impar(x):
    if x % 2 == 0:
        return f'{x} e par'
    return f'{x} e impar'

print(par_ou_impar(2))
print(par_ou_impar(3))