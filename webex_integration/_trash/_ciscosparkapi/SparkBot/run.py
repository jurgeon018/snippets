'''
https://github.com/UniversalSuperBox/SparkBot
https://sparkbot.readthedocs.io/en/latest/

uses Falcon.
Uses ciscospartbot - old version of webexteamssdk
Doesnt run.
'''

import logging
from logging.config import fileConfig
import os
import sparkbot
from sparkbot import receiver, commandhelpers
from ciscosparkapi import CiscoSparkAPI

LOGGER = logging.getLogger('sparkbot')

# Initialize the environment
spark_api = CiscoSparkAPI(
    access_token='NTZlNTM4MGItYTc1Zi00YzRkLWE1NzItMzM5YmU5ODEyMjFiZDAwYTJmNDQtNTcw_PF84_fc071398-50cf-465e-8a63-2b0ee5238f75',
)
bot = sparkbot.SparkBot(
    spark_api, 
    root_url='https://ef808eee778f.ngrok.io',
    logger=LOGGER,
)

# Add commands here
@bot.command("ping")
def ping(caller, room_id):
    """
    Usage: `ping`

    Returns **pong**.
    """

    if commandhelpers.is_group(spark_api, room_id):
        return '{}, **pong**'.format(commandhelpers.mention_person(caller))
    else:
        return '**pong**'
