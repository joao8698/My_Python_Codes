# Mantendo estados dentro da classe

class Camera:

    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} JA esta filmando')
            return

        print(f'{self.nome} esta filmando...')
        self.filmando = True

    def parar_filmagem(self):
        if not self.filmando:
            print(f'{self.nome} nao esta filmando')
            return
        
        else:
            self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} nao pode fotografar enquanto filma!')
            return

        print(f'{self.nome} fotografou')

c1 = Camera('Canon')
c2 = Camera('Sony')

c1.filmar()
c1.fotografar()
c1.parar_filmagem()
c1.fotografar()