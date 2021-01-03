import datetime
import json

import requests
from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_required, login_user, logout_user
from sqlalchemy.sql import func
from werkzeug.security import check_password_hash, generate_password_hash
from app.services.mail import send_email

from app import app, db
from app.forms import (ChangePasswordForm, ForgotPasswordForm, LogbookForm,
                       LoginForm, ProfileForm, RegisterForm)
from app.models import Logbook, User, Evento_1, Evento_2, Evento_3
from app.tools import get_all_time, get_all_time2
from app.get_user import get_flight, get_ifatc, get_icao




@app.route('/')
@app.route('/index')
def index():    
    log = Logbook.query.order_by(Logbook.data_create.desc()).limit(5).all()
    users = User.query.order_by(User.data_create.desc()).limit(5).all()
    tusuario = User.query.all()
    tlogbook = Logbook.query.all()    
    return render_template('index.html', 
    users=users, 
    log=log, 
    flight=get_flight(),
    atc=get_ifatc(),
    fixo=get_icao(),
    tusuario=tusuario,
    tlogbook=tlogbook)

@app.route('/pilotos')
def pilotos():
    log = Logbook.query.all()
    user = User.query.all() 
    return render_template('pilotos.html', users=user, log=log)

@app.route('/user_profile/<int:id>') 
def unique(id):
    va = get_all_time2(Logbook.query.filter_by(user_id=id).all())
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
        return redirect(url_for('login'))

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
    va = get_all_time2(Logbook.query.filter_by(user_id=id).all())
    user = User.query.get(id)
    flying_time = get_all_time(Logbook.query.filter_by(user_id=id).all())
    log = Logbook.query.filter_by(user_id=id).order_by(Logbook.data_create.desc()).all()
    return render_template('user.html', user=user, log=log, flying_time=flying_time, va=va)


@app.route("/recuperar-senha", methods=["GET", "POST"])
@login_required
def forgot_password():
    form = ForgotPasswordForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data)
        if not user:
            flash("usuário não encontrado", "danger")
            return redirect(url_for(".forgot_password"))  

        send_email(user.email, "recuperar senha", "forgot", user=user)

    return render_template("forgot-password.html", form=form)

@app.route("/user/profile", methods=["GET", "POST"])
@login_required
def profile():
    form = ProfileForm()

    if form.validate_on_submit():
        current_user.email = form.email.data
        current_user.idade = form.idade.data 
        current_user.sobremim = form.sobremim.data
        current_user.registro = form.registro.data
        current_user.gametag = form.gametag.data
        current_user.ifcomunity = form.ifcomunity.data
        current_user.sobrenome =  form.sobrenome.data
        current_user.username = form.username.data
        current_user.base = form.base.data
        current_user.pais = form.pais.data

        db.session.add(current_user)
        db.session.commit()
        
        flash("dados alterados com sucesso", "success")
        return redirect(url_for(".profile"))

    form.email.data = current_user.email
    form.idade.data = current_user.idade
    form.sobremim.data = current_user.sobremim
    form.registro.data = current_user.registro
    form.gametag.data = current_user.gametag
    form.ifcomunity.data = current_user.ifcomunity
    form.sobrenome.data = current_user.sobrenome
    form.username.data = current_user.username
    form.base.data = current_user.base
    form.pais.data = current_user.pais

    return render_template("user/profile/edit.html", form=form)

@app.route("/user/profile/change-password", methods=["GET", "POST"])
@login_required
def change_password():
    form = ChangePasswordForm()

    if form.validate_on_submit():
        if not check_password_hash(current_user.password, form.old_password.data):
            flash("a senha antiga está incorreta.", "danger")
            return redirect(url_for(".change_password"))
               
        if form.new_password.data != form.confirm_password.data:            
            flash("a nova senha deve ser igual a confirmação de senha", "danger")
            return redirect(url_for(".change_password"))

        current_user.password = generate_password_hash(form.new_password.data)
        db.session.add(current_user)
        db.session.commit()

        flash("dados alterados com com sucesso", "success")
        return redirect(url_for(".change_password"))
    
    return render_template("user/profile/change_password.html", form=form)



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
        current_user.cont_tempo = get_all_time2(Logbook.query.filter_by(user_id=id).all())
        current_user.cont_tempo_str = get_all_time(Logbook.query.filter_by(user_id=id).all())
        current_user.cont_voo = len(Logbook.query.filter_by(user_id=id).all())          
        db.session.add(book)
        db.session.add(current_user)
        db.session.commit()
        flash('LogBook Registrado com Sucesso!!', 'success')
        return redirect(url_for('logbook', id=current_user.id))
    

    return render_template('logbook.html', form=form, book=book)

@app.route('/top10')
def top10():
    users_top_10 = User.query.order_by(User.cont_tempo.desc()).all()
    users_top_voo = User.query.order_by(User.cont_voo.desc()).all()
    users = User.query.order_by(User.pontos.desc()).all()
    return render_template('top10.html',    top_10=users_top_10, users=users, users_top_voo=users_top_voo)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/carreira')
def carreira():
    return render_template('carreira.html')

@app.route('/pontos')
def pontos():
    return render_template('pontos.html')

@app.route('/tracker')
def tracker():
    return render_template('tracker.html')


@app.route('/evento1')
def evento1():    
    form = Evento_1.query.order_by(Evento_1.last_seen.desc()).all()
    return render_template('evento1.html', form=form)

@app.route('/evento2')
def evento2():    
    form = Evento_2.query.order_by(Evento_2.last_seen.desc()).all()
    return render_template('evento2.html', form=form )

@app.route('/evento3')
def evento3():    
    form = Evento_3.query.order_by(Evento_3.last_seen.desc()).all()
    return render_template('evento3.html', form=form)



