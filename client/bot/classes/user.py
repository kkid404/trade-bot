
class User:

    def __init__(self, id, lang):
        self.id = id
        self.lang = lang

    def get_lang(self):
        return self.lang