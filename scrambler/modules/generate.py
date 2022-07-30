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
    try:
        cube_msg = message.text.split(" ")[1]
    except IndexError:  # Fallback to 3x3
        cube_msg = "3x3"

    cube_notation = getcubenotation(cube_msg)
    cube_moves = getcubemoves(cube_msg)
    cube_type = getcubetype(cube_msg)

    # Get size of the notation
    cube_notation_size = len(cube_notation) - 1

    # Generate scramble
    scramble = open("scramble.txt", "a")
    scramble.write(f"Requested scramble generated for {cube_type}:\n\n")
    old_move = " "
    counter = 0

    while counter < cube_moves:
        move = cube_notation[SystemRandom().randint(0, cube_notation_size)]
        if __debug__:
            if move[0] == old_move[0]:
                print(f"[DEBUG]: move = {move} | old_move = {old_move} | SKIP")
            else:
                print(f"[DEBUG]: move = {move} | old_move = {old_move}")
        if move[0] != old_move[0]:
            scramble.write(f"{move} ")
            counter += 1
        old_move = move
    scramble.close()
    bot.edit_message_text(open("scramble.txt", "r").read(), msg.chat.id, msg.message_id)

    # Cleanup for the next run
    remove("scramble.txt")
    print("[LOG]: Finished generating scramble!")
