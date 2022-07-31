#!/usr/bin/python3
#
# Copyright (C) 2022 Giovanni Ricca
#
# SPDX-License-Identifier: Apache-2.0
#

from scrambler.__init__ import bot, LOG, DEBUG


def main():
    LOG("Started!")
    if __debug__:
        DEBUG("Debug mode enabled")
    bot.polling()
