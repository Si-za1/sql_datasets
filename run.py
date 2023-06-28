from database.connection import Connection

def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return ""

# Creating an instance of Connection
with Connection() as connection:
    # Connecting to the database
    # This step is handled automatically when using the context manager
    
    # Read the SQL files
    create_tables_sql = read_file("sql\create\create.sql")
    insert_values_sql = read_file("sql\insert\insert.sql")
    insert_values1_sql= read_file("sql\insert\sales.sql")
    fetch_data_sql = read_file("sql/fetch/fetch.sql")
    
    # Create tables
    if create_tables_sql:
        connection.execute_query(create_tables_sql)
    
    # Insert values
    if insert_values_sql:
        connection.execute_query(insert_values_sql)
        connection.execute_query(insert_values1_sql)
    
    # Fetch data
    if fetch_data_sql:
        connection.fetch_data(fetch_data_sql)
    
# Disconnect from the database
# This step is handled automatically when exiting the context manager
