import sys

from PyInquirer import prompt
from validator_collection import validators

import menu
from cli.user.cli_admin import DecoratedCliAdmin
from cli.user.cli_customer import DecoratedCliCustomer
from core.user import password
from core.user.admin import Admin
from core.user.customer import Customer
from core.user.user import User
from core.user.user_factory import UserFactory


class Cli:
    def __init__(self, parameters, database):
        self.parameters = parameters
        self.database = database
        self.option_selected = 0

        while self.option_selected == 0:
            self.option_selected = menu.show_login_menu()

            if self.option_selected == 0:
                self.perform_login()

            if self.option_selected == 1:
                self.perform_register()

            if self.option_selected == 2:
                self.perform_exit()

            self.option_selected = 0

    def perform_login(self) -> None:

        while True:
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

            response = User.login(answers['username'], answers['password'], self.database)

            if not response["login"]:
                prompt_answer = menu.show_login_fail_menu()
                if prompt_answer == 0:
                    continue
                else:
                    return None
            else:
                logged_user = UserFactory.create_user(response["type"], response["username"], self.database)

                if isinstance(logged_user, Admin):
                    DecoratedCliAdmin(logged_user).execute()
                else:

                    DecoratedCliCustomer(logged_user).execute()

            break

    def perform_register(self) -> None:
        questions = [
            {
                'type': 'input',
                'name': 'username',
                'message': 'Username:',
                'validate': self.existing_user
            },
            {
                'type': 'password',
                'name': 'password',
                'message': 'Password:',
                'validate': self.valid_password,
            },
            {
                'type': 'input',
                'name': 'email',
                'message': 'Email:',
                'validate': self.validate_email,
            }

        ]
        answers = prompt(questions)
        User.register(self.database, answers['username'], answers['password'], answers['email'])

    @staticmethod
    def perform_exit():
        sys.exit()

    @staticmethod
    def validate_email(email):
        try:
            validators.email(email)
            return True
        except Exception as e:
            return "Please enter a valid email address"

    @staticmethod
    def valid_password(passwd):

        response = password.check_password(passwd)

        if response is not True:
            return " AND ".join(response)
        else:
            return True

    def existing_user(self, username):
        if User.has_user(self.database, username):
            return "Existing user with that username already exists!"
        else:
            return True
