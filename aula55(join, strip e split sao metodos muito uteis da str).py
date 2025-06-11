'''
split e join com list e str
split - divide uma string
join - une uma string
'''

frase = 'Olha so que, coisa interessante'
# lista_palavras = frase.split()
# print(lista_palavras)

# .split() leva um argumento que e uma str, onde voce pode colocar qual caractere
# seja o ponto onde voce quer que ele faca a divisao
# Ex.:
# lista_palavras = frase.split(', ')
# print(lista_palavras)

# for i, frase in enumerate(lista_palavras):
#     print(lista_palavras[i].strip())

# .strip() corta os espacos do comeco e do fim da string
# .rstrip() corta apenas os espacos da direita da string
# .lstrip() corta apenas os espacoes da esquerda da string

# frases_unidas = '-'.join('abc')
# print(frases_unidas)

frases_unidas = ' '.join(frase)
print(frases_unidas)
