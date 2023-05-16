from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class Loja:

    tarifa = 1.03

    def __init__(self, endereco: str) -> None:
        self.__endereco = endereco

    def get_endereco(self) -> str:
        return self.__endereco

    @classmethod
    def vender(cls) -> int:
        return 40 * cls.tarifa

    @classmethod
    def alterar_tarifa(cls, novaTarifa: int) -> None:
        cls.tarifa = novaTarifa


class formLoja(FlaskForm):
    loja1 = StringField('loja 1', validators=[DataRequired()])
    loja2 = StringField('loja 2', validators=[DataRequired()])
    novaTarifa = IntegerField('Nova Tarifa', validators=[DataRequired()])
    botao = SubmitField('Calcular')
