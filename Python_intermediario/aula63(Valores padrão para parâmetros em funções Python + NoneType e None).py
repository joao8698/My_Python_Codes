'''
Valores padrao para parametros
Ao definir uma funcao, os parametros podem
ter valores padrao. Caso o valor nao seja
enviado para o parametro, o valor padrao sera
usado.
Refatorar: editar o seu codigo.
'''
def soma(x, y, z=None):
    if z is not None:
        print(x + y + z)
    else:
        print(x + y)

soma(10, 10)

soma(10, 10, 5)

# Todo o parametro que vier depois de um parametro nomeado, precisa ser tambem nomeado.