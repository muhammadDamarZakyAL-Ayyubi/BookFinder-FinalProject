# 🌈 BOOKFINDER – FINAL PROJECT PRAKTIK APLIKASI WEB

<p align="center">
  <img src="https://img.shields.io/badge/BookFinder-FINAL%20PROJECT-blueviolet?style=for-the-badge&logo=bookstack&logoColor=white"/>
  <img src="https://img.shields.io/badge/FLASK-Framework-black?style=for-the-badge&logo=flask"/>
  <img src="https://img.shields.io/badge/NLP-NLTK-green?style=for-the-badge&logo=apache-spark"/>
  <img src="https://img.shields.io/badge/Dashboard-Chart.js-orange?style=for-the-badge&logo=chartdotjs"/>
  <img src="https://img.shields.io/badge/Deployment-Render.com-blue?style=for-the-badge&logo=render"/>
</p>

---

## ✨ Deskripsi Proyek

BookFinder adalah aplikasi web yang menggabungkan pencarian buku, crawling Wikipedia, analisis NLP, dashboard visual, dan otomatisasi data dalam satu platform modern. Proyek ini dibuat untuk memenuhi Final Project mata kuliah **Praktik Aplikasi Web**.

Aplikasi ini memudahkan pengguna untuk:

- 🔍 Mencari buku berdasarkan kata kunci  
- 🌐 Mengambil ringkasan dari Wikipedia  
- 🧠 Melakukan analisis teks (NLP)  
- 📊 Menampilkan dashboard data  
- 🤖 Menyimpan hasil otomatis ke CSV/PNG  

---

## 🎯 Fitur Utama

### 🔍 1. Pencarian Buku
✔ Mengambil data dari **Google Books API**  
✔ Menampilkan cover, judul, penulis, rating, dan link detail  

### 🌐 2. Crawling Wikipedia
✔ Mengambil ringkasan otomatis  
✔ Bisa diaktifkan lewat checkbox “Tambahkan Crawling”  

### 🧠 3. NLP (Natural Language Processing)
Menggunakan **NLTK** untuk:  
- Tokenizing  
- Stopword removal  
- Stemming  
- Word frequency  
- Sentiment Analysis (VADER)  

### 📊 4. Dashboard Premium
✔ Bar chart (Frekuensi kata)  
✔ Pie chart (Distribusi rating)  
✔ Wordcloud  
✔ Sentiment summary  

### ⚙️ 5. Otomasi Data
Semua output otomatis tersimpan di:

static/outputs/
├── otomasi_.csv
├── otomasi_.png
└── wordcloud_dashboard.png

yaml
Salin kode

---

## 🖼 Preview UI (Opsional)
Kamu bisa mengganti screenshot sesuai hasilmu nanti:

⭐ Home Page
⭐ Dashboard Analisis

yaml
Salin kode

---

## 🗂 Struktur Proyek

BookFinder-FinalProject
│── app.py
│── otomasi.py
│── Procfile
│── requirements.txt
│
├── templates/
│ ├── index.html
│ ├── dashboard.html
│ └── about.html
│
└── static/
├── style.css
└── outputs/

yaml
Salin kode

---

## 🛠 Cara Menjalankan

1. Install library:
pip install -r requirements.txt

markdown
Salin kode

2. Jalankan server:
python app.py

markdown
Salin kode

3. Buka di browser:
http://127.0.0.1:5000

yaml
Salin kode

---

## 🧰 Teknologi yang Digunakan

| Teknologi | Keterangan |
|----------|------------|
| Python | Backend utama |
| Flask | Routing & server |
| Google Books API | Pencarian buku |
| BeautifulSoup | Crawling Wikipedia |
| NLTK | NLP Processing |
| Chart.js | Dashboard grafik |
| Matplotlib / Wordcloud | Visualisasi otomatis |
| Render / Railway | Deployment |

---

## 👨‍💻 Developer
**Muhammad Damar Zaky Al-Ayyubi**  
Program Studi **Teknologi Informasi**  
Universitas Negeri Yogyakarta  
**NIM: 23051130033**

---

## ⭐ Dukung Project Ini
Klik ⭐ **Star** di GitHub untuk meningkatkan nilai profesional proyek ini 🙌
