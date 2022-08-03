#!/usr/bin/python3
#
# Copyright (C) 2022 Giovanni Ricca
#
# SPDX-License-Identifier: Apache-2.0
#

from scrambler.vars.notations import (
    two_cube,
    three_cube,
    four_cube,
    five_cube,
)

switcher = {
    "2x2": {1: two_cube, 2: 9, 3: "2x2"},
    "3x3": {1: three_cube, 2: 21, 3: "3x3"},
    "4x4": {1: four_cube, 2: 45, 3: "4x4"},
    "5x5": {1: five_cube, 2: 60, 3: "5x5"},
}


def getcubeprops(var):
    # Fall back to 3x3
    return switcher.get(var, {1: three_cube, 2: 21, 3: "3x3"})
