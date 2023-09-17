#!/usr/bin/python3
'''
This script retrieves and lists all cities from a MySQL database.
'''

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
        host='localhost')

    c = db.c()
    c.execute(
        'SELECT cities.id, cities.name, states.name FROM cities JOIN states ON\
        cities.state_id = states.id;')

    s = c.fetchall()

    for state in s:
        print(state)
