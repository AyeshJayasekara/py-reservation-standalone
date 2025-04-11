from config import Database
from core.reservation.room import Room
from core.user.user import User


class Admin(User):


    def __init__(self, database: Database, username: str):
        super().__init__(database, username)

    def add_room(self, room: Room):
        pass

    def remove_room(self, room: Room):
        pass

    def edit_room(self, room: Room):
        pass

    def view_bookings(self):
        pass

    def delete_booking(self, room: Room):
        pass