'''
Introducao ao try/except
try -> tentar executar o codigo
except -> ocorreu algum erro ao tentar executar
'''

numero_str = input('Digite qualquer numero que eu vou multiplica-lo: ')
try:
    numero_float = float(numero_str)
    print(f'O dobro do numero {numero_float} e {numero_float * 2}')
except:
    print('Isso nao e um numero!')

# fail fast - errar o mais rapido possivel pra chegar na excessao