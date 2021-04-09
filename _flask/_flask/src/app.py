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

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from models import Post, Tag, User, Role
from admin import PostModelView, TagModelView, UserModelView, HomeAdminView

admin = Admin(app, 'FlaskApp', url='/', index_view=HomeAdminView(name='home'))
admin.add_view(PostModelView(Post, db.session))
admin.add_view(UserModelView(User, db.session))
admin.add_view(TagModelView(Tag, db.session))

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# from app import user_datastore
# user_datastore.create_role(name='admin', description='admin role')
# user_datastore.create_user(email='an@sdf.sdf', password='password')

from posts.blueprint import posts
from users.views import users

app.register_blueprint(posts, url_prefix='/posts')
app.register_blueprint(users, url_prefix='/users')

# Root views without blueprint
import views
