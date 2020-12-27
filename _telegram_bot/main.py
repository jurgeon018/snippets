from flask import Flask, request, jsonify
import requests
import json
import re
from flask_sslify import SSLify

URL = 'https://api.telegram.org/bot731296971:AAEmJjfLxvhjyAFy-RScvk9kOtf8MKlD_7c/'


def write_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def get_price(text):
    crypto = re.search(r'/\w+', text).group()[1:]
    url = f'https://api.coinmarketcap.com/v1/ticker/{crypto}'
    r = requests.get(url).json()
    write_json(r, 'get_price.json')
    price = r[-1]['price_usd']
    return str(price) + 'usd'


def send_message(chat_id, text):
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(URL + 'sendMessage', json=answer)
    return r.json()


app = Flask(__name__)
sslify = SSLify(app)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return '<h1>Bot Welcomes You</h1>'
    if request.method == 'POST':
        r = request.get_json()
        message = r['message']['text']
        if re.search(r'/\w+', message):
            chat_id = r['message']['chat']['id']
            price = get_price(message)
            send_message(chat_id, text=price)
        return jsonify(r)


if __name__ == '__main__':
    requests.get(URL + f"setWebhook?url=https://aa3a3f48.ngrok.io")
    app.run(port=5000)
