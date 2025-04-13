from abc import ABC, abstractmethod

from typing_extensions import override

from core.reservation.booking import Booking
from core.reservation.room import Room
from core.user.admin import Admin

from simple_term_menu import TerminalMenu

class AdminDecorator(Admin, ABC):

    def __init__(self, user: Admin):
        self._admin = user

    def execute(self):
        menu_cursor = "> "
        menu_cursor_style = ("fg_red", "bold")
        menu_style = ("bg_red", "fg_yellow")
        admin_menu_title = "  Administration View.\n  Press E to exit\n"
        admin_menu_options = ["[a] Add a room",
                              "[e] Edit room",
                              "[r] Remove a room",
                              "[v] View rooms",
                              "[s] Show reservations",
                              "[c] Cancel reservation",
                              "[x] Sync database",
                              "[l] Logout"]
        admin_menu = TerminalMenu(
            menu_entries=admin_menu_options,
            title=admin_menu_title,
            menu_cursor=menu_cursor,
            menu_cursor_style=menu_cursor_style,
            menu_highlight_style=menu_style,
            cycle_cursor=True,
            clear_screen=True,
        )

        while (True):
            option = admin_menu.show()

            if option == 0:
                self.cli_add_room()
            if option == 1:
                self.cli_edit_room()
            if option == 2:
                self.cli_remove_room()
            if option == 3:
                self.cli_view_rooms()
            if option == 4:
                self.cli_view_bookings()
            if option == 5:
                self.cli_delete_booking()
            if option == 6:
                self.cli_sync_database()
            if option == 7:
                return



    @abstractmethod
    def cli_add_room(self):
        pass

    @override
    def add_room(self, room: Room) -> None:
        return self._admin.add_room(room)

    @abstractmethod
    def cli_remove_room(self):
        pass

    def remove_room(self, room: Room):
        self._admin.remove_room(room)

    @abstractmethod
    def cli_edit_room(self):
        pass

    def edit_room(self, room: Room):
        self._admin.edit_room(room)

    @abstractmethod
    def cli_view_rooms(self):
        pass

    def view_rooms(self):
        return self._admin.view_rooms()

    @abstractmethod
    def cli_view_bookings(self):
        pass

    def view_bookings(self):
        return self._admin.view_bookings()

    @abstractmethod
    def cli_delete_booking(self):
        pass

    def delete_booking(self, reservation: Booking):
        return self._admin.delete_booking(reservation)

    def cli_sync_database(self):
        return self.sync_database()

    def sync_database(self):
        return self._admin.sync_database()