import requests, json, time


URL = 'https://api.telegram.org/bot731296971:AAEmJjfLxvhjyAFy-RScvk9kOtf8MKlD_7c/'
global last_update_id
last_update_id = 0

def get_btc():
    url = 'https://yobit.net/api/2/btc_usd/ticker'
    response = requests.get(url).json()
    price = response['ticker']['last']
    return str(price) +' usd'

def get_message():
    data = requests.get(URL + 'getupdates'l).json()
    last_object = data['result'][-1]
    current_update_id = last_object['update_id']
    global last_update_id
    if last_update_id != current_update_id:
        last_update_id = current_update_id
        chat_id = last_object['message']['chat']['id']
        message_text = last_object['message']['text']
        message = {'chat_id':chat_id, 'text':message_text}
        return message
    return None

# def send_message(chat_id, text):
#     url = URL + f'sendmessage?chat_id={chat_id}&text={text}'
#     requests.get(url)
def send_message(chat_id, text):
    answer = {'chat_id':chat_id, 'text':text}
    requests.post(URL + 'sendMessage', json=answer)

def main():
    # d = requests.get(URL + 'getupdates'l).json()
    # with open('updates.json', 'w') as file:
    #      json.dump(d, file, indent=2, ensure_ascii=False)

    while True:
        answer = get_message()
        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']
            if text=='/btc':
                send_message(chat_id, get_btc())
        else:
            continue
        time.sleep(3)




if __name__ == '__main__':
    main()
