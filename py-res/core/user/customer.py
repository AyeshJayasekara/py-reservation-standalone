from datetime import datetime

from config import Database
from core.user.user import User



class Customer(User):

    def __init__(self, database: Database, username: str):
        super().__init__(database, username)

    def view_available_rooms(self):
        pass

    def book_room(self, room_id: int, check_in: datetime.date, check_out: datetime.date):
        pass

    def cancel_room(self, booking_id: int):
        pass


