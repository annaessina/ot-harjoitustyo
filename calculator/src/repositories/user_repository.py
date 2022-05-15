from entities.user import User
from database_connection import get_database_connection


def user_by_row(row):
    return User(row["username"], row["password"]) if row else None


class UserRepository:
    """Database containing data on all users"""

    def __init__(self, connection):
        """Constructor that assignes a path

        Args:
            connection: path
        """
        self._connection = connection

    def create_user(self, user):
        """Creates new user

        Args:
            user (User): User-class object

        Returns:
            "User created": confirmation message
        """
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO Users (username, password) VALUES (?, ?)", [user.username, user.password])
        self._connection.commit()

        return "User created"

    def find_user(self, username):
        """Looks for already existing user

        Args:
            username (str): username

        Returns:
            User: returns user, if it exists and None, if don't
        """
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM Users WHERE username= ?", [username])
        row = cursor.fetchone()

        if row:
            return user_by_row(row)
        return None

    def find_all_users(self):
        """Looks for all users

        Returns:
            list: shoes all existing users in database
        """
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM Users")
        rows = cursor.fetchall()

        return list(map(user_by_row, rows))


    def delete_user(self, username):
        """Deletes user

        Args:
            username (str): username

        Returns:
            text: message that user is deleted from database
        """
        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM Users WHERE username= ?", [username])
    
        cursor.execute("DELETE FROM Records WHERE username= ?", [username])

        return "User deleted"

    def delete_all_users(self):
        """Deletes all users from database"""
        cursor = self._connection

        cursor.execute("DELETE FROM Users")
        
        cursor.execute("DELETE FROM Records")
        self._connection.commit()


user_repository = UserRepository(get_database_connection())
users = user_repository.find_all_users()
