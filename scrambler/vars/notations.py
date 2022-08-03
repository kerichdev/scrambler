#!/usr/bin/python3
#
# Copyright (C) 2022 Giovanni Ricca
#
# SPDX-License-Identifier: Apache-2.0
#

# Source: https://github.com/cs0x7f/cstimer/blob/master/src/js/scramble/megascramble.js

two_cube = [
    # U
    "U",
    "U'",
    "U2",
    # R
    "R",
    "R'",
    "R2",
    # F
    "F",
    "F'",
    "F2",
]

three_cube = two_cube + [
    # D
    "D",
    "D'",
    "D2",
    # L
    "L",
    "L'",
    "L2",
    # B
    "B",
    "B'",
    "B2",
]

four_cube = three_cube + [
    # Uw
    "Uw",
    "Uw'",
    "Uw2",
    # Rw
    "Rw",
    "Rw'",
    "Rw2",
    # Fw
    "Fw",
    "Fw'",
    "Fw2",
]

five_cube = four_cube + [
    # Dw
    "Dw",
    "Dw'",
    "Dw2",
    # Lw
    "Lw",
    "Lw'",
    "Lw2",
    # Bw
    "Bw",
    "Bw'",
    "Bw2",
]
