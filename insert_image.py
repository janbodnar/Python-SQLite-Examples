#!/usr/bin/python

import sqlite3
import sys

def readImage():

    fin = None

    try:
        fin = open("sid.jpg", "rb")
        img = fin.read()
        return img

    except IOError as e:

        print(e)
        sys.exit(1)

    finally:

        if fin:
            fin.close()

con = None

try:
    con = sqlite3.connect('ydb.db')

    cur = con.cursor()

    data = readImage()
    binary = sqlite3.Binary(data)
    cur.execute("INSERT INTO images(data) VALUES (?)", (binary,) )

    con.commit()

except sqlite3.Error as e:

    if con:
        con.rollback()

    print(e)
    sys.exit(1)

finally:

    if con:
        con.close()
