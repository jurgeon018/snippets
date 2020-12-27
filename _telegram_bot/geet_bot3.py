import telebot
from telebot.types import Message
import random
import json

# telebot.apihelper.proxy = {'https':'3.17.167.222:8080'}

TOKEN = '731296971:AAEmJjfLxvhjyAFy-RScvk9kOtf8MKlD_7c'
bot = telebot.TeleBot(TOKEN)


smiles = ['😞', '😂', '😜', '😘', '❤️', '😍', '😊', '😁', '😔', '😄', '😭', '💋']


# bot.send_message('393782627', 'Привет. Это сообщение,которое бот будет отправлять при запуске скрипта')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Hello!')


@bot.message_handler(content_types=['text','sticker'],func=lambda message: True)
def upper(message):
    if message.from_user.id == '393782627':
    # if message.chat.id == '393782627':
        bot.reply_to(message, 'Ты мой создатель')
    else:
        bot.reply_to(message, 'Ты не мой создатель')
    if message.content_type == 'text':
        bot.reply_to(message, message.text.upper())
        bot.reply_to(message, random.choice(smiles))
    elif message.content_type == 'sticker':
        bot.send_sticker(message.chat.id, 'CAADAgADoAQAAoJRKAMBSYNMZEbQdgI')


bot.polling()
