"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
from colorama import Fore, Style, init
init(autoreset=True)

user_input = input(Fore.GREEN + 'Que horas sao agora? --> ' + Style.RESET_ALL)

try:
    user_input_float = float(user_input)

    if user_input_float > 23.59:
        print(Fore.RED + 'Nao conheco essa hora!' + Style.RESET_ALL)

    if user_input_float % 2 == 0:
        user_input_float = int(user_input_float)

    if user_input_float >= 0 and user_input_float <= 11.59:
        print(Fore.LIGHTYELLOW_EX + f'Bom dia! ({user_input_float}H)' + Style.RESET_ALL)

    elif user_input_float >= 12 and user_input_float <= 17.59:
        print(Fore.YELLOW + f'Boa tarde! ({user_input_float}H)' + Style.RESET_ALL)

    elif user_input_float >= 18 and user_input_float <= 23.59:
        print(Fore.BLACK + f'Boa noite! ({user_input_float}H)' + Style.RESET_ALL)

except:
    print(Fore.RED + 'Isso nao e uma hora!' + Style.RESET_ALL)