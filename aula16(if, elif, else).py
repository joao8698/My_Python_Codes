# if/ elif      / else
# se/ se nao se/ se nao

# Digamos que
entrada = input('Voce quer entrar ou sair?: ')

# O if sempre vai retornar um True ou um False
# ele verifica se algo e True ou False
# se for True, ele executa o codigo que esta dentro do seu bloco
# se for False, ele pula aquela parte do codigo e executa a proxima

# Desse jeito

if entrada == 'entrar':
    print('Voce entrou no sistema')
elif entrada == 'sair':
    print('Voce saiu do sistema')
else:
    print('Voce nao digitou nem entrar nem sair.')

# Temos que usar a indentacao do python, que se refere aos espacos
# usados para fazer um bloco de codigo

condicao = True

if condicao :
    print('Este e o codigo do if')
print('fora do if')

# vai exibir Este e o codigo do if + fora do if

# agora se fosse assim

condicao = True

if condicao :
    print('Este e o codigo do if')
print('fora do if')

# Vai exibir apenas fora do if, porque condicao e False

# Da pra ter if sozinho, da pra ter if e varios elif sem terminar com else
# e da pra ter if e else sem ter elif!!!!

# LEMBRA DOS ...?? (USADO COMO PLACE HOLDER)
# TAMBEM PODEMOS USAR O pass
# O pass E TIPO, "PASSA QUE DEPOIS EU ESCREVO"!

# desse jeito

if condicao:
    print('OK!')
elif entrada:
    pass
else:
    print('NOT OK!')

# A PARTIR DO MOMENTO EM QUE UMA CONDICAO E TRUE NOS BLOCOS IF, ELIF E ELSE
# ELE PARA DE VERIFICAR AS CONDICOES E PULA PRA PROXIMA PARTE DO CODIGO

c1 = False
c2 = False
c3 = True
c4 = False

if c1:
    print('E verdadeiro')
elif c2:
    print('E verdadeiro')
elif c3:
    print(f'{c3=} e verdadeiro')
elif c4:
    print('E verdadeiro')
else:
    print('Nenhuma das alternativas e verdadeira!')

# Debug = tirar o problema
# De = tirar
# bug = inseto (problema)

# É possível adicionar um if dentro de outro fazendo várias condições aninhadas.
# numero = 10
# if numero > 1:
#     if numero > 2:
#         if numero > 3:
#             print('Número maior que 3')
#         else:
#             print('Número menor que 3')
#     else:
#         print('Número menor que 2')
# else:
#     print('Número menor que 1')