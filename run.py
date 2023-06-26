#importing all the files and classes needed 
import psycopg2
from database.connection import Connection
from database.create import CreateTable
from database.insert import InsertValue
from database.fetch import FetchData


# Creating an instance of PostgreSQLConnection
db_connection = Connection()
#connecting the connection with the database
db_connection.connect()

#now for the create table
table_create=CreateTable()
table_create.create_sql_from_file("sql/create/create.sql")

#now for inserting the values
value_inserter = InsertValue()
value_inserter.insert_sql_from_file("sql/insert/insert.sql")
value_inserter.insert_sql_from_file("sql/insert/sales.sql")

#now for fetching the values
data_fetch= FetchData()
data_fetch.fetch_data_from_file("sql/fetch/fetch.sql")

# Disconnect from the PostgreSQL database
db_connection.disconnect()