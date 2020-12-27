USERS = set()

@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def echo_digits(message: Message):
    if 'Alex Goodkid' in message.text:
        bot.reply_to(message, text='Alex is good kid!')
        return None
    reply = str(random.random())
    if message.from_user.id in USERS:
        reply += f'{message.from_user}, hello again!'
    bot.reply_to(message, text=reply)
    USERS.add(message.from_user.id)
    print(USERS)

@bot.inline_handler(lambda query: query.query == 'text')
def query_text(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', 'Result', types.InputTextMessageContent('Result message.'))
        r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('Result message2.'))
        bot.answer_inline_query(inline_query.id, [r, r2])
    except Exception as e:
        print(e)
