# 🌈 BOOKFINDER – FINAL PROJECT PRAKTIK APLIKASI WEB

<p align="center">
  <img src="https://img.shields.io/badge/BookFinder-FINAL%20PROJECT-blueviolet?style=for-the-badge&logo=bookstack&logoColor=white"/>
  <img src="https://img.shields.io/badge/FLASK-Framework-black?style=for-the-badge&logo=flask"/>
  <img src="https://img.shields.io/badge/NLP-NLTK-green?style=for-the-badge&logo=apache-spark"/>
  <img src="https://img.shields.io/badge/Dashboard-Chart.js-orange?style=for-the-badge&logo=chartdotjs"/>
  <img src="https://img.shields.io/badge/Deployment-Render.com-blue?style=for-the-badge&logo=render"/>
</p>

<p align="center">
  <img src="https://i.ibb.co/Sdtd0Sx/banner-gradient-bookfinder.png" width="900"/>
</p>

---

## ✨ Deskripsi Proyek

BookFinder adalah aplikasi web untuk mencari buku, melakukan crawling Wikipedia, melakukan analisis NLP, membuat dashboard visual, serta otomatisasi data cuaca. Proyek ini dibangun untuk memenuhi Final Project mata kuliah Praktik Aplikasi Web.


BookFinder adalah aplikasi web modern yang menggabungkan:

🔍 Pencarian buku menggunakan Google Books API

🌐 Crawling otomatis dari Wikipedia

🧠 NLP processing (tokenizing, stopwords, sentiment analysis)

⭐ Dashboard interaktif menggunakan Chart.js

🎨 Dark/Light Mode Premium

🤖 Otomasi data (CSV & Wordcloud PNG)

Semua fitur tersebut dikemas dalam UI elegan, responsif, dan profesional.

🎯 Fitur Utama
🔍 1. Pencarian Buku

Mengambil data realtime dari Google Books API

Menampilkan cover, judul, penulis, rating, link detail

🌐 2. Crawling Wikipedia

Mengambil ringkasan otomatis

Bisa diaktifkan melalui checkbox

🧠 3. NLP (Natural Language Processing)

Menggunakan NLTK:

Tokenizing

Stopword removal

Stemming

Sentiment Analysis (VADER)

Word Frequency

📊 4. Dashboard Premium

Dilengkapi grafik:

Bar Chart (frekuensi kata)

Pie Chart (rating buku)

Wordcloud

Sentiment Summary

⚙️ 5. Otomasi

Hasil otomatis disimpan ke:

static/outputs/
 ├── otomasi.csv
 ├── grafik_otomasi.png
 └── wordcloud.png

🖼 Preview UI (Ganti dengan screenshot punyamu nanti)
⭐ Home Page
<p align="center"> <img src="https://i.ibb.co/ZHnfgqk/homemock.png" width="700"> </p>
⭐ Dashboard Analisis
<p align="center"> <img src="https://i.ibb.co/r6x9xTj/dashboardmock.png" width="700"> </p>
🗂 Struktur Proyek
BookFinder-FinalProject
│── app.py
│── otomasi.py
│── Procfile
│── requirements.txt
│
├── templates/
│     ├── index.html
│     ├── dashboard.html
│     └── about.html
│
└── static/
      ├── style.css
      └── outputs/

🛠 Cara Menjalankan
1. Install library:
pip install -r requirements.txt

2. Jalankan server:
python app.py

3. Buka browser:
http://127.0.0.1:5000

🧰 Teknologi yang Digunakan
Teknologi	Keterangan
Python	Backend utama
Flask	Routing & server
Google Books API	Pencarian Buku
BeautifulSoup	Web Crawling
NLTK	NLP
Chart.js	Dashboard
Matplotlib / Wordcloud	Gambar otomatis
Render / Heroku / Railway	Deployment
👨‍💻 Developer
Muhammad Damar Zaky Al-Ayyubi

⭐ Teknologi Informasi — Universitas Negeri Yogyakarta
⭐ NIM: 23051130033

⭐ Dukung Project Ini!

Klik ⭐ Star di GitHub untuk membantu tampil lebih profesional 🙌
