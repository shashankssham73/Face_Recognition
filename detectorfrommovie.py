import cv2
import numpy as np
import sqlite3
import os
import glob
img_dir = "/face recognition/xyz" # Enter Directory of all images 
data_path = os.path.join(img_dir,'*g')
files = glob.glob(data_path)

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
rec=cv2.face.LBPHFaceRecognizer_create()
rec.read("recognizer\\trainingData.yml")
sampleNum=42;

for f1 in files:
    img = cv2.imread(f1,0)
    gray = cv2.imread(f1,0)
    #gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        sampleNum=sampleNum+1;
        cv2.imwrite("xyz/User."+"1."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv2.destroyAllWindows()
