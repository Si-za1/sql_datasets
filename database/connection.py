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

    @staticmethod
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

    def execute_query(self, query):
        try:
            self.db_cursor.execute(query)
            self.db_connection.commit()
            print("Query executed successfully!")
        except psycopg2.Error as error:
            print("Error executing SQL query:", error)

    def fetch_data(self, query):
        try:
            self.db_cursor.execute(query)
            rows = self.db_cursor.fetchall()
            return rows
        except psycopg2.Error as error:
            print("Error executing SQL query:", error)
            return []
    
    @staticmethod
    def disconnect(self):
        if self.db_cursor:
            self.db_cursor.close()
        if self.db_connection:
            self.db_connection.close()
        print("Disconnected from Postgres")





# def create_tables(connection, filename):
#     sql = read_file(filename)
#     if sql:
#         connection.execute_query(sql)


# def insert_values(connection, filename):
#     sql = read_file(filename)
#     if sql:
#         connection.execute_query(sql)


# def execute_queries(connection, filename):
#     sql = read_file(filename)
#     if sql:
#         queries = sql.split(';')
#         try:
#             for query in queries:
#                 if query.strip():
#                     connection.execute_query(query)
#             print("All queries executed successfully!")
#         except psycopg2.Error as error:
#             connection.db_connection.rollback()  # Roll back the transaction
#             print("Error executing SQL query:", error)


# def fetch_data(connection, filename):
#     sql = read_file(filename)
#     if sql:
#         queries = sql.split(';')
#         for query in queries:
#             if query.strip():
#                 rows = connection.fetch_data(query)
#                 print("Answers for each query:")
#                 for row in rows:
#                     print(row)
#                     print("\n")



