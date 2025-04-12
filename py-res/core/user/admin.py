from config import Database
from core.reservation.booking import Booking
from core.reservation.room import Room
from core.user.user import User


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



