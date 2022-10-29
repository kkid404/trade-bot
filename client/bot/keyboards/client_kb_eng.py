from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

class Keyboard:
    back = KeyboardButton("Back")

    def start_kb():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        settings = KeyboardButton("Settings")
        keyboard.add(settings)
        return keyboard

    def settings_kb():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        language = KeyboardButton("Language")
        signals = KeyboardButton("Volatility")
        depth = KeyboardButton("Depth of Market")
        back = KeyboardButton("Back")
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