from flask_security import UserMixin, RoleMixin

from datetime import datetime
import re

from app import db


def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', str(s))

post_tags = db.Table(
    'post_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
)

roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)


class SaveMixin:

    def save(self, *args, **kwargs):
        db.session.add(self)
        db.session.commit()


class User(db.Model, SaveMixin, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', 
                            secondary=roles_users, 
                            backref=db.backref('users', lazy='dynamic'))


class Role(db.Model, SaveMixin, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(255))


class Post(db.Model, SaveMixin): 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text())
    created = db.Column(db.DateTime, default=datetime.now)
    tags = db.relationship('Tag',
                            secondary=post_tags,
                            backref=db.backref('posts'),
                            lazy='dynamic')

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '<Post id: {}, title: {}'.format(self.id, self.title)


class Tag(db.Model, SaveMixin): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    slug = db.Column(db.String(100))

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return '<Tag id: {}, name: {}>'.format(self.id, self.name)
