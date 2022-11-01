import sqlite3 as sq

class CallDb():

    def __init__(self):
        self.base = sq.connect('data.db')
        self.cur = self.base.cursor()

    def sql_start(self):
        if self.base:
            print("Data successfully connect!")
        self.cur.execute('CREATE TABLE IF NOT EXISTS user(telegram_id INTEGER PRIMARY KEY, lang TEXT)')
        self.base.commit()

    def add_user(self, telegram_id, lang):
        self.cur.execute("INSERT INTO user VALUES (?, ?)", (telegram_id, lang))
        self.base.commit()

    def chek_user(self, telegram_id):
        res =  self.cur.execute(f'SELECT telegram_id FROM user WHERE telegram_id == {telegram_id}').fetchone()
        if res:
            return True
        else:
            return False

    def update_lang(self, lang, user):
        self.cur.execute("UPDATE user SET lang = ? WHERE telegram_id = ?", (lang, user))
        self.base.commit()

    def get_lang(self, telegram_id):
        res =  self.cur.execute(f'SELECT lang FROM user WHERE telegram_id == {telegram_id}').fetchone()
        return res[0]
