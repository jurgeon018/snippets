from app.auth import auth
from flask import redirect, render_template, url_for, flash, request
from flask_login import current_user, login_user, logout_user, login_required
from app.auth.forms import *
from app import db
from werkzeug.urls import url_parse
from app.auth.email import send_password_reset_email

@auth.route('/register', methods=['POST','GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.generate_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You have been registered!')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

@auth.route('/login', methods=['POST','GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            next = request.args.get('next')
            login_user(user, remember=form.remember_me.data)
            if not next or url_parse(next).netloc != '':
                flash('You have been logged in')
                return redirect(url_for('main.index'))
            else:
                flash('You have been logged in')
                return redirect(url_for(next))
        else:
            flash('Email or password is invalid')
            return redirect(url_for('auth.login'))
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('auth.login'))


@auth.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_password_request.html',
                           title='Reset Password', form=form)


@auth.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('main,index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.generate_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_password.html', form=form)
