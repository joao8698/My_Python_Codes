# Introducao as generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0):
    yield 1

gen = generator(n=0)
print(next(gen))