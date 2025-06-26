import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [{**produto, 'preco': produto['preco'] * 1.05} if produto['preco'] > 20 else {**produto} for produto in produtos if produto['preco'] > 10]
print(*novos_produtos, sep='\n')
# print()
# print(*produtos, sep='\n')

# p(novos_produtos)

# filtro e diferente de map, eu nao quero incluir determinado numero se a condicao que eu passar for verdadeira
# isso e feito com um if sem else depois do for

lista = [n for n in range(10) if n < 5]
print(lista)