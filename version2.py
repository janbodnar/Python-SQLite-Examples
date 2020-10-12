#!/usr/bin/python

import sqlite3

con = sqlite3.connect('ydb.db')

with con:

    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')

    data = cur.fetchone()[0]

    print(f"SQLite version: {data}")
