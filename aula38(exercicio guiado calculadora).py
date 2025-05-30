''' Calculadora com While '''
from colorama import Fore, Style, init
init(autoreset=True)

print(Fore.BLUE + 'Escolha qual operacao deseja realizar...\n'
'adicao (adicao)\n'
'subtracao (subtracao)\n'
'multiplicacao (multiplicacao)\n'
'divisao (divisao)\n'
'potenciacao (potenciacao)\n'
'resto (resto)\n'
'Se quiser sair, pode digitar "sair"' + Style.RESET_ALL)

while True:
    operacao_input = input(Fore.GREEN + 'Qual vai ser a operacao? (se quiser sair, digite "sair") ... ----> ')
    if operacao_input == 'adicao' \
    or operacao_input == 'subtracao' \
    or operacao_input == 'multiplicacao' \
    or operacao_input == 'divisao' \
    or operacao_input == 'potenciacao' \
    or operacao_input == 'resto' \
    or operacao_input == 'sair':
        if operacao_input == 'sair':
            print(Fore.RED + 'Voce saiu!' + Style.RESET_ALL)
            exit()
        try:
            primeiro_numero = int(input(Fore.GREEN + f'({operacao_input}) Qual o primeiro numero? --> '))
            segundo_numero = int(input(f'{primeiro_numero} ... Qual o segundo? --> ' + Style.RESET_ALL))
        except:
            print(Fore.RED + 'Numero invalido!' + Style.RESET_ALL)
            break
    else:
        print(Fore.RED + 'Operacao invalida!' + Style.RESET_ALL)
        break

    if operacao_input == 'adicao':
        print(Fore.CYAN + f'{primeiro_numero} + {segundo_numero} = {primeiro_numero + segundo_numero}' + Style.RESET_ALL)

    elif operacao_input == 'subtracao':
        print(Fore.CYAN + f'{primeiro_numero} - {segundo_numero} = {primeiro_numero - segundo_numero}' + Style.RESET_ALL)

    elif operacao_input == 'multiplicacao':
        print(Fore.CYAN + f'{primeiro_numero} * {segundo_numero} = {primeiro_numero * segundo_numero}' + Style.RESET_ALL)

    elif operacao_input == 'divisao':
            print(Fore.CYAN + f'{primeiro_numero} / {segundo_numero} = {primeiro_numero / segundo_numero}' + Style.RESET_ALL)

    elif operacao_input == 'potenciacao':
        print(Fore.CYAN + f'{primeiro_numero} ** {segundo_numero} = {primeiro_numero ** segundo_numero}' + Style.RESET_ALL)

    elif operacao_input == 'resto':
        print(Fore.CYAN + f'{primeiro_numero} % {segundo_numero} = {primeiro_numero % segundo_numero}' + Style.RESET_ALL)