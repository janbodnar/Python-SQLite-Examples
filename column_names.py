#!/usr/bin/python

import sqlite3

con = sqlite3.connect('ydb.db')

with con:

    cur = con.cursor()

    cur.execute('PRAGMA table_info(cars)')

    data = cur.fetchall()

    for d in data:
        print(f"{d[0]} {d[1]} {d[2]}")
