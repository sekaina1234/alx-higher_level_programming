#!/usr/bin/python3
'''
script that lists all cities from the database
'''

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password,
                db=database)

        cursor = db.cursor()

        cursor.execute(
        'SELECT cities.id, cities.name, states.name FROM cities JOIN states ON\
        cities.state_id = states.id;')

        results = cursor.fetchall()
        for row in results:
            print(row)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)
