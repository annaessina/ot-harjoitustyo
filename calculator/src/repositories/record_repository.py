from entities.user import User
from entities.record import Record
from database_connection import get_database_connection


class RecordRepository:
    """Class which is responsible for records database"""

    def __init__(self, connection):
        """Constructor which assigns a path to database

        Args:
            connection: path
        """
        self._connection = connection

    def show_all_records(self, username):
        """Shows all records for current user

        Args:
            username (str): username

        Returns:
            records: returns all records for current user
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT number1, number2, add2, dist, mult, div, username FROM Records WHERE username= ?",
            [username])
        rows = cursor.fetchall()

        records = []
        for row in rows:
            records.append((row["number1"], row["number2"], row["add2"], row["dist"], row["mult"], row["div"]))

        return records

    def add_record(self, record):
        """Adds record to database

        Args:
            purchase (Purchase): Record-class object

        Returns:
            "Record added" : message that record is added
        """
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO Records (number1, number2, add2, dist, mult, div, username) VALUES (?, ?, ?, ?, ?, ?, ?)", [
                       record.number1, record.number2, record.add2, record.dist, record.mult, record.div, record.username])

        self._connection.commit()

        return "Record added"

    def delete_all_records(self, username):
        """Deletes all records for current user

        Args:
            username (str): username

        Returns:
            "All records deleted": message that all records are deleted
        """
        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM Records WHERE username= ?", [username])
        self._connection.commit()

        return "All records deleted"

    def delete_all_records_from_all_users(self):
        """Deletes all records for all users"""
        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM Records")
        self._connection.commit()


record_repository = RecordRepository(get_database_connection())
