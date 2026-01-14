<div align="center">

# 🥗 COOKING TIME: ULTIMATE ELEGANCE

<img src="assets/image/background_game.png" alt="Cooking Time Banner" width="100%" style="border-radius: 10px; box-shadow: 0px 0px 20px rgba(255,192,203,0.5);">

<br><br>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Engine-Pygame-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Genre](https://img.shields.io/badge/Genre-Casual_Simulation-pink?style=for-the-badge)

<br>

**"Potong, Sajikan, Nikmati!"**
<br>
Mini-game simulasi memotong sayuran dengan mekanik *Drag-to-Cut* yang memuaskan dan visual yang sangat estetik.

[View Features](#-key-features) • [Technical Review](#-technical-retrospective) • [Installation](#-installation)

</div>

---

## 🥗 About The Game

**Cooking Time!** bukan sekedar game memasak biasa. Proyek ini bereksperimen dengan **Mouse Gesture Recognition** untuk mensimulasikan gerakan pisau dapur. Pemain harus "menggeser" mouse seolah sedang mengiris sayuran di atas talenan.

Fokus utama pengembangan game ini adalah pada **"Juicy" Game Feel** — memberikan kepuasan visual dan audio maksimal pada setiap interaksi pemain, mulai dari potongan sayur yang terbang hingga efek kilauan cahaya.

---

## ✨ Key Features

### 🔪 Drag-to-Cut Mechanic
Lupakan tombol klik biasa! Gunakan gerakan geser (*drag*) mouse untuk memotong sayuran. Sistem akan mendeteksi:
* **Panjang Geseran:** Harus cukup panjang agar terhitung sebagai potongan valid.
* **Arah Potongan:** Mendeteksi potongan horizontal yang realistis.

### 🌟 High-Fidelity Visuals
* **Particle System:** Efek kilauan (*sparkles*) di menu dan *sunbeams* (sinar matahari) yang dinamis di dapur.
* **Flying Animations:** Potongan sayur tidak langsung muncul di mangkok, tapi "terbang" melengkung (*parabolic arc*) dari talenan ke mangkok secara mulus.
* **Feedback Text:** Teks "NICE!" atau "OOPS!" yang muncul dan memudar (*fade-out*) memberikan respon instan pada aksi pemain.

### 🥒 Multiple Ingredients
Beralih otomatis antara Timun dan Terong setelah jumlah potongan terpenuhi, memberikan variasi visual dan tantangan.

---

## 🧐 Technical Retrospective

*Analisis teknis mendalam mengenai struktur kode game ini.*

### ✅ Kelebihan (Strengths)
1.  **Vector Mathematics:** Penggunaan `math.hypot` dan `math.atan2` untuk menghitung jarak dan sudut potongan pisau, serta `clipline` untuk mendeteksi apakah garis potongan melewati sayuran.
2.  **Interpolation Logic:** Animasi potongan sayur terbang menggunakan *Linear Interpolation (Lerp)* yang dikombinasikan dengan rotasi dinamis, menghasilkan gerakan yang terlihat alami.
3.  **Alpha Blending:** Penggunaan `pygame.Surface` dengan `SRCALPHA` secara ekstensif untuk membuat efek bayangan, sinar matahari transparan, dan UI panel yang elegan.

### ⚠️ Kekurangan (Areas for Improvement)
1.  **Bounding Box Hitbox:** Deteksi potongan masih menggunakan kotak (`rect`). *Next update: Implementasi "Pixel Perfect Collision" atau Polygon Collider agar bentuk sayur yang tidak kotak terdeteksi lebih akurat.*
2.  **Limited Gameplay Loop:** Saat ini game hanya berulang (looping) tanpa kondisi kalah atau level yang bertingkat. *Next update: Tambahkan sistem Order/Pesanan dengan batas waktu.*
3.  **Hardcoded Positions:** Posisi mangkok dan talenan dikunci pada koordinat piksel tertentu. *Next update: Gunakan sistem Anchor Layout agar elemen UI tetap proporsional di berbagai ukuran layar.*

---

## 🛠️ Tools Used

* **Language:** Python 3.10+
* **Library:** Pygame
* **Concept:** Mouse Gesture & Particle System
* **Art Style:** Soft Pastel & Kawaii Aesthetic

---

## 🕹 Controls

| Input | Aksi |
| :---: | :--- |
| **Tahan Klik Kiri + Geser** | Memotong Sayuran (Seperti mengiris pisau) |
| **Klik Kiri** | Navigasi Menu |

---

## 💻 Installation

1.  **Clone Repository**
    ```bash
    git clone [https://github.com/kyyyyykyyy/cooking-time.git](https://github.com/kyyyyykyyy/cooking-time.git)
    ```

2.  **Masuk ke Folder**
    ```bash
    cd cooking-time
    ```

3.  **Install Pygame**
    ```bash
    pip install pygame
    ```

4.  **Mulai Memasak!**
    ```bash
    python main.py
    ```

---

<div align="center">
  
  ### 👨‍💻 Developed by **Muhamad Adzky Maulana**
  
  <a href="https://github.com/kyyyyykyyy">
    <img src="https://img.shields.io/badge/GitHub-kyyyyykyyy-181717?style=for-the-badge&logo=github" alt="GitHub">
  </a>
  
  <p>Aceh, Indonesia</p>
  
  
</div>
