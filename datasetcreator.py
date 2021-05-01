import cv2
import numpy as np
import sqlite3
faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
eyeDetect=cv2.CascadeClassifier('haarcascade_eye.xml');
a="Known Person"
def insertOrUpdate(Id,Name):
    conn=sqlite3.connect("faceDatabase.db")
    crsr = conn.cursor() 
    crsr.execute("SELECT rowid FROM emp WHERE id_number = ?", (Id,))
    data=crsr.fetchone()
    if data==None:
        isRecordExist=0
    else:
        isRecordExist=1
    cmd="SELECT * FROM emp"
    cursor=conn.execute(cmd)
    if(isRecordExist==1):
        conn.execute("UPDATE emp SET name=? WHERE id_number =? ;",(Name,Id))
        conn.execute("UPDATE emp SET branch=? WHERE id_number=?",(a,Id))
        conn.commit()
    else:
        conn.execute("INSERT INTO emp Values(?,?,?)",(Id,Name,a))
        conn.commit()
    conn.commit()
    conn.close()
        
cam=cv2.VideoCapture(0);
ID=input('enter user id')
name=raw_input("enter the name")
insertOrUpdate(ID,name)

sampleNum=0;
while(True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    eye=eyeDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        sampleNum=sampleNum+1;
        cv2.imwrite("dataSet/User."+str(ID)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.waitKey(100);
    for(x,y,w,h) in eye:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("Face",img);
    if(sampleNum>100):
       break;
cam.release()
cv2.destroyAllWindows()
