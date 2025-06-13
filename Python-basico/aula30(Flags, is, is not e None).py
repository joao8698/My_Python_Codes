'''
Flag (Bandeira) - Marcar um local
None = nao valor
is e is not = e ou nao e (tipo, valor, identidade)
id = Identidade
'''
condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faca algo')
else:
    print('Nao faca algo')

if passou_no_if is None: # COM O None, VOCE GERALMENTE VAI USAR O is
    print('Nao passou no if')
else:
    print(passou_no_if, passou_no_if is not None)

# O codigo acima e um codigo ruim porque definimos a variavel passou_no_if
# dentro do bloco de um if
# o que acontece aqui e que queremos printar essa variavel fora desse bloco
# ai que pode dar o erro, porque a variavel so vai ser definida
# se o bloco if for executado
# ou seja, caso contrario, aquela variavel nunca vai existir e o print
# na ultima linha vai dar erro porque esta tentando printar algo que nao foi definido ainda, que ainda nao existe!!!
# Por isso, sempre antes de mexer com qualquer variavel, defina ela fora de qualquer bloco, isso se chama variavel global

# Algoritimo = solucao criada para resolver determinado problema