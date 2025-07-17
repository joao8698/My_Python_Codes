class Pessoa:
    def __init__(self, nome, sobrenome): # self e a instancia da classe
        self.nome = nome # Aqui e como se a gente estisvesse criando metodos para a nossa instancia (p1 abaixo) (o self referencia ao nosso novo objeto criado (instancia))
        self.sobrenome = sobrenome

p1 = Pessoa('Gabrielly', 'Vieira')

print(p1)