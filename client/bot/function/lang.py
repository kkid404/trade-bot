lang = {
    "rus" : {
        "messages" : {
            "hello" : "Привет! Я бот для автоматической покупки и"
            " продажи криптовалюты на спотовом рынке binance."
            " В данный момент я ничего не умею, но очень скоро "
            "я смогу делать очень крутые штуки!",
            "settings" : "Здесь можно настроить уведомления и язык отображения",
            "lang" : "Выбери язык на котором будет отображаться меню и вся информация",
            "back" : "Хорошо",
            "progress" : "Этот блок в процессе работы",
            },

        "keyboards" : {
            "settings" : "Настройки",
            "lang" : "Язык",
            "volatil" : "Волатильность",
            "depth" : "Стакан цен",
            "back" : "Назад",
            },
    },
    
    "eng" : {
        "messages" : {
            "hello" : "Hello! I am a bot to automatically buy and"
            " sell cryptocurrency on the binance spot market."
            " At the moment I can’t do anything, but very soon "
            "I will be doing unrealistically cool things!",
            "settings" : "Here you can configure what exactly to send you and the language",
            "lang" : "Select the language in which you would like to receive information",
            "back" : "Okay",
            "progress" : "This block is in progress",
            },
        
        "keyboards" : {
            "settings" : "Settings",
            "lang" : "Language",
            "volatil" : "Volatility",
            "depth" : "Depth of Market",
            "back" : "Back",
            },
    }
    }

def chek_lang(lang):
    if lang == "🇺🇸":
        return "eng"
    if lang == "🇷🇺":
        return "rus"
