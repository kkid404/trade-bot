
class User:

    def __init__(self, id, username, lang):
        self.id = id
        self.username = username
        self.lang = lang

    def get_lang(self):
        return self.lang