from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from function.lang import lang

class Keyboard:

    def back(self, user_lang):
        back = KeyboardButton(lang[user_lang]["keyboards"]["back"])
        return back

    def start_kb(self, user_lang):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        settings = KeyboardButton(lang[user_lang]["keyboards"]["settings"])
        keyboard.add(settings)
        return keyboard

    def settings_kb(self,user_lang):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        language = KeyboardButton(lang[user_lang]["keyboards"]["lang"])
        signals = KeyboardButton(lang[user_lang]["keyboards"]["volatil"])
        depth = KeyboardButton(lang[user_lang]["keyboards"]["depth"])
        back = self.back(user_lang)
        keyboard.add(language, signals, depth, back)
        return keyboard

    def language_kb(self, back = None):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        russian = KeyboardButton("🇷🇺")
        english = KeyboardButton("🇺🇸")
        if(back):
            keyboard.add(russian, english).row(back)
        else:
            keyboard.add(russian, english)
        return keyboard