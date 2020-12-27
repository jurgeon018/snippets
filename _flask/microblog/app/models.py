from datetime import datetime
from hashlib import md5
from time import time
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from app import app, db, login


followers = db.Table(
    'followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    followed = db.relationship(
        # 'User' — это правая сторона связи (левая сторона — это родительский класс). Поскольку это самореферентное отношение, я должен использовать тот же класс с обеих сторон.
        'User',
        # secondary кофигурирует таблицу ассоциаций, которая используется для этой связи, которую я определил прямо над этим классом.
        secondary=followers,
        # primaryjoin указывает условие, которое связывает объект левой стороны (follower user) с таблицей ассоциаций. Условием объединения для левой стороны связи является идентификатор пользователя, соответствующий полю follower_id таблицы ассоциаций. Выражение followers.c.follower_id ссылается на столбец follower_id таблицы ассоциаций
        primaryjoin=(followers.c.follower_id == id),
        # secondaryjoin определяет условие, которое связывает объект правой стороны (followed user) с таблицей ассоциаций. Это условие похоже на primaryjoin, с той лишь разницей, что теперь я использую followed_id, который является другим внешним ключом в таблице ассоциаций.
        secondaryjoin=(followers.c.followed_id == id),
        #     backref определяет, как эта связь будет доступна из правой части объекта. С левой стороны отношения пользователи называются followed, поэтому с правой стороны я буду использовать имя followers, чтобы представить всех пользователей левой стороны, которые связаны с целевым пользователем в правой части. Дополнительный lazy аргумент указывает режим выполнения этого запроса. Режим dynamic настройки запроса не позволяет запускаться до тех пор, пока не будет выполнен конкретный запрос, что также связано с тем, как установлено отношения «один ко многим».
        # -lazy похож на параметр с тем же именем в backref, но этот относится к левой, а не к правой стороне.
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        return self.followed.filter(
            followers.c.followed_id == user.id).count() > 0

    def followed_posts(self):
        followed = Post.query.join(
            followers, (followers.c.followed_id == Post.user_id)).filter(
                followers.c.follower_id == self.id)
        own = Post.query.filter_by(user_id=self.id)
        return followed.union(own).order_by(Post.timestamp.desc())

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
