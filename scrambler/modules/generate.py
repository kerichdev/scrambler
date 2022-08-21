#!/usr/bin/python3
#
# Copyright (C) 2022 Giovanni Ricca
#
# SPDX-License-Identifier: Apache-2.0
#

from scrambler import bot, LOG, DEBUG
from scrambler.defs.switcher import getcubeprops
from secrets import SystemRandom
from time import sleep


@bot.message_handler(func=lambda message: True, commands=["generate"])
def generate(message):
    LOG("Starting generating scramble!")
    msg = bot.send_message(message.chat.id, "Generating a scramble...") # 'Scrambling...' / "Getting you a scramble..." - TO-DO: randomize? fun stuff
    # Sleep for 1 second
    sleep(1)

    # Get some info about the cube mentioned, fall back to 3x3 if it doesn't exist
    try:
        cube_msg = message.text.split(" ")[1]
    except IndexError:  # Fallback to 3x3
        cube_msg = "3x3"

    cube_notation = getcubeprops(cube_msg)[1]
    cube_moves = getcubeprops(cube_msg)[2]
    cube_type = getcubeprops(cube_msg)[3]

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
                DEBUG(f"move = {move} | old_move = {old_move} | SKIP")
            else:
                DEBUG(f"move = {move} | old_move = {old_move}")
        if move[0] != old_move[0]:
            scramble.append(move)
            counter += 1
        old_move = move
    bot.edit_message_text(
        f"Scramble generated for {cube_type}\n\n{' '.join(scramble)}",
        msg.chat.id,
        msg.message_id,
    )
    LOG("Finished generating scramble!")
