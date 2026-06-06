##Live Attendance System Using Face Recognition

->A Python-based smart attendance management system that uses Face Recognition technology to automatically mark student attendance in real time.

->The system allows student registration, live face detection, automatic attendance marking, CSV report generation, and attendance viewing through a Flask web dashboard. Overview

->Traditional attendance systems require manual effort and are prone to errors. This project automates the attendance process using computer vision and facial recognition.

->The system captures student face images during registration, stores them in a dataset, and later recognizes them through a live camera feed. Once recognized, attendance is

automatically marked and saved.

##Features

1.Student Registration using GUI

2.Live Camera Preview

3.Face Capture and Storage

4.Duplicate Registration Detection

5. Real-Time Face Recognition

6. Automatic Attendance Marking

7. Attendance Report Generation

8. CSV-Based Data Storage

9. Flask Web Dashboard

10. Easy-to-Use Interface

###Technologies Used
Python

OpenCV

Face Recognition

Tkinter

Flask

Pandas

Pillow (PIL)

pip install -r requirements.txt

Requirements
opencv-python
face-recognition
pandas
flask
pillow
numpy


Usage
1. Register Students

Run:

python Face_Registration.py

##Registration Process
i) Enter Student Name
ii) Enter Phone Number
iii) Click Capture & Save
iv) Face image is stored inside the dataset folder

**Duplicate Protection

If the student is already registered, the system will show:

Already Registered

and prevent duplicate entries.

2. Start Live Attendance

Before running attendance, update the IP Webcam URL:

video_url = "camera ip camera/video"

Run:

• python live_attendance.py
• What Happens?
• Loads all registered faces
• Starts camera feed
• Detects faces in real time
• Matches faces with dataset
• Marks attendance automatically
• Displays names on screen

Press:

Q

to stop attendance.

3. Attendance Generation

After closing the attendance window:

attendance.csv

is automatically generated.

Example:

Name  ,  Status
Avinash, Present
Rahul,   Absent
Priya,   Present

4. Open Attendance Dashboard

Run:

python app.py

Open browser:

http://127.0.0.1:5000

The attendance data will be displayed on a web page.

## System Workflow
Student Registration

          │
          ▼

          
Face Image Stored

          │
          ▼

          
Load Dataset

          │
          ▼

          
Start Camera Feed

          │
          ▼

          
Detect Face

          │
          ▼
          
          

          
Recognize Face

          │
          ▼


          
Mark Attendance

          │
          ▼


Save CSV File

          │
          ▼

          
Display on Flask Dashboard
## Screenshots
Student Registration Window

(Add Screenshot Here)

Live Attendance Recognition

(Add Screenshot Here)

Attendance Dashboard

(Add Screenshot Here)

## Future Enhancements
• Attendance Date and Time Tracking
• Database Integration (MySQL)
• Admin Login System
• Cloud Storage Support
• Face Recognition Accuracy Improvement
• Multi-Camera Support
• Attendance Analytics Dashboard
• Export Attendance to Excel/PDF
• Student Management Portal

##Learning Outcomes

This project demonstrates:

• Computer Vision
• Face Recognition
• GUI Development using Tkinter
• Flask Web Development
• CSV Data Handling
• Real-Time Camera Processing
• Python Project Development

### Author

Avinash kumar Ray

GitHub: https://github.com/kumarrayavinash452-debug

### License

This project is created for educational and learning purposes.

