from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

controle_tv = []
controle_comodo = []
class_map = {

}
class ControleRemoto():

    def __init__(self, televisao, comodo):
        self.televisao = televisao
        self.comodo = comodo
        self.canal = 1
        controle_tv.append(self.televisao)
        controle_comodo.append(self.comodo)
        class_map[self.televisao] = self.canal
        print(controle_tv, controle_comodo)


    def escolher_canal(self, canal):
        self.canal = canal
        class_map[self.televisao] = self.canal
        return "canal selecionado: " + self.canal

class FormControle(FlaskForm):
    televisao = StringField('Televisao', validators=[DataRequired()])
    comodo = StringField('Comodo', validators=[DataRequired()])
    botao = SubmitField('Criar')

    mudar = StringField('Mudar Canal', validators=[DataRequired()])
    btnMudar = SubmitField('Mudar')



