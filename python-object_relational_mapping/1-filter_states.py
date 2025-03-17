#!/usr/bin/python3
"""
Write a script that lists all states with a name starting with N from the database
"""
import sys
import mysql.connector

if __name__ == "__main__":
    db = mysql.connector.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in c.fetchall() if state[1][0] == "N"]
