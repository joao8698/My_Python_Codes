# Try, except, else e finally

# try:
#     a = 18
#     b = 0
#     # print(b[0])
#     print('Linha 1'[1000])
#     c = a / b
#     print('Linha 2')
# except ZeroDivisionError:
#     print('Dividiu por zero.')
# except NameError:
#     print('Nome b não está definido')
# except (TypeError, IndexError):
#     print('TypeError + IndexError')
# except Exception:
#     print('ERRO DESCONHECIDO.')

# print('CONTINUAR')

try:
    a = 18
    print(a[1000])
    b = 0
    c = a / b
except (ZeroDivisionError, TypeError) as error:
    print(error.__class__.__name__ ,error)

#####################################

try:
    print(1)
finally:
    print(2)

#####################################

try:
    print(1)
    8/0
except Exception as error:
    print(error)
finally:
    print('Acabou finalmente!')

#####################################

try:
    print(1)
    # 8/0
except Exception as error:
    print(error)
else:
    print('Nao deu nenhum erro')
finally:
    print('Acabou finalmente!')