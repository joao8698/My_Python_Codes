'''
Introducao ao desempacotamento + tuples (tuplas)
'''

###################DESEMPACOTAMENTO######################

nomes = ['Maria', 'Helena', 'Joao']

# Vamos desempacotar essa lista
# criar variaveis cada uma contendo um dos valores dessa lista acima
# assim

nome1, nome2, nome3 = nomes

# Vamos printar o nome2

print(nome2)

# Desse jeito abaixo temos exatamente a mesma coisa

nam1, nam2, nam3 = ['Maria', 'Helena', 'Joao']

print(nam2)

# E se a gente quiser pegar apenas um dos valores dessa lista?

nome1, *nome_variavel_qualquer = ['Maria', 'Helena', 'Joao']

print(nome1, nome_variavel_qualquer)

# Por convencao, quando a gente vai criar um variavel para empacotar o resto da lista
# e a gente tem certeza absoluta que aquela variavel nunca vai ser usada, por convencao
# a gente faz assim

nome1, *_ = ['Maria', 'Helena', 'Joao']

# Colocamos um underline depois do *, e uma variavel utilizavel como qualquer outra
# mas pela convencao, damos a entender que ela nunca sera utilizada!

# so pra ver que funciona igual qualquer variavel, vamos dar um print nela
print(nome1, _)

# E se a gente quiser pegar o segundo valor, e simples, segue abaixo

_, nome2, *_ = ['Maria', 'Helena', 'Joao']

print(nome2)

# pra pegar o terceiro nome

_, _, nome3 = ['Maria', 'Helena', 'Joao']

print(nome3)

# E ainda por CIMA podemos ter a variavel de resto no final, mesmo se a gente ja atribui variaveis pra todos os valores

_, _, nome3, *_ = ['Maria', 'Helena', 'Joao']

print(_) # Vai printar uma lista vazia!!!!!!!

###################DESEMPACOTAMENTO######################

###################TUPLES (TUPLAS)#######################

'''
Tipo tupla - Uma lista imutavel
'''
nomes = 'Helena', 'Maria', 'Joao' # pode deixar sem parenteses

# OU

nomes = ('Helena', 'Maria', 'Joao') # ou com paretenses

# tuplas sao imutaveis, ou seja, nao da pra alterar nenhum valor nela ou adicionar ou qualquer outro tipo de coisas que
# dava pra fazer com as listas

# o codigo abaixo vai gerar um erro

# nomes[0] = 1

# print(nomes)

# Da pra fazer a conversao de uma lista para um tupla

lista = ['Joao', 'Davi', 'Hiago']
lista = tuple()

# Resumindo a ideia, tuplas sao basicamente listas, so que imutaveis!