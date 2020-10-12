#!/usr/bin/python

import sqlite3

con = sqlite3.connect('ydb.db')

with con:

    cur = con.cursor()
    cur.execute('SELECT * FROM cars')

    col_names = [cn[0] for cn in cur.description]

    rows = cur.fetchall()

    print(f"{col_names[0]:3} {col_names[1]:10} {col_names[2]:7}")

    for row in rows:
        print(f"{row[0]:<3} {row[1]:<10} {row[2]:7}")
