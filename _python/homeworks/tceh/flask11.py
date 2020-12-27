

from flask import Flask, request, render_template, flash
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
import random
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '1234'
app.config['WTF_CSRF_ENABLED'] = False

class Form(FlaskForm):
    number = IntegerField('Input Number')
    submit = SubmitField('Submit')
# +1. Пользователь по GET запросу на адрес / получает
# сообщение: "Число загадано"
@app.route('/', methods=['POST','GET'])
def guesser():
    number = random.randint(1, 10)
    form = Form()
    if request.method == 'GET':
        return f"""
        <form method='POST'>
            <h1>Число Загадано</h1>
            <p>{form.number.label}</p>
            <p>{form.number}</p>
            <p>{form.submit}</p>
        </form>
        """
    if form.validate_on_submit():
        if form.number.data == number:
            return f"""
            <form method='POST'>
                <h1> Поздравляю! Число {number}</h1>
                <p>{form.number.label}</p>
                <p>{form.number}</p>
                <p>{form.submit}</p>
            </form>
            """
        elif form.number.data > number:
            return f"""
            <form method='POST'>
                <h1> > </h1>
                <p>{form.number.label}</p>
                <p>{form.number}</p>
                <p>{form.submit}</p>
            </form>
            """
        elif form.number.data < number:
            return f"""
            <form method='POST'>
                <h1> < </h1>
                <p>{form.number.label}</p>
                <p>{form.number}</p>
                <p>{form.submit}</p>
            </form>
            """
# +2. Пользователь по POST запросе на адрес /guess
# получает один из следующих результатов: ">", "<", "="

# +3. Если число угадано - загадываем новое число

# +4. Flask при старте сервера - устанавливает seed для
# random, генерирует случайное число для угадывания

# +5. Администратор задает seed для модуля рандом через
# переменную окружения FLASK_RANDOM_SEED

if __name__ == '__main__':
    app.run()
