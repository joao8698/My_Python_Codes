"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = '1000'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(string)
print(outra_variavel)
print(string.zfill(10))

# str, int, float e bool sao objetos
# O que isso quer dizer?
# Quer dizer que tem acoes que eu posso executar dentro desses objetos!

# Como por exemplo o metodo capitalize, utilizado nas str
print('hello world!'.capitalize()) # Deixa a primeira letra maiuscula

print('hello world!'.zfill(20)) # Preenche a str com zeros a esquerda