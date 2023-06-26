from database.connection import psycopg2, Connection

class FetchData:
    def __init__(self):
        self.connection = Connection()
        # self.cursor = self.connection.cursor()
        self.connection.connect()

    def fetch_data_from_file(self, filename):
            try:
                fetch_sql_file = open(filename, "r")
                fetch_sql = fetch_sql_file.read()
                queries = fetch_sql.split(';')

                for query in queries:
                    # Execute query if it is not empty
                    if query.strip():
                        cursor = self.connection.cursor  # Get the cursor
                        cursor.execute(query)  # Execute the query
                        # Print the query
                        print("Answers for each query:")
                        for row in cursor:
                            print(row)
                            print("\n")
            except FileNotFoundError:
                print(f"SQL file '{filename}' not found.")
            
            except psycopg2.Error as error:
                print("Error while connecting to Postgres:", error)

            def disconnect(self):
                self.connection.disconnect()