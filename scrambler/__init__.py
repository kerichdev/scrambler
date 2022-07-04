#!/usr/bin/python3
#
# Copyright (C) 2022 Giovanni Ricca
#
# SPDX-License-Identifier: Apache-2.0
#

from pathlib import Path
from importlib import import_module
from pkgutil import iter_modules
import configparser, telebot

parser = configparser.ConfigParser()
parser.readfp(open(r"config.txt"))

API_KEY = parser.get("config", "API_KEY")
bot = telebot.TeleBot(API_KEY)

# Import modules
bot_path = Path(__file__).parent
modules_path = bot_path / "modules"

for module_name in [name for _, name, _ in iter_modules([str(modules_path)])]:
    import_module(f"scrambler.modules.{module_name}")
