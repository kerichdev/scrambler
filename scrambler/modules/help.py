#!/usr/bin/python3
#
# Copyright (C) 2022 Giovanni Ricca
#
# SPDX-License-Identifier: Apache-2.0
#

from scrambler import bot
from scrambler.defs.switcher import switcher

help_message = [
    f"""
Scrambler help:

> /help: Shows this message

> /generate <cube type>: Generate a scramble for the cube, example /generate 3x3
  Currently supported cubes: {', '.join(switcher)}

> /start: Hey, i'm alive
"""
]


@bot.message_handler(commands=["help"])
def ping(message):
    bot.reply_to(message, help_message)
