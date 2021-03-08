import sqlite3
import os
from sqlite3 import Error
from dotenv import load_dotenv

load_dotenv()


class Connection:

    def __init__(self, cwd):
        print('sdjk')
        self.cwd = cwd
        print(cwd)
        self.db = self.cwd + '/db/auto_bell_db.db'

    def create_connection(self):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect(self.db)
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()
