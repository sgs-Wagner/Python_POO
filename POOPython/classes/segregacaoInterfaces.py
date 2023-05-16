from abc import ABC, abstractmethod

class AveVoadora(ABC):

    @abstractmethod
    def comer(self):
        raise 'obrigatorio implementar metodo comer'

    @abstractmethod
    def voar(self):
        raise 'obrigatorio implementar metodo voar'

    @abstractmethod
    def gritar(self):
        raise 'deve implementer metodo gritar'

class AveQueNaoVoa(ABC):

    @abstractmethod
    def comer(self):
        raise 'obrigatorio implementar metodo comer'

    @abstractmethod
    def gritar(self):
        raise 'deve implementer metodo gritar'


class Canario(AveVoadora):

    def comer(self):
        print('estou comendo')

    def voar(self):
        print('voando...')

    def gritar(self):
        print('estou gritando...')

class Pinguim(AveQueNaoVoa):

    def comer(self):
        print('estou comendo')

    def gritar(self):
        print('estou gritando...')
        
# ao inves de criar uma interface para ave, segrega-se essa possivel classe em duas, pois os "filhos" nao usam os mesmos métodos...

canario = Canario()
pinguim = Pinguim()

canario.voar()
pinguim.gritar()