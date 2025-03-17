#!/usr/bin/python3
"""
Write a script that lists all states from the database
"""
 
import MySQLdb
import sys
 
 
def states(username, userPassword, database_name):
     """
     Connects to a MySQL database and executes a query to retrieve all states.
     """
 
     db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=userPassword,
                         db=database_name)
 
     cur = db.cursor()
 
     cur.execute("SELECT * FROM states ORDER BY states.id")

     rows = cur.fetchall()

     for row in rows:
         print(row)

     cur.close()

     db.close()


if __name__ == "__main__":

     user = sys.argv[1]
     passw = sys.argv[2]
     bd = sys.argv[3]
 
     states(user, passw, bd)
