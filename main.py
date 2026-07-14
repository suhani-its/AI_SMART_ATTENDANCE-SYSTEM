import cv2
import numpy as np
import pandas as pd
import os

# Face detector & recognizer load karo
face_detector = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')

# Attendance file setup
if not os.path.exists('attendance.csv'):
    df = pd.DataFrame(columns=['Name', 'Time'])
    df.to_csv('attendance.csv', index=False)

# Webcam on karo
cam = cv2.VideoCapture(0)

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        if confidence < 70:
            # Attendance mark karo
            name = str(id)  # Agar tumne dataset me 1.jpg, 2.jpg rakha hai
            df = pd.read_csv('attendance.csv')
            if name not in df['Name'].values:
                import datetime
                now = datetime.datetime.now()
                df.loc[len(df)] = [name, now.strftime("%H:%M:%S")]
                df.to_csv('attendance.csv', index=False)
                print(f"✅ Attendance marked for {name}")
        else:
            name = "Unknown"

        cv2.putText(img, name, (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), 2)

    cv2.imshow('Face', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()