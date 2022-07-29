#!/usr/bin/python3
#
# Copyright (C) 2022 Giovanni Ricca
#
# SPDX-License-Identifier: Apache-2.0
#

from scrambler.__init__ import bot


def main():
    print("[LOG]: Started!")
    if __debug__:
        print("[DEBUG]: Debug mode enabled")
    bot.polling()
