import datetime
from abc import abstractmethod

import bcrypt

from config import Database

RETRIEVE_USER = ('SELECT * FROM USER WHERE username = ?')
INSERT_USER = ('INSERT INTO USER(username, password, user_type, email, created_date) VALUES (?, ?, ?, ?, ?)')


class User:

    def __init__(self, database: Database, username: str = None):
        self.username = username
        self.database = database

    @staticmethod
    def login(username: str, password: str, database: Database) -> {}:
        database.cursor.execute(RETRIEVE_USER, (username,))
        record = database.cursor.fetchone()

        if record is None:
            return {"login": False}

        comparison = bcrypt.checkpw(password.encode('utf-8'), record[1])

        if comparison:
            return {"login": True, "username": record[0], "type": record[2]}

        else:
            return {"login": False}

    @staticmethod
    def register(database: Database, username: str, password: str, email: str):
        encrypted_password = database.encrypt_password(password)

        if User.has_user(database, username):
            raise ValueError("Username already exists!")

        database.cursor.execute(INSERT_USER, (username, encrypted_password, 'USER', email, datetime.datetime.now()))
        database.cursor.connection.commit()


    @staticmethod
    def has_user(database: Database, username):
        database.cursor.execute(RETRIEVE_USER, (username,))
        record = database.cursor.fetchone()

        if record is None:
            return False
        else:
            return True
