from simple_term_menu import TerminalMenu

menu_cursor = "> "
menu_cursor_style = ("fg_red", "bold")
menu_style = ("bg_red", "fg_yellow")
menu_exit = False

login_menu_title = "  Main Menu.\n  Press E to exit\n"
login_menu_options = ["[l] Login", "[r] Register", "[e] Exit"]
login_menu = TerminalMenu(
    menu_entries=login_menu_options,
    title=login_menu_title,
    menu_cursor=menu_cursor,
    menu_cursor_style=menu_cursor_style,
    menu_highlight_style=menu_style,
    cycle_cursor=True,
    clear_screen=True,
)

admin_menu_title = "  Administration View.\n  Press E to exit\n"
admin_menu_options = ["[a] Add a room", "[e] Edit room", "[r] Remove a room", "[v] View rooms", "[s] Show reservations",
                      "[c] Cancel reservation"]
admin_menu = TerminalMenu(
    menu_entries=admin_menu_options,
    title=admin_menu_title,
    menu_cursor=menu_cursor,
    menu_cursor_style=menu_cursor_style,
    menu_highlight_style=menu_style,
    cycle_cursor=True,
    clear_screen=True,
)

user_menu_title = "  Reservations user.\n  Press E to exit\n"
user_menu_options = ["[s] Show rooms", "[b] Book room", "[c] Check availability", "[v] View rooms",
                     "[s] Show reservations", "[e] Exit"]
user_menu = TerminalMenu(
    menu_entries=user_menu_options,
    title=user_menu_title,
    menu_cursor=menu_cursor,
    menu_cursor_style=menu_cursor_style,
    menu_highlight_style=menu_style,
    cycle_cursor=True,
    clear_screen=True,
)

login_fail_menu_title = "  Logon Failed!.\n  Press E to exit\n"
login_fail_options = ["[l] Try again", "[e] Exit"]
login_fail_menu = TerminalMenu(
    menu_entries=login_fail_options,
    title=login_fail_menu_title,
    menu_cursor=menu_cursor,
    menu_cursor_style=menu_cursor_style,
    menu_highlight_style=menu_style,
    cycle_cursor=True,
    clear_screen=True,
)


def show_login_menu() -> int:
    return login_menu.show()


def show_admin_menu() -> int:
    return admin_menu.show()


def show_user_menu() -> int:
    return user_menu.show()

def show_login_fail_menu() -> int:
    return login_fail_menu.show()
