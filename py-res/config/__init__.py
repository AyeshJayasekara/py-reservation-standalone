import datetime
import sqlite3
import bcrypt

USER_TABLE_DDL = (
    'CREATE TABLE IF NOT EXISTS USER(username varchar(20), password varchar(100), user_type varchar(20),email varchar(50),  created_date datetime)')
RETRIEVE_USER = ('SELECT * FROM USER WHERE username = ?')


class Database:

    def __init__(self, log, config, initialize):
        self.log = log
        self.config = config
        self.connection = sqlite3.connect(self.config['database'])
        self.cursor = self.connection.cursor()

        if initialize:
            self.initialize_database()

    def initialize_database(self):
        self.log.info('DATABASE INITIALIZED')
        self.create_tables(self.cursor)
        self.log.info('DATABASE TABLES INITIALIZED')
        self.create_power_user(self.cursor)
        self.log.info('ADMIN POWER USER INITIALIZED')

    def create_tables(self, cursor):
        cursor.execute(USER_TABLE_DDL)

    def create_power_user(self, cursor):
        self.log.info('CREATING ADMIN POWER USER >>')
        cursor.execute('INSERT INTO USER(username, password, user_type,email, created_date) VALUES (?, ?, ?, ?, ?)', (
        'admin', self.encrypt_password(self.config['temp_password']), 'ADMIN', '', datetime.datetime.now()))
        cursor.connection.commit()

    def encrypt_password(self, password):
        # converting password to array of bytes
        _bytes = password.encode('utf-8')

        # Hashing the password
        return bcrypt.hashpw(_bytes, bcrypt.gensalt())
