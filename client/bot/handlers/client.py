from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from loader import bot, dp
from keyboards.client_kb import Keyboard
from classes import User
from function import lang
from states import LangStates

# # Response to start command
# @dp.message_handler(CommandStart())
# async def command_start(message: types.Message, kb = Keyboard):
#     await bot.send_message(
#     message.from_user.id,
#     "Select the language in which you would like to receive information",
#     reply_markup=kb.language_kb())

# @dp.message_handler(text="🇺🇸")
# async def command_language(message: types.Message, kb = Keyboard):
#     user = User(message.from_user.id, "eng")
#     await bot.send_message(
#     message.from_user.id,
#     lang[user.lang]["message"][0],
#     reply_markup=kb.start_kb())

# @dp.message_handler(text="Settings")
# async def command_settings(message: types.Message, kb = Keyboard):
#     await bot.send_message(
#     message.from_user.id,
#     "Here you can configure what exactly to send you and the language",
#     reply_markup=kb.settings_kb())

# @dp.message_handler(text="Language")
# async def command_language(message: types.Message, kb = Keyboard):
#     await bot.send_message(
#     message.from_user.id,
#     "Select the language in which you would like to receive information",
#     reply_markup=kb.language_kb(kb.back))

# @dp.message_handler(text="Back")
# async def command_language(message: types.Message, kb = Keyboard):
#     await bot.send_message(
#     message.from_user.id,
#     "Okay!",
#     reply_markup=kb.start_kb())


# Response to start command
@dp.message_handler(CommandStart())
async def command_start(message: types.Message, kb = Keyboard):
    await bot.send_message(
    message.from_user.id,
    "Select the language in which you would"
    "like to receive information\n—————————\n"
    "Выберите ваш языка",
    reply_markup=kb.language_kb())
    await LangStates.lang.set()

@dp.message_handler(state=LangStates.lang)
async def select_lang(message: types.Message, state: FSMContext, kb = Keyboard):
    async with state.proxy() as data:
        data["lang"] = message.text
        user_lang = data["lang"]
    if user_lang == "🇺🇸":
        user = User(message.from_user.id, "eng")
    elif user_lang == "🇷🇺":
        user = User(message.from_user.id, "rus")
    try:
        await state.finish()
        await bot.send_message(
            message.from_user.id, 
            lang[user.lang]["messages"][0],
            reply_markup=kb.start_kb(user.lang)
            )
    except UnboundLocalError:
        await bot.send_message(message.from_user.id, "wrong answer, tap on start")
        await state.finish()
