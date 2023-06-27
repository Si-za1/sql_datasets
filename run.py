from database.connection import Connection

def read_file():
    # Implement your code to read the file here
    pass

# Creating an instance of Connection
with Connection() as datab_connection:
    # Connecting to the database
    # This step is handled automatically when using the context manager
    
    # Create SQL
    datab_connection.create_sql_from_file("sql\create\create.sql")
    
    # Insert values
    datab_connection.insert_sql_from_file("sql/insert/insert.sql")
    datab_connection.insert_sql_from_file("sql/insert/sales.sql")
    
    # Fetch data
    datab_connection.fetch_data_from_file("sql/fetch/fetch.sql")
    
# Disconnect from the database
# This step is handled automatically when exiting the context manager
