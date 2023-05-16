from abc import ABC, abstractmethod
from typing import Type

class FomasInterface(ABC):

    @abstractmethod
    def get_perimetro(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

class TerrenoQuadrado(FomasInterface):

    def __init__(self, lado):
        self.lado = lado

    def get_perimetro(self):
        perimetro = self.lado * 4
        return perimetro

    def get_area(self):
        area = self.lado * self.lado
        return area


class TerrenoRetangulo(FomasInterface):

    def __init__(self, lado, comprimento):
        self.lado = lado
        self.comprimento = comprimento

    def get_perimetro(self):
        perimetro = self.lado * 2 + self.comprimento * 2
        return perimetro

    def get_area(self):
        area = self.lado * self.comprimento
        return area


class Engenheiro:

    def __init__(self, nome):
        self.nome = nome

    def medir_perimetro(self, terreno: Type[FomasInterface]):
        perimetro = terreno.get_perimetro()
        print('{} mediu o perimetro: {}'.format(self.nome, perimetro))

    def medir_area(self, terreno: Type[FomasInterface]):
        area = terreno.get_area()
        print('{} mediu a area: {}'.format(self.nome, area))


engenheiro = Engenheiro('wagner')
terrenoQuadrado = TerrenoQuadrado(4)
terrenoRetangular = TerrenoRetangulo(2,3)

engenheiro.medir_area(terrenoQuadrado)
engenheiro.medir_perimetro(terrenoQuadrado)

engenheiro.medir_perimetro(terrenoRetangular)
engenheiro.medir_area(terrenoRetangular)