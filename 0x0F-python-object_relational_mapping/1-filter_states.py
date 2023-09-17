#!/usr/bin/python3
#!/usr/bin/python3
'''
lists all states with a name starting with N
'''

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database_name)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    db.close()
