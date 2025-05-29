'''
Repeticoes
while (enquanto)
Executa uma acao enquanto uma condicao for True
Loop infinito --> quando um codigo nao tem fim
'''
qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=}, {coluna=}')
        coluna += 1

    linha += 1  

print('Acabou')

# toda vez que o primeiro while rodar, o while que esta dentro dele ira rodar quantas vezes seu argumento for verdadeiro, ate o
# final
# depois disso o primeiro while ira rodar, e assim ira comecar tudo de novo