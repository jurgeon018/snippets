from flask import request, render_template, session, redirect, url_for

from . import cert

from markupsafe import escape


@cert.route('/', methods=['GET','POST'])
def index():
    context = {}
    context['name'] = 'Ivan'
    # app.logger.debug('A value for debugging')
    # app.logger.warning('A warning occurred (%d apples)', 42)
    # app.logger.error('An error occurred')
    return render_template('index.html', **context)

@cert.route('contacts/')
def contacts():
    context = {}
    return render_template('contacts.html', **context)


@cert.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % escape(username)


@cert.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id


@cert.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath %s' % escape(subpath)


@cert.route('/projects/')
def projects():
    return 'The project page'


@cert.route('/about')
def about():
    return 'The about page'
