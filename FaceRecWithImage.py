import numpy as np
import cv2
import os
from PIL import Image
import pickle
import sqlite3

recognizer=cv2.createLBPHFaceRecognizer()
recognizer.load('recognizer/trainingData.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def getProfile(id):
    conn=sqlite3.connect("StudentDataBase.db")
    cmd="SELECT * FROM StudentDetails WHERE ID="+str(Id)
    cursor=conn.execute(cmd)
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile

imgname=raw_input('Enter the image name');
im = cv2.imread(imgname)
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(gray, 1.3, 5)
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        if(Id==76):
            Id="Shreeshma"
            cv2.cv.PutText(cv2.cv.fromarray(im),str(Id),(x,y+h),font, 255)
        elif(Id==81):
            Id="Varalakshmi"
            cv2.cv.PutText(cv2.cv.fromarray(im),str(Id),(x,y+h),font, 255)
        else:
            Id="Unknown"
            cv2.cv.PutText(cv2.cv.fromarray(im),str(Id),(x,y+h),font, 255)
cv2.imshow('im',im)
cv2.waitKey(0)
cv2.destroyAllWindows()

