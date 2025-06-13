"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
import re

while True:
    resultado_digito1 = 0
    contador_multiplicativo_regresivo = 10
    user_input = input('Por favor, digite um CPF e diremos o se ele e valido!: ')
    # cpf = ''.join(filter(str.isdigit, user_input))
    # OU
    cpf = re.sub(r'[^0-9]', '', user_input) 
    if cpf == cpf[0] * 11:
        print('CPF invalido, todos os digitos sao iguais!')
        continue
    if len(cpf) == 11:
        for numero in cpf[:9]:
            numeros = int(numero)
            numeros *= contador_multiplicativo_regresivo
            resultado_digito1 += numeros
            contador_multiplicativo_regresivo -= 1

        resultado_digito1 *= 10
        resultado_digito1 %= 11

        resultado_digito1 = resultado_digito1 if resultado_digito1 <= 9 else 0

        resultado_digito2 = 0
        contador_multiplicativo_regresivo = 11
        for numero in cpf[:10]:
            numeros = int(numero)
            numeros *= contador_multiplicativo_regresivo
            resultado_digito2 += numeros
            contador_multiplicativo_regresivo -= 1

        resultado_digito2 *= 10
        resultado_digito2 %= 11

        resultado_digito2 = resultado_digito2 if resultado_digito2 <= 9 else 0

        validacao = 'CPF valido!' if str(resultado_digito1) == cpf[-2] and str(resultado_digito2) == cpf[-1] else 'CPF invalido!'
        print(validacao)
    else:
        print('CPF invalido!')
"""
Calculo do segundo dígito do CPF
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""