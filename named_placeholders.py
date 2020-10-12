#!/usr/bin/python

import sqlite3

uId = 4

con = sqlite3.connect('ydb.db')

with con:

    cur = con.cursor()
    cur.execute("SELECT name, price FROM cars WHERE Id=:Id", {"Id": uId})

    row = cur.fetchone()
    print(f"{row[0]}, {row[1]}")
