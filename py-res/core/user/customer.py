from datetime import datetime

from config import Database
from core.user.user import User


class Customer(User):

    def __init__(self, database: Database, username: str):
        super().__init__(database, username)

    def view_rooms(self):
        FETCH_ROOMS = ('SELECT * FROM ROOM')
        self.database.cursor.execute(FETCH_ROOMS)
        records = self.database.cursor.fetchall().copy()
        return records

    def view_available_rooms(self, check_in_year: int, check_in_month: int, check_in_day: int, check_out_year: int,
                             check_out_month: int, check_out_day: int):
        AVALABLE_ROOMS = "SELECT * FROM ROOM WHERE room_id NOT IN (SELECT res_sum.room_id FROM RESERVATION_SUMMARY_VIEW as res_sum WHERE datetime(date(? || '-01-01', '+' || (? - 1) || ' month', '+' || (? - 1) || ' day'),'+841 minutes') BETWEEN res_sum.check_in AND res_sum.check_out) AND room_id NOT IN (SELECT res_sum.room_id FROM RESERVATION_SUMMARY_VIEW as res_sum WHERE datetime(date(? || '-01-01', '+' || (? - 1) || ' month', '+' || (? - 1) || ' day'), '+841 minutes') BETWEEN res_sum.check_in AND res_sum.check_out)"

        self.database.cursor.execute(AVALABLE_ROOMS, (
            check_in_year, check_in_month, check_in_day, check_out_year, check_out_month, check_out_day))

        records = self.database.cursor.fetchall().copy()
        return records

    def book_room(self, room_id: int, check_in_year: int, check_in_month: int, check_in_day: int,
                  check_out_year: int,
                  check_out_month: int, check_out_day: int):
        BOOK_ROOM = (
            'INSERT INTO RESERVATION (username, room_id, check_in_year, check_in_month, check_in_day, check_out_year, check_out_month, check_out_day) VALUES (?,?,?,?,?,?,?,?)')

        self.database.cursor.execute(BOOK_ROOM, (self.username, room_id,
                                                 check_in_year, check_in_month, check_in_day, check_out_year,
                                                 check_out_month, check_out_day))

        self.database.cursor.connection.commit()

    def show_reservations(self):
        FETCH_RES = 'SELECT res.res_id, r.room_type,r.price,res.check_in_year,res.check_in_month,res.check_in_day,res.check_out_year,res.check_out_month,res.check_out_day FROM RESERVATION as res INNER JOIN main.ROOM r on res.room_id = r.room_id WHERE res.username = ?'
        self.database.cursor.execute(FETCH_RES, (self.username,))
        records = self.database.cursor.fetchall().copy()
        return records

    def cancel_room(self, booking_id: int):
        CANCEL_RES = ('DELETE FROM RESERVATION WHERE res_id = ?')
        self.database.cursor.execute(CANCEL_RES, (booking_id,))
        self.database.connection.commit()

