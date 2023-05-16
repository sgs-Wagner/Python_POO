class Pai:

    def __init__(self):
        self.nome = 'Wagner'

    def comer(self):
        print('estou comendo com garfo...')

class Filho(Pai):

    def __init__(self):
        super().__init__()
        self.nome = 'Junior'

    def comer(self):
        print('estou comendo de colher...')

wagner = Pai()
wagner.comer()

junior = Filho()
junior.comer()