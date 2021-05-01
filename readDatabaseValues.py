import cv2
import numpy as np
import sqlite3
connection = sqlite3.connect("faceDatabase.db") 
def getProfile():
    conn=sqlite3.connect("faceDatabase.db")
    cmd="SELECT * FROM emp"
    cursor=conn.execute(cmd)
    for row in cursor:
        print "ID = ", row[0]
        print "NAME = ", row[1]
        print "ADDRESS = ", row[2], "\n"
    conn.close()


# cursor  
crsr = connection.cursor() 
# execute the command to fetch all the data from the table emp 
crsr.execute("SELECT * FROM emp")  
# store all the fetched data in the ans variable
getProfile()
# close the connection 
connection.close()
