# Sets - Conjuntos em Python (tipo set)
# Conjuntos sao ensinados na matematica
# Representados graficamente pelo diagrama de Venn
# Sets em Python sao mutaveis, porem aceitam apenas tipos imutaveis como valor interno.

# criando um set
# set(iteravel) ou {1, 2, 3}
# s1 = set()
# print(s1)

# Se voce passar algum valor dentro dos parenteses, o set vai agir como um iterador para cada elemento daquele valor
# s1 = set('Gabrielly')
# print(s1)

# Se voce nao quiser que isso acontece, crie um set usando {}, mas lembre-se sempre de ja colocar os valores dentro
# se nao voce estara criando um dict

# s1 = {'Gabrielly', 1, 2, 3, 3, 3, 3, 3, 1}
# print(s1)

# Sets sao eficientes para remover valores duplicados
# de iteraveis.
# - eles nao tem indexes;
# - eles nao garantem ordem;
# - eles sao iteraveis (for, in, not in)

# Metodos uteis:
# add, update, clear, discard

s1 = set()
s1.add('Joao')
s1.update('Ola mundo')
s1.discard('Joao') # Muito parecido com o add, mas adiciona itens de forma iterada
print(s1)
s1.clear() # limpa todo o set
print(s1)

# Operadores uteis:
# uniao | uniao (union) - Une
# interseccao & (intersection) - Itens presentes em ambos
# diferenca - Itens presentes apenas no set da esquerda
# diferenca simetrica ^ - Itens que nao estao em ambos

s2 = {1, 2, 3}
s3 = {2, 3, 4}

# uniao |

s4 = s2 | s3
print(s4)

# interseccao &

s4 = s2 & s3
print(s4)

# diferenca -

s4 = s2 - s3 # Se inverter a ordem, voce vera apenas o item que esta no set do s3
print(s4)

# diferenca simetrica ^

s4 = s2 ^ s3
print(s4)