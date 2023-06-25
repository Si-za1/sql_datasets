import psycopg2 
from config import (
    DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USERNAME
)


try:
    connection = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USERNAME,
        password=DB_PASSWORD,
        port=DB_PORT
    )
    cursor = connection.cursor()

    # Execute SQL statements to create tables
    create_sql_file = open("sql\create\create.sql", "r")
    create_sql = create_sql_file.read()
    cursor.execute(create_sql)
    connection.commit()
    print("Tables created successfully!")


    # Execute SQL statements to insert values in tables menu and members
    insert_sql_file = open("sql\insert\insert.sql", "r")
    insert_sql = insert_sql_file.read()
    cursor.execute(insert_sql)
    print("Values inserted successfully!")

    #sales
    create_sql_file = open("sql\insert\sales.sql", "r")
    create_sql = create_sql_file.read()
    cursor.execute(create_sql)

    connection.commit()
    print("Values inserted successfully!")

    #fetch data 
    # Read SQL query from file
    fetch_sql_file = open(r"sql\fetch\fetch.sql", "r")
    fetch_sql = fetch_sql_file.read()
   
    queries = fetch_sql.split(';')

    # Execute each query from the SQL file
    for query in queries:
    # Execute query if it is not empty
        if query.strip():
            cursor.execute(query)
            # Get the query description (the original query)
            query_description = cursor.description
            # Fetch and print the results
            rows = cursor.fetchall()
            # Print the query
            print(f"Answers for each query: ")

            for row in rows:
                print(row)
                print("\n")

    # Perform database operations here
    cursor.close()
    connection.close()

except psycopg2.Error as error:
    print("Error while connecting to PostgreSQL:", error)


