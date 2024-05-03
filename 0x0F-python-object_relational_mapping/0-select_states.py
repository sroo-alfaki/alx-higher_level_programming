import MySQLdb

def list_states(username, password, database_name):
    # Establish a connection to the MySQL server
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
            )


    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()

    for row in rows:
        state_id = row[0]
        state_name = row[1]
        print("({}, '{}')".format(state_id, state_name))

    cursor.close()
    db.close()
