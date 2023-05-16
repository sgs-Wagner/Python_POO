from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class Estado:

    def __init__(self):
        self.__sgEstado = {
            'SP': 'São paulo',
            'RJ': 'Rio de Janeiro',
            'MG': 'Minas Gerais',
            'ES': 'Espirito Santo'
        }

    def get_estado(self):
        return self.__sgEstado

    def set_estado(self, nome, estado):
        self.__sgEstado[nome] = estado


class FormEstado(FlaskForm):
    nome = StringField('Sigla', validators=[DataRequired()])
    estado = StringField('Estado', validators=[DataRequired()])
    botao = SubmitField('Submit')