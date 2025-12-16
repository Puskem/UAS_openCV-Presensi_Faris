import cv2
import os
import csv
from datetime import datetime

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Load model pengenal wajah
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("face_model.yml")

# Mapping label ke nama
label_map = {
    0: "Faris",
    1: "Wildan",
    2: "Zidan"
}

# File presensi
csv_file = "presensi.csv"

# Cek apakah file presensi sudah ada
if not os.path.exists(csv_file):
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Nama", "Tanggal", "Waktu"])

cap = cv2.VideoCapture(0)
sudah_hadir = set()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.2, minNeighbors=5
    )

    for (x, y, w, h) in faces:
        face_img = gray[y:y+h, x:x+w]

        label, confidence = recognizer.predict(face_img)

        if confidence < 80:
            nama = label_map[label]

            if nama not in sudah_hadir:
                waktu = datetime.now()
                with open(csv_file, "a", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow([
                        nama,
                        waktu.strftime("%Y-%m-%d"),
                        waktu.strftime("%H:%M:%S")
                    ])
                sudah_hadir.add(nama)

            text = f"{nama}"
            color = (0, 255, 0)
        else:
            text = "Tidak Dikenal"
            color = (0, 0, 255)

        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(frame, text, (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    cv2.imshow("Presensi Wajah", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
