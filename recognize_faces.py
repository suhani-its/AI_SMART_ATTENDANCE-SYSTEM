import cv2
import pandas as pd
import os
from datetime import datetime

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
faceCascade = cv2.CascadeClassifier("haarcascade/haarcascade_frontalface_default.xml")

df = pd.read_csv('student_detail.csv')
names = ['None'] + df['StudentName'].tolist()

if not os.path.exists('Attendance'):
    os.makedirs('Attendance')

cam = cv2.VideoCapture(0)
print("Camera On! \n 'S' dabao = Photo + Attendance Save \n 'ESC' dabao = Band")

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.2, 5)
    
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        
        if confidence < 80: # 80 se kam ho to hi naam manega
            name = names[id]
            conf = f" {round(100-confidence)}%"
        else:
            name = "unknown"
            conf = " "
        
        cv2.putText(img, name, (x+5,y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
        cv2.putText(img, conf, (x+5,y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 1)
    
    cv2.imshow('Face Attendance', img)
    
    k = cv2.waitKey(10) & 0xff
    
    # 'S' dabao to attendance save hogi
    if k == ord('s'):
        for(x,y,w,h) in faces:
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
            if confidence < 80:
                name = names[id]
                time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open('Attendance/attendance.csv', 'a') as f:
                    f.write(f"\n{name},{id},{time_now}")
                print(f"Attendance Marked: {name} at {time_now}")
    
    # ESC dabao to band
    if k == 27:
        break

cam.release()
cv2.destroyAllWindows()