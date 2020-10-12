#!/usr/bin/python

import sqlite3
import sys


def writeImage(data):

    fout = None

    try:
        fout = open('sid2.jpg','wb')
        fout.write(data)

    except IOError as e:

        print(e)
        sys.exit(1)

    finally:

        if fout:
            fout.close()

con = None

try:
    con = sqlite3.connect('ydb.db')

    cur = con.cursor()
    cur.execute("SELECT data FROM images LIMIT 1")
    data = cur.fetchone()[0]

    writeImage(data)


except sqlite3.Error as e:

    print(e)
    sys.exit(1)

finally:

    if con:
        con.close()
