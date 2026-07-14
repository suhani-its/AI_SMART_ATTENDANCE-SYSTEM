# AI Smart Attendance System 🚀

A Face Recognition based Smart Attendance System built using Python, OpenCV, and LBPH algorithm. This system automatically marks attendance using face recognition and stores it in a CSV file.

## 📌 Features
- 🔍 Real-time face detection using Haar Cascade
- 👤 Face recognition using LBPH algorithm  
- 📝 Automatic attendance marking in CSV/Excel
- 📸 Dataset training for new students
- 📊 Screenshots of training process
- 🖥️ Simple GUI for easy use
- 🔄 Data augmentation for better accuracy

## 🛠️ Tech Stack
- **Language**: Python 3.x
- **Libraries**: OpenCV, NumPy, Pandas, PIL
- **Algorithm**: LBPH Face Recognizer
- **Database**: CSV/Excel

## 🚀 How to Run
1. Clone the repository
```bash
git clone https://github.com/suhani-its/AI_SMART_ATTENDANCE-SYSTEM.git
cd AI_SMART_ATTENDANCE-SYSTEM
1.Install requirements
JAVASCRIPT
bash
pip install opencv-contrib-python pillow numpy pandas
2. CAPTURE FACES FOR DATASETS
JAVASCRIPT
bash
python capture_faces.py
3.TRAIN THE MODEL
JAVASCRIPT
bash
python train_model.py
4.RUN ATTENDANCE SYSTEM
JAVASCRIPT
bash
python check_face.py
📸SCREENSHOTS
Training Process
!screenshots/a.47.jpg
🔧 PROJECT STRUCTURE
AI_SMART_ATTENDANCE-SYSTEM/
├── dataset/              # Student face images
├── haarcascade/          # Haar cascade XML files
├── screenshots/          # Project screenshots
├── trainer/              # Trained model file
├── capture_faces.py      # For capturing dataset
├── train_model.py        # For training model
├── check_face.py         # For marking attendance
└── student_detail.csv    # Attendance records
📄 LICENSE
THIS PROJECT IS FOR EDUCATIONAL PURPOSE ONLE.

AUTHOR
SUHANI SINGH
GITHub: https://github.com/suhani-its
