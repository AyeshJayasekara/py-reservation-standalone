from abc import ABC, abstractmethod

from simple_term_menu import TerminalMenu

from core.user.customer import Customer


class CustomerDecorator(Customer, ABC):

    def __init__(self, user: Customer):
        self._customer = user

    def execute(self):
        menu_cursor = "> "
        menu_cursor_style = ("fg_red", "bold")
        menu_style = ("bg_red", "fg_yellow")

        user_menu_title = "  Reservations user.\n  Press E to exit\n"
        user_menu_options = ["[v] View rooms",
                             "[c] Check availability",
                             "[b] Book room",
                             "[s] Show reservations",
                             "[q] Cancel reservation",
                             "[l] Logout"]
        user_menu = TerminalMenu(
            menu_entries=user_menu_options,
            title=user_menu_title,
            menu_cursor=menu_cursor,
            menu_cursor_style=menu_cursor_style,
            menu_highlight_style=menu_style,
            cycle_cursor=True,
            clear_screen=True,
        )

        while (True):
            option = user_menu.show()

            if option == 0:
                self.cli_view_rooms()
            if option == 1:
                self.cli_check_availability()
            if option == 2:
                self.cli_book_room()
            if option == 3:
                self.cli_show_reservations()
            if option == 4:
                self.cli_cancel_res()
            if option == 5:
                return

    @abstractmethod
    def cli_view_rooms(self):
        pass

    def view_rooms(self):
        return self._customer.view_rooms()

    @abstractmethod
    def cli_check_availability(self):
        pass

    def check_availability(self, check_in_year: int, check_in_month: int, check_in_day: int, check_out_year: int,
                           check_out_month: int, check_out_day: int):

        return self._customer.view_available_rooms(check_in_year, check_in_month, check_in_day, check_out_year,
                                                   check_out_month, check_out_day)

    @abstractmethod
    def cli_book_room(self):
        pass

    def book_room(self, room_id: int, check_in_year: int, check_in_month: int, check_in_day: int,
                  check_out_year: int,
                  check_out_month: int, check_out_day: int):
        return self._customer.book_room(room_id, check_in_year, check_in_month, check_in_day, check_out_year,
                                        check_out_month, check_out_day)

    @abstractmethod
    def cli_show_reservations(self):
        pass

    def show_reservations(self):
        return self._customer.show_reservations()

    @abstractmethod
    def cli_cancel_res(self):
        pass

    def cancel_booking(self, booking_id: int):
        return self._customer.cancel_room(booking_id)
    # @abstractmethod
    # def cli_view_bookings(self):
    #     pass
    #
    # def view_bookings(self):
    #     return self._admin.view_bookings()

    # @abstractmethod
    # def cli_delete_booking(self):
    #     pass
    #
    # def delete_booking(self, reservation: Booking):
    #     return self._admin.delete_booking(reservation)
