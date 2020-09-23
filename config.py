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
    FLASK_ADMIN_SWATCH = 'Darkly'
    