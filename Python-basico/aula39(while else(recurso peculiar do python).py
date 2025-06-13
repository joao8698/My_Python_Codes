''' while/else '''

string = 'Valor qualquer'

i = 0
# while i < len(string):
#     letra = string[i]

#     print(letra)
#     i += 1

# else:
#     print('O else foi executado')

# Quando o codigo passa pelo while e le ele todo, sem sair dele forcadamente
# ele executa, tambem, o else embaixo dele!

# Quando o codigo sai do while forcadamente, o else nao e executado!

while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1

else:
    print('Foi encontrado um espaco!')

print('Fora do while')