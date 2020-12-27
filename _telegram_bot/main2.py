from flask import Flask, request, jsonify
from flask_sslify import SSLify
import re
import json
import requests

URL = 'https://api.telegram.org/bot731296971:AAEmJjfLxvhjyAFy-RScvk9kOtf8MKlD_7c/'

app = Flask(__name__)
sslify = SSLify(app)


def write_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def get_price(text):
    crypto = re.search(r'/\w+', text).group()[1:]
    url = f'https://api.coinmarketcap.com/v1/ticker/{crypto}'
    r = requests.get(url).json()
    price = r[-1]['price_usd']
    return price


def send_message(chat_id, text):
    r = requests.post(URL+'sendMessage', json={'chat_id': chat_id, 'text': text})
    return r


@app.route('/', methods={'POST', 'GET'})
def index():
    if request.method == 'POST':
        r = request.get_json()
        message = r['message']['text']
        if re.search(r'/\w+', message):
            chat_id = r['message']['chat']['id']
            send_message(chat_id, get_price(message))
            return jsonify(r)
        else:
            return jsonify(r)
    if request.method == 'GET':
        return '<h1>Hello</h1>'


if __name__ == '__main__':
    requests.get(URL + f"setWebhook?url=https://a40227a3.ngrok.io")
    app.run(port=5000)
