from abc import ABC, abstractmethod

class AbstractClass(ABC):

    def __init__(self):
        self.atributo = 'ola, mundo'

    def metodo(self, elemento):
        print(elemento)

    @abstractmethod
    def metodo_abstrato(self):
        pass # filha é obrigado a ter esse metodo!


class Filha(AbstractClass):

    def apresentar_metodo(self):
        print(self.atributo)

    def metodo_abstrato(self):
        print('implementando metodo abstrato')

filha = Filha()
filha.apresentar_metodo()
filha.metodo('usando metodo da mae...')
filha.metodo_abstrato()