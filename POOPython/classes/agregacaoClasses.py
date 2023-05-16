from typing import Type

class Produto:

    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    def informacoes_produtos(self):
        print('Produto {} tem valor R$ {}'.format(self.__nome, self.__valor))

class CarrinhoDeCompras:

    def __init__(self):
        self.__produtos = []

    def adicionar_produto(self, produto: Type[Produto]):
        self.__produtos.append(produto)

    def finalizar_compra(self):
        print('compras finalizada')

        for produto in self.__produtos:
            produto.informacoes_produtos()
            self.__produtos = []

# da p colocar interface e adicionar ao carrinho servicos, por exemplo

carro = CarrinhoDeCompras()
monitor = Produto('monitor', 100)
tv = Produto('tv', 150)
mouse = Produto('mouse', 200)
cerveja = Produto('cerveja', 300)
cama = Produto('cama', 400)
porta = Produto('porta', 500)

carro.adicionar_produto(monitor)
carro.adicionar_produto(tv)
carro.adicionar_produto(mouse)
carro.adicionar_produto(cerveja)
carro.adicionar_produto(cama)
carro.adicionar_produto(porta)

carro.finalizar_compra()