from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from function import lang

class Keyboard:

    def back(user_lang):
        back = KeyboardButton(lang[user_lang]["keyboards"][0])
        return back

    def start_kb(user_lang):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        settings = KeyboardButton(lang[user_lang]["keyboards"][1])
        keyboard.add(settings)
        return keyboard

    def settings_kb(self,user_lang):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        language = KeyboardButton(lang[user_lang]["keyboards"][2])
        signals = KeyboardButton(lang[user_lang]["keyboards"][3])
        depth = KeyboardButton(lang[user_lang]["keyboards"][4])
        back = self.back()
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