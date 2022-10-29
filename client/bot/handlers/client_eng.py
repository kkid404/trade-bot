from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from loader import bot, dp
from keyboards.client_kb_eng import Keyboard

# Response to start command
@dp.message_handler(CommandStart())
async def command_start(message: types.Message, kb = Keyboard):
    await bot.send_message(
    message.from_user.id,
    "Hello! I am a bot to automatically buy and"
    " sell cryptocurrency on the binance spot market."
    " At the moment I can’t do anything, but very soon "
    "I will be doing unrealistically cool things!",
    reply_markup=kb.start_kb())

@dp.message_handler(text="Settings")
async def command_settings(message: types.Message, kb = Keyboard):
    await bot.send_message(
    message.from_user.id,
    "Here you can configure what exactly to send you and the language",
    reply_markup=kb.settings_kb())

@dp.message_handler(text="Language")
async def command_language(message: types.Message, kb = Keyboard):
    await bot.send_message(
    message.from_user.id,
    "Select the language in which you would like to receive information",
    reply_markup=kb.language_kb())

@dp.message_handler(text="🇺🇸")
async def command_language(message: types.Message, kb = Keyboard):
    await bot.send_message(
    message.from_user.id,
    "Changes saved!",
    reply_markup=kb.start_kb())