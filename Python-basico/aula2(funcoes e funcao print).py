# print e uma funcao
# () e um argumento da funcao ou metodo
# se eu quiser passar mais de um argumento para a funcao ou metodo eu uso a ,
print(123, 'Hello World!')
'''
se eu selecionar qualquer lugar de uma linha de codigo no VS Code eu consigo dar ctrl+c e depois ctrl+v e ele cola
o codigo para a proxima linha
'''
print(123, 'Hello World!')
print(123, 'Hello World!')
print(123, 'Hello World!')
print(123, 'Hello World!')
print(123, 'Hello World!')

# USAR SEPARADORES sep=''
print(234, 'Hello World!', sep='-')
# vai printar 234-Hello World!
# O sep='' muda o jeito que os argumentos se separam entre si, podendo configurar eles pra que se separem com um - ou um espaco qualquer!
print(234525, 'Oi', sep='p')
# vai printar 234525pOi
print(17, 'Joao', sep='Gaby')
print(423434, 'sla', sep='')
# se eu nao colocar nada dentro do sep='' ele nao separa os argumentos!!!!!
# \r\n -> CRLF
# \n -> LF

# argumento end=''
# significa o final do print...(depois do ultimo argumento)
# por padrao o windows usa \r\n
print(123, 'nao sei', sep=' ', end='\r\n')
# nos windows mais atuais ou em versoes mais recentes pode ser usado apenas o \n(LF)
print(123, 'nsei', sep=' ', end='\n')

# E se eu colocar duas ## no end='' ?????
# E isso que acontece
print(123, 'oi', sep=' ', end='##')
print('ola')
# Vai printar 123 oi##ola

# OU SEJA ele nao pula pra uma nova linha e o argumento termina com o final "##"

# E da pra colocar qualquer coisa dentro do end='' !!!

# Tambem da pra fazer isso com end=''
print('ola', end='##\n')
print('tudo bem?')
'''
vai printar "ola##
             tudo bem?"
'''

# OU

print(123, end='\n##')
print('ola')
#vai printar "123
              ##ola"