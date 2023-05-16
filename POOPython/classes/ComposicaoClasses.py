class Select:

    def select_many(self):
        print('select Many')

    def select_one(self):
        print('Select One')

class Insert:

    def insert_many(self):
        print('Insert Many')

    def insert_one(self):
        print('Insert One')

# instancia as classes acima na classe repositorio,
# assim a classe repositorio é composta por objetos delas é um
# meio de se aproveitar das outras classes mas sem usar heranca tbm


class Repositorio:

    def __init__(self):
        self.__insert = Insert()
        self.__select = Select()

    def select_by_id(self):
        self.__select.select_one()

repo = Repositorio()
repo.select_by_id()