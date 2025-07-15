import os

caminho_arquivo = 'C:\\Users\\brois\\Documents\\Python_My_Codes\\'
caminho_arquivo += 'arquivo.txt'

with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
    print(arquivo)

# os.remove(caminho_arquivo)