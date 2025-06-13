# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -
# TODAS AS CONTAS VAO SER EXECUTADAS SEGUINDO A SEQUENCIA ACIMA

conta_1 = 1 + 1 ** 5 + 5
print(conta_1)

# A conta vai dar 7 porque primeiro ele faz a exponenciacao/potenciacao entre 1 e 5 (1 ** 5)
# e so depois as somas

# no caso 1 + 1 ** 5 + 5
#           1 + 1 + 5
#             2 + 5
#               7

# Se eu quiser que o valor da conta acima de 1024, podemos forcar algumas execucoes, desse jeito

conta_2 = (1 + 1) ** (5 + 5)
print(conta_2)

# no caso (1 + 1) ** (5 + 5)
#               2 ** 10
#                1024