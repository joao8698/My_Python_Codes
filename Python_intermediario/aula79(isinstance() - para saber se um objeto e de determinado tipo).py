# isinstance - para saber se objeto e de determinado tipo

lista = ['a', 1, 1.1, True, [0, 1, 2], (1,2), {0, 1}, {'nome': 'Gabrielly'}]

for item in lista:
    if isinstance(item, set):
        print(item, isinstance(item, set))

    if isinstance(item, str):
        print(item.upper(), isinstance(item, str))

    if isinstance(item, (int, float)):
        print(item, isinstance(item, (int, float)))

    if isinstance(item, tuple):
        print(item, isinstance(item, tuple))

    if isinstance(item, dict):
        print(item, isinstance(item, dict))

    if isinstance(item, list):
        print(item, isinstance(item, list))