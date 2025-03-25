import menu

class User:

    def __init__(self, database):
        option_selected = menu.show_user_menu()

        while option_selected != 5:
            if option_selected == 1:
                # do somthining
                print("test")
