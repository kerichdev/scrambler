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


def getcubeprops(var):
    return {
        "2x2": {1: std_cube, 2: 9, 3: "2x2"},
        "3x3": {1: std_cube, 2: 21, 3: "3x3"},
        "4x4": {1: four_cube, 2: 45, 3: "4x4"},
        "5x5": {1: four_cube, 2: 60, 3: "4x4"},
    }.get(var, {1: std_cube, 2: 21, 3: "3x3"})
