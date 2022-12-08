import configparser

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import types

config = configparser.ConfigParser()
config.read("settings.ini")
TOKEN = config["BOT"]["TOKEN"]
ADMIN = config["BOT"]["ADMIN"]
HOST = config["DB"]["HOST"]
USERNAME = config["DB"]["USERNAME"]
PASSWORD = config["DB"]["PASSWORD"]
DATABASE = config["DB"]["DATABASE"]

if ',' in ADMIN:
    ADMIN = ADMIN.split(",")
else:
    if len(ADMIN) >= 1:
        ADMIN = [ADMIN]
    else:
        print("Admin ID not specified")

# Accessing RAM
storage = MemoryStorage()

# Basic bot variables
bot = Bot(TOKEN,  parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)
