'''
Higher Order Functions - funcoes de primeira classe
'''
def saudacao(msg):
    return msg

def executa(funcao, msg):
    return funcao(msg)

saudacao_2 = saudacao # Agora saudacao_2 aponta pra mesma funcao que e saudacao

v = executa(saudacao_2, 'Bom dia')

print(v)