#!/usr/bin/python

import sqlite3


def readData():

    f = open('cars.sql', 'r')

    with f:

        data = f.read()

        return data


con = sqlite3.connect(':memory:')

with con:

    cur = con.cursor()

    sql = readData()
    cur.executescript(sql)

    cur.execute("SELECT * FROM cars")

    rows = cur.fetchall()

    for row in rows:
        print(row)
