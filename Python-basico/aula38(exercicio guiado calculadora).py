''' Calculadora com While '''
from colorama import Fore, Style, init
init(autoreset=True)

print(Fore.BLUE + 'Escolha qual operacao deseja realizar...\n'
'[1] adicao\n'
'[2] subtracao\n'
'[3] multiplicacao\n'
'[4] divisao\n'
'[5] potenciacao\n'
'[6] resto\n'
'[0] sair' + Style.RESET_ALL)

while True:
    operacao_input = input(Fore.GREEN + 'Qual vai ser a operacao? ([0] se quiser sair) ... ----> ')
    if operacao_input == '1' \
    or operacao_input == '2' \
    or operacao_input == '3' \
    or operacao_input == '4' \
    or operacao_input == '5' \
    or operacao_input == '6' \
    or operacao_input == '0':
        if operacao_input == '0':
            print(Fore.RED + 'Voce saiu!' + Style.RESET_ALL)
            exit()
        try:
            primeiro_numero = float(input(Fore.GREEN + f'({operacao_input}) Qual o primeiro numero? --> '))
            segundo_numero = float(input(f'{primeiro_numero} ... Qual o segundo? --> ' + Style.RESET_ALL))
        except ValueError:
            print(Fore.RED + 'Numero invalido!' + Style.RESET_ALL)
            continue
    else:
        print(Fore.RED + 'Operacao invalida!' + Style.RESET_ALL)
        continue

    if operacao_input == '1':
        print(Fore.CYAN + f'{primeiro_numero} + {segundo_numero} = {primeiro_numero + segundo_numero}' + Style.RESET_ALL)

    elif operacao_input == '2':
        print(Fore.CYAN + f'{primeiro_numero} - {segundo_numero} = {primeiro_numero - segundo_numero}' + Style.RESET_ALL)

    elif operacao_input == '3':
        print(Fore.CYAN + f'{primeiro_numero} * {segundo_numero} = {primeiro_numero * segundo_numero}' + Style.RESET_ALL)

    elif operacao_input == '4':
            if segundo_numero == 0:
                print('Impossivel realizar divisao por zero!')
                continue
            print(Fore.CYAN + f'{primeiro_numero} / {segundo_numero} = {primeiro_numero / segundo_numero}' + Style.RESET_ALL)

    elif operacao_input == '5':
        print(Fore.CYAN + f'{primeiro_numero} ** {segundo_numero} = {primeiro_numero ** segundo_numero}' + Style.RESET_ALL)

    elif operacao_input == '6':
        print(Fore.CYAN + f'{primeiro_numero} % {segundo_numero} = {primeiro_numero % segundo_numero}' + Style.RESET_ALL)