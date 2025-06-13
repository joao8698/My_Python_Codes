"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
from colorama import Fore, Style, init
init(autoreset=True)

nome = input(Fore.BLUE + 'Qual o seu nome? --> ' + Style.RESET_ALL)

if nome == '':
    print(Fore.RED + 'Voce nao digitou nada!' + Style.RESET_ALL)

elif len(nome) <= 4:
    print(Fore.YELLOW + 'Seu nome e curto' + Style.RESET_ALL)

elif len(nome) >= 5 and len(nome) <= 6:
    print(Fore.YELLOW + 'Seu nome e normal' + Style.RESET_ALL)

elif len(nome) > 6:
    print(Fore.YELLOW + 'Seu nome e muito grande!' + Style.RESET_ALL)

print(len(nome))