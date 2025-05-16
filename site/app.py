
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_ultrasecreta'

class ContactForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Telefone')
    service = SelectField('Serviço', choices=[
        ('', 'Selecione um serviço'),
        ('lavagem', 'Lavagem Completa'),
        ('polimento', 'Polimento'),
        ('vitrificacao', 'Vitrificação'),
        ('estofados', 'Limpeza de Estofados')
    ])
    message = TextAreaField('Mensagem')
    submit = SubmitField('Enviar')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/servicos')
def servicos():
    services = [
        {'nome': 'Lavagem Premium', 'desc': 'Lavagem completa com cera em pasta', 'preco': 'R$ 120,00'},
        {'nome': 'Polimento', 'desc': 'Remoção de riscos e imperfeições', 'preco': 'R$ 300,00'},
        {'nome': 'Vitrificação', 'desc': 'Proteção da pintura por 1 ano', 'preco': 'R$ 800,00'},
        {'nome': 'Higienização', 'desc': 'Limpeza profunda de estofados', 'preco': 'R$ 250,00'}
    ]
    return render_template('servicos.html', services=services)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    form = ContactForm()
    if form.validate_on_submit():
        flash('Sua mensagem foi enviada com sucesso!', 'success')
        return redirect(url_for('contato'))
    return render_template('contato.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
