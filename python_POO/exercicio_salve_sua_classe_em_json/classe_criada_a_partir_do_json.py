import json
from exercicio_salve_sua_classe_em_json import Carro, criar_carro

JSON_FILE = 'python_POO/exercicio_salve_sua_classe_em_json/classes_carro.json'

with open(JSON_FILE, 'r') as arquivo:
    carros = json.load(arquivo)

celta = Carro(carros['Celta']['nome'])

celta.acelerar()

criar_carro('mazda', 'Mazda')