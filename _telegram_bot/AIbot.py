from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import apiai
import json
updater = Updater(token='731296971:AAEmJjfLxvhjyAFy-RScvk9kOtf8MKlD_7c')  # Токен API к Telegram
dispatcher = updater.dispatcher
# Обработка команд


def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Привет, давай пообщаемся?')


def textMessage(bot, update):
    # Токен API к Dialogflow
    request = apiai.ApiAI('96799fc86f6d4bd18b4d37323d10776e').text_request()
    request.lang = 'ru'  # На каком языке будет послан запрос
    request.session_id = 'mendela_andrew_bot'  # ID Сессии диалога (нужно, чтобы потом учить бота)
    request.query = update.message.text  # Посылаем запрос к ИИ с сообщением от юзера
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']  # Разбираем JSON и вытаскиваем ответ
    # Если есть ответ от бота - присылаем юзеру, если нет - бот его не понял
    if response:
        bot.send_message(chat_id=update.message.chat_id, text=response)
    else:
        bot.send_message(chat_id=update.message.chat_id, text='Я Вас не совсем понял!')


# Хендлеры
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
# Добавляем хендлеры в диспетчер
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
# Начинаем поиск обновлений
updater.start_polling(clean=True)
# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()
