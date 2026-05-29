import cv2
import face_recognition
import os
import pandas as pd

# --------------------
# STEP 1: Load dataset
# --------------------
dataset_path = "dataset"

known_encodings = []
known_names = []

for file in os.listdir(dataset_path):
    if not file.lower().endswith(('.jpg', '.jpeg', '.png')):
        continue
    img = face_recognition.load_image_file(os.path.join(dataset_path, file))
    encodings = face_recognition.face_encodings(img)
    if len(encodings) > 0:
        known_encodings.append(encodings[0])
        known_names.append(file.split("_")[0])

# Attendance dictionary
attendance = {name: "Absent" for name in known_names}

# --------------------
# STEP 2: Connect Mobile/IP Webcam
# --------------------
video_url ="http://10.24.161.81:8080/video"  # Replace with your phone IP + /video
cap = cv2.VideoCapture(video_url)

if not cap.isOpened():
    print("❌Please open your IP webcam")
    exit()

# --------------------
# STEP 3: Live Attendance Loop
# --------------------
while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        print("❌data is not coming from IP webcam")
        continue

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect all faces
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            index = matches.index(True)
            name = known_names[index]
            attendance[name] = "Present"

        # Draw rectangle & label
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # Show frame
    cv2.imshow("Live Attendance", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# --------------------
# STEP 4: Save Attendance CSV
# --------------------
df = pd.DataFrame(list(attendance.items()), columns=["Name"  , "Status"])
df.index += 1
df.to_csv("attendance.csv", index=False)
print("✅ Attendance Saved")
print(df)
cap.release()
cv2.destroyAllWindows()