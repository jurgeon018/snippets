from flask import Flask, request, render_template, session, redirect, url_for
from markupsafe import escape


app = Flask(__name__)
app.secret_key = 'f'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)


@app.route('/', methods=['GET','POST'])
def hello_world():
    app.logger.debug('A value for debugging')
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')
    return 'Hello, World!'


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about1():
    return 'The about page1'


@app.route('/about/')
def about2():
    return 'The about page2'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)




