from flask import Flask
from flask.json import jsonify

app = Flask(__name__)

# 1. По адресу /locales должен возвращаться массив в формате json с тремя локалями: ['ru', 'en', 'it']
@app.route('/locale')
def dict():
    return jsonify({'ru': 'russian', 'en': 'english', 'it': 'italian'})

# 2. По адресу /sum/<int:first>/<int:second> должен получать в url-адресе два числа, возвращать их сумму
@app.route('/sum/<first>/<second>', methods=['POST','GET'])
def sum(first, second):
    return str(int(first)+int(second))
# 3. По адресу /greet/<user_name> должен получать имя пользователя, возвращать текст 'Hello, имя_которое_прислали'
@app.route('/greet/<user_name>')
def greet(user_name):
    return 'Hello '+user_name
# 4. По адресу /form/user должен принимать POST запрос с параментрами: email, пароль и подтверждение пароля. Необходимо валидировать email, что обязательно присутствует, валидировать пароли, что они минимум 6 символов в длину и совпадают. Возрващать пользователю json вида:
#  "status" - 0 или 1 (если ошибка валидации),
#  "errors" - список ошибок, если они есть,
#  или пустой список.
from flask import Flask, request
from flask.json import jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError

app.config.update({
    'SECRET_KEY': 'asdasdasd',
    'DEBUG': True,
    'WTF_CSRF_ENABLED': False
})


def confirm_password(form, field):
    if form.data['password'] != form.data['confirm_password']:
        raise ValidationError('Пароли не совпадают"')

class UserForm(FlaskForm):
    email = StringField(label='E-mail', validators=[
        validators.Length(min=5, max=35), validators.Email()
    ])
    password = StringField(label='password:', validators =[
        validators.Length(min=6, max=12)
    ])
    confirm_password = StringField(label='confirm password:', validators=[
        validators.Length(min=6, max=20), confirm_password
    ])

@app.route('/form/user', methods =['GET', 'POST'])
def post_data():
    if request.method == 'POST':
        user_form = UserForm(request.form)
        status_output = {0:'Проверка пройдена', 1: 'Ошибка валидации'}
        if user_form.validate():
            # print('email:', request.form['email'])
            # print('pass:', request.form['password'])
            status_check = jsonify(status_output[0])
            return status_check
        else:
            status_check = jsonify(status_output[1])
            error_list = jsonify(user_form.errors)
            # print(user_form.errors)
            return status_check and error_list
    return 'Done!'
# 5. По адресу /serve/<path:filename> должен возвращать содержимое запрашиваемого файла из папки ./files. Файлы можно туда положить любые текстовые. А если такого нет - 404.
@app.route('/serve/<path:filename>', methods=['POST','GET'])
def serve(filename):
    import os
    path = '/home/jurgeon/Desktop/dev/homeworks/tceh/files/'+filename
    if not os.path.exists(path):
        return '404: file does not exists'
    else:
        with open(path, 'r') as f:
            return f.read()

if __name__ == '__main__':
    app.run(port=5000, debug=True)
