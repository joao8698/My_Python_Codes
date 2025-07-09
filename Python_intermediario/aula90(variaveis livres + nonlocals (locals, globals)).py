# Variaveis livres + nonlocals (locals, globals)

# print(globals())

# def fora(x):
#     a = x

#     def dentro():
#         print(locals())
#         return a
    
#     return dentro

# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())

# def concatenar(string_inicial):
#     valor_final = string_inicial

#     def interna(valor_a_concatenar):
#         valor_final += valor_a_concatenar # Isso vai gerar um ERRO! Porque valor_final nao e do escopo da func interna, ou seja, so podemos ler o seu valor mas nao altera-lo.
#         return valor_final
    
#     return interna

# c = concatenar('a')

# print(c('b'))

# PARA CONSERTAR ISSO USAREMOS O nonlocal, para definir uma variavel nao local, para fazermos o Python buscar o valor da variavel no escopo acima!

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    
    return interna

c = concatenar('a')

print(c('b'))
print(c('c'))
print(c('d'))

final = c()

print(final)