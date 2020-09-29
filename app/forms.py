from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError, email
from wtforms.fields.html5 import TimeField
from app.models import User


paises = SelectField('País de origem', choices=[
        ("África do Sul", "África do Sul"),
        ("Albânia", "Albânia"),
        ("Alemanha", "Alemanha"),
        ("Andorra", "Andorra"),
        ("Angola", "Angola"),
        ("Anguilla", "Anguilla"),
        ("Antigua", "Antigua"),
        ("Arábia Saudita", "Arábia Saudita"),
        ("Argentina", "Argentina"),
        ("Armênia", "Armênia"),
        ("Aruba", "Aruba"),
        ("Austrália", "Austrália"),
        ("Áustria", "Áustria"),
        ("Azerbaijão", "Azerbaijão"),
        ("Bahamas", "Bahamas"),
        ("Bahrein", "Bahrein"),
        ("Bangladesh", "Bangladesh"),
        ("Barbados", "Barbados"),
        ("Bélgica", "Bélgica"),
        ("Benin", "Benin"),
        ("Bermudas", "Bermudas"),
        ("Botsuana", "Botsuana"),
        ("Brasil", "Brasil"),
        ("Brunei", "Brunei"),
        ("Bulgária", "Bulgária"),
        ("Burkina Fasso", "Burkina Fasso"),
        ("botão", "botão"),
        ("Cabo Verde", "Cabo Verde"),
        ("Camarões", "Camarões"),
        ("Camboja", "Camboja"),
        ("Canadá", "Canadá"),
        ("Cazaquistão", "Cazaquistão"),
        ("Chade", "Chade"),
        ("Chile", "Chile"),
        ("China", "China"),
        ("Cidade do Vaticano", "Cidade do Vaticano"),
        ("Colômbia", "Colômbia"),
        ("Congo", "Congo"),
        ("Coréia do Sul", "Coréia do Sul"),
        ("Costa do Marfim", "Costa do Marfim"),
        ("Costa Rica", "Costa Rica"),
        ("Croácia", "Croácia"),
        ("Dinamarca", "Dinamarca"),
        ("Djibuti", "Djibuti"),
        ("Dominica", "Dominica"),
        ("EUA", "EUA"),
        ("Egito", "Egito"),
        ("El Salvador", "El Salvador"),
        ("Emirados Árabes", "Emirados Árabes"),
        ("Equador", "Equador"),
        ("Eritréia", "Eritréia"),
        ("Escócia", "Escócia"),
        ("Eslováquia", "Eslováquia"),
        ("Eslovênia", "Eslovênia"),
        ("Espanha", "Espanha"),
        ("Estônia", "Estônia"),
        ("Etiópia", "Etiópia"),
        ("Fiji", "Fiji"),
        ("Filipinas", "Filipinas"),
        ("Finlândia", "Finlândia"),
        ("França", "França"),
        ("Gabão", "Gabão"),
        ("Gâmbia", "Gâmbia"),
        ("Gana", "Gana"),
        ("Geórgia", "Geórgia"),
        ("Gibraltar", "Gibraltar"),
        ("Granada", "Granada"),
        ("Grécia", "Grécia"),
        ("Guadalupe", "Guadalupe"),
        ("Guam", "Guam"),
        ("Guatemala", "Guatemala"),
        ("Guiana", "Guiana"),
        ("Guiana Francesa", "Guiana Francesa"),
        ("Guiné-bissau", "Guiné-bissau"),
        ("Haiti", "Haiti"),
        ("Holanda", "Holanda"),
        ("Honduras", "Honduras"),
        ("Hong Kong", "Hong Kong"),
        ("Hungria", "Hungria"),
        ("Iêmen", "Iêmen"),
        ("Ilhas Cayman", "Ilhas Cayman"),
        ("Ilhas Cook", "Ilhas Cook"),
        ("Ilhas Curaçao", "Ilhas Curaçao"),
        ("Ilhas Marshall", "Ilhas Marshall"),
        ("Ilhas Turks & Caicos", "Ilhas Turks & Caicos"),
        ("Ilhas Virgens (brit.)", "Ilhas Virgens (brit.)"),
        ("Ilhas Virgens(amer.)", "Ilhas Virgens(amer.)"),
        ("Ilhas Wallis e Futuna", "Ilhas Wallis e Futuna"),
        ("Índia", "Índia"),
        ("Indonésia", "Indonésia"),
        ("Inglaterra", "Inglaterra"),
        ("Irlanda", "Irlanda"),
        ("Islândia", "Islândia"),
        ("Israel", "Israel"),
        ("Itália", "Itália"),
        ("Jamaica", "Jamaica"),
        ("Japão", "Japão"),
        ("Jordânia", "Jordânia"),
        ("Kuwait", "Kuwait"),
        ("Latvia", "Latvia"),
        ("Líbano", "Líbano"),
        ("Liechtenstein", "Liechtenstein"),
        ("Lituânia", "Lituânia"),
        ("Luxemburgo", "Luxemburgo"),
        ("Macau", "Macau"),
        ("Macedônia", "Macedônia"),
        ("Madagascar", "Madagascar"),
        ("Malásia", "Malásia"),
        ("Malaui", "Malaui"),
        ("Mali", "Mali"),
        ("Malta", "Malta"),
        ("Marrocos", "Marrocos"),
        ("Martinica", "Martinica"),
        ("Mauritânia", "Mauritânia"),
        ("Mauritius", "Mauritius"),
        ("México", "México"),
        ("Moldova", "Moldova"),
        ("Mônaco", "Mônaco"),
        ("Montserrat", "Montserrat"),
        ("Nepal", "Nepal"),
        ("Nicarágua", "Nicarágua"),
        ("Niger", "Niger"),
        ("Nigéria", "Nigéria"),
        ("Noruega", "Noruega"),
        ("Nova Caledônia", "Nova Caledônia"),
        ("Nova Zelândia", "Nova Zelândia"),
        ("Omã", "Omã"),
        ("Palau", "Palau"),
        ("Panamá", "Panamá"),
        ("Papua-nova Guiné", "Papua-nova Guiné"),
        ("Paquistão", "Paquistão"),
        ("Paraguai", "Paraguai"),
        ("Peru", "Peru"),
        ("Polinésia Francesa", "Polinésia Francesa"),
        ("Polônia", "Polônia"),
        ("Porto Rico", "Porto Rico"),
        ("Portugal", "Portugal"),
        ("Qatar", "Qatar"),
        ("Quênia", "Quênia"),
        ("Rep. Dominicana", "Rep. Dominicana"),
        ("Rep. Tcheca", "Rep. Tcheca"),
        ("Reunion", "Reunion"),
        ("Romênia", "Romênia"),
        ("Ruanda", "Ruanda"),
        ("Rússia", "Rússia"),
        ("Saipan", "Saipan"),
        ("Samoa Americana", "Samoa Americana"),
        ("Senegal", "Senegal"),
        ("Serra Leone", "Serra Leone"),
        ("Seychelles", "Seychelles"),
        ("Singapura", "Singapura"),
        ("Síria", "Síria"),
        ("Sri Lanka", "Sri Lanka"),
        ("St. Kitts & Nevis", "St. Kitts & Nevis"),
        ("St. Lúcia", "St. Lúcia"),
        ("St. Vincent", "St. Vincent"),
        ("Sudão", "Sudão"),
        ("Suécia", "Suécia"),
        ("Suiça", "Suiça"),
        ("Suriname", "Suriname"),
        ("Tailândia", "Tailândia"),
        ("Taiwan", "Taiwan"),
        ("Tanzânia", "Tanzânia"),
        ("Togo", "Togo"),
        ("Trinidad & Tobago", "Trinidad & Tobago"),
        ("Tunísia", "Tunísia"),
        ("Turquia", "Turquia"),
        ("Ucrânia", "Ucrânia"),
        ("Uganda", "Uganda"),
        ("Uruguai", "Uruguai"),
        ("Venezuela", "Venezuela"),
        ("Vietnã", "Vietnã"),
        ("Zaire", "Zaire"),
        ("Zâmbia", "Zâmbia"),
        ("Zimbábue", "Zimbábue")])


class ProfileForm(FlaskForm):
    username = StringField('Nome',  validators=[DataRequired('O campo e obrigatório')])
    sobrenome = StringField('Sobrenome', validators=[DataRequired()])
    email = StringField('E-mail', validators=[Email()])
    gametag = StringField('Gametag', validators=[DataRequired()])
    registro = StringField('Registro', validators=[DataRequired()])
    ifcomunity = StringField('IFComunity', validators=[DataRequired()])
    sobremim = TextAreaField('Sobre mim', validators=[DataRequired()]) 
    base = StringField('Base', validators=[DataRequired()])
    idade = StringField('Data de Nascimento', validators=[DataRequired()])
    grau =  SelectField('Grau', choices=[('3', '3'), ('4', '4'), ('5', '5')])
    pais = paises
    submit = SubmitField("salvar")


class ForgotPasswordForm(FlaskForm):
    email = StringField('E-mail', validators=[Email()])
    submit = SubmitField("Recuperar")


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Senha antiga')
    new_password = PasswordField('Nova Senha', validators=[Length(3, 9, 'O campo dever conter 3 á 9 caracters' )])
    confirm_password = PasswordField('Confirmar Nova Senha', validators=[Length(3, 9, 'O campo dever conter 3 á 9 caracters' )])
    submit = SubmitField("salvar")


class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[Email()])
    password = PasswordField('Password', validators=[Length(3, 9, 'O campo dever conter 3 á 9 caracters' )])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Entrar')


class RegisterForm(FlaskForm):
    username = StringField('Nome',  validators=[DataRequired('O campo e obrigatório')])
    sobrenome = StringField('Sobrenome', validators=[DataRequired()])
    email = StringField('E-mail', validators=[Email()])
    password = PasswordField('Password', validators=[Length(3, 9, 'O campo dever conter 3 á 9 caracters' )]) 
    password2 = PasswordField('Repete a Senha', validators=[DataRequired(), EqualTo('password')])
    gametag = StringField('Gametag', validators=[DataRequired()])
    registro = StringField('Registro', validators=[DataRequired()])
    ifcomunity = StringField('IFComunity', validators=[DataRequired()])
    sobremim = TextAreaField('Sobre mim', validators=[DataRequired()]) 
    base = StringField('Base', validators=[DataRequired()])
    idade = StringField('Data de Nascimento', validators=[DataRequired()])
    grau =  SelectField('Grau', choices=[('3', '3'), ('4', '4'), ('5', '5')])
    pais = paises

    submit = SubmitField('Registrar')    

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Por favor usar um email diferente')
    
        
class LogbookForm(FlaskForm):

    saida = StringField('Saida', validators=[DataRequired()])
    chegada = StringField('Chegada', validators=[DataRequired()])
    aeronave = SelectField('Aeronave', choices=[
        ("Airbus A318-100", "Airbus A318-100"),
        ('Airbus A319-100', 'Airbus A319-100'),
        ('Airbus A320-200', 'Airbus A320-200'),
        ('Airbus A321-200', 'Airbus A321-200'),
        ('Airbus A330-200F', 'Airbus A330-200F'),
       
    ])
    voo = StringField('Voo', validators=[DataRequired()])
    tempo = TimeField('Tempo Total',  validators=[DataRequired('O campo e obrigatório')])    
    submit = SubmitField('Enviar')

