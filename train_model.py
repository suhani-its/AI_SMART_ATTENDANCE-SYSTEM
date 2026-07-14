import cv2
import numpy as np
import os
from PIL import Image

# Recognizer initialize karo
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Face detector haarcascade load karo
face_detector = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')

def getImagesAndLabels(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg') or f.endswith('.png')]
    faceSamples=[]
    ids = []

    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L')
        img_numpy = np.array(PIL_img,'uint8')

        # Image path se ID extract karo: dataset/1.1.jpg → 1
        id = int(os.path.split(imagePath)[-1].split(".")[0])

        # Face detect karo
        faces = face_detector.detectMultiScale(img_numpy)

        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)

    return faceSamples,ids

# Dataset se faces & ids get karo
faces,ids = getImagesAndLabels('dataset')

# Train karo
recognizer.train(faces, np.array(ids))

# Trainer folder banake trainer.yml save karo
if not os.path.exists('trainer'):
    os.makedirs('trainer')
recognizer.write('trainer/trainer.yml')

print("✅ Training Complete. trainer.yml saved")
