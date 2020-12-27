'''
https://github.com/Paul-weqe/python_webex_bot

Bot in native python 
'''

from python_webex.v1.Bot import Bot
from python_webex import webhook

bot = Bot('NTZlNTM4MGItYTc1Zi00YzRkLWE1NzItMzM5YmU5ODEyMjFiZDAwYTJmNDQtNTcw_PF84_fc071398-50cf-465e-8a63-2b0ee5238f75')         
# the program will automatically know the bot being referred to y the auth_token

# create a webhook to expose it to the internet
# rememer that url we got from step 2, this is where we use it. In my case it was http://87a942a1.ngrok.io. 
# We will be creating a webhook that will be listening when messages are sent
bot.create_webhook(
    name="quickstart_webhook", 
    target_url="http://ef808eee778f.ngrok.io",
    resource="messages", 
    event="created"
)

# we create a function that responds when someone says hi
# the room_id will automatically be filled with the webhook. Do not forget it
@bot.on_hears("hi")
def greet_back(room_id=None):
    return bot.send_message(room_id=room_id, text="Hi, how are you doing?")

# We create a default response in case anyone types anything else that we have not set a response for
# this is done using * [ don't ask me what happend when someone sends '*' as the message, that's on my TODO]
# @bot.on_hears("*")
# def default_response(room_id=None):
#     return bot.send_message(room_id=room_id, text="Sorry, could not understand that")


# make the webhook know the bot to be listening for, and we are done
webhook.bot = bot

if __name__ == "__main__":
    webhook.app.run(
        port=8000,
        debug=True,
    )         
    # don't keep debug=True in production



