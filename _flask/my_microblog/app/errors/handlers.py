from app.errors import errors
from flask import render_template

@errors.app_errorhandler(400)
def error400(error):
    return render_template('errors/400.html')


@errors.app_errorhandler(404)
def error404(error):
    return render_template('errors/404.html')

@errors.app_errorhandler(500)
def error500(error):
    return render_template('errors/500.html')

@errors.app_errorhandler(403)
def error403(error):
    return render_template('errors/403.html')
