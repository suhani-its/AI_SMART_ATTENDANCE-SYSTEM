import cv2
import os

face_detector = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
folder = 'photos' # yaha se photo lega
output = 'dataset' # yaha save karega

if not os.path.exists(output):
    os.makedirs(output)

count = 1
for file in os.listdir(folder):
    if file.endswith('.jpg') or file.endswith('.png'):
        img = cv2.imread(os.path.join(folder, file))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            face = gray[y:y+h, x:x+w]
            cv2.imwrite(f"{output}/1.Aarav.{count}.jpg", face)
            count += 1
print(f"Total {count-1} photo crop ho gayi")