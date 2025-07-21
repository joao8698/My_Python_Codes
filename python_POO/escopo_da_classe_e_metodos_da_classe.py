# Escopo da classe e metodos da classe

class Animal:

    # nome = 'Leao'

    def __init__(self, nome):
        self.nome = nome

    def comendo(self, alimento):
        return f'{self.nome} esta comendo {alimento}'
    
leao = Animal('Leao')
print(leao.comendo('Maca'))