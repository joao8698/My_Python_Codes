# __dict__ e vars para atributos de instancia

from datetime import date

class Pessoa:
    ANO_ATUAL = date.today().year

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_de_nascimento(self):
        return Pessoa.ANO_ATUAL - self.idade

dados = {'nome': 'Joao', 'idade': 18}

p1 = Pessoa(**dados)
# p1.nome = 'EITA'
# del p1.nome

# p1.__dict__['outra'] = 'coisa'
# p1.__dict__['nome'] = 'Jorge'

# del p1.__dict__['nome']

# print(p1.__dict__)
print(vars(p1))