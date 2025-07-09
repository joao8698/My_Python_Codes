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

arquivo = open(caminho_arquivo, 'w')

arquivo.close()