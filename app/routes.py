from flask import Flask, flash, redirect, render_template, request, url_for 
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash

from app import app, db
from app.forms import LogbookForm, LoginForm, RegisterForm
from app.models import User, Logbook
from sqlalchemy.sql import func

import requests
import json

def get_json(url):
    return json.loads(requests.get(url).text)


flight = get_json('http://infinite-flight-public-api.cloudapp.net/v1/Flights.aspx?'
            'apikey=78879b1d-3ba3-47de-8e50-162f35dc6e04&sessionid=7e5dcd44-1fb5-49cc-bc2c-a9aab1f6a856')

points = get_json('https://raw.githubusercontent.com/Dalmocabral/infinteflightaerobrasil_atc/master/exceljson.json')

atc = get_json('http://infinite-flight-public-api.cloudapp.net/v1/GetATCFacilities.aspx?'
                'apikey=78879b1d-3ba3-47de-8e50-162f35dc6e04&sessionid=7e5dcd44-1fb5-49cc-bc2c-a9aab1f6a856')

@app.route('/')
@app.route('/index')
def index():    
    log = Logbook.query.order_by(Logbook.data_create.desc()).all()
    users = User.query.order_by(User.data_create.desc()).all()
    return render_template('index.html', 
    users=users, 
    log=log, 
    flight=flight, 
    point=points, 
    atc=atc )

@app.route('/pilotos')
def pilotos():
    log = Logbook.query.all()
    user = User.query.all() 
    return render_template('pilotos.html', users=user, log=log)

@app.route('/user_profile/<int:id>') 
def unique(id):
    va = db.session.query(func.sum(Logbook.tempo)).filter_by(user_id=id).all()    
    user= User.query.get(id)    
    log = Logbook.query.filter_by(user_id=id).order_by(Logbook.data_create.desc()).all()    
    return render_template('user_profile.html', user=user, log=log, va=va)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user = User()
        user.username = form.username.data.capitalize()
        user.email = form.email.data
        user.password = generate_password_hash(form.password.data)
        user.sobrenome = form.sobrenome.data.capitalize()
        user.gametag = form.gametag.data
        user.registro = form.registro.data
        user.ifcomunity = form.ifcomunity.data
        user.sobremim = form.sobremim.data
        user.base = form.base.data.upper()
        user.idade = form.idade.data
        user.grau = form.grau.data
        user.pais = form.pais.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if not user:
            flash('E-mail ou senha ínvalidas', 'danger')
            return redirect(url_for('login'))

        if not check_password_hash(user.password, form.password.data):
            flash('E-mail ou senha ínvalidas', 'danger')
            return redirect(url_for('login'))
            
        login_user(user)
        return redirect(url_for('index'))

    return render_template('login.html', form=form)

@app.route('/user/<int:id>')
@login_required
def user(id):
    user = User.query.get(id)
    va = db.session.query(func.sum(Logbook.tempo)).filter_by(user_id=id).all()  
    log = Logbook.query.filter_by(user_id=id).order_by(Logbook.data_create.desc()).all()
    return render_template('user.html', user=user, log=log, va=va)

@app.route('/user/<int:id>/add-logbook/', methods=['GET', 'POST'])
def logbook(id):
    form = LogbookForm()
    book =  Logbook.query.filter_by(user_id=current_user.id).all()
    if form.validate_on_submit():
        book = Logbook()
        book.saida = form.saida.data.upper()
        book.chegada = form.chegada.data.upper()
        book.aeronave = form.aeronave.data.upper()
        book.voo = form.voo.data.upper()        
        book.tempo = form.tempo.data
        book.user_id = current_user.id  
        book.status = 'Em analise'      
        db.session.add(book)
        db.session.commit()
        flash('LogBook Registrado com Sucesso!!', 'success')
        return redirect(url_for('logbook', id=current_user.id))    

    return render_template('logbook.html', form=form, book=book)

@app.route('/top10')
def top10():
    users = User.query.all()
    horas = db.session.query(func.sum(Logbook.tempo)).all()
    return render_template('top10.html', horas=horas, users=users)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
