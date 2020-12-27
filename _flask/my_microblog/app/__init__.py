from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_mail import Mail
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_security import SQLAlchemyUserDatastore, Security
from app.config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)
moment = Moment(app)
mail = Mail(app)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

from app.models import *
admin = Admin(app)
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(User, db.session))
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
# security = Security(app, user_datastore)

from app.auth import auth
app.register_blueprint(auth)
from app.main import main
app.register_blueprint(main)
from app.errors import errors
app.register_blueprint(errors)
from app.models import *
