# Atributos de classes
from datetime import date

class Pessoa:
    # atributo = ... -------> ISSO E UM ATRIBUTO DE CLASSE
    ANO_ATUAL = date.today().year

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_de_nascimento(self):
        return Pessoa.ANO_ATUAL - self.idade
    
p1 = Pessoa('Joao', 18)

print(p1.get_ano_de_nascimento())