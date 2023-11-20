from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        has_digits = any(char.isdigit() for char in password)
        special_symbols="!@#$%^*()-_=+[];:'\",.></?"
        has_special_symbol = any(char in special_symbols for char in password)
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        if len(username) < 3:
            raise UserInputError("Username too short")
        
        if password != password_confirmation:
            raise UserInputError("Nonmatching Password And Password Confirmation")
        
        if len(password) < 8 or not (has_digits or has_special_symbol):
            raise UserInputError("Invalid Password")



user_service = UserService()
