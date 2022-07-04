#!/bin/bash
#
# Copyright (C) 2022 Giovanni Ricca
#
# SPDX-License-Identifier: Apache-2.0
#

PYTHON3="python3 -O -m"

while [ "${#}" -gt 0 ]; do
    case "${1}" in
        -d | --debug )
                PYTHON3="python3 -m"
                ;;
    esac
    shift
done

${PYTHON3} scrambler
