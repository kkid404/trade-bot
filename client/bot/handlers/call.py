from aiogram import types
from function.lang import lang, chek_lang
from aiogram.utils.callback_data import CallbackData
from aiogram.dispatcher import filters
from aiogram.utils.exceptions import MessageNotModified

from keyboards.client_kb import Keyboard
from loader import bot, dp


@dp.callback_query_handler(text=list(lang["rus"]["time"].keys()))
async def catt_test(callback: types.CallbackQuery, kb = Keyboard()):
    try:
        message = callback.message.message_id
        await bot.edit_message_reply_markup(
            callback.from_user.id, 
            message, 
            reply_markup=kb.new_volatil_kb(callback.message.reply_markup, callback.data)
        )
    except MessageNotModified:
        pass
        