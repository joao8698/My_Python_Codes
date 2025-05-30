'''
Iterando strings com while
'''
#       012345678
# nome = 'Gabrielly' # Iteraveis
#      -987654321

nome = 'Gabrielly Ensfeld Vieira'
nova_str = ''
indice = 0
while indice < len(nome):
        nova_str += f'*{nome[indice]}'
        indice += 1
nova_str += '*'
print(nova_str)