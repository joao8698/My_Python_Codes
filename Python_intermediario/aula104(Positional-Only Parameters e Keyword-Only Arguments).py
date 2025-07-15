# Controlando a quantidade de argumentos posicioanais e nomeados em funcoes
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)

# 🟢 Positional-Only Parameters (/) - Tudo antes da barra deve
# ser ! APENAS ! posicional.
# PEP 570 - Python Positional-Only Parameters

# 🟢 Keyword-Only Arguments (*) - * sozinho ! NAO SUGA ! valores.
# PEP 3102 - Keyword-Only Arguments

def soma(a, b, /, x, y):
    print(a + b + x + y)

soma(1, 2, 3, 4)