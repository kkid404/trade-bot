from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from loader import bot, dp
from keyboards.client_kb_rus import KeyboardRus

# # Response to start command
# @dp.message_handler(CommandStart())
# async def command_start(message: types.Message, kb = KeyboardRus()):
#     await bot.send_message(
#     message.from_user.id,
#     "Привет! Я бот для автоматической покупки и"
#     " продажи криптовалюты на спотовом рынке binance."
#     " В данный момент я ничего не умею, но очень скоро "
#     "я смогу делать очень крутые штуки!",
#     reply_markup=kb.start_kb())

@dp.message_handler(text="Настройки")
async def command_settings_rus(message: types.Message, kb = KeyboardRus):
    await bot.send_message(
    message.from_user.id,
    "Здесь можно настроить уведомления и язык отображения",
    reply_markup=kb.settings_kb())

@dp.message_handler(text="Язык")
async def command_language_rus(message: types.Message, kb = KeyboardRus):
    await bot.send_message(
    message.from_user.id,
    "Выбери язык на котором будет отображаться меню и вся информация",
    reply_markup=kb.language_kb())

@dp.message_handler(text="🇷🇺")
async def command_language(message: types.Message, kb = KeyboardRus):
    await bot.send_message(
    message.from_user.id,
    "Изменения сохранены!",
    reply_markup=kb.start_kb())