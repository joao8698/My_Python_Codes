nome = 'Joao Luiz'
altura = 1.70
peso = 60
imc = peso / (altura * altura)
# ou da pra tirar proveito da precedencia
imc = peso / altura ** 2

print(nome, 'tem', altura, 'de altura, seu peso e de', peso, 'kilos e seu IMC (indice de massa corporal) e', imc)

# IMC e calculado pela seguinte formula --> IMC = peso / (altura x altura)

# OBS: nome_variavel = ... os tres pontinhos na variavel e chamado de elipses
# elipses e usado para varias coisas
# uma delas e que ele pode ser usado como place holder