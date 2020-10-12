#!/usr/bin/python

import sqlite3

uId = 1
uPrice = 62300

con = sqlite3.connect('ydb.db')

with con:

    cur = con.cursor()
    cur.execute("UPDATE cars SET price=? WHERE id=?", (uPrice, uId))

    print(f"Number of rows updated: {cur.rowcount}")
