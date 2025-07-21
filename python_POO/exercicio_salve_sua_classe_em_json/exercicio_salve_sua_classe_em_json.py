# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import os
import json
import time

BASE_DIR = os.path.dirname(__file__)
SAVE_TO = os.path.join(BASE_DIR, 'classes_carro.json')

dict_de_carros = dict()

class Carro:

    VELOCIDADE_MAX = 200
    VELOCIDADE_MIN = -20

    def __init__(self, nome, velocidade=0):
        self.nome = nome
        self.velocidade = velocidade

    def acelerar(self):
        if self.velocidade == Carro.VELOCIDADE_MAX:
            print(f'{self.nome} ja atingiu sua velocidade maxima!')
            return
        
        while self.velocidade <= Carro.VELOCIDADE_MAX:
            time.sleep(0.5)
            self.velocidade += 10
            print(f'{self.nome} esta a {self.velocidade}KM/H!')

    def re(self):
        if self.velocidade == Carro.VELOCIDADE_MIN:
            print(f'{self.nome} esta dando re!')
            return

        while self.velocidade >= Carro.VELOCIDADE_MIN:
            time.sleep(2)
            self.velocidade -= 10
            print(f'{self.nome} esta a {self.velocidade}KM/H!')

def salvar_carro():
    with open(SAVE_TO, 'w', encoding='utf-8') as arquivo:
        json.dump(dict_de_carros, arquivo, ensure_ascii=False, indent=2)

def criar_carro(instancia, nome, velocidade=0):
    instancia = Carro(nome, velocidade)
    dict_de_carros[nome] = instancia.__dict__
    salvar_carro()

criar_carro('celta', 'Celta')
criar_carro('fiat', 'Fiat')
criar_carro('lamborghini', 'Lamborghini')
criar_carro('ferrari', 'Ferrari')