from abc import ABC, abstractmethod

from typing_extensions import override

from config import Database
from core.user.admin import Admin
from core.user.customer import Customer
from core.user.user import User


class UserFactory(ABC):


    def __init__(self, db: Database):
        self.database = db

    @staticmethod
    def create_user(user_type="USER", username= None, database: Database = None) -> User:

        user_type_map = {
            "USER": CustomerFactory(database),
            "ADMIN": AdminFactory(database),
        }

        return user_type_map[user_type].initialize_user(username)


    @abstractmethod
    def initialize_user(self, username: str) -> User:
        pass


class CustomerFactory(UserFactory):

    def __init__(self, database: Database = None):
        super().__init__(database)

    @override
    def initialize_user(self, username: str) -> User:
        return Customer(self.database, username)

class AdminFactory(UserFactory):

    def __init__(self, database: Database = None):
        super().__init__(database)

    @override
    def initialize_user(self, username: str) -> User:
        return Admin(self.database , username)