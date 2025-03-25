import menu

class Admin:

    def __init__(self):
        option_selected = menu.show_admin_menu()

        while option_selected != 5:
            if option_selected == 1:
                menu.show_admin_menu()
