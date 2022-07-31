#!/usr/bin/python3
#
# Copyright (C) 2022 Giovanni Ricca
#
# SPDX-License-Identifier: Apache-2.0
#

from scrambler.__init__ import bot
from scrambler.vars.switcher import (
    std_cube,
    switcher_notation,
    switcher_moves,
    switcher_type,
)
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

    cube_notation = switcher_notation.get(cube_msg, std_cube)
    cube_moves = switcher_moves.get(cube_msg, 21)
    cube_type = switcher_type.get(cube_msg, "3x3")

    # Get size of the notation
    cube_notation_size = len(cube_notation) - 1

    # Generate scramble
    scramble = []
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
            scramble.append(move)
            counter += 1
        old_move = move
    bot.edit_message_text(
        f"Scramble generated for {cube_type}\n\n" + " ".join(scramble),
        msg.chat.id,
        msg.message_id,
    )
    print("[LOG]: Finished generating scramble!")
