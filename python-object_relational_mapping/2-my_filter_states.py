#!/usr/bin/python3
"""
Script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
"""
import sys
import MySQLdb


# Ensures the script runs only if executed directly
if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Retrieve command-line arguments.
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]  # The state name to search for

    # Establish a connection to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query
    query = """
    SELECT * FROM states WHERE name LIKE BINARY'{}' ORDER BY states.id ASC
    """
    query = query.format(state_name)
    cursor.execute(query)

    # Fetch all results from the executed query
    results = cursor.fetchall()

    # Print each row in the result set
    for row in results:
        print(row)

    # Close the cursor after execution
    cursor.close()

    # Close the database connection
    db.close()
