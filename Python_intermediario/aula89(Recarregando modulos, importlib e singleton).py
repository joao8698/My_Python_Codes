import importlib

import modulo_exemplo

for modulo in range(10):
    importlib.reload(modulo_exemplo)

print('Fim')