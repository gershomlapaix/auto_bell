import sqlite3
from sqlite3 import Error


class Connection:
    def __init__(self, cwd):
        self.cwd = cwd
        self.db = self.cwd + '/db/auto_bell_db.db'
        self.connect()

    def connect(self):
        try:
            return sqlite3.connect(self.db)
        except Error as e:
            print(e)
            return None
