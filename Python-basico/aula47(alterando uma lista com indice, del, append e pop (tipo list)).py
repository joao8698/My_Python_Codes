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
lista = [10, 20, 30, 40]

lista[2] += 30

del lista[2]

numero = lista[2]

print(numero)
print(lista)

# numero = 40 porque demos um del lista[2], ou seja, o 40 passou a ser o indice 2 da lista, depois que deletamos
# o 30

lista.append('Counter Strike')
lista.insert(1, 'Oi') # adiciona qualquer tipo de dados no referente indice da lista (recebe dois argumentos - indice, dado)
# isso nao apaga o valor do indice indicado, e sim troca todos os valores de lugar para inserir o novo valor na lista
# nao insira nenhum valor na lista se ela for muito grande

print(lista)

ultimo_valor = lista.pop(1)

print(lista, f'removido {ultimo_valor}')

lista.clear()
print(lista)

# ARGUMENTOS SAO VALORES QUE VOCE PASSA PARA OS METODOS