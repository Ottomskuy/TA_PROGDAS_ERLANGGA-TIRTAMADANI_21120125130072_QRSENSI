# QRSENSI : Absensi dengan Memanfaatkan QR CODE

Deskripsi Singkat
-----------------
Aplikasi GUI berbasis Python yang menggunakan kode QR sebagai sarana presensi yang cepat, ringkas, dan mudah. Pengguna Login menggunakan Username dan Password sendiri. 
Aplikasi dapat men-generate kode QR yang berisi Nama dan NIM. Pengguna dapat presensi hanya dengan menyodorkan kode QR mereka sendiri ke dalam kamera yang menjadi salah satu fitur aplikasi

Tools
-----------------
• **VS Code** — IDE utama untuk pengembangan kode Python & integrasi modul.  
• **Python Library** — `tkinter`, `os`, `qrcode`, `csv`, `cmv2` , `PIL` , 

Struktur Proyek
---------------
```bash
Tugas Akhir/\
├─ app.py                
├─ absensi.py         
├─ users.py                
├─ qrcode_generator.py                 
├─ qrcode_scanner.py   
├─ data_absensi.csv
├─ users.csv                
└─ README.md                
```

Fitur Utama
-----------
1. Registrasi Pengguna
2. Generate QR Code
3. Scan QR Code
4. GUI Interaktif

Cara Menjalankan Aplikasi
-------------------------
1. Clone Repository
2. Instal Dependencies  
```bash
pip install opencv-python qrcode pillow              
```
3. Jalanan Program

Alur Penggunaan
---------------
1. User mendaftar (username, password, NIM, nama)
2. Login ke aplikasi
3. Pilih:
- Generate QR → simpan QR identitas
- Absensi → arahkan QR ke kamera
4. Sistem akan membaca QR dan mencatat kehadiran ke file CSV

Pengembang 
----------
Erlangga Tirtamadani — 21120125130072
Universitas Diponegoro
Mata Kuliah: Pemrograman Dasar