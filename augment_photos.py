import cv2
import os
import numpy as np

# Settings
student_id = "1"
student_name = "Aarav"
input_photo = "photos/aarav.jpg"  # is photo ko photos folder me rakho

if not os.path.exists('dataset'):
    os.makedirs('dataset')
if not os.path.exists('photos'):
    os.makedirs('photos')

img = cv2.imread(input_photo)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_detector = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
faces = face_detector.detectMultiScale(gray, 1.3, 5)

count = 0
for (x,y,w,h) in faces:
    face = gray[y:y+h, x:x+w]
    
    # 15 tarah ki photo banayenge
    for angle in [-20, -10, 0, 10, 20]:
        for brightness in [40, 0, -40]: # dark, normal, bright
            rotated = cv2.getRotationMatrix2D((w//2,h//2), angle, 1.0)
            rotated_face = cv2.warpAffine(face, rotated, (w,h))
            bright_face = cv2.convertScaleAbs(rotated_face, alpha=1, beta=brightness)
            
            count += 1
            cv2.imwrite(f"dataset/{student_id}.{student_name}.{count}.jpg", bright_face)
            if count >= 15: break
        if count >= 15: break

print(f"Ho gaya! 1 photo se {count} photo bana di dataset me")