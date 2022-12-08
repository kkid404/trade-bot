from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from loader import bot, dp
from keyboards.client_kb import Keyboard
from classes import User
from function.lang import lang, chek_lang
from states import LangStates
from data.db import CallDb


# Response to start command
@dp.message_handler(CommandStart())
async def command_start(message: types.Message, kb = Keyboard()):
    await bot.send_message(
    message.from_user.id,
    "Select the language in which you would"
    "like to receive information\n—————————\n"
    "Выберите ваш языка",
    reply_markup=kb.language_kb())
    await LangStates.lang.set()

@dp.message_handler(state=LangStates.lang)
async def select_lang(message: types.Message, state: FSMContext, kb = Keyboard(), db = CallDb()):
    async with state.proxy() as data:
        data["lang"] = message.text
        user_lang = data["lang"]
    
    if chek_lang(data["lang"]):
        user_lang = chek_lang(data["lang"])
        user = User(message.from_user.id, message.from_user.username, user_lang)
    try:
        await state.finish()

        if(not db.chek_user(int(user.id))):
            db.add_user(int(user.id), user.username, user.lang)
        if(user.lang != db.get_lang(int(user.id))):
            db.update_lang(user.lang, int(user.id))
        if(user.username != db.get_username(int(user.id))):
            db.update_username(user.username, int(user.id))
        
        await bot.send_message(
            message.from_user.id, 
            lang[user.lang]["messages"]["hello"],
            reply_markup=kb.start_kb(user.lang)
            )
    
    except UnboundLocalError:
        await bot.send_message(
            message.from_user.id, 
            "Wrong answer, tap on /start")
        await state.finish()

