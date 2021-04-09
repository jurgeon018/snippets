from flask import Blueprint, render_template


users = Blueprint(
    'users',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/static',
)


@users.route('/')
def index():
    context = {}
    return render_template('users/index.html', **context)

@users.route('/contacts')
def contacts():
    context = {}
    return render_template('users/contacts.html', **context)

