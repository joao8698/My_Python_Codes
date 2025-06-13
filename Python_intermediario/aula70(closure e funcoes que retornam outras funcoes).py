'''
Closure e funcoes que retornam outras funcoes
'''
def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}!'
    return saudar

saudacao1 = criar_saudacao('Bom dia', 'Gabrielly')
saudacao2 = criar_saudacao('Boa noite', 'Gabrielly')

# print(saudacao1)
# print(saudacao2)

print(saudacao1())
print(saudacao2())

# Eu tambem posso adiar a passagem de algum argumento, desse jeito:

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

saudacao1 = criar_saudacao('Bom dia')
saudacao2 = criar_saudacao('Boa noite')

# print(saudacao1)
# print(saudacao2)

print(saudacao1('Joao Luiz'))
print(saudacao2('Gabrielly'))

for nome in ['Joao', 'Gabrielly', 'Sogra']:
    print(saudacao1(nome))