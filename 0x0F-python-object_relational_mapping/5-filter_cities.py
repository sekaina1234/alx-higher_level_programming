#!/usr/bin/python3
'''
script that takes in the name of a state as an argument and lists all cities
'''

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

 cursor = db.cursor()
    cursor.execute(
        'SELECT cities.name FROM cities\
        INNER JOIN states ON cities.state_id = states.id\
        WHERE states.name = %s \
        ORDER BY cities.id ASC', (sys.argv[4], ))

    cities = cursor.fetchall()

    idx = 0
    for city in cities:
        if idx != 0:
            print(", ", end="")
        print("%s" % city, end="")
        idx += 1
    print("")

    cursor.close()
    db.close()
