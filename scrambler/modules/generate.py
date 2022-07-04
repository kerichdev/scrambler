#!/usr/bin/python3
#
# Copyright (C) 2022 Giovanni Ricca
#
# SPDX-License-Identifier: Apache-2.0
#

from scrambler.__init__ import bot
from scrambler.defs.getcube import (
    getcubenotation,
    getcubemoves,
    getcubetype,
)
from os import remove
from secrets import SystemRandom
from time import sleep


@bot.message_handler(func=lambda message: True, commands=["generate"])
def generate(message):
    print("[LOG]: Starting generating scramble!")
    msg = bot.send_message(message.chat.id, "Starting generating a scramble!")
    # Sleep for 1 second
    sleep(1)

    # Get some info about the cube mentioned, fall back to 3x3 if it doesn't exist
    cube_notation = getcubenotation(message.text.replace("/generate ", ""))
    cube_moves = getcubemoves(message.text.replace("/generate ", ""))
    cube_type = getcubetype(message.text.replace("/generate ", ""))

    # Get size of the notation
    cube_notation_size = len(cube_notation) - 1

    if __debug__:
        print("[LOG]: Cube notation size =", cube_notation_size)

    # Generate scramble
    scramble = open("scramble.txt", "a")
    scramble.write("Requested scramble generated for %s:\n\n" % cube_type)
    old_move = " "
    counter = 0

    while counter < cube_moves:
        move = cube_notation[SystemRandom().randint(0, cube_notation_size)]
        if __debug__:
            print("[LOG]: move =", move, "old_move =", old_move)
        if move[0] != old_move[0]:
            scramble.write("%s " % move)
            counter += 1
        old_move = move
    scramble.close()
    bot.edit_message_text(open("scramble.txt", "r").read(), msg.chat.id, msg.message_id)

    # Cleanup for the next run
    remove("scramble.txt")
    print("[LOG]: Finished generating scramble!")
