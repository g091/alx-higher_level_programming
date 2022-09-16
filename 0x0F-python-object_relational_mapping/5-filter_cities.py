#!/usr/bin/python3
""" Takes in the name of a state as an argument & lists
    all cities of that state, using the database hbtn_0e_4_usa """


from sys import argv
import MySQLdb

if __name__ == '__main__':

    db_user = argv[1]
    db_passwd = argv[2]
    db_name = argv[3]
    user_state = argv[4]

    database = MySQLdb.connect(host='localhost', port=3306,
                               user=db_user, passwd=db_passwd, db=db_name)

    cursor = database.cursor()

    cursor.execute('SELECT cities.name FROM cities\
                   JOIN states\
                   ON cities.state_id = states.id\
                   WHERE states.name = %s\
                   ORDER BY states.id ASC', (user_state,))
    result = []
    print(', '.join([value[0] for value in cursor.fetchall()]))
