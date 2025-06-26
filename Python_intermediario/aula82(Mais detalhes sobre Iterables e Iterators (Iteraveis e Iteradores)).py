# Generator expression, Iterables e Iterators em Python

import sys

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__() # tem__iter__e__next__

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# lista = [n for n in range(1000000)] # A lista ja esta toda na memoria

generator = (n for n in range(1000000)) # Enquanto o generator esta esperando eu pedir um valor pra ele!

for valor in generator:
    print(valor)

print(sys.getsizeof(generator))