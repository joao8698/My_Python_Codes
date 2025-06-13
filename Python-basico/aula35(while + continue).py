'''
Repeticoes
while (enquanto)
Executa uma acao enquanto uma condicao for True
Loop infinito --> quando um codigo nao tem fim
'''
contador = 0

while contador <= 30:
    contador += 1

    if contador == 6:
        print('Nao vou mostrar o 6')
        continue # ----> toda vez que o interpretador ver o continue dentro de um laco, ele volta pro comeco do laco.

    if contador >= 10 and contador <= 27:
        print('Nao vou mostrar o', contador)
        continue

    print(contador)

print('acabou')