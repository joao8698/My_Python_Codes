nome = 'Joao Luiz'
altura = 1.70

linha_1 = 'nome tem altura de altura'

# Vamos dar INTRODUCAO a formatacao de strings
# vamos colocar um f no comeco da variavel sem estar dentro das aspas, desse jeito

linha_1 = f'nome tem altura de altura'

# Colocando o f desse jeito, habilita a possibilidade de colocar variaveis dentro de strings!
# Para fazer isso, simplismente envolva o nome das variaveis dentro das strings com chaves, desse jeito

linha_1 = f'{nome} tem {altura} de altura'

print(linha_1)

# Da tambem para formatar as casas decimais de um numero float utilizando o f, desse jeito
linha_1 = f'{nome} tem {altura:.2f} de altura'
# colocamos dois pontos e depois . e quantas casas decimais a gente quer e um f no final
print(linha_1)
print(f'{altura:.10f}')

# Tambem da pra colocar virgulas no numero, caso queira separar ou algo assim, desse jeito
altura = 10000.500
print(f'{altura:,.3f}')
# Vai mostrar o numero 10,000.500

# Alias o nome desse metodo de formatacao de strings e chamado de f-strings (f de formatacao(formatting))