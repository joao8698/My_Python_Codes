''' for / in - estrutura de repeticao para coisas finitas '''

texto = 'Python'
nova_str = ''

for letra in texto:
    nova_str += f'-{letra}'
    print(letra)
print(nova_str)