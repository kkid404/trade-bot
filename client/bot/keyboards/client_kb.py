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

    def volatil_kb(self, user_lang):
        keyboard = InlineKeyboardMarkup(row_width=1)
        for time, value in lang[user_lang]["time"].items():
            res = InlineKeyboardButton(value, callback_data=time)
            keyboard.add(res)
        return keyboard

    def new_volatil_kb(self, kb: InlineKeyboardMarkup, button):
        keyboard = InlineKeyboardMarkup(row_width=1)
        symbol = "✅"
        count = [x.text for y in kb.inline_keyboard for x in y if symbol in x.text]
        for btn_list in kb.inline_keyboard:
            for value in btn_list:
                sumcount = len(count)
                if (value["callback_data"] == button) \
                and (symbol not in value["text"]) \
                and (sumcount < 2):
                    res = InlineKeyboardButton(value["text"] + f" {symbol}", 
                    callback_data=value["callback_data"])
                    count.append(value["text"] + f" {symbol}")
                    keyboard.add(res)
                elif (value["callback_data"] == button) and (symbol in value["text"]):
                    res = InlineKeyboardButton(str(value["text"]).replace(f" {symbol}", ""), 
                    callback_data=value["callback_data"])
                    keyboard.add(res)
                else:
                    res = InlineKeyboardButton(value["text"], callback_data=value["callback_data"])
                    keyboard.add(res)
        return keyboard