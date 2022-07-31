#!/usr/bin/python3
#
# Copyright (C) 2022 Giovanni Ricca
#
# SPDX-License-Identifier: Apache-2.0
#

from pathlib import Path
from importlib import import_module
from pkgutil import iter_modules
from telebot import TeleBot
from os import getenv
from dotenv import load_dotenv

# Load .env
load_dotenv()
bot = TeleBot(getenv("API_KEY"))

# Import modules
for module_name in [
    name for _, name, _ in iter_modules([str(Path(__file__).parent / "modules")])
]:
    import_module(f"scrambler.modules.{module_name}")

# Define logging vars
def LOG(var):
    return print(f"[LOG]: {var}")


def DEBUG(var):
    return print(f"[DEBUG]: {var}")
