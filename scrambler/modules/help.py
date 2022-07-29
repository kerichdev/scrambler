#!/usr/bin/python3
#
# Copyright (C) 2022 Giovanni Ricca
#
# SPDX-License-Identifier: Apache-2.0
#

from scrambler.__init__ import bot

help_message = [
    """
Scrambler help:

> /help: Shows this message

> /generate <cube type>: Generate a scramble for the cube, example /generate 3x3
  Currently supported cubes: 2x2, 3x3, 4x4, 5x5

> /start: Hey, i'm alive
"""
]


@bot.message_handler(commands=["help"])
def ping(message):
    bot.reply_to(message, help_message)
