import psycopg2
from config import (
    DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USERNAME
)

class Connection:
    def __init__(self):
        self.db_connection = None
        self.db_cursor = None

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        try:
            self.db_connection = psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USERNAME,
                password=DB_PASSWORD,
                port=DB_PORT
            )
            self.db_cursor = self.db_connection.cursor()
            print("Connection established successfully")

        except psycopg2.Error as error:
            print("Error while connecting to Postgres:", error)

    def create_sql_from_file(self, filename):
        try:
            with open(filename, "r") as create_sql_file:
                create_sql = create_sql_file.read()
                self.db_cursor.execute(create_sql)
                self.db_connection.commit()
                print("Tables created successfully!")

        except FileNotFoundError:
            print(f"'{filename}' is not found")

    def insert_sql_from_file(self, filename):
        try:
            with open(filename, "r") as insert_sql_file:
                insert_sql = insert_sql_file.read()
                self.db_cursor.execute(insert_sql)
                self.db_connection.commit()
                print("Values inserted successfully!")
        except FileNotFoundError:
            print(f"'{filename}' was not found")
        except psycopg2.Error as error:
            print("Error executing SQL query:", error)

    def fetch_data_from_file(self, filename):
        try:
            with open(filename, "r") as fetch_sql_file:
                fetch_sql = fetch_sql_file.read()
                queries = fetch_sql.split(';')

                for query in queries:
                    # Execute query if it is not empty
                    if query.strip():
                        cursor = self.db_connection.cursor()  # Get the cursor
                        try:
                            cursor.execute(query)  # Execute the query
                            # Print the query
                            print("Answers for each query:")
                            for row in cursor:
                                print(row)
                                print("\n")
                        except psycopg2.Error as error:
                            print("Error executing SQL query:", error)
        except FileNotFoundError:
            print(f"SQL file '{filename}' not found.")


    def disconnect(self):
        if self.db_cursor:
            self.db_cursor.close()
        if self.db_connection:
            self.db_connection.close()
        print("Disconnected from Postgres")
