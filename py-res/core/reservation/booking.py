from core.reservation.room import Room


class Booking:

    def __init__(self, res_id, username, room_id, check_in_year, check_in_month, check_in_day, check_out_year, check_out_month, check_out_day):
        self.res_id = res_id
        self.username = username
        self.room_id = room_id
        self.check_in_year = check_in_year
        self.check_in_month = check_in_month
        self.check_in_day = check_in_day
        self.check_out_year = check_out_year
        self.check_out_month = check_out_month
        self.check_out_day = check_out_day