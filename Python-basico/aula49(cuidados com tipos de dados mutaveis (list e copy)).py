'''
Cuidados com dados mutaveis
= - copiado o valor (imutaveis)
= - aponta para o mesmo valor na memoria (mutavel)
'''

lista_a = ['Luiz', 'Gaby']
lista_b = lista_a.copy() # Retorna uma nova lista a partir da lista_a para a lista_b

# OU seja, se a gente fizer qualquer alteracao na lista_a, essa alteracao nao acontecera
# na lista_b, pois a lista_b e uma nova lista.

lista_a[0] = 500

print(lista_a)
print(lista_b)

# Agora se so copiarmos a lista_a para a lista_b, qualquer alteracao que fizermos na lista_a
# vai ser feito tambem na lista_b, porque a lista_b e a lista_a

lista_a = ['Luiz', 'Gaby']
lista_b = lista_a

lista_a[0] = 500

print(lista_a)
print(lista_b)