"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
from colorama import Fore, Style, init
init(autoreset=True)

numero = input( Fore.LIGHTCYAN_EX + 'Por favor, digite um numero INTEIRO --> ' + Style.RESET_ALL)

try:
    numero = int(numero)

    if numero % 2 == 0:
        print(Fore.GREEN + f'Seu numero {numero} e um numero par' + Style.RESET_ALL)

    elif numero % 2 != 0:
        print(Fore.GREEN + f'Seu numero {numero} e um numero impar' + Style.RESET_ALL)
except:
    print( Fore.RED + 'Voce nao digitou um numero inteiro!' + Style.RESET_ALL)