#!/usr/bin/python3
#
# Copyright (C) 2022 Giovanni Ricca
#
# SPDX-License-Identifier: Apache-2.0
#

from scrambler.__init__ import bot

welcome_message = [
    """
Welcome user:

You can generate a standard cube (3x3) scramble with /generate
Type /help if you want to know more about this bot

Bot made by @GiovanniRN5
"""
]


@bot.message_handler(commands=["start"])
def ping(message):
    bot.reply_to(message, welcome_message)
