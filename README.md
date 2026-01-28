# Tes Junior Programmer – FastPrint

**Django & MySQL Implementation**

Repository ini berisi hasil pengerjaan **Tes Junior Programmer FastPrint** menggunakan **Django Framework** dan **MySQL**, dengan integrasi API eksternal FastPrint serta fitur CRUD dan validasi data.

---

## Fitur Utama

* Integrasi API FastPrint dengan **autentikasi dinamis**
* Penyimpanan data produk ke database
* Menampilkan produk dengan status **“bisa dijual”**
* Fitur **Tambah, Edit, Hapus** produk
* Validasi form (nama wajib, harga numerik)
* Konfirmasi hapus menggunakan JavaScript `confirm()`
* Relasi database menggunakan Django ORM
* Serializer menggunakan Django REST Framework

---

## Struktur Database

**Produk**

* id_produk
* nama_produk
* harga
* kategori (FK)
* status (FK)

**Kategori**

* id_kategori
* nama_kategori

**Status**

* id_status
* nama_status

---

## API FastPrint

**Endpoint**

```
https://recruitment.fastprint.co.id/tes/api_tes_programmer
```

**Autentikasi**

* Username berubah mengikuti waktu server
* Password (MD5):

```
bisacoding-{tanggal}-{bulan}-{2 digit tahun}
```

API diakses menggunakan library `requests` dengan pengecekan **response, header, dan cookies**.

---

## Teknologi

* Python 3.10+
* Django 5.x
* MySQL
* Bootstrap 5
* Django REST Framework

---

## Cara Menjalankan

```bash
git clone https://github.com/username-anda/fastprint_test.git
cd fastprint_test
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Akses:

```
http://127.0.0.1:8000/
```

