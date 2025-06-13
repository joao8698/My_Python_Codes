'''
Escopo de funcoes em Python
Escopo significa o local onde aquele codigo pode atingir.
Existe o escopo global e local.
O escopo global e o escopo onde todo o codigo e alcancavel.
O escopo local e o escopo onde apenas os nomes do mesmo local
podem ser alcancados.
'''
x = 1

def escopo():
    x = 10 # Este x nao e igual ao outro x (ja que esta dentro do escopo da funcao)
    def outra_funcao():
        y = 5
        print(y, x)
    outra_funcao()
    print(x)

print(x)

escopo()

x = 1
# Todo o codigo que esta dentro de uma funcao, vao estar protegidos.

print('#####################################')

def escopo2():
    x = 5
    def escopo_dentro_de_outro_escopo():
        print(x)
    escopo_dentro_de_outro_escopo()

escopo2()

print(x)

print('#####################################')

x = 1

def func():
    global x
    x = 10
    def func1():
        x = 5
        y = 2
        print(y, x)
    func1()

func()
print(x)