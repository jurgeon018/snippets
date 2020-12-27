"""
https://github.com/hpreston/webexteamsbot
"""

import os
from webexteamsbot import TeamsBot

# Retrieve required details from environment variables
# bot_email = os.getenv("TEAMS_BOT_EMAIL")
# teams_token = os.getenv("TEAMS_BOT_TOKEN")
# bot_url = os.getenv("TEAMS_BOT_URL")
# bot_app_name = os.getenv("TEAMS_BOT_APP_NAME")

bot_email = 'ltq_statusboard_bot@webex.bot'
teams_token = 'NTZlNTM4MGItYTc1Zi00YzRkLWE1NzItMzM5YmU5ODEyMjFiZDAwYTJmNDQtNTcw_PF84_fc071398-50cf-465e-8a63-2b0ee5238f75'
bot_url = 'https://612a0279ba1f.ngrok.io/'
bot_app_name = 'ltq_statusboard_bot'


# Create a Bot Object
bot = TeamsBot(
    bot_app_name,
    teams_bot_token=teams_token,
    teams_bot_url=bot_url,
    teams_bot_email=bot_email,
    debug=True,
)
bot.set_help_message("Welcome to the Super Cool Bot! You can use the following commands:\n")

# A simple command that returns a basic string that will be sent as a reply
def do_something(incoming_msg):
    """
    Sample function to do some action.
    :param incoming_msg: The incoming message object from Teams
    :return: A text or markdown based reply
    """
    return "i did what you said - {}".format(incoming_msg.text)

bot.add_command("/dosomething", "help for do something", do_something)


def handle_webhooks():
    print('hello')
    return 'hello'

bot.add_new_url("/webhooks", "webhooks", handle_webhooks)

if __name__ == "__main__":
    bot.run(
        host="0.0.0.0", 
        port=5000,
    )



