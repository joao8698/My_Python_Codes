# A funcao input coleta dados inseridos pelo usuario
# podemos armazenar esses dados dentro de variaveis, desse jeito

_nome_ = input('Qual o seu nome?: ')

print(f'Seu nome e: {_nome_=}')

# Da pra pegar o valor da variavel junto com o nome dela apenas coloquando um sinal de = no junto do nome da variavel

# Se quisermos fazer um calculo entre dois numeros, utilizando a funcao input()
# teriamos que converter os valores inseridos em int (ou float), pois a funcao input()
# sempre retorna uma str (string), independentemente se voce inserir numeros dentro dela
# desse jeito

numero_1 = input('Digite um numero: ')
numero_2 = input('Digite outro numero: ')
print(f'O valor do calculo entre eles e igual a: {numero_1 + numero_2}')
# Nesse caso o resultado ira ser 15 (se voce digitou 1 e 5) pois ele esta concatenando as duas strings, devido ao fato de que
# nao convertemos (fizemos a coercao) dos inputs

# O jeito certo seria esse

numero_1 = int(input('Digite um numero: '))
numero_2 = int(input('Digite outro numero: '))
print(f'O valor do calculo e igual a: {numero_1 + numero_2}')
# Aqui o resultado vai ser 20 (se voce digitou 10 e 10), porque fizemos a coercao dos inputs