# https://www.youtube.com/watch?v=7FKASflZ8F4&t=509s

# content_types = [
#     'text', 'audio', 'document', 'photo', 'sticker',
#     'video', 'video_note', 'voice', 'location',
#     'contact', 'new_chat_members', 'left_chat_member',
#     'new_chat_title', 'new_chat_photo', 'delete_chat_photo',
#     'group_chat_created', 'supergroup_chat_created',
#     'channel_chat_created', 'migrate_to_chat_id',
#     'migrate_from_chat_id', 'pinned_message']

# message. content_type(), message_id(), from_user(), date, char,

# @bot.edited_message_handler()
# @bot.message_handler()
    # bot.reply_to()
    # bot.forward_message()
    # bot.get_me()
    # bot.get_updates()
    # bot.set_webhook()
    # bot.remove_webhook()
    # bot.send_:
        #  audio, chat_action(), contact(), document(), game(), invoice(), location(), media_group(), message(),  photo(), sticker(), venue(), video(), video_note(), voice()

# @bot.callback_query_handler()
    # bot.answer_callback_query() - всплывающее сообщение

# @bot.chosen_inline_handler
# @bot.inline_handler()
    # bot.answer_inline_query()


# types. :
# InlineKeyboardMarkup()
    # InlineKeyboardButton()
# ReplyKeyboardMarkup()
    # KeyboardButton()
# InlineQueryResultArticle
# InlineQueryResultPhoto
#     InputTextMessageContent
# ReplyKeyboardRemove - hides a previously sent ReplyKeyboardMarkup
# ForceReply - forces a user to reply to a message
from telebot import types
# from types import Message
import telebot
from geopy.distance import vincenty


TOKEN = '731296971:AAEmJjfLxvhjyAFy-RScvk9kOtf8MKlD_7c'
bot = telebot.TeleBot(TOKEN)
MAGAZINS = ({
                'title': 'Магазин на Комендантском',
                'lonm': 30.25,
                'latm': 60.00,
                'adress': 'г. СПб, Гаккелевская, д.34'
            },
            {
                'title': 'Магазин на Ветеранов',
                'lonm': 30.21,
                'latm': 59.85,
                'adress': 'г. СПб, Ветеранов, д.100'
            },
            {
                'title': 'Магазин на Невском',
                'lonm': 30.21,
                'latm': 59.93,
                'adress': 'г. СПб, Невский, д.98'
            }
)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Привет!!! Я бот интернет магазина!', reply_markup=markup_menu)

def gen_markup():
    markup = types.InlineKeyboardMarkup()
    markup.row_width=2
    markup.add(types.InlineKeyboardButton('Yes', callback_data='cb_yes'),
                types.InlineKeyboardButton('No', callback_data='cb_no'))
    return(markup)


markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                        row_width=2)
btn_adress = types.KeyboardButton('Адреса магазинов',
                            # request_contact=True,
                            request_location=True)
btn_payment = types.KeyboardButton('Способы оплаты')
btn_delivery = types.KeyboardButton('Способы доставки')
markup_menu.add(btn_adress, btn_delivery, btn_payment)


markup_inline_payment = types.InlineKeyboardMarkup()
btn_in_cash = types.InlineKeyboardButton('Наличные', callback_data='cash')
btn_in_card = types.InlineKeyboardButton('Карта', callback_data='card')
btn_in_invoice = types.InlineKeyboardButton('Банковский перевод', callback_data='invoice')
markup_inline_payment.add(btn_in_card, btn_in_cash, btn_in_invoice)


markup_inline_delivery = types.InlineKeyboardMarkup()
btn_in_courier = types.InlineKeyboardButton('Курьерская доставка', callback_data='courier')
btn_in_pickup = types.InlineKeyboardButton('Самовывоз', callback_data='pickup')
btn_in_post = types.InlineKeyboardButton('Почта России', callback_data='post')
markup_inline_delivery.add(btn_in_courier, btn_in_pickup, btn_in_post)


@bot.edited_message_handler(func=lambda message:True)
@bot.message_handler(func=lambda message:True)
def echo_all(message):
    if message.text == 'Способы доставки':
        bot.reply_to(message, 'В наших магазинах доступны следующие способы доставки:', reply_markup=markup_inline_delivery)
    elif message.text == 'Способы оплаты':
        bot.reply_to(message,
                    'В наших магазинах доступны следующие способы оплаты:', reply_markup=markup_inline_payment)
    else:
        bot.reply_to(message, message.text, reply_markup=markup_menu)
        bot.send_message(message.chat.id, 'Answer: Yes or No?', reply_markup=gen_markup())


@bot.message_handler(func=lambda message: True, content_types=['location'])
def magazin_location(message):
    lon = message.location.longitude
    lat = message.location.latitude
    distance = [vincenty(i['latm'], i['lonm']) for i in MAGAZINS]

    index = distance.index(min(distance))
    bot.send_message(message.chat.id, 'Ближайший магазин')
    bot.send_venue(message.chat.id, MAGAZINS[index]['latm'],
                                    MAGAZINS[index]['lonm'],
                                    MAGAZINS[index]['title'],
                                    MAGAZINS[index]['adress'],)
    bot.send_location(message.chat.id, latitude=lat, longitude=lon)
    bot.send_message(message.chat.id, f"Your longitude:{lon}, and latitude:{lat}\nShop longitude:{MAGAZINS[index]['latm']}, and latitude:{MAGAZINS[index]['lonm']}")



@bot.callback_query_handler(func=lambda call:True)
def call_back_payment(call):

    if call.data == 'cb_yes':
        bot.answer_callback_query(call.id, 'Your answer is yes')
    if call.data == 'cb_no':
        bot.answer_callback_query(call.id, 'Your answer is no')

    if call.data == 'cash':
        bot.send_message(call.message.chat.id, text='Наличная оплата производится в рублях, в кассе магазина', reply_markup=markup_inline_payment)
    elif call.data == 'card':
        bot.send_message(call.message.chat.id, text='Оплата по карте производится на счет 5168 7573 5937 2218', reply_markup=markup_inline_payment)
    elif call.data == 'invoice':
        bot.send_message(call.message.chat.id, text='Банковский перевод осуществляется при помощи перевода банка', reply_markup=markup_inline_payment)
    elif call.data == 'courier':
        bot.send_message(call.message.chat.id, text='Курьерская доставка осуществяется курьером на мопеде', reply_markup=markup_inline_delivery)
    elif call.data == 'pickup':
        bot.send_message(call.message.chat.id, text='Самовывоз осуществляется вами лично', reply_markup=markup_inline_delivery)
    elif call.data == 'post':
        bot.send_message(call.message.chat.id, text='Отправка почтой осуществляется Почтой России', reply_markup=markup_inline_delivery)


STICKER = 'CAADAgADCQIAAtzyqwdEux5ezoBTwQI'
@bot.message_handler(content_types=['sticker'])
def sticker_handler(message):
    print(message)
    print(message.sticker)
    bot.send_sticker(message.chat.id, STICKER)

# https://github.com/eternnoir/pyTelegramBotAPI/blob/master/examples/inline_example.py
@bot.inline_handler(lambda query: query.query == 'text')
def query_text(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', 'Result1', types.InputTextMessageContent('Result message.'))
        r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('Result message2.'))
        bot.answer_inline_query(inline_query.id, [r, r2])
    except Exception as e:
        print(e)

bot.polling()
