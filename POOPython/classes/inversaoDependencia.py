from abc import ABC, abstractmethod
from typing import Type


class Repositorio(ABC):
    @abstractmethod
    def inserir(self,dado):
        pass
    @abstractmethod
    def deletar(self, dado):
        pass

class MySql(Repositorio):

    def inserir(self, dado):
        print('Inserindo  {} no banco '.format(dado))

    def deletar(self, dado):
        print('deletando {} do banco'.format(dado))

class MongoDB(Repositorio):

    def inserir(self,dado):
        print('Inserindo  {} no banco '.format(dado))

    def deletar(self, dado):
        print('deletando {} do banco'.format(dado))

class Usuario:

    def __init__(self, repositorio: Type[Repositorio]):
        self.__repositorio = repositorio

    def armazenar_dado(self, dado):
        self.__repositorio.inserir(dado)

    def remover_dado(self, dado):
        self.__repositorio.deletar(dado)

# moral de usar interface, usuario n fica refem de um
# repositorio especifico, usa-se uma interface,
# os repositorios a obedece


usuario = Usuario(MySql())
usuario.armazenar_dado(23)
usuario.remover_dado(50)