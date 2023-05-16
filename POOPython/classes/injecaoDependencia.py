from typing import Type

class Casa:

    def __init__(self) -> None:
        self.__endereco = 'Rua dos Bobos'

    def acender_luzes(self):
        return 'estou ligando as luzes...'

    def get_endereco(self):
        return self.__endereco

class Pessoa:

    def __init__(self, nome, local:Type[Casa]):
        self.__local = local
        self.__nome = nome

    def entrar_no_local(self):
        return self.__local.acender_luzes()

    def apresentar_local(self):
        return self.__local.get_endereco()

