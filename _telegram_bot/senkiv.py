from flask import Flask
from flask import request
#from flask import jsonify
import time
import re
import requests
import json
import telegram

# TOKEN = '791986674:AAECftWKFlQ3baeDQ5xL_WDY-uq4v0x_fWY'
TOKEN = '731296971:AAEmJjfLxvhjyAFy-RScvk9kOtf8MKlD_7c'

bot = telegram.Bot(token=TOKEN)

URL = 'https://api.telegram.org/bot' + TOKEN

list_in = str
glob_value = str
num = str
valin = str
valfrom = str
mes_list = []

#from flask_sslify import SSLify

app = Flask(__name__)


#sslify = SSLify(app)

# Запис отриманого повідомленя в json :
def write_json(data, filename='answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# Надсилання повідомлення користувачу в телеграм:
def send_message(chat_id, text='bla bla'):
    url = URL + 'sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=answer)
    return r.json()


def today_date():
    d = time.strftime("%Y%m%d")
    return d


# Парсимо введений текст
def parse_text(text):
    try:
        pattern = r'\d+'
        parse = re.findall(pattern, text)
        global num
        num = parse[0]
    except:
        pattern2 = r'\D\w+'
        parse2 = re.findall(pattern2, text)
        global valin
        try:
            valin = [parse2[0], parse2[1]]
        except:
            valin = [parse2[0]]


# Отримуємо число, яке треба конвертувати
def return_num():
    global num
    return (float(num))


# Отримуємо валюту в яку або з якої треба конвертувати
def return_val():
    global valin
    try:
        a = valin[0] + valin[1]
    except:
        a = valin[0]
    return (str(a))


# Отримуємо курс валюти на сьогоднішній день
def get_price(val):
    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={}'.format(val) + '&date=' + today_date() + '&json'
    r = requests.get(url).json()
    rate = r[0]['rate']
    return float(rate)


# Отримуємо курс вибраної валюти на задану дату
def get_archive_val(val,date):
    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={}'.format(val) + '&date={}'.format(date) + '&json'
    r = requests.get(url).json()
    rate = r[0]['rate']
    return str(round(rate, 3))


# Обмінник:
def fromua():
    c = (get_dict_val()).get(return_val())
    a = return_num() / float(get_price(c))
    b = (str(round(a, 2)) + ' ' + return_val())
    return str(b)


# Отримуємо словник із назвами усіх валют через апі НБУ:
def get_dict_val():
    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date=' + today_date() + '&json'
    r = requests.get(url).json()

    def value(n):
        try:
            d = {r[n]['txt']: r[n]['cc']}
            return (d)
        except:
            return {}
    i = 0
    d = {}
    while i < 100:
        a = value(i)
        i += 1
        d.update(a)
    else:
        return d


# Виводимо клавіатуру і обробляємо введені дані:
def keyboard(message, chat_id):
    val = get_dict_val()
    parse_text(message)

    # /start
    def start(chat_id):
        button = [['Обмінник', 'Курс']]
        reply_markup = telegram.ReplyKeyboardMarkup(button, resize_keyboard=0, one_time_keyboard=False)
        bot.send_message(chat_id=chat_id, text="Виберіть дію: 💸 ", reply_markup=reply_markup)

    # Кнопка обмін
    def obmin(chat_id):
        button = [['Валюту', 'Гривню'], ['Назад']]
        reply_markup = telegram.ReplyKeyboardMarkup(button, resize_keyboard=0, one_time_keyboard=False)
        bot.send_message(chat_id=chat_id, text="Виберіть що обміняти: 🔄 ", reply_markup=reply_markup)

    # Кнопка обмін гривні
    def obmin_uah(chat_id):
        button = [['Долар США', 'Євро', 'Фунт стерлінгів', 'Злотий'], ['Повторити', 'Назад']]
        reply_markup = telegram.ReplyKeyboardMarkup(button, resize_keyboard=0, one_time_keyboard=False)
        bot.send_message(chat_id=chat_id, text="Виберіть в яку валюту: 🔰", reply_markup=reply_markup)

    #Кнопка обмін валюти
    def obmin_val1(chat_id):
        button = [['Долар США', 'Євро', 'Фунт стерлінгів', 'Злотий'], ['Назад']]
        reply_markup = telegram.ReplyKeyboardMarkup(button, resize_keyboard=0, one_time_keyboard=False)
        bot.send_message(chat_id=chat_id, text="Виберіть яку валюту: 🌐", reply_markup=reply_markup)

    #Кнопка 2 обмін валюти
    def obmin_val2(chat_id):
        button = [['Гривня'],['Долар США', 'Євро', 'Фунт стерлінгів', 'Злотий'], ['Повтор', 'Назад']]
        reply_markup = telegram.ReplyKeyboardMarkup(button, resize_keyboard=0, one_time_keyboard=False)
        bot.send_message(chat_id=chat_id, text="Виберіть в яку валюту: ⏬ ", reply_markup=reply_markup)

    # Кнопка курс
    def kurs(chat_id):
        button = [['Долар США', 'Євро', 'Фунт стерлінгів', 'Злотий'], ['Уся валюта','Архів',], [ 'Назад']]
        reply_markup = telegram.ReplyKeyboardMarkup(button, resize_keyboard=0, one_time_keyboard=False)
        bot.send_message(chat_id=chat_id, text="Виберіть валюту: 💵 ", reply_markup=reply_markup)

    # Відправляємо курс вибраної валюти
    def valuta(message, chat_id):
        a = val.get(message)
        b = (str(round((float(get_price(a))), 3)) + ' uah 🇺🇦')
        send_message(chat_id, text=b)

    # Відправляємо список усіх валют
    def all_valuta(chat_id):
        a = val.keys()
        b = "\n".join(map("".join, a))
        send_message(chat_id, text='Введіть потрібну валюту з клавіатури: \n\n' + (b))

    # Архів валют
    def ar_val(chat_id):
        button = [['Долар США', 'Євро', 'Фунт стерлінгів', 'Злотий'], [ 'Назад']]
        reply_markup = telegram.ReplyKeyboardMarkup(button, resize_keyboard=0, one_time_keyboard=False)
        bot.send_message(chat_id=chat_id, text="Виберіть валюту: 💵 ", reply_markup=reply_markup)

    # Перевіряємо отримане повідомлення і виконуємо відповідні дії
    if message.lower() == '/start' or message.lower() == 'start':
        start(chat_id)
        mes_list.clear()

    elif message.lower() == '/help' or message.lower() == 'help':
        send_message(chat_id,text='Бот для конвертації та перегляду курсу валют💰\n\nВ меню "Обмін" можна отримати курс гривні до іншої валюти і навпаки\n\nВ меню "Курс" можна отримати курс валют на сьогоднішню дату, а також переглянути курс на вибрану дату(підменю "Архів")\n\nДля початку роботи натисніть /start')

    elif message.lower() == 'назад':
        start(chat_id)
        mes_list.clear()

    #Обробляємо курс валют
    elif message.lower() == 'курс':
        kurs(chat_id)

    elif message.lower() == 'архів' or message == 'Ще раз' :
        ar_val(chat_id)

    elif mes_list[0] == 'Архів' or mes_list[0] == 'Ще раз':
        if message in val:
            parse_text(message)
            reply_markup = telegram.ReplyKeyboardRemove()
            bot.send_message(chat_id=chat_id, text='Введіть дату в форматі: "день місяць рік" (Наприклад: 29 03 2012): ⬇️', reply_markup=reply_markup)

    elif mes_list[0] == 'Курс':
        if message in val:
            valuta(message, chat_id)

    elif message.lower() == 'уся валюта':
        all_valuta(chat_id)

    elif mes_list[0] == 'Уся валюта':
        if message in val:
            parse_text(message)
            valuta(message, chat_id)

    #Обробляємо обмінник
    elif message.lower() == 'обмінник':
        obmin(chat_id)
        mes_list.clear()

    elif message.lower() == 'валюту' or message == 'Повтор':
        obmin_val1(chat_id)
        parse_text(message)

    #Гривню
    elif message.lower() == 'гривню' or message == 'Повторити':
        reply_markup = telegram.ReplyKeyboardRemove()
        bot.send_message(chat_id=chat_id, text='Введіть значення: ⬇️', reply_markup=reply_markup)

    elif mes_list[0] == 'Гривню' or mes_list[0] == 'Повторити':
        obmin_uah(chat_id)
        parse_text(message)

    elif mes_list[1] == 'Гривню' or mes_list[1] == 'Повторити':
        parse_text(message)
        a = fromua()
        b = str(return_num()) + ' Грн 🇺🇦' + ' = ' + str(a) + ' ✅️'
        send_message(chat_id, b)
        mes_list.clear()

    #Валюту
    elif mes_list[0] == 'Валюту' or mes_list[0] == 'Повтор':
        c = (get_dict_val()).get(return_val())
        global valfrom
        valfrom = get_price(c)
        reply_markup = telegram.ReplyKeyboardRemove()
        bot.send_message(chat_id=chat_id, text='Введіть значення: ⬇️', reply_markup=reply_markup)

    elif mes_list[1] == 'Валюту' or mes_list[1] == 'Повтор':
        obmin_val2(chat_id)

    elif mes_list[2] == 'Валюту' or mes_list[2] == 'Повтор':
        if message == 'Гривня':
            a = round((float(return_num())*float(valfrom)), 3)
            b =  str(return_num()) + ' ' + str(mes_list[1]) + ' 💎 ' + ' = ' + str(a) + ' грн 🇺🇦'
            send_message(chat_id, text=b)
        else:
            a = (get_dict_val()).get(return_val())
            b = round((float(return_num())*float(valfrom)/float(get_price(a))), 3)
            c = str(mes_list[0]) + ' ' + str(mes_list[1])+' 🔽 ' + ' = ' + str(b) + ' ' + message + ' 🔼'
            send_message(chat_id, text=c)

    #Обробляємо архів
    elif mes_list[1] == 'Архів' or mes_list[1] == 'Ще раз':
        pattern = r'\d+'
        parse = re.findall(pattern, message)
        a = parse[2] + parse[1] + parse[0]
        b = val.get(return_val())
        c = get_archive_val(b,str(int(a)))
        d = mes_list[0] + ' на задану дату коштував: ' + c + ' грн 🗒'
        button = [['Ще раз'], ['Назад']]
        reply_markup = telegram.ReplyKeyboardMarkup(button, resize_keyboard=0, one_time_keyboard=False)
        bot.send_message(chat_id=chat_id, text=d ,reply_markup=reply_markup)
        mes_list.clear()

    elif mes_list[0] in val:
        valuta(message, chat_id)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        chat_id = r['message']['chat']['id']
        # write_json(r)
        try:
            message = r['message']['text']
            keyboard(message, chat_id)
            global mes_list
            mes_list.insert(0, message)
        except:
            button = [['Обмінник', 'Курс']]
            reply_markup = telegram.ReplyKeyboardMarkup(button, resize_keyboard=0, one_time_keyboard=False)
            bot.send_message(chat_id=chat_id, text="Wrong data ! 🚫 ", reply_markup=reply_markup)

    return '<h1> It works!  You`re welcome! </h1>'


if __name__ == '__main__':
    app.run()
