# Operadores in e not in
# Strings sao iteraveis
#  0 1 2 3 4 5 # Voce pode navegar entre os itens usando os indices positivos
#  O t a v i o
# -6-5-4-3-2-1 # Quanto pode navegar pelos itens usando os indices negativos

# iteraveis, iteravel significa que e um negocio onde voce pode
# navegar item por item

nome = 'Otavio'
# print(nome[2]) Vai printar 'a'
# print(nome[-4]) Tambem vai printar 'a'

# Usando o operar in
print('a' in nome) # Se 'a' estiver entre as letras de nome, retorna um valor de False ou True
print('V' in nome) # Vai dar False porque o v que tem dentro das letras nome e minusculo!
print('vio' in nome) # Vai dar True, porque todas essas letras tem dentro de nome!!!!
print('Ova' in nome) # Vai dar False, porque nao tem a mesma sequencia que esta dentro de nome!!!
print('avi' in nome) # Vai dar True, porque esta na mesma sequencia que esta dentro de nome!!!!
print(30 * '-') # Da pra fazer tracos no terminal fazendo esse truque!
# Agora usando o operador not in
print('zero' not in nome) # Vai dar True porque 'zero' nao esta dentro de nome!!!
print('Oav' not in nome) # Vai dar True, porque mesmo que as letras estejam dentro de nome, a sequencia nao e igual!!!
print('Ota' not in nome) # Vai dar False porque 'Ota' esta dentro de nome e a sequencia e igual!!!
print('O' not in nome) # Algo mais simples, mas so pra lembrar que 'O' esta dentro de nome, portante da False