from flask_security import UserMixin, RoleMixin

from datetime import datetime

from app import db


roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)


class BaseMixin:

    # @classmethod
    # def get_or_create(model, **kwargs):
    #     instance = model.query.filter(**kwargs)
    #     if instance:
    #         instance = instance.first()
    #     else:
    #         instance = model(**kwargs)
    #     return instance

    def save(self, *args, **kwargs):
        db.session.add(self)
        db.session.commit()


class Template(db.Model, BaseMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)


class User(db.Model, BaseMixin, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', 
                            secondary=roles_users, 
                            backref=db.backref('users', lazy='dynamic'))


class Role(db.Model, BaseMixin, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(255))
