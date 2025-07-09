# Funcoes recursivas e recursividade
# - Funcoes que podem se chamar de volta
# - uteis p/ dividir problemas grandes em partes menores
# Toda funcao recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursao
# - Fatorial - n! = 5 * 4 * 3 * 2 * 1 = 120

def recursiva(inicio=0, fim=10):
    # Caso Base
    if inicio >= fim:
        return fim

    # Caso recursivo
    # Contar ate chegar ao final
    inicio += 1
    return recursiva(inicio, fim)

recursiva()

# ============ FATORIAL ============ #

def factorial(n):
    if n <= 1:
        return 1
    
    return n * factorial(n - 1)

print(factorial(5))