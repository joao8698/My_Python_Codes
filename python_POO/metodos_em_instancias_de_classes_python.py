# Metodos em instancias de classes Python

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} esta acelerando')

celta = Carro('Celta')
celta.acelerar()