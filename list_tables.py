#!/usr/bin/python

import sqlite3

con = sqlite3.connect('ydb.db')

with con:

    cur = con.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")

    rows = cur.fetchall()

    for row in rows:
        print(row[0])
