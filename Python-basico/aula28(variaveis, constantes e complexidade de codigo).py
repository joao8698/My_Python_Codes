'''
CONSTANTE = "Variaveis" que nao vao mudar
Muitas condicoes no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
'''
velocidade = 61 # velocidade atual do carro
local_carro = 101 # local em que o carro esta na estrada

RADAR_1 = 60 # velocidade maxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 esta
RADAR_RANGE = 1 # a distancia onde o radar pega

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_1) and \
local_carro <= (LOCAL_1 + RADAR_RANGE)

if velocidade_carro_passou_radar_1:
    print('Velocidade carro passou do radar 1')
else:
    print('Carro na velocidada permitida')

if carro_multado_radar_1 and \
velocidade_carro_passou_radar_1:
    print('Carro multado em radar 1')

# Existe um tipo de convencao no Python onde se voce quiser
# que uma variavel seja constante (coisa que nao existe no python como padrao)
# voce escreve o nome da variavel so com letras MAIUSCULAS

# Para quebrar a linha de um codigo use a barra invertida \
# desse jeito
# print() blablabla \
# print....

# Variaveis nao servem para resumir o seu codigo
# e sim, deixa-lo mais legivel