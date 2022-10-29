from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

class KeyboardRus:

    back = KeyboardButton("Назад")

    def start_kb():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        settings = KeyboardButton("Настройки")
        keyboard.add(settings)
        return keyboard

    def settings_kb():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        language = KeyboardButton("Язык")
        signals = KeyboardButton("Волатильность")
        depth = KeyboardButton("Биржевой стакан")
        back = KeyboardButton("Назад")
        keyboard.add(language, signals, depth, back)
        return keyboard

    def language_kb(back = None):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        russian = KeyboardButton("🇷🇺")
        english = KeyboardButton("🇺🇸")
        if(back):
            keyboard.add(russian, english).row(back)
        else:
            keyboard.add(russian, english)
        return keyboard