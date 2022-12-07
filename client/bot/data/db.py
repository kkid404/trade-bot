from loader import USERNAME, HOST, PASSWORD, DATABASE
import pymysql

class CallDb():

    def __init__(self):
        self.connection = pymysql.connect(
            host=HOST,
            user=USERNAME,
            password=PASSWORD,
            database=DATABASE,
            cursorclass=pymysql.cursors.DictCursor,
        )

    def add_user(self, telegram_id, username, lang):
        with self.connection.cursor() as cursor:
            cursor.execute("INSERT INTO `user` (telegram_id, username, lang)\
                            VALUES (%s, %s, %s)", (telegram_id, username, lang))
        self.connection.commit()
    
    def chek_user(self, telegram_id):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT telegram_id FROM `user` WHERE telegram_id = %s",
            (telegram_id))
            res = cursor.fetchone()
            return res["telegram_id"]
    
    def update_lang(self, lang, telegram_id):
        with self.connection.cursor() as cursor:
            cursor.execute("UPDATE `user` SET lang = %s WHERE telegram_id = %s",
            (lang, telegram_id))
        self.connection.commit()
    
    def get_lang(self, telegram_id):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT lang FROM `user` WHERE telegram_id = %s", 
            (telegram_id))
            res = cursor.fetchone()
            return res["lang"]

    def get_username(self, telegram_id):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT username FROM `user` WHERE telegram_id = %s",
            (telegram_id))
            res = cursor.fetchone()
            return res["username"]

    def update_username(self, username, telegram_id):
        with self.connection.cursor() as cursor:
            cursor.execute("UPDATE `user` SET username = %s WHERE telegram_id = %s",
            (username, telegram_id))
        self.connection.commit()