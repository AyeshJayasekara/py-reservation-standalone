from validator_collection import validators, checkers, errors
from PyInquirer import prompt
import menu
from cli.user import User
from cli.admin import Admin
from config import Database

def is_password_valid(password: str):
     return "Invalid password"


class Login:


    def __init__(self, database: Database):
        self.database = database

        questions = [
            {
                'type': 'input',
                'name': 'username',
                'message': 'Username:',
            },
            {
                'type': 'password',
                'name': 'password',
                'message': 'Password:'
            }
        ]
        answers = prompt(questions)

        login = self.check_login(answers)

        while login is None:
            selected_option = menu.show_login_fail_menu()

            if selected_option == 1:
                menu.show_login_menu()

            answers = prompt(questions)
            login = self.check_login(answers)

        if login == 'USER':
            User(database)
        else:
            Admin()

    def check_login(self, answers):
        return self.database.validate_user(answers['username'], answers['password'])




