import datetime
import sqlite3
from pathlib import Path

import bcrypt

USER_TABLE_DDL = (
    'CREATE TABLE IF NOT EXISTS USER(username varchar(20), password varchar(100), user_type varchar(20),email varchar(50),  created_date datetime)')

ROOM_TABLE_DDL = (
    'CREATE TABLE IF NOT EXISTS ROOM( room_id integer not null constraint ROOM_pk primary key, room_type varchar(100) not null, price REAL not null)')

RESERVATION_TABLE_DDL = (
    'CREATE TABLE IF NOT EXISTS RESERVATION ( res_id integer primary key autoincrement,username varchar(20) not null, room_id integer not null, check_in_year int not null, check_in_month  integer not null, check_in_day integer not null, check_out_year integer not null, check_out_month integer not null, check_out_day integer not null)')

RESERVATION_SUMMARY_VIEW = (
    "CREATE VIEW IF NOT EXISTS RESERVATION_SUMMARY_VIEW AS SELECT room_id, datetime(date(check_in_year || '-01-01', '+' || (check_in_month - 1) || ' month', '+' || (check_in_day - 1) || ' day'), '+840 minutes') as check_in,datetime(date(check_out_year || '-01-01', '+' || (check_out_month - 1) || ' month', '+' || (check_out_day - 1) ||' day'), '+600 minutes') as check_out FROM RESERVATION")

RETRIEVE_USER = ('SELECT * FROM USER WHERE username = ?')


class Database:

    def __init__(self, log, config, initialize):
        self.log = log
        self.config = config
        self.connection = sqlite3.connect(str(Path.home()) + self.config['database'])
        # self.connection = sqlite3.connect(self.config['database'])
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
        cursor.execute(ROOM_TABLE_DDL)
        cursor.execute(RESERVATION_TABLE_DDL)
        cursor.execute(RESERVATION_SUMMARY_VIEW)
        cursor.connection.commit()

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
