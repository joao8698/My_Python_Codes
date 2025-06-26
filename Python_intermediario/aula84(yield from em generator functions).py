# yield from

def gen1():
    yield 1
    yield 2
    yield 3

def gen2():
    yield from gen1() # continua o yield onde o gen1 parou.
    yield 4
    yield 5
    yield 6

# Entao agora eu so usaria o meu gen2()

g = gen2()

for numero in g:
    print(numero)