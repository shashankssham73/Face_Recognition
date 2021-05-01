import cv2
import numpy as np
import sqlite3
faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
eyeDetect=cv2.CascadeClassifier('haarcascade_eye.xml');
connection = sqlite3.connect("faceDatabase.db") 
def getProfile(id):
    conn=sqlite3.connect("faceDatabase.db")
    cmd="SELECT * FROM emp WHERE id_number="+str(id)
    cursor=conn.execute(cmd)
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile



# cursor  
crsr = connection.cursor() 
# SQL command to create a table in the database 
sql_command = """CREATE TABLE emp (  
id_number INTEGER PRIMARY KEY,  
name VARCHAR(20),  
branch VARCHAR(20));"""
# execute the statement 
crsr.execute(sql_command)
sql_command = """INSERT INTO emp VALUES (1,"Shashank S","Known Person");"""
crsr.execute(sql_command)
# To save the changes in the files. Never skip this.  
# If we skip this, nothing will be saved in the database. 
connection.commit()
# execute the command to fetch all the data from the table emp 
crsr.execute("SELECT * FROM emp")  
# store all the fetched data in the ans variable
profile=getProfile(1)
print str(profile[2])
# close the connection 
connection.close()



        
