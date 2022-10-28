from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from loader import bot, dp

# Response to start command
@dp.message_handler(CommandStart())
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id,
    "Hello! I am a bot to automatically buy and"
    " sell cryptocurrency on the binance spot market."
    "At the moment I can’t do anything, but very soon "
    "I will be doing unrealistically cool things!"
    )