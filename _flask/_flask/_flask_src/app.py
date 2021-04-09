from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_login import LoginManager
from flask_admin import Admin

from flask_security import SQLAlchemyUserDatastore, Security

from config import Configuration


app = Flask(__name__)
app.config.from_object(Configuration)
app.secret_key = 'f'

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from models import User, Role, Template
from admin import TemplateModelView, UserModelView, HomeAdminView

admin = Admin(app, 'FlaskApp', url='/', index_view=HomeAdminView(name='home'))
admin.add_view(UserModelView(User, db.session))
admin.add_view(TemplateModelView(Template, db.session))

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

from app import user_datastore
user_datastore.create_role(name='admin', description='admin role')
user_datastore.create_user(email='an@sdf.sdf', password='password')

# Root views without blueprint
import views
import commands

app.cli.add_command(commands.user_cli)
app.cli.add_command(commands.gen_templates)
