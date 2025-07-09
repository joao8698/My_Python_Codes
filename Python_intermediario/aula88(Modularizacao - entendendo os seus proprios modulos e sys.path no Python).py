# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__Add commentMore actions
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

# import sys

import Package_Exemplo

print('Este modulo se chama', __name__)

print(Package_Exemplo.dobra(2))

# print(*sys.path, sep='\n')