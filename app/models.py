from app import db
from app import login_manager
from flask_login import UserMixin
from hashlib import md5
from datetime import datetime



@login_manager.user_loader
def current_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    sobrenome = db.Column(db.String(200))
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password = db.Column(db.String(120), nullable=False)
    gametag = db.Column(db.String(200))
    registro = db.Column(db.String(200))
    ifcomunity = db.Column(db.String(400))
    sobremim = db.Column(db.String(200))
    pais = db.Column(db.String(200))
    base = db.Column(db.String(200))
    idade = db.Column(db.String(200))
    grau = db.Column(db.String(200))    
    logbook = db.relationship('Logbook', backref='user', lazy='dynamic')  #lazy='dynamic'
    data_create = db.Column(db.DateTime, default=datetime.utcnow)
    pontos = db.Column(db.Integer(), default=0)
    cont_tempo = db.Column(db.Float, default=0)
    cont_tempo_str = db.Column(db.String(20000), default='00:00:00')
    cont_voo = db.Column(db.Integer, default=0)
    

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)


    def __str__(self):

        return self.username

class Logbook(db.Model):

    __tablename__ = 'logbooks'

    id = db.Column(db.Integer, primary_key=True)
    saida = db.Column(db.String(200))
    chegada = db.Column(db.String(200))
    aeronave = db.Column(db.String(200))
    voo = db.Column(db.String(200))
    tempo = db.Column(db.Time, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))     
    data_create = db.Column(db.DateTime, default=datetime.utcnow)


    def __str__(self):

        return self.voo


class Evento_1(db.Model):

    __tablename__ = 'eventos_1'

    id = db.Column(db.Integer, primary_key=True)     
    
    logo = db.Column(db.String(20))    
    origem = db.Column(db.String(120))    
    destino = db.Column(db.String(120))
    p_data = db.Column(db.String(20))
    voo = db.Column(db.String(200))       
    hora_partida = db.Column(db.String(120))
    hora_chegada = db.Column(db.String(120))
    aeronave = db.Column(db.String(120))
    gate = db.Column(db.String(120))    
    piloto = db.Column(db.String(120))    
    status = db.Column(db.String(120))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

class Evento_2(db.Model):

    __tablename__ = 'eventos_2'

    id = db.Column(db.Integer, primary_key=True)     
    logo = db.Column(db.String(20))    
    origem = db.Column(db.String(120))    
    destino = db.Column(db.String(120))    
    p_data = db.Column(db.String(20))
    voo = db.Column(db.String(200))       
    hora_partida = db.Column(db.String(120))
    hora_chegada = db.Column(db.String(120))
    aeronave = db.Column(db.String(120))
    gate = db.Column(db.String(120))    
    piloto = db.Column(db.String(120))    
    status = db.Column(db.String(120))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

class Evento_3(db.Model):

    __tablename__ = 'eventos_3'

    id = db.Column(db.Integer, primary_key=True)     
    logo = db.Column(db.String(20))    
    origem = db.Column(db.String(120))    
    destino = db.Column(db.String(120))    
    p_data = db.Column(db.String(20))
    voo = db.Column(db.String(200))       
    hora_partida = db.Column(db.String(120))
    hora_chegada = db.Column(db.String(120))
    aeronave = db.Column(db.String(120))
    gate = db.Column(db.String(120))    
    piloto = db.Column(db.String(120))    
    status = db.Column(db.String(120))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)



'''
$ flask db stamp head
$ flask db migrate
$ flask db upgrade

'''