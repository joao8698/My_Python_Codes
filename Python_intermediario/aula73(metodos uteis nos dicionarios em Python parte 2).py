'''
get - obtem uma chave
pop - apaga um item com a chave especificada (del)
popitem - apaga o ultimo item adicionado
update - atualiza um dicionario com outro
'''

###########get##############

p1 = {
    'nome': 'Gabrielly',
    'sobrenome': 'Ensfeld',
}
# print(p1.get('nome', 'sem nome'))

###########pop##############

# pop apaga um item com a chave especificada, tipo o del, mas com uma diferenca, a gente pode pegar
# o item apagado e jogar em algum lugar, por exemplo, em uma variavel

# nome = p1.pop('nome')
# print(nome)
# print(p1)

#########popitem############

# elimina a ultima chave do dicionario

# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

########update##############

# update - atualiza o dicionario

# p1.update({
#     'nome': 'novo nome'
# })

# tambem da pra usar argumentos nomeados ao inves de usar as chaves como strings

# p1.update(nome='novo nome', sobrenome='novo sobrenome')

# tambem da pra usar tuplas

# tupla = ('nome', 'novo nome'), ('sobrenome', 'novo sobrenome'), ('idade', 18)

# e tambem da pra usar listas

lista = [['nome', 'novo nome'], ['sobrenome', 'novo sobrenome'], ['idade', 18]]

p1.update(lista)

print(p1)