#!/usr/bin/python

import sqlite3

con = sqlite3.connect('ydb.db')

with con:

    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM cars")

    rows = cur.fetchall()

    for row in rows:
        print(f"{row['id']} {row['name']} {row['price']}")
