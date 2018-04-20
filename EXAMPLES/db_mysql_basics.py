#!/usr/bin/env python

from contextlib import closing
import pymysql

with closing(
        pymysql.connect(
        host="localhost",
        db="python2",
        user="scripts",
        passwd="scripts"
    )
) as myconn:
    mycursor = myconn.cursor()

    # select first name, last name from all presidents
    row_count = mycursor.execute('''
        select fname, lname
        from presidents
    ''')

    print("{} rows in result set\n".format(row_count))

    for row in mycursor.fetchall():
        print(row)
        print(' '.join(row))
    print()
