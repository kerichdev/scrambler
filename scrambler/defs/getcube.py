#!/usr/bin/python3
#
# Copyright (C) 2022 Giovanni Ricca
#
# SPDX-License-Identifier: Apache-2.0
#

from scrambler.vars.notations import (
    std_cube,
    four_cube,
)


def getcubenotation(var):
    switcher = {
        "2x2": std_cube,
        "3x3": std_cube,
        "4x4": four_cube,
        "5x5": four_cube,
    }
    return switcher.get(var, std_cube)


def getcubemoves(var):
    switcher = {
        "2x2": 9,
        "3x3": 21,
        "4x4": 45,
        "5x5": 60,
    }
    return switcher.get(var, 21)


def getcubetype(var):
    switcher = {
        "2x2": "2x2",
        "3x3": "3x3",
        "4x4": "4x4",
        "5x5": "5x5",
    }
    return switcher.get(var, "3x3")
