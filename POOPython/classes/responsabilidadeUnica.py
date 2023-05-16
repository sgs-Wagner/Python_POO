from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

# futuro: try catch
class SistamaCadastral:

    def __init__(self, nome: str, idade: int) -> None:
        if self.__verificar_dados(nome, idade):
            self.__armazenar_usuario(nome, idade)
        else:
            self.__indicar_erro()


    def __verificar_dados(self, nome: str, idade: int) -> bool:
        if isinstance(nome, str) and isinstance(idade, int):
                return True
        else:
            return False

    def __armazenar_usuario(self, nome: str, idade: int) -> None:
        print(f'acessando bd...{nome}, com {idade} anos, cadastrado com sucesso')

    def __indicar_erro(self) -> None:
        print('dados inválidos...')

class FormSistemaCadastral(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    idade = IntegerField('Idade', validators=[DataRequired()])
    botao = SubmitField('Cadastrar')