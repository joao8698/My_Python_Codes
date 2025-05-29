'''
Iterando strings com while
'''
#       012345678
# nome = 'Gabrielly' # Iteraveis
#      -987654321

nome = 'Gabrielly'
tamanho_nome = len(nome)
nova_str = ''
indice = 0
while indice < tamanho_nome:
        nova_str += f'*{nome[indice]}*'
        print(nova_str)
        indice += 1