# 📰 Sistem Informasi Jurnal – REST API
Sistem Informasi Jurnal adalah RESTful API berbasis Django yang menyediakan endpoint untuk mengelola data jurnal ilmiah secara efisien dan terstruktur. Proyek ini menggunakan Django REST Framework dan dokumentasi API telah disediakan melalui Swagger dan Redoc.

---

## 🚀 Fitur Utama
- Autentikasi dan manajemen pengguna
- CRUD untuk informasi jurnal
- Relasi dengan institusi, negara, dan mata uang
- Dokumentasi API (Swagger, Redoc, OpenAPI)

---

## 🛠️ Instalasi
### 1. Clone repositori
```bash
git clone https://github.com/tarokeitaro/sij-backend.git cd sistem-informasi-jurnal
```

### 2. Buat Virtual Environment
```bash
python -m venv venv source venv/bin/activate # Linux/macOS 
```
```bash
venv\Scripts\activate # Windows
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Konfigurasi Environment Variables
Buat file `.env` di root direktori berdasarkan file contoh:
```bash
cp .env.example .env
```
Lalu sesuaikan nilai-nilai environment.

---

## ⚙️ Konfigurasi Penting di `settings.py`
```conf
CORS_ALLOWED_ORIGINS = [
    "http://0.0.0.0:8000",
] 
CSRF_TRUSTED_ORIGINS = [
    'http://0.0.0.0:8000',
]
```
Pastikan pengaturan ini diaktifkan saat development agar frontend bisa mengakses API dengan aman.

---

## 🧪 Menjalankan Server
```bash
python manage.py migrate
```
```bash
python manage.py runserver
```

---

## 📚 Dokumentasi API
Akses dokumentasi API pada endpoint berikut:

- **OpenAPI schema (raw)**: [`/api/schema/`](http://localhost:8000/api/schema/)
- **Swagger UI**: [`/api/schema/swagger-ui/`](http://localhost:8000/api/schema/swagger-ui/)
- **Redoc**: [`/api/schema/redoc/`](http://localhost:8000/api/schema/redoc/)

---

## 📬 Kontak
Jika ada pertanyaan atau kontribusi, silakan buat [issue](https://github.com/tarokeitaro/sij-backend/issues) atau hubungi maintainer proyek.