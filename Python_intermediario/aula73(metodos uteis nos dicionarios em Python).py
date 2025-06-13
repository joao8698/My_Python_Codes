'''
Metodos uteis em dicionarios em Python
len - quantas chaves
keys - iteravel com as chaves
values - iteravel com os valores
item - iteravel com as chaves e valores
setdefault - adiciona valor se a chave nao existe
copy - retorna uma copia rasa (shallow copy)
get - obtem uma chave
pop - apaga um item com a chave especificada (del)
popitem - apaga o ultimo item adicionado
update - atualiza um dicionario com outro
'''
pessoa = {
    'nome': 'Gabrielly',
    'sobrenome': 'Ensfeld',
    'idade': 18,
    # 'altura': 1.51
}

############len################

print(pessoa.__len__())

print(len(pessoa))

# Se eu criar varias chaves com nomes iguais, eu vou continuar tendo a mesma quantidade de chaves
# porque a cada criacao de uma chave com nome igual a outra, eu atualizo apenas o valor da chave
# Ex.:

exemplo = {
    'chave': '1',
    'chave': '2',
    'chave': '3'
}

print(len(exemplo), exemplo['chave'])

#################################

#########keys####################

print(pessoa.keys())

print(tuple(pessoa.keys())[0])
# ou
print(list(pessoa.keys())[0])

#########values###################

print(pessoa.values())
print(list(pessoa.values()))

########items#####################

print(pessoa.items())
print(list(pessoa.items()))
print(list(pessoa.items())[0][1])

#####utilizando o for no dict#############

for valor in pessoa.values():
    print(valor)

for chave in pessoa.keys():
    print(chave)

for chave, valor in pessoa.items():
    print(chave, valor)

##########setdefault############

pessoa.setdefault('altura', 'Sem idade')

print(pessoa['altura'])


############ shallow copy ##################

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [1, 2, 3]
}

# d2 = d1 # o sinal de atribuicao apenas faz com que o dict d2 aponte para o mesmo dicionario que o d1

# # tanto que se eu tentar alterar d2, d1 tambem sera alterado

# d2['c1'] = 100

# print(d1)

d2 = d1.copy() # copia o dict de d1 para d2 sendo um novo dicionario

# agora se eu alterar d2, d1 nao sera alterado

d2['c1'] = 100

print(d1)
print(d2)

# .copy() e uma copia rasa, tudo que for valor imutavel no outro dicionario ele ira copiar
# agora supondo que o dict tenha uma lista (que e mutavel) ele nao ira copiar a lista, na verdade
# ele vai fazer com que o d2 aponte para a mesma lista de d1

# por isso e chamado de shallow copy, porque e uma copia rasa, ele nao entra dentro de subniveis

# na pratica

d2['l1'][0] = 999999

print(d1, d2)

# Se voce quiser fazer uma copia TOTAL do outro dict, o Python tem um modulo que e chamado de copy

import copy

d3 = copy.deepcopy(d1)

d3['l1'][0] = 10

print(d3, d1)