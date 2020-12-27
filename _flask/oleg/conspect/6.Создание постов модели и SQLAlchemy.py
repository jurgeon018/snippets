# 2.Подготовка к работе

#console
sudo apt-get install mysql-server
sudo mysql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '1';
# пароль 1
mysql -u root -p
show databases;
create database test2 character set utf8 collate utf8_unicode_ci;

virtualenv venv
source venv/bin/activate
pip3 install flask

# 6.Создание постов модели и SQLAlchemy

# console
pip3 install flask-sqlalchemy
pip3 install mysql-connector == 2.1.4

# config.py
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:1@localhost/test2'

# console
from models import *
from app import db
db.create_all()
p = Post(title='First post', body='first post body')
db.session.add(p)
db.session.commit()
p2 = Post(title='second post', body='second post body')
db.session.add(p2)
db.session.commit()
p3 = Post(title='third post! 3-test', body='third post body')
db.session.add(p3)
db.session.commit()
posts = Post.query.all()
p4 = Post.query.filter(Post.title.contains('second')).all()
p5 = Post.query.filter(Post.title == '!').all()
p5 = Post.query.filter(Post.title='Third post! 3-test').all()
p5 = Post.query.filter(Post.title='Third post! 3-test').first()

# 7.Миграции, теги, связь тегов и постов
python3 manage.py db init
python3 manage.py db migrate
python3 manage.py db upgrade
