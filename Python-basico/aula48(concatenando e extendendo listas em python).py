"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

lista_c = lista_a + lista_b
lista_a.extend(lista_b) # O metedo .extend() mexe diretamente na lista em si, mas nao retorna nenhum valor
# se voce tentar armazenar o valor do metedo extend em alguma variavel, essa mesma ira retornar o valor None
# se quiser ver o valor, de print na lista em que voce fez o metedo .extend() ai sim voce tera o resultado!

print(lista_c)
print(lista_a)