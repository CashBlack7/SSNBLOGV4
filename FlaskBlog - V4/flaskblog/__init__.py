import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__) #to look for static files etc
app.config['SECRET_KEY'] = '7748664f010afab4160bad2d7b7bfcd4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

# /// -> same path
db = SQLAlchemy(app)

migrate = Migrate(app,db)

bcrypt = Bcrypt(app) 
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'testerflask25@gmail.com'
app.config['MAIL_PASSWORD'] = 'qweasdzxc#11'
mail = Mail(app)

from flaskblog import routes