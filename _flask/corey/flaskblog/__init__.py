from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = '123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

mail_settings = {
 "MAIL_SERVER": 'smtp.gmail.com',
 "MAIL_PORT": 465,
 "MAIL_USE_TLS": False,
 "MAIL_USE_SSL": True,
 "MAIL_USERNAME": 'jurgeon018@gmail.com',
 "MAIL_PASSWORD": 'yfpfhrj69018'}
app.config.update(mail_settings)

db = SQLAlchemy(app)
bcrypt = Bcrypt()
mail = Mail(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

# нужно импортировать в самом низу чтобы небыло циклического импорьирования
from flaskblog.users.routes import users
from flaskblog.main.routes import main
from flaskblog.posts.routes import posts
from flaskblog.errors.handlers import errors
app.register_blueprint(users)
app.register_blueprint(main)
app.register_blueprint(posts)
app.register_blueprint(errors)
