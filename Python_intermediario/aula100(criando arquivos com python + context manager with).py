# Criando Arquivos com Python + Context Manager with

# criando arquivos com Python
# Usamos a funcao open para abrir um arquivo em Python (se ele existir)

'''
Modos:

r(leitura), w(escrita), x(para criacao)

a(escreve ao final), b(binario)

t(modo texto), +(leitura e escrita)
'''

# Context Manager - with (abre e fecha)

'''
Metodos uteis:

write, read (escrever e ler)

writelines (escrever varias linhas)

seek (move o cursor)

readline (ler linha)

readlines (ler linhas)
'''

# Vamos falar mais sobre o modulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo

# Vamos falar mais sobre o modulo json, mas:
# json.dump = gera um arquivo json
# json.load

# ================================================== #

caminho_arquivo = 'C:\\Users\\brois\Documents\\Python_My_Codes\\'
caminho_arquivo += 'arquivo.txt'

# arquivo = open(caminho_arquivo, 'w')

# arquivo.close()

# USANDO O CONTEXT MANAGER NESSAS SITUACOES:
# o with (do context manager) + open (ou qualquer outro comando evolvendo pastas) ja abre e FECHA o arquivo tudo em uma unica linha de codigo
# nao importa o que aconteca!

# with open(caminho_arquivo, 'w+') as arquivo:
#     print(type(arquivo))
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )
#     arquivo.seek(0, 0)
#     print(arquivo.read())
#     print('Lendo')
#     arquivo.seek(0, 0)
#     print(arquivo.readline(), end='')
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip())

#     print()
#     arquivo.seek(0, 0)

#     print('ReadLines')
#     for linha in arquivo.readlines():
#         print(linha.strip())

# print('#' * 10)
# print()

# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())

with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )