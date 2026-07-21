import sqlite3

DATABASE = "gps_tracker.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def save_location(latitude, longitude):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO locations (latitude, longitude)
        VALUES (?, ?)
        """,
        (latitude, longitude),
    )

    connection.commit()
    connection.close()


def get_latest_location():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM locations
        ORDER BY id DESC
        LIMIT 1
        """
    )

    row = cursor.fetchone()

    connection.close()

    return row


def get_all_locations():
    connection = get_connection()
    cursor = connection.cursor()    
  

    cursor.execute(
        """
        SELECT *
        FROM locations
        ORDER BY id DESC
        """
    )

    rows = cursor.fetchall()

    connection.close()

    return rows
def delete_location(location_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM locations
        WHERE id = ?
        """,
        (location_id,),
    )

    connection.commit()
    connection.close()


def delete_all_locations():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM locations
        """
    )

    connection.commit()
    connection.close()
