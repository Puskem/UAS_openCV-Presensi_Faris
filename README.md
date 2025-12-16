# UAS_openCV-Presensi_Faris


#Struktur file 
presensi_opencv/
│
├── dataset/
│   ├── Faris/
│   │   ├── 0.jpg
│   │   ├── 3.jpg
│   ├── Wildan/
│   │   ├── 94.jpg
│   │   ├── e.jpg
├── haarcascade_frontalface_default.xml
├── train_model.py
├── presensi.py


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


