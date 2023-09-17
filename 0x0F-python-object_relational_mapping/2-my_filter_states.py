#!/usr/bin/python3
""" takes in an argument
    and displays all values
    in the states table of
    hbtn_0e_0_usa where name matches the argument
     Usage: ./2-my_filter_states.py <mysql username>
                                    <mysql password>
                                    <database name>
                                    <state name searched>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database_name)

    cursor = db.cursor()

    query = """SELECT * FROM states
                WHERE name LIKE BINARY '{}'
                ORDER BY states.id ASC""".format(sys.argv[4]).strip("'")

    cursor.execute(query, (state_name,))

    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    db.close()
