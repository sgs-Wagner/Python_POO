class Circo:

    def apresentar(self, apresentador: any):
        return apresentador.apresentar()


class Malabarista:

    def apresentar(self):
        x = 1 + 2
        return "malabarista aprensentando seu show..."

class Palhaco:

    def apresentar(self):
        x = "palhaco aprensentando seu show..."
        return x

class Domador:

    def apresentar(self):
        print('domador apresentando seu show...')

circo = Circo()
domador = Domador()
malabarista = Malabarista()

x = circo.apresentar(malabarista)
circo.apresentar(domador)
print(x, "........!!")