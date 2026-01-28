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
git clone https://github.com/TeguhAldianto/fastprint_test.git
cd fastprint-test

```

### 2. Buat dan Aktifkan Virtual Environment (Opsional tapi Disarankan)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

*(Catatan: Jika file `requirements.txt` belum ada, install manual paket berikut: `django mysqlclient requests djangorestframework`)*

### 4. Konfigurasi Database

1. Buat database kosong di MySQL (misal: `db_fastprint`).
2. Buka file `fastprint_test/settings.py`.
3. Sesuaikan bagian `DATABASES` dengan kredensial MySQL Anda:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_fastprint',
        'USER': 'root',      # Sesuaikan user
        'PASSWORD': '',      # Sesuaikan password
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

```



### 5. Jalankan Migrasi Database

```bash
python manage.py makemigrations
python manage.py migrate

```

---

## 📥 Cara Mengambil Data API (Penting)

Project ini dilengkapi dengan **Custom Management Command** untuk menangani logika otentikasi API yang rumit (Username/Password dinamis berdasarkan Tanggal & Jam).

Jalankan perintah berikut di terminal untuk menarik data dari server FastPrint dan menyimpannya ke database lokal:

```bash
python manage.py get_products

```

**Output yang diharapkan:**

```
Connecting with User: tesprogrammer280126C...
Login Berhasil! Menyimpan data...
Data berhasil disimpan!

```

---

## 🖥️ Menjalankan Aplikasi

Setelah data berhasil ditarik, jalankan server Django:

```bash
python manage.py runserver

```

Buka browser dan akses: **https://www.google.com/search?q=http://127.0.0.1:8000**

## 🧩 Struktur Database

Sesuai instruksi soal, relasi tabel dibuat sebagai berikut:

* **Tabel Produk:** `id_produk`, `nama_produk`, `harga`, `kategori_id` (FK), `status_id` (FK).
* **Tabel Kategori:** `id_kategori`, `nama_kategori`.
* **Tabel Status:** `id_status`, `nama_status`.


## 📝 Catatan Pengembang

* **Logika Username:** Menggunakan format `tesprogrammer` + `ddMMyy` + `C` + `Jam (24h) + 1 jam` (sesuai pola `C19` untuk jam 18:00/19:00).
* **Security:** Password di-hash menggunakan MD5 sesuai instruksi API.
* **Framework:** Saya memilih Django karena skalabilitas dan keamanannya (built-in CSRF protection & SQL Injection prevention).

**Dikembangkan oleh:** Teguh Aldianto

