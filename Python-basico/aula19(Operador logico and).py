# Operadores logicos
# and (e) or (ou) not (nao)
# and - Todas as condicoes precisam ser verdadeiras (True)
# Se qualquer valor for considerado falso,
# a expressao inteira sera avaliada naquele valor (ou seja o valor daquela expressao vai ser False)
# o interpretador vai parar naquele valor que foi considera False e nao ira nem ler os proximos valores!!!
# Sao considerados falsy (que ja vimos)
# 0, 0.0, '', False (Sao os tipos de valor que sao consideras falsy(falso))
# Tambem existe o tipo None que e
# usado para representar um nao valor
entrar = input('Voce deseja [E]ntrar ou [S]sair?: ')
if entrar == 'S':
    print('Voce saiu!')
    quit()
senha = (input('Qual a senha?: '))
senha_permitida = '123456'

if senha != senha_permitida:
    print('Voce digitou a senha errada!')
elif entrar == 'E' and senha == senha_permitida:
    print('Voce entrou!')
else:
    print('Digite uma das opcoes acima!!!')

# Avaliacao de curto circuito
print(True and False and True)

# Ira parar na condicao e RETORNAR o valor da condicao!
print(True and 0 and True)