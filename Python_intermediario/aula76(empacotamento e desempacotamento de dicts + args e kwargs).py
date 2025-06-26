# Empacotamento e desempacotamento de dicionarios
# a, b = 1, 2
# a, b = b, a
# print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Dias',
}

# a, b = pessoa
# print(a, b)

# a, b = pessoa.values()
# print(a, b)

# a, b = pessoa.items()
# print(a, b)

# (a1, a2), b = pessoa.items()
# print(a1, a2)
# print(b)

dados_pessoa = {
    'idade': 16,
    'altura': 1.68,
}

# pessoa.update(dados_pessoa)

# print(pessoa)

pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)

outra_pessoa = {**pessoa, 'chave': 1}
print(outra_pessoa)

def mostro_kwargs(*args, **kwargs):
    print('nao nomeados:', args)
    for chave, valor in kwargs.items():
        print(valor)

mostro_kwargs(1, 2, 3, oi='oi', souumakwarg='ola eu sou kwarg')
mostro_kwargs(**pessoa)

# args e kwargs
# args (ja vimos)
# kwargs - keyword arguments (argumentos nomeados)