# groupby - agrupando valores (itertools)

from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

# alunos = ['a', 'a', 'a', 'a', 'b', 'c', 'a', 'a']

# grupos = groupby(sorted(alunos))

# for chave, valor in grupos:
#     print(chave)
#     print(list(valor))

alunos_agrupados = sorted(alunos, key=lambda a: a['nota'])
grupos = groupby(alunos_agrupados, key=lambda a: a['nota'])

for aluno in alunos_agrupados:
    print(aluno)