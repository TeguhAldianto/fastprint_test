import hashlib
import requests
import datetime
from django.core.management.base import BaseCommand
from produk_app.models import Produk, Kategori, Status

class Command(BaseCommand):
    help = 'Mengambil data produk dari API FastPrint'

    def handle(self, *args, **kwargs):
        # 1. Generate Auth Credentials Sesuai Rumus
        now = datetime.datetime.now()
        
        # Rumus Username: tesprogrammer + ddMMyy + C + HH (Jam 24 format)
        # Note: 'C' + 19 (dari contoh user C19, asumsi 19 adalah jam saat itu)
        username = f"tesprogrammer{now.strftime('%d%m%y')}C{now.strftime('%H')}"
        
        # Rumus Password: bisacoding-dd-mm-yy -> MD5
        password_raw = f"bisacoding-{now.strftime('%d-%m-%y')}"
        password_md5 = hashlib.md5(password_raw.encode()).hexdigest()

        url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"
        payload = {
            'username': username,
            'password': password_md5
        }

        # 2. Hit API
        self.stdout.write(f"Connecting with User: {username}...")
        try:
            response = requests.post(url, data=payload)
            data = response.json()
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error connecting: {e}"))
            return

        if data.get('error') == 0:
            self.stdout.write("Login Berhasil! Menyimpan data...")
            
            # 3. Looping dan Simpan ke DB
            products_list = data['data']
            for item in products_list:
                # Hindari data kotor (kadang ada yg tidak punya kategori/status)
                if not item['kategori'] or not item['status']:
                    continue

                # Get or Create Kategori
                kat_obj, _ = Kategori.objects.get_or_create(
                    nama_kategori=item['kategori']
                )

                # Get or Create Status
                stat_obj, _ = Status.objects.get_or_create(
                    nama_status=item['status']
                )
                
                # Update or Create Produk (agar tidak duplikat saat run ulang)
                # Pastikan harga berupa angka
                harga_clean = item['harga'] if str(item['harga']).isdigit() else 0

                Produk.objects.update_or_create(
                    id_produk=item['id_produk'],
                    defaults={
                        'nama_produk': item['nama_produk'],
                        'harga': harga_clean,
                        'kategori': kat_obj,
                        'status': stat_obj
                    }
                )
            self.stdout.write(self.style.SUCCESS("Data berhasil disimpan!"))
        else:
            self.stdout.write(self.style.ERROR(f"Gagal: {data.get('ket')}"))