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
            "volatil" : "Здесь вы можете настроить нижнюю и верхнюю границу времени уведомлений о волатильности",
            },

        "keyboards" : {
            "settings" : "Настройки",
            "lang" : "Язык",
            "volatil" : "Волатильность",
            "depth" : "Стакан цен",
            "back" : "Назад",
            },

        "time" : {
            "1_second" : "1 Секунда",
            "5_second" : "5 Секунд",
            "30_second" : "30 Секунд",
            "1_minute" : "1 Минута",
            "5_minute" : "5 Минут",
            "10_minute" : "10 Минут",
            "1_hour" : "1 Час",
            "3_hour" : "3 Часа",
            "5_hour" : "5 Часов",
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
            "volatil" : "Here you can set the lower and upper limit of the volatility notification time",
            },
        
        "keyboards" : {
            "settings" : "Settings",
            "lang" : "Language",
            "volatil" : "Volatility",
            "depth" : "Depth of Market",
            "back" : "Back",
            },

        "time" : {
            "1_second" : "1 Second",
            "5_second" : "5 Seconds",
            "30_second" : "30 Seconds",
            "1_minute" : "1 Minute",
            "5_minute" : "5 Minutes",
            "10_minute" : "10 Minutes",
            "1_hour" : "1 Hour",
            "3_hour" : "3 Hours",
            "5_hour" : "5 Hours",
        },
    }
    }

def chek_lang(lang):
    if lang == "🇺🇸":
        return "eng"
    if lang == "🇷🇺":
        return "rus"

