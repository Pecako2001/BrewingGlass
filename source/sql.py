import sqlite3

# Define the database name
dbname = 'data.sqlite'

def createdatabase():
    # Connect to the SQLite database. If the database does not exist, it will be created.
    conn = sqlite3.connect(dbname)

    # Create a cursor object using the cursor() method
    cursor = conn.cursor()

    # Create table as per requirement
    sql = '''
    CREATE TABLE beer_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        brewery TEXT NOT NULL,
        type TEXT NOT NULL,
        amount INTEGER NOT NULL CHECK (amount >= 0)
    )
    '''
    # Execute the SQL command
    cursor.execute(sql)
    # Commit the changes
    conn.commit()
    sql = '''
    CREATE TABLE wish_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        brewery TEXT NOT NULL,
        type TEXT NOT NULL,
        amount INTEGER NOT NULL CHECK (amount >= 0)
    )
    '''
    # Execute the SQL command
    cursor.execute(sql)
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()