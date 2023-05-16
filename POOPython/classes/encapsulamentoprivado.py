from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class Calculadora:
    def __init__(self):
        pass

    def calcular(self, op, num1, num2):
        if op == '+':
            return self.__adicionar(num1, num2)
        elif op == '-':
            return self.__subtrair(num1, num2)
        else:
            return f'erro...'

    def __adicionar(self, num1, num2):

        soma = int(num1) + int(num2)
        return soma

    def __subtrair(self, num1, num2):
        subt = int(num1) - int(num2)
        return subt

class FormEncapsulamentoPrivado(FlaskForm):
    num1 = StringField('Numero 1 ', validators=[DataRequired()])
    num2 = StringField('Numero 2 ', validators=[DataRequired()])
    btnSomar = SubmitField('Somar')
    btnSubtrair = SubmitField('Subtrair')