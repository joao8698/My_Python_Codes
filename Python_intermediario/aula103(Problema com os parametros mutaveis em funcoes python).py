# Problema dos parametros mutaveis em funcoes Python

def adiciona_clientes(nome, lista=[]):
    lista.append(nome)
    return lista

cliente1 = adiciona_clientes('Luiz')
adiciona_clientes('Maria', cliente1)
print(cliente1)