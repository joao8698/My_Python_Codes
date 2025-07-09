# Funcoes decoradoras e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funcoes decoradoras sao funcoes que decoram outras funcoes
# Decoradores sao usados para fazer o Python
# usar as funcoes decoradoras em outras funcoes.
# Decoradores sao "Syntax Sugar" (cucar sintatico)

# ============= FUNCOES DECORADORAS ============= #

# def criar_funcao(func):
#     def interna(*args, **kwargs):
#         print('Vou te decorar')
#         for arg in args:
#             e_string(arg)
#         resultado = func(*args, **kwargs)
#         print(f'O seu resultado foi {resultado}.')
#         print('Ok, agora você foi decorada')
#         return resultado
#     return interna


# def inverte_string(string):
#     return string[::-1]


# def e_string(param):
#     if not isinstance(param, str):
#         raise TypeError('param deve ser uma string')


# inverte_string_checando_parametro = criar_funcao(inverte_string)
# invertida = inverte_string_checando_parametro('123')
# print(invertida)

# ============= ## ============= ## ============= ## ============= #

# ============= DECORADORES ============= #

# Decoradores em Python (@syntax_sugar)

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora você foi decorada')
        return resultado
    return interna

@criar_funcao # ------> Decorador (@Syntax Sugar)
def inverte_string(string):
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')

invertida = inverte_string('123')
print(invertida)