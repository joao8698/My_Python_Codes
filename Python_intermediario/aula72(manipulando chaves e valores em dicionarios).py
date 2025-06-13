# Manipulando chaves e valores em dicionarios no Python

pessoa = {}

##
##

# Como o exemplo abaixo, da para criar chaves dentro de um dict usando o sinal de atribuicao.

pessoa['nome'] = 'Gabrielly'
pessoa['sobrenome'] = 'Ensfeld'

# Posso apagar alguma chave dentro do dict? SIM! usando del:
del pessoa['sobrenome']

print(pessoa)
print(pessoa['nome']) # pessoa['sobrenome']) ira dar erro pois deletamos a chave 'sobrenome' anteriormente

try:
    print(pessoa['sobrenome'])
except KeyError:
    print('Essa chave nao existe!')

# Se voce quiser ao inves de usar o try except, usar o if, pode fazer desse jeito abaixo:
if pessoa.get('sobrenome', None): # por padrao esse metodo retorna None se a chave nao existir, caso contrario ele retorna o valor da chave em si!
    print('Existe!')
else:
    print('Nao existe!')

print(pessoa.get('sobrenome', 'nao existe'))

# OUUUUU

if pessoa.get('sobrenome') is None: # ou da pra usar is not tambem.
    print('Nao existe!')
else:
    print(pessoa['sobrenome'])

# Dicionarios tem que possuir chaves, se nao ira acontecer uma excessao, e isso para a execucao programa (nao queremos isso)