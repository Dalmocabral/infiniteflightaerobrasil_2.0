import os
basedir = os.path.abspath(os.path.dirname(__file__))



class Config(object):

    # Configuração da chave secreta flask WTF
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'

    # Configuração do flask-sqlachemy no banco de dados
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuração Flask-Admin tema
    FLASK_ADMIN_SWATCH = 'lumen'
    
    MAIL_SENDER=''
    MAIL_SERVER='mtp.googlemail.com'
    MAIL_PORT=587
    MAIL_USERNAME='dalmo.santos.cabral'
    MAIL_PASSWORD='aretha160491'
    MAIL_USE_TLS=True
    MAIL_USE_SSL=False
