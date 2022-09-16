#!/usr/bin/python3
""" Displays all values in the states table where name matches the argument
    that is safe from MySQL injections """


from sys import argv
import MySQLdb

if __name__ == '__main__':

    db_user = argv[1]
    db_passwd = argv[2]
    db_name = argv[3]
    search = '{}'.format(argv[4])

    database = MySQLdb.connect(host='localhost', port=3306,
                               user=db_user, passwd=db_passwd, db=db_name)

    cursor = database.cursor()

    cursor.execute('SELECT id, name FROM states\
                   WHERE name = %s\
                   ORDER BY states.id ASC;', (search,))

    for row in cursor.fetchall():
        print(row)
