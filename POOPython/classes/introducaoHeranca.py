class Mae:

    def __init__(self, endereco):
        self.endereco = endereco
        self.sobrenome = 'souza gomes silva'

    def comer(self):
        print('estou comendo...')

    def estudar(self):
        print('estou estudando...')

class Filha(Mae):

    def __init__(self, endereco):
        super().__init__(endereco)

    def brincar(self, brinquedo):
        print('estou brincando de {}'.format(brinquedo))

class Neta(Filha):

    def __init__(self, endereco):
        super().__init__(endereco)

wagner = Mae('rua dos bobos')
souza = Filha('rua 10')
souza.brincar('correr')

print(wagner.endereco)