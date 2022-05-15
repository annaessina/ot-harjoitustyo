from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS Users;")
    cursor.execute("DROP TABLE IF EXISTS Records;")
    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute(
        "CREATE TABLE Users (username TEXT PRIMARY KEY, password TEXT);")
    
    cursor.execute(
        "CREATE TABLE Records (id SERIAL PRIMARY KEY, number1 DOUBLE, number2 DOUBLE, add2 DOUBLE, dist DOUBLE, mult DOUBLE, div DOUBLE, username TEXT);")

    connection.commit()


def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
