# UAS_openCV-Presensi_Faris


Alur Kerja 
1. Buat folder 'dataset'
dataset/

2. Buat sub-folder per orang
dataset/Faris/
dataset/Wildan/
dataset/Zidan/

3. Masukkan foto wajah
dataset/Faris/0.jpg
dataset/Wildan/94.jpg
dataset/Zidan/3a.jpg

4. Jalankan training
python train_model.py
Program akan:
-membaca semua folder
-mengenali siapa pemilik wajah
-membuat face_model.yml otomatis

5. Jalankan presensi
python presensi.py
Program akan membuka kamera dan mendeteksi wajah.
Jika wajah terdeteksi dan cocok dengan dataset maka → data presensi tercatat dan masuk ke dalam file presensi.csv yang dibuat otomatis oleh program.


🪩##Penjelasan setiap fungsi kode:


import cv2 berfungsi untuk mengimpor library OpenCV yang digunakan untuk pengolahan citra dan video, seperti membuka kamera, mendeteksi wajah, mengubah warna gambar, dan menampilkan jendela kamera.

import os digunakan untuk mengakses fungsi sistem operasi, misalnya untuk mengecek apakah sebuah file sudah ada atau belum.

import csv digunakan untuk membaca dan menulis file dengan format CSV yang nantinya dipakai untuk menyimpan data presensi.

from datetime import datetime digunakan untuk mengambil waktu dan tanggal saat ini ketika presensi dilakukan.

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") berfungsi untuk memuat file Haar Cascade yang digunakan sebagai model pendeteksi wajah berbasis fitur wajah manusia. File XML ini harus tersedia di folder yang sama atau diberi path yang benar.

recognizer = cv2.face.LBPHFaceRecognizer_create() berfungsi untuk membuat objek pengenal wajah menggunakan metode LBPH (Local Binary Pattern Histogram) yang cocok untuk pengenalan wajah.

recognizer.read("face_model.yml") berfungsi untuk memuat model hasil training wajah yang sebelumnya sudah disimpan dalam file `face_model.yml`.

label_map = { 0: "Faris", 1: "Wildan", 2: "Zidan" } berfungsi sebagai pemetaan antara label numerik hasil prediksi model dengan nama asli orang, sehingga angka hasil prediksi dapat diubah menjadi nama manusia.

csv_file = "presensi.csv" berfungsi untuk menentukan nama file CSV yang akan digunakan sebagai tempat penyimpanan data presensi.

if not os.path.exists(csv_file): berfungsi untuk mengecek apakah file presensi tersebut sudah ada atau belum.

with open(csv_file, "w", newline="") as f: berfungsi untuk membuat file CSV baru jika belum ada dan membukanya dalam mode tulis.

writer = csv.writer(f) berfungsi untuk membuat objek penulis CSV.

writer.writerow(["Nama", "Tanggal", "Waktu"]) berfungsi untuk menuliskan header kolom pada file CSV.

cap = cv2.VideoCapture(0) berfungsi untuk membuka kamera utama (webcam) dengan indeks 0.

sudah_hadir = set() berfungsi untuk membuat sebuah set kosong yang digunakan untuk menyimpan nama orang yang sudah tercatat presensi agar tidak tercatat dua kali.

while True: membuat perulangan tak terbatas agar kamera terus aktif sampai dihentikan.

ret, frame = cap.read() berfungsi untuk mengambil satu frame dari kamera, di mana `ret` menandakan keberhasilan pengambilan frame dan `frame` berisi gambar hasil tangkapan kamera.

if not ret: digunakan untuk mengecek jika kamera gagal mengambil frame.
break berfungsi untuk menghentikan perulangan jika frame tidak berhasil diambil.

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) berfungsi untuk mengubah gambar berwarna menjadi grayscale karena proses deteksi dan pengenalan wajah lebih efektif menggunakan citra abu-abu.

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5) berfungsi untuk mendeteksi wajah pada gambar grayscale, di mana `scaleFactor` mengatur skala pencarian wajah dan 'minNeighbors` menentukan tingkat akurasi deteksi.

for (x, y, w, h) in faces: digunakan untuk melakukan perulangan pada setiap wajah yang terdeteksi.

face_img = gray[y:y+h, x:x+w] berfungsi untuk memotong area wajah dari gambar grayscale berdasarkan koordinat hasil deteksi.

label, confidence = recognizer.predict(face_img) berfungsi untuk memprediksi identitas wajah menggunakan model LBPH, di mana `label` adalah ID wajah dan `confidence` menunjukkan tingkat keyakinan prediksi (semakin kecil semakin baik).

if confidence < 80: digunakan untuk menentukan apakah wajah dianggap dikenal berdasarkan nilai confidence.

nama = label_map[label] berfungsi untuk mengubah label numerik menjadi nama sesuai dengan mapping yang sudah dibuat.

if nama not in sudah_hadir: berfungsi untuk mengecek apakah orang tersebut sudah pernah tercatat presensi.

waktu = datetime.now() berfungsi untuk mengambil waktu dan tanggal saat ini.

with open(csv_file, "a", newline="") as f: membuka file CSV dalam mode tambah data.

writer = csv.writer(f) membuat objek penulis CSV.

writer.writerow([ nama, waktu.strftime("%Y-%m-%d"), waktu.strftime("%H:%M:%S") ]) berfungsi untuk menuliskan nama, tanggal, dan waktu ke dalam file presensi.

sudah_hadir.add(nama) berfungsi untuk menandai bahwa orang tersebut sudah hadir.

text = f"{nama}" berfungsi untuk menentukan teks yang akan ditampilkan di layar kamera.

color = (0, 255, 0) berfungsi untuk menentukan warna hijau sebagai tanda wajah dikenal.

else: dijalankan jika wajah tidak dikenali.

text = "Tidak Dikenal" menentukan teks untuk wajah yang tidak dikenal.

color = (0, 0, 255) menentukan warna merah sebagai tanda wajah tidak dikenal.

cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2) berfungsi untuk menggambar kotak di sekitar wajah.

cv2.putText(frame, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2) berfungsi untuk menampilkan teks nama atau status di atas kotak wajah.

cv2.imshow("Presensi Wajah", frame) berfungsi untuk menampilkan hasil video kamera pada sebuah jendela.

if cv2.waitKey(1) & 0xFF == ord('q'): berfungsi untuk mendeteksi jika tombol `q` ditekan.

break menghentikan perulangan saat tombol `q` ditekan.

cap.release() berfungsi untuk melepaskan akses kamera.

cv2.destroyAllWindows() berfungsi untuk menutup semua jendela OpenCV yang terbuka.


