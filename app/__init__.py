from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_babel import Babel
from flask_mail import Mail
from flask_uploads import configure_uploads, IMAGES, UploadSet

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from werkzeug.security import generate_password_hash
from app import filters


app = Flask(__name__)
app.config.from_object(Config)
filters.init_app(app)
Babel(app, "pt_BR")
mail = Mail(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
bootstrap = Bootstrap(app)
admin = Admin(app, name='My admin name', template_mode='bootstrap3')
app.config['UPLOADED_IMAGES_DEST'] = 'uploads/imagem'
app.config['FLASK_ADMIN_SWATCH'] = 'lumen'
images = UploadSet('images', IMAGES)
configure_uploads(app, images)

from app import routes, models

from app.models import User, Logbook, Evento_1, Evento_2, Evento_3

class UserView(ModelView): 

    create_modal = True
    edit_modal = True
    column_editable_list = ['username', 'sobrenome', 'registro']
    column_searchable_list = ['username', 'registro', 'telefone']
    column_exclude_list = ['password', 'ifcomunity', 'sobremim', 'pais', 'base', 'telefone', 'grau', 'pontos', 'email', 'cont_tempo', 'cont_tempo_str', 'cont_voo']
    column_filters = ['username', 'registro']

    def on_model_change(self, form, model, is_created):

        model.password = generate_password_hash(form.password.data)

class LogbookView(ModelView):

    create_modal = True
    edit_modal = True
    column_searchable_list = ['voo']


admin.add_view(UserView(User, db.session))
admin.add_view(LogbookView(Logbook, db.session))
admin.add_view(LogbookView(Evento_1, db.session))
admin.add_view(LogbookView(Evento_2, db.session))
admin.add_view(LogbookView(Evento_3, db.session))

