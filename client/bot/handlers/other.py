from cgitb import handler
from aiogram import types

from loader import bot, dp
from keyboards.client_kb import Keyboard
from classes import User
from function.lang import lang, chek_lang
from data.db import CallDb

@dp.message_handler(content_types=["text"])
async def command_settings(message: types.Message, kb = Keyboard(), db = CallDb()):
    user = User(message.from_user.id, db.get_lang(int(message.from_user.id)))
    
    if message.text == lang[user.lang]["keyboards"]["settings"]:
        await bot.send_message(
            user.id,
            lang[user.lang]["messages"]["settings"],
            reply_markup=kb.settings_kb(user.lang)
        )
    
    if message.text == lang[user.lang]["keyboards"]["lang"]:
        await bot.send_message(
            user.id,
            lang[user.lang]["messages"]["lang"],
            reply_markup=kb.language_kb(kb.back(user.lang))
        )

    if chek_lang(message.text):
        user_lang = chek_lang(message.text)
        db.update_lang(user_lang, user.id)
        user.lang = user_lang
        await bot.send_message(
            user.id,
            lang[user.lang]["messages"]["back"],
            reply_markup=kb.settings_kb(user.lang)
        )

    if message.text == lang[user.lang]["keyboards"]["volatil"]:
            await bot.send_message(
                user.id,
                lang[user.lang]["messages"]["progress"],
                reply_markup=kb.settings_kb(user.lang)
            )

    if message.text == lang[user.lang]["keyboards"]["depth"]:
            await bot.send_message(
                user.id,
                lang[user.lang]["messages"]["progress"],
                reply_markup=kb.settings_kb(user.lang)
            )

    if message.text == lang[user.lang]["keyboards"]["back"]:
            await bot.send_message(
                user.id,
                lang[user.lang]["messages"]["back"],
                reply_markup=kb.start_kb(user.lang)
            )