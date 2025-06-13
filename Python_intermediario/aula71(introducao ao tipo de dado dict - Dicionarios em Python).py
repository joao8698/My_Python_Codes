# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')

pessoa = {
    'nome': 'Gabrielly',
    'sobrenome': 'Vieira',
    'idade': 18,
    'altura': 'anao',
    'peso': '2kg',
    'enderecos': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'isso aquilo', 'numero': 321}
    ]
}

pessoa2 = {
    'nome': 'Joao Luiz',
    'sobrenome': 'Machado',
    'idade': 18,
    'altura': 'Gigante',
    'peso': 'Matheus meu fih tu nao pesa uma grama'
}

# print(pessoa)
# print(pessoa2)

# Posso passar tambem nome como argumentos nomeados na hora de criar um dicionario

pessoa3 = dict(nome='Pedrin', sobrenome='Do pneu', idade=18, altura=1.67, peso='44kg')

print(pessoa['nome'])

# o dicionario no Python por si nao e um iteravel, mas se utilizarmos o for nele, o iterador nos entregara as chaves dentro do dict

# for chave in pessoa:
#     print(chave)

# se quiser pegar tambem o valor, pode fazer o seguinte jeito:

for chave in pessoa:
    print(chave, pessoa[chave])