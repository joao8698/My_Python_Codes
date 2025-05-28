# Vamos pegar o codigo da aula19
# entrar = input('Voce deseja [E]ntrar ou [S]sair?: ')
# if entrar == 'S':
#     print('Voce saiu!')
#     quit()
# senha = (input('Qual a senha?: '))
# senha_permitida = '123456'

# if senha != senha_permitida:
#     print('Voce digitou a senha errada!')
# elif entrar == 'E' and senha == senha_permitida:
#     print('Voce entrou!')
# else:
#     print('Digite uma das opcoes acima!!!')

# Agora vamos adicionar um or no elif entrar == 'E' and senha == senha_permitida:

# Desse jeito

entrar = input('Voce deseja [E]ntrar ou [S]sair?: ')
if entrar == 'S':
    print('Voce saiu!')
    quit()
senha = (input('Qual a senha?: '))
senha_permitida = '123456'

if senha != senha_permitida:
    print('Voce digitou a senha errada!')
elif entrar == 'E' or entrar == 'e' and senha == senha_permitida:
    print('Voce entrou!')
else:
    print('Digite uma das opcoes acima!!!')

# Agora o codigo aceita Tanto e minusculo quanto E maisculo como input!!!!

# Se qualquer valor for avaliado como verdadeiro (utilizando o or)
# a expressao inteira sera avaliada naquele valor

# Avaliacao de curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)