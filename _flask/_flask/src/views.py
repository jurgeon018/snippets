from flask import render_template, request
from app import app
from flask_security import login_required

import json
# @login_required

def get_json_data(request):
    data = request.data.decode('utf-8')
    if data:
        data = json.loads(data)
    json_data = {}
    return json_data

@app.route('/', methods=['POST', 'GET'])
def index():
    # json_data = get_json_data(request)
    # print(json_data)
    print("request.form: ", request.form)
    print("request.args: ", request.args)
    return render_template('index.html')

@app.route('/error_page')
def error_page():
    return fdsasdf

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def error_500(e):
    return render_template('500.html'), 500
