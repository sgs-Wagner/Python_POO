from flask import Flask, request, render_template, flash, url_for, redirect
from classes.classescontexto import FormControle, ControleRemoto, controle_tv, controle_comodo, class_map
from classes.encapsulamentoprivado import FormEncapsulamentoPrivado, Calculadora
from classes.gettersetter import FormEstado, Estado
from classes.responsabilidadeUnica import SistamaCadastral, FormSistemaCadastral
from classes.variaveismetodosclasse import formLoja, Loja
from classes.metodosEstaticos import Error
from classes.associacaoDeClasses import Interruptor, form_associacaoClasse, Pessoa
from classes.abertoFechado import Circo, Palhaco, Malabarista
from classes.injecaoDependencia import Casa, Pessoa


app = Flask(__name__)
app.config['SECRET_KEY'] = "123456"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/composicaoClasses')
def composicaoClasses():
    return render_template('composicaoClasses.html')

@app.route('/agregacaoClasses')
def agregacaoClasses():
    return render_template('agregacaoClasses.html')

@app.route('/inversaoDependencia')
def inversaoDependencia():
    return render_template('inversaoDependencia.html')

@app.route('/segregacaoInterface')
def segregacaoInterface():
    return render_template('segregacaoInterface.html')

@app.route('/interface')
def interface():
    return render_template('interface.html')

@app.route('/metodosClassesAbstratas')
def metodosClassesAbstratas():
    return render_template('metodosClassesAbstratas.html')

@app.route('/polimorfismo')
def polimorfismo():
    return render_template('polimorfismo.html')

@app.route('/principioSubstituicao')
def principioSubstituicao():
    return render_template('principioSubstituicao.html')

@app.route('/encapsulamentoHeranca')
def encapHeranca():
    return render_template('encapsulamentoHeranca.html')

@app.route('/introducaoHeranca')
def introHeranca():
    return render_template('introducaoHeranca.html')

@app.route('/variaveisemetodosdeclasse', methods=['GET', 'POST'])
def variaveisEmetodos():
    form_variaveismetodosclasse = formLoja()
    loja1 = None
    loja2 = None
    loja1Inicial = None
    loja2Inicial = None
    novaTarifa = form_variaveismetodosclasse.novaTarifa.data
    if 'botao' in request.form:
        loja1 = Loja(form_variaveismetodosclasse.loja1.data)
        loja2 = Loja(form_variaveismetodosclasse.loja2.data)
        loja1Inicial = loja1.vender()
        loja2Inicial = loja2.vender()
        loja1.alterar_tarifa(novaTarifa)
    return render_template('variaveisMetodosDeClasse.html',  form_variaveismetodosclasse=form_variaveismetodosclasse, loja1=loja1, loja2=loja2, novaTarifa=novaTarifa, loja2Inicial= loja2Inicial, loja1Inicial=loja1Inicial)


@app.route('/metodosEstaticos')
def metodosEstaticos():
    classe = Error()
    ex1 = classe.error_500()
    ex2 = classe.error_404()
    return render_template('metodosEstaticos.html', classe=classe, ex1=ex1, ex2=ex2)

@app.route('/injecaoDependencia')
def injecaoDependencia():
    casa = Casa()
    pessoa = Pessoa('wagner', casa)

    return render_template('injecaoDependencia.html', pessoa=pessoa)
@app.route('/bilateral')
def bilateral():
    return  render_template('bilateral.html')

@app.route('/associacaoDeClasses', methods=['GET', 'POST'])
def associacaoClasses():
    form = form_associacaoClasse()
    inter1 = None
    inter2 = None
    acenderLuz = None
    apagarLuz = None
    proprio = None

    if 'botao' in request.form:
        inter1 = Interruptor(form.interruptor1.data)
        inter2 = Interruptor(form.interruptor2.data)
        pessoa = Pessoa()
        acenderLuz = pessoa.acender_luz(inter1)
        apagarLuz = pessoa.apagar_luz(inter2)
        proprio = pessoa.funcao_propria()

    return render_template('/associacaoClasses.html', form=form, inter1=inter1, inter2=inter2, acenderLuz=acenderLuz, apagarLuz=apagarLuz, proprio=proprio)

@app.route('/abertoFechado', methods=['GET', 'POST'])
def abertoFechado():
    circo = Circo()
    palhaco = Palhaco()
    malabarista = Malabarista()
    p = circo.apresentar(palhaco)
    m = circo.apresentar(malabarista)
    print(p)
    print(m)
    return render_template('abertoFechado.html', p=p, m=m)

@app.route('/responsabilidadeUnica',  methods=['GET', 'POST'])
def responsabilidadeUnica():
    form_resUnica = FormSistemaCadastral()
    sistema = None
    if 'botao' in request.form:
        sistema = SistamaCadastral(form_resUnica.nome.data, form_resUnica.idade.data)

    return render_template('responsabilidadeUnica.html', form_resUnica=form_resUnica, sistema=sistema)

@app.route('/estados', methods=['GET', 'POST'])
def estados():
    frm_estado= FormEstado()
    estado = Estado()

    if 'botao' in request.form:
        sg = frm_estado.nome.data
        nome = frm_estado.estado.data
        estado.set_estado(sg, nome)

    return render_template('gettersetter.html', frm_estado=frm_estado, estado=estado)














@app.route('/classescontexto', methods=['GET', 'POST'])
def classescontexto():
    form_criarcontrole = FormControle()
    if 'botao' in request.form:
        tv = form_criarcontrole.televisao.data
        comodo = form_criarcontrole.comodo.data
        controle = ControleRemoto(tv, comodo)
        flash(f'Controle criado com sucesso...', 'alert-success')
        return redirect(url_for('classescontexto'))

    if 'btnMudar' in request.form:
        novocanal = form_criarcontrole.mudar.data
        tvSelecionada = request.form['televisao']
        class_map[tvSelecionada]= novocanal

    return render_template('classescontexto.html', form_criarcontrole=form_criarcontrole, controle_comodo=controle_comodo, controle_tv=controle_tv, class_map=class_map)


@app.route('/encapsulamentoprivado', methods=['GET', 'POST'])
def encapsulamentoprivado():
    form_ePrivado = FormEncapsulamentoPrivado()
    resposta = 'Insira os número e escolha a operação primeiro'
    if 'btnSomar' in request.form:
        calculadora = Calculadora()
        resposta = calculadora.calcular('+', form_ePrivado.num1.data , form_ePrivado.num2.data )

    if 'btnSubtrair' in request.form:
        calculadora = Calculadora()
        resposta = calculadora.calcular('-', form_ePrivado.num1.data , form_ePrivado.num2.data )

    return render_template('encapsulamentoprivado.html', form_ePrivado=form_ePrivado, resposta=resposta)


if __name__ == '__main__':
    app.run(debug=True)



