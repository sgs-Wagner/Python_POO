class Pessoa:

    def __init__(self, nome):
        self.__local = None
        self.__nome = nome

    def entrar_no_local(self):
        self.__local.acender_luzes()

    def apresentar_local(self):
        endereco = self.__local.get_endereco()
        print(endereco)

    def se_apresentar(self):
        print('olá, sou  {}'.format(self.__nome))

    def set_local(self, local: any):
        self.__local = local

    def get_local(self):
        return self.__local

class Casa:

    def __init__(self):
        self.__endereco = 'rua dos bobos'
        self.__proprietario = None

    def acender_luzes(self):
        print('estou acendendo as luzes')

    def get_endereco(self):
        return self.__endereco

    def set_proprietario(self, proprietario: any):
        self.__proprietario = proprietario

    def get_proprietario(self):
        return self.__proprietario




casa = Casa()
wagner = Pessoa('wagner')

wagner.set_local(casa)
casa.set_proprietario(wagner)

proprietario = casa.get_proprietario()

proprietario.se_apresentar()

wagner.apresentar_local()
