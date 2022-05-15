from entities.user import User
from entities.record import Record
from repositories.user_repository import user_repository as default_user_repository
from repositories.record_repository import record_repository as default_record_repository


class UsernameError(Exception):
    pass


class InvalidUsernameOrPasswordError(Exception):
    pass


class CalculatorServices:
    """Class which is responsible for all user's actions"""

    def __init__(
            self,
            user_repository=default_user_repository,
            record_repository=default_record_repository):
        """Constructor creates an instance of class"""

        self._user = None
        self._user_repository = user_repository
        self._record_repository = record_repository

    def login(self, username, password):
        """Responsible for log in process

        Args:
            username (str): name of a user
            password (str): password

        Raises:
            InvalidUsernameOrPasswordError: if username+password is not correct

        Returns:
            User: user
        """
        user = self._user_repository.find_user(username)
        if not user or user.password != password:
            raise InvalidUsernameOrPasswordError(
                "Incorrect username or password")

        self._user = user

        return user

    def create_user(self, username, password):
        """Creates new user

        Args:
            username (str): username
            password (str): password

        Raises:
            UsernameError: username is already in use

        Returns:
            User: user
        """
        existing = self._user_repository.find_user(username)
        if existing:
            raise UsernameError("Username taken")

        user = self._user_repository.create_user(
            User(username, password))
        return user

    def get_current_user(self):
        """Returns already logged in username

        Returns:
            User: user
        """
        return self._user

    def delete_user(self, username):
        """Deletes user

        Args:
            username (str): username
        """
        self._user_repository.delete_user(username)

    def add_record(self, number1, number2, add2, dist, mult, div, username):
        """Creates new record

        Args:
            number1 (float): first entered number
            number2 (float): second entered number
            add2 (float): result of addition
            dist (float): result of distraction
            mult (float): result of multiplication
            div (float): result of division
            username (str): username of current user
        """
        self._record_repository.add_record(Record(number1, number2, add2, dist, mult, div, username))

    def show_all_records(self):
        """Shows all records of current user"""
        username = self.get_current_user().username
        self._purchase_repository.show_all_records(Record(username))


    def delete_all_records(self, username):
        """Deletes all records of current user

        Args:
            username (str): username of current user
        """
        self._purchase_repository.delete_all_records(username)


calculator_services = CalculatorServices()
