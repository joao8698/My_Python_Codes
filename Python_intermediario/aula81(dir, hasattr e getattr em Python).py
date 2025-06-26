# dir, hasattr e getattr em Python
string = 'Luiz'
metodo = 'upper'

print(dir(string))

print(getattr(string, metodo)())

if hasattr(string, 'upper'):
    print('existe metodo upper')
    print(string.upper())