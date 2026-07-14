import cv2
import os

# Haarcascade file ka path
face_detector = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')

# Camera on karo
cam = cv2.VideoCapture(0)

# Yaha ID aur Name puchega
student_id = input('Enter Student ID: ')
student_name = input('Enter Student Name: ')

# Agar dataset folder nahi hai to bana do
if not os.path.exists('dataset'):
    os.makedirs('dataset')

count = 0
print("Camera on ho gaya... 50 photo leni hai. Band karne ke liye Q dabao")

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        count += 1
        
        # Photo save hogi: 1.Aarav.1.jpg is tarah
        cv2.imwrite("dataset/" + str(student_id) + "." + student_name + "." + str(count) + ".jpg", gray[y:y+h,x:x+w])
        
        cv2.putText(img, str(count), (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    
    cv2.imshow('Face Capture', img)
    
    # 50 photo ho jaye ya Q daba do to band
    if cv2.waitKey(1) == ord('q') or count >= 50:
        break

cam.release()
cv2.destroyAllWindows()
print(f"Kaam ho gaya! Total {count} Photos Captured in dataset folder")