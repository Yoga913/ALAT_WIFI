1. **Pastikan Lingkungan Terinstal**:
   Pastikan Anda memiliki Python,pip dan git terinstal di sistem Anda.Jika belum,
   - instal Python dari [situs resmi Python](https://www.python.org/downloads/).
   - install git dari [situs resmi git](https://git-scm.com/).
2. **Instalasi aplikasi di cmd/powershell** :

   - git clone https://github.com/Yoga913/ALAT_WIFI/new/main

3. **Install Dependencies di cmd/powershel**:

   Instal Flask menggunakan pip:

   ```bash
   pip install flask
   ```

4. **masuk ke directory file tempat anda mengunduh**:
    cd C:/"direktory anda mengunduh folder"/ALAT_WIFI

5. **Jalankan Aplikasi**:

   Jalankan aplikasi Flask dengan menjalankan `app.py`:

   ```bash
   python app.py
   ```

6. **Akses Aplikasi di Browser**:
   Buka browser dan akses `http://127.0.0.1:5000` untuk menggunakan aplikasi.

### Aturan Penggunaan

1. **Jalankan Sebagai Administrator**:
   Beberapa perintah `netsh` memerlukan hak akses administrator untuk berjalan dengan benar. Jalankan terminal atau command prompt Anda sebagai administrator sebelum menjalankan aplikasi.

2. **Khusus untuk Windows**:
   Aplikasi ini dirancang khusus untuk sistem operasi Windows, karena menggunakan perintah `netsh` yang spesifik untuk Windows.

3. **Keamanan**:
   - Pastikan hanya Anda atau orang yang Anda percayai yang memiliki akses ke aplikasi ini, karena ini dapat mengekspos informasi sensitif seperti kata sandi Wi-Fi.
   - Jangan menjalankan aplikasi ini pada jaringan yang tidak aman atau komputer publik.

4. **Perbarui Sistem**:
   Pastikan sistem Windows Anda diperbarui untuk menghindari masalah kompatibilitas dan keamanan.

5. **Dependencies**:
   Jika Anda menambahkan lebih banyak fitur atau menggunakan pustaka tambahan, pastikan untuk mengelola dependencies dengan baik menggunakan `requirements.txt`:

   ```bash
   pip freeze > requirements.txt
   ```

### Contoh `requirements.txt` untuk Proyek Ini

Untuk memastikan lingkungan Anda dapat direplikasi dengan mudah, buat file `requirements.txt` dengan isi berikut:

```bash
Flask==2.0.1
```

Anda bisa menginstal dependencies dari file ini menggunakan:

```bash
pip install -r requirements.txt
```

### Menjalankan Aplikasi di Produksi

Untuk menjalankan aplikasi di lingkungan produksi, Anda mungkin ingin menggunakan server aplikasi seperti Gunicorn (untuk Unix) atau waitress (untuk Windows).

1. **Install Gunicorn (untuk Unix)**:

   ```bash
   pip install gunicorn
   ```

   Kemudian jalankan:

   ```bash
   gunicorn -w 4 app:app
   ```

2. **Install waitress (untuk Windows)**:

   ```bash
   pip install waitress
   ```

   Kemudian jalankan:

   ```bash
   waitress-serve --port=5000 app:app
   ```

Dengan mengikuti langkah-langkah dan aturan di atas, Anda dapat menerapkan dan menggunakan aplikasi web ALAT Wi-Fi dengan lebih aman dan efektif.

