import json
import os

pessoa = {
    'nome': 'Luiz Otavio',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

BASE_DIR = os.path.dirname(__file__)
SAVE_TO = os.path.join(BASE_DIR, 'arquivo-python.json')

with open(SAVE_TO, 'w') as file:
    json.dump(pessoa, file, indent=2, ensure_ascii=False)