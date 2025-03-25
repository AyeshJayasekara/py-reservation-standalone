from validator_collection import validators, checkers, errors
from PyInquirer import prompt
import menu
from cli.user import User
from cli.admin import Admin
from config import Database
from cli import password





class Register:

    def __init__(self, database: Database):
        self.database = database
        self.questions = [
            {
                'type': 'input',
                'name': 'username',
                'message': 'Username:',
                'validate': self.existing_user,
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
        answers = prompt(self.questions)


        self.create_login(answers)


    def create_login(self, answers):
        return self.database.add_new_user(answers['username'], answers['password'], 'USER', answers['email'])

    def validate_email(self, email):
        try:
            validators.email(email)
            return True
        except Exception as e:
            return "Please enter a valid email address"

    def existing_user(self, username):
        if self.database.has_user(username):
            return "Existing user with that username already exists!"
        else:
            return True

    def valid_password(self, passwd):

        response = password.check_password(passwd)

        if response is not True:
            return " AND ".join(response)
        else:
            return True


