import psycopg2
from aiogram import types


class ManagerBD:
    def __init__(self, dbname, dbuser, user_password):
        self.conn = psycopg2.connect(dbname=dbname, user=dbuser, password=user_password)
        self.curs = self.conn.cursor()

    def user_exist(self, tg_id) -> bool:
        self.curs.execute('SELECT * FROM "User" WHERE "tg_id" = %s', (tg_id, ))
        return bool(len(self.curs.fetchall()))
    
    def add_user(self, user: types.User):
        self.curs.execute('INSERT INTO "User" (username, tg_id) VALUES(%s, %s)',
                          (user.username, user.id)
                          )
        self.conn.commit()

    def get_stuff(self):
        self.curs.execute('SELECT "tg_id" FROM "User" WHERE "stuff" = true;')
        return self.curs.fetchall()

    def close(self):
        self.conn.close()