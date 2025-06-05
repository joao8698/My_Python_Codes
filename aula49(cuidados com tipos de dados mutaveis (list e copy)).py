'''
Cuidados com dados mutaveis
= - copiado o valor (imutaveis)
= - aponta para o mesmo valor na memoria (mutavel)
'''

lista_a = ['Luiz', 'Gaby']
lista_b = lista_a

print(lista_b)

lista_b = lista_a[0]

print(lista_b)