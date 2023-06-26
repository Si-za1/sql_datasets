import psycopg2
from config import (
    DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USERNAME
)

class Connection:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USERNAME,
                password=DB_PASSWORD,
                port=DB_PORT
            )
            self.cursor = self.connection.cursor()
            print("Connection established successfully")

        except psycopg2.Error as error:
            print("Error while connecting to Postgres:", error)

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Disconnected from the Postgres")
