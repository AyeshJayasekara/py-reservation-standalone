from config import Database
from core.reservation.booking import Booking
from core.reservation.room import Room
from core.user.user import User
import pandas as pd
import os
import openpyxl


class Admin(User):

    def __init__(self, database: Database, username: str):
        super().__init__(database, username)

    def add_room(self, room: Room):

        RETRIEVE_ROOM = ('SELECT * FROM ROOM WHERE room_id = ?')
        self.database.cursor.execute(RETRIEVE_ROOM, (room.room_id,))
        record = self.database.cursor.fetchone()

        if record is None:
            self.database.cursor.execute('INSERT INTO ROOM(room_id, room_type, price) VALUES (?, ?, ?)', (
                room.room_id, room.room_type, room.price))

            self.database.cursor.connection.commit()
            return True
        else:
            return False

    def edit_room(self, room: Room):

        RETRIEVE_ROOM = ('SELECT * FROM ROOM WHERE room_id = ?')
        self.database.cursor.execute(RETRIEVE_ROOM, (room.room_id,))
        record = self.database.cursor.fetchone()

        if record is None:
            return False
        else:
            UPDATE_ROOM = ('UPDATE ROOM SET room_type = ?, price = ? WHERE room_id = ?')
            self.database.cursor.execute(UPDATE_ROOM, (room.room_type, room.price, room.room_id))
            self.database.cursor.connection.commit()
            return True

    def remove_room(self, room: Room):
        RETRIEVE_ROOM = ('SELECT * FROM ROOM WHERE room_id = ?')
        self.database.cursor.execute(RETRIEVE_ROOM, (room.room_id,))
        record = self.database.cursor.fetchone()
        if record is None:
            return False
        else:
            DELETE_ROOM = ('DELETE FROM ROOM WHERE room_id = ?')
            self.database.cursor.execute(DELETE_ROOM, (room.room_id,))
            self.database.cursor.connection.commit()
            return True


    def view_rooms(self):
        FETCH_ROOMS = ('SELECT * FROM ROOM')
        self.database.cursor.execute(FETCH_ROOMS)
        records = self.database.cursor.fetchall().copy()
        return records

    def view_bookings(self):
        FETCH_RESERVATIONS = ("SELECT res.res_id, "
                              "res.room_id,"
                              "u.email,"
                              "r.room_type,"
                              "r.price,"
                              "concat(res.check_in_year, '-', res.check_in_month, '-', res.check_in_day) as check_in,"
                              "concat(res.check_out_year, '-', res.check_out_month, '-', res.check_out_day) as check_out "
                              "FROM RESERVATION as res "
                              "INNER JOIN main.USER u on res.username = u.username "
                              "INNER JOIN ROOM r on res.room_id = r.room_id")
        self.database.cursor.execute(FETCH_RESERVATIONS)
        records = self.database.cursor.fetchall().copy()
        return records

    def delete_booking(self, reservation: Booking):
        RETRIEVE_RES = ('SELECT * FROM RESERVATION WHERE res_id = ?')
        self.database.cursor.execute(RETRIEVE_RES, (reservation.res_id,))
        record = self.database.cursor.fetchone()
        if record is None:
            return False
        else:
            DELETE_RES = ('DELETE FROM RESERVATION WHERE res_id = ?')
            self.database.cursor.execute(DELETE_RES, (reservation.res_id,))
            self.database.cursor.connection.commit()
            return True

    def sync_database(self):
        user_records = pd.read_sql("SELECT row_number() over (ORDER BY created_date) as 'Row' , username 'User Name', password as 'Password', user_type as 'User Type', email as 'Email', created_date as 'Created Date' FROM USER", self.database.connection)
        room_records = pd.read_sql("SELECT row_number() over (ORDER BY room_id) as 'Row', room_id as 'Room ID', room_type as 'Room Type', price as 'Price Per Night' FROM ROOM", self.database.connection)
        reservation_records = pd.read_sql("SELECT row_number() over (ORDER BY res_id) as 'Row' , res.res_id as 'Reservation ID', res.room_id as 'Room ID', u.email as 'Customer Email', r.room_type as 'Room Type', r.price as 'Price Per Night', concat(res.check_in_year, '-', res.check_in_month, '-', res.check_in_day) as 'Check In', concat(res.check_out_year, '-', res.check_out_month, '-', res.check_out_day) as 'Check Out' FROM RESERVATION as res INNER JOIN main.USER u on res.username = u.username INNER JOIN ROOM r on res.room_id = r.room_id", self.database.connection)
        res_summary_records = pd.read_sql("Select r.room_id as 'Room ID', check_in as 'Check In', check_out as 'Check Out' , Cast (( JulianDay(check_out) - JulianDay(check_in)) As Integer) + 1 as 'Number of Nights' , r.price * (Cast (( JulianDay(check_out) - JulianDay(check_in)) As Integer) + 1) as 'Estimated Charge' FROM RESERVATION_SUMMARY_VIEW INNER JOIN main.ROOM R on RESERVATION_SUMMARY_VIEW.room_id = R.room_id", self.database.connection)

        with pd.ExcelWriter(os.getcwd() + '/data/database.xlsx') as writer1:
            user_records.to_excel(writer1, sheet_name='Users')
            room_records.to_excel(writer1, sheet_name='Rooms')

        with pd.ExcelWriter(os.getcwd() + '/data/reservations.xlsx') as writer2:
            reservation_records.to_excel(writer2, sheet_name='Reservations')
            res_summary_records.to_excel(writer2, sheet_name='Reservations Summary')





