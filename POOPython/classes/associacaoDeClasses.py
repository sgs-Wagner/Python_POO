from typing import Type
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class Interruptor:

    def __init__(self, comodo: str) -> None:
        self.__comodo = comodo

    def acender(self):
        return f"acendendo {self.__comodo}"

    def apagar(self):
        return f'apagando {self.__comodo}'

class Pessoa:

    def __init__(self):
        pass

    def acender_luz(self, interruptor: Type[Interruptor]):
        return interruptor.acender()

    def apagar_luz(self, interruptor: Type[Interruptor]):
        return interruptor.apagar()

    def funcao_propria(self):
        return f'respirando....'

class form_associacaoClasse(FlaskForm):
    interruptor1 = StringField('Interruptor', validators=[DataRequired()])
    interruptor2 = StringField('Interruptor 2', validators=[DataRequired()])
    botao = SubmitField('Criar Interruptores')

