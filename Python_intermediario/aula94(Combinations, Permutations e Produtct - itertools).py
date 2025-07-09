# Combinacao - OOrdem nao importa - iteravel + tamanho do grupo

# Permutacao - Ordem importa

# Produto - Ordem  importa e repete valores unicos

from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')

pessoas = [
    'Joao', 'Joana', 'Luiz', 'Gabrielly',
]

camiseta = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino'],
    ['algodao', 'poliester'],
]

print('# ====================COMBINATIONS========================== #')
print_iter(combinations(pessoas, 2))
print('# ====================PERMUTATIONS========================== #')
print_iter(permutations(pessoas, 2))
print('# ====================PRODUTCT========================== #')
print_iter(product(*camiseta))