#!/usr/bin/python3
#
# Copyright (C) 2022 Giovanni Ricca
#
# SPDX-License-Identifier: Apache-2.0
#

from scrambler.vars.notations import (
    std_cube,
)


def getcubenotation(var):
    switcher = {
        "3x3": std_cube,
        "2x2": std_cube,
    }
    return switcher.get(var, std_cube)


def getcubemoves(var):
    switcher = {
        "3x3": 21,
        "2x2": 9,
    }
    return switcher.get(var, 21)


def getcubetype(var):
    switcher = {
        "3x3": "3x3",
        "2x2": "2x2",
    }
    return switcher.get(var, "3x3")
