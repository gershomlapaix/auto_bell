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
        print('\nRunning migrations ........\n')
        self.create_users_table()
        self.create_bells_table()
        self.create_timetables_table()
        self.create_playsounds_table()

    def create_timetables_table(self):
        query = "CREATE TABLE IF NOT EXISTS timetables ( id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, " \
                " day TEXT CHECK (day IN " \
                "('MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY', 'ALL_DAYS', " \
                "'WEEK_DAYS', 'WEEKEND' )) NOT NULL, time TEXT NOT NULL, duration INTEGER DEFAULT 10, status  CHECK (" \
                "status IN  ('ACTIVE', 'INACTIVE' )) DEFAULT 'ACTIVE', timestamps TIMESTAMP DEFAULT " \
                "CURRENT_TIMESTAMP); "
        self.cursor.execute(query)
        self.connection.commit()

    def create_playsounds_table(self):
        query = "CREATE TABLE IF NOT EXISTS playsounds ( id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, " \
                "path TEXT NOT NULL, status  CHECK (" \
                "status IN  ('ACTIVE', 'INACTIVE' )) DEFAULT 'ACTIVE', timestamps TIMESTAMP DEFAULT " \
                "CURRENT_TIMESTAMP); "
        self.cursor.execute(query)
        self.connection.commit()

    def create_bells_table(self):
        query = "CREATE TABLE IF NOT EXISTS bells ( id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, " \
                "location TEXT NOT NULL, serial TEXT NOT NULL UNIQUE , status  CHECK (" \
                "status IN  ('ACTIVE', 'INACTIVE' )) DEFAULT 'ACTIVE', timestamps TIMESTAMP DEFAULT " \
                "CURRENT_TIMESTAMP); "
        self.cursor.execute(query)
        self.connection.commit()

    def create_users_table(self):
        query = "CREATE TABLE IF NOT EXISTS users ( id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL " \
                "UNIQUE, " \
                "password TEXT NOT NULL, email TEXT NOT NULL UNIQUE , full_names TEXT NOT NULL, status CHECK (" \
                "status IN  ('ACTIVE', 'INACTIVE' )) DEFAULT 'ACTIVE', timestamps TIMESTAMP DEFAULT " \
                "CURRENT_TIMESTAMP); "
        self.cursor.execute(query)
        self.connection.commit()

    def __del__(self):
        print('Migrations run successfully')
        self.connection.close()
