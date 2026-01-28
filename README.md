# FastPrint Junior Programmer Test - Django Implementation

Repository ini berisi solusi teknis untuk Tes Junior Programmer FastPrint. Aplikasi ini dibangun menggunakan **Django Framework** dan **MySQL**, mencakup integrasi API eksternal dengan otentikasi dinamis, manajemen database, dan fitur CRUD (Create, Read, Update, Delete).

## 📋 Fitur Utama

Sesuai dengan kebutuhan tes, aplikasi ini memiliki kemampuan:
* **Integrasi API Dinamis:** Script otomatis untuk mengambil data dari API FastPrint dengan algoritma otentikasi (Username & Password) yang berubah sesuai waktu server.
* **Filter Otomatis:** Menampilkan data produk yang hanya memiliki status "bisa dijual".
* **CRUD System:** Fitur Tambah, Edit, dan Hapus produk.
* **Validasi Data:** Validasi input menggunakan Django Forms dan Serializer (memastikan harga angka & nama terisi).
* **Konfirmasi Keamanan:** Alert konfirmasi JavaScript saat menghapus data.
* **Tech Stack Modern:** Menggunakan Django ORM untuk relasi tabel (Produk, Kategori, Status).

## 🛠️ Teknologi yang Digunakan

* **Backend:** Python 3.10+, Django 5.x
* **Database:** MySQL
* **Frontend:** HTML5, Bootstrap 5
* **Libraries:** `requests` (API Call), `mysqlclient` (DB Driver), `djangorestframework` (Serializer Support)

## ⚙️ Prasyarat (Prerequisites)

Sebelum menjalankan aplikasi, pastikan Anda telah menginstal:
1.  **Python** (versi 3.8 ke atas)
2.  **MySQL Server** (bisa menggunakan Laragon/XAMPP)
3.  **Git**

## 🚀 Panduan Instalasi (Step-by-Step)

Ikuti langkah-langkah berikut untuk menjalankan project di local environment Anda:

### 1. Clone Repository
```bash
git clone [https://github.com/username-anda/fastprint-test.git](https://github.com/username-anda/fastprint-test.git)
cd fastprint-test
