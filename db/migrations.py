from sqlite3 import connect

# Replace username with your own A2 Hosting account username:
from db.connection import Connection
import os
from dotenv import load_dotenv

load_dotenv()


class Migration:
    def __init__(self, connection: Connection):
        self.connection = connection.connect()
        print('Connected to database Successfully')
        self.cursor = self.connection.cursor()

    def run_migrations(self):
        self.create_test_table()

    def create_test_table(self):
        query = "CREATE TABLE contacts ( contact_id INTEGER PRIMARY KEY, first_name TEXT NOT NULL, last_name TEXT NOT " \
                "NULL, email TEXT NOT NULL UNIQUE,phone TEXT NOT NULL UNIQUE); "
        self.cursor.execute(query)
        self.connection.commit()

    def __del__(self):
        self.connection.close()
