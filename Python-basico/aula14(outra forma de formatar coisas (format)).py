a = 'A'
b = 'B'
c = 1.1
formato = ''

print(formato)

# Tudo dentro do Python e um objeto, e todo o objeto tem um metodo dentro dele
# um dos metodos que as strings(objeto) tem, e o meteodo .format()

formato = 'a={} b={} c={}'.format(a, b, c)
print(formato)

# primeira chave referencia ao primeiro valor, segunda ao segundo e terceira ao terceiro (depende da ordem)

string = 'a={2:.2f} b={0} c={1}'
formato = string.format(a, b, c)
print(formato)

# Da pra mudar tambem a order da formatacao usando o indice

# os parametros dentro do .format() sao chamados de parametro nomeado
# Parametro nomeado e quando voce da um nome as coisas dentro da chamada das funcoes ou da criacao das funcoes

string = 'a={nome1} b={nome2} c={nome3}'
formato = string.format(
    nome1 =a, nome2=b, nome3=c
    #parametro/argumento, parametro/argumento, parametro/argumento
)
# Tudo que vem depois de um parametro nomeado, precisa tambem ser nomeado

print(formato)

# Toda funcao que esta dentro de um objeto e chamada de metodo (method)

# Vamos passar a, b e c para a funcao .format()
# nesse momento a, b e c sao argumentos, que estao sendo passadas para dentro de .format()