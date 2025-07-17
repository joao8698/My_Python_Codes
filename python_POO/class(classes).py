# class - Classes sao moldes para criar novos objetos.

# As classes geram novos objetos (instancias) que podem ter seus proprios atributos e metodos.

# Os objetos gerados pela classe podem usar seus dados internos para realizar varias acoes.

# Por convencao, usamos PascalCase para nomes de classes.

class Pessoa:
    ...

p1 = Pessoa()
p1.nome = 'Joao'
p1.sobrenome = 'Luiz'

print(p1.nome, p1.sobrenome)