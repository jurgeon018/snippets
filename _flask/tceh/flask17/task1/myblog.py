#!/usr/bin/python
from flask import Flask, request, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

import config as config


__author__ = 'BorisRubin'


myblog = Flask(__name__, template_folder='templates')
myblog.config.from_object(config)


db = SQLAlchemy(myblog)


@myblog.route('/', methods=['GET'])
def index():
    '''
    Основная страница блога для ввода имени и сообщения
    '''
    all_messages = Message.query.all()

    return render_template('index.html', messages=all_messages)


@myblog.route('/comment', methods=['POST'])
def comment():
    '''
    Cтраница валидации и сохранения сообщения
    '''
    form = MessageForm(request.form)

    if form.validate():
        message = Message(**form.data)

        db.session.add(message)
        db.session.commit()

        flash('New message added from {}'.format(request.form['name']), 'Success')
    else:
        flash(str(form.errors), 'Errors')

    return redirect(url_for('index'))


if __name__ == '__main__':

    from models import *
    from forms import *

    db.create_all()

    myblog.run(debug=True, port=5010)
