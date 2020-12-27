# -*- coding: utf-8 -*-

from myblog import db


class Message(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    text = db.Column(db.String(3000), nullable=False)

    def __str__(self):
        return '<Message from {}: "{}">'.format(self.name, self.text)
