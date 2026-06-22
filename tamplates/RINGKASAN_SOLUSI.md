# 🎉 RINGKASAN SOLUSI LENGKAP
## PBL0301 & PBL0302 - Car Management System dengan Flask

---

## ✅ APA YANG TELAH DIBUAT

### 📁 File-file yang Dihasilkan:

```
Solusi Lengkap/
│
├── 📄 DOKUMENTASI
│   ├── README.md                    ← Dokumentasi lengkap aplikasi
│   ├── PANDUAN_IMPLEMENTASI.md      ← Panduan step-by-step
│   └── RINGKASAN_SOLUSI.md          ← File ini
│
├── 🐍 PYTHON BACKEND
│   ├── app.py                       ← Flask application (CONTROLLER + MODEL)
│   └── requirements.txt              ← Python dependencies
│
├── 📱 FRONTEND TEMPLATES (dalam folder templates/)
│   ├── base.html                    ← Base template dengan navbar
│   ├── index.html                   ← Menampilkan semua mobil (READ)
│   ├── createcar.html               ← Form tambah mobil baru (CREATE)
│   ├── readcar.html                 ← Detail satu mobil (READ)
│   ├── updatecar.html               ← Form edit mobil (UPDATE) ⭐
│   └── searchcar.html               ← Form cari mobil (SEARCH) ⭐
│
└── 🗄️ DATABASE
    └── carsweb.db                   ← SQLite database (otomatis dibuat)
        └── Table 'cars':
            - id (INTEGER, PK)
            - brand (TEXT)
            - model (TEXT)
            - year (INTEGER)
            - color (TEXT)
            - price (REAL)
```

---

## 📋 REQUIREMENT PEMENUHAN

### ✅ PBL0301: Complete CRUDS Function (UPDATE and SEARCH)

#### 1. **CREATE** ✓
- **File**: `createcar.html`, `app.py` (routes: /createcar)
- **Fungsi**: Menambah data mobil baru
- **Form Fields**: Brand, Model, Tahun, Warna, Harga
- **Database**: INSERT INTO cars

#### 2. **READ** ✓
- **File**: `index.html`, `readcar.html`, `app.py`
- **Routes**: 
  - `/` - List semua mobil
  - `/readcar/<id>` - Detail mobil
- **Fungsi**: Menampilkan data mobil
- **Database**: SELECT * FROM cars

#### 3. **UPDATE** ✅ ⭐ REQUIREMENT
- **File**: `updatecar.html`, `app.py` (route: /updatecar/<id>)
- **Fungsi**: Mengubah data mobil yang sudah ada
- **Form Fields**: Brand, Model, Tahun, Warna, Harga (pre-filled)
- **Database**: UPDATE cars SET ... WHERE id = ?
- **Status**: ✅ SELESAI

#### 4. **DELETE** ✓
- **File**: `app.py` (route: /deletecar/<id>)
- **Fungsi**: Menghapus data mobil
- **Database**: DELETE FROM cars WHERE id = ?

#### 5. **SEARCH** ✅ ⭐ REQUIREMENT
- **File**: `searchcar.html`, `app.py` (route: /searchcar)
- **Fungsi**: Mencari mobil berdasarkan:
  - Brand (merek)
  - Model (tipe)
  - Color (warna)
- **Database**: SELECT * FROM cars WHERE brand LIKE ? OR model LIKE ? OR color LIKE ?
- **Status**: ✅ SELESAI

---

### ✅ PBL0302: Create CAR DATA CRUDS from Framework

#### Requirements:
1. ✅ **Framework**: Flask (Python Microframework)
2. ✅ **Database**: SQLite (carsweb.db)
3. ✅ **CRUD Operations**: CREATE, READ, UPDATE, DELETE
4. ✅ **Tambahan**: SEARCH functionality

#### Status:
- ✅ Framework: Flask
- ✅ Database Engine: SQLite
- ✅ CRUD Lengkap
- ✅ ORM: Peewee
- ✅ Template Engine: Jinja2

---

## 🚀 CARA MENGGUNAKAN

### 1. Persiapan Awal

```bash
# 1. Copy semua file ke folder project
mkdir Monolith
cd Monolith
# Copy: app.py, requirements.txt, templates folder

# 2. Buat virtual environment
python3 -m venv monolith-env

# 3. Aktivasi virtual environment
# Linux/Mac:
source monolith-env/bin/activate

# Windows:
monolith-env\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt
```

### 2. Menjalankan Aplikasi

```bash
# Pastikan sudah di folder Monolith dan venv aktif
python app.py

# Output:
# * Serving Flask app 'app'
# * Debug mode: on
# * Running on http://127.0.0.1:5000
# * Press CTRL+C to quit

# Buka browser: http://localhost:5000
```

### 3. Test Semua Fitur

#### Test CREATE:
1. Buka http://localhost:5000
2. Klik "Tambah Mobil"
3. Isi form dengan data:
   - Brand: Toyota
   - Model: Avanza
   - Tahun: 2023
   - Warna: Merah
   - Harga: 150000000
4. Klik "Simpan Mobil"

#### Test READ:
1. Kembali ke halaman utama
2. Lihat tabel dengan data yang baru ditambahkan
3. Klik "Lihat" untuk melihat detail

#### Test UPDATE (⭐ REQUIREMENT):
1. Dari detail mobil, klik "Edit Data"
2. Ubah data yang ada (misal: harga menjadi 160000000)
3. Klik "Perbarui Data"
4. Verifikasi data berubah di list

#### Test SEARCH (⭐ REQUIREMENT):
1. Klik menu "Cari Mobil"
2. Ketik "Toyota" di search box
3. Klik "Cari"
4. Lihat hasil pencarian
5. Coba cari dengan Model (misal "Avanza") atau Warna (misal "Merah")

#### Test DELETE:
1. Di list mobil, klik "Hapus"
2. Konfirmasi penghapusan
3. Mobil dihapus dari database

---

## 📂 STRUKTUR FOLDER FINAL

```
Monolith/
├── app.py                    ← Main application
├── carsweb.db               ← Database (otomatis dibuat)
├── requirements.txt         ← Dependencies
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── createcar.html
│   ├── readcar.html
│   ├── updatecar.html
│   └── searchcar.html
├── static/                  ← (Optional) CSS, JS, images
├── monolith-env/            ← Virtual environment (auto created)
└── README.md                ← Dokumentasi
```

---

## 💻 CODE HIGHLIGHTS

### app.py - CONTROLLER Functions

```python
# CREATE
@app.route('/createcar', methods=['GET', 'POST'])
def createcar():
    if request.method == 'POST':
        Car.create(
            brand=request.form['brand'],
            model=request.form['model'],
            year=int(request.form['year']),
            color=request.form['color'],
            price=float(request.form['price'])
        )

# UPDATE ⭐
@app.route('/updatecar/<int:car_id>', methods=['GET', 'POST'])
def updatecar(car_id):
    car = Car.get_by_id(car_id)
    if request.method == 'POST':
        car.brand = request.form['brand']
        car.save()

# SEARCH ⭐
@app.route('/searchcar', methods=['GET', 'POST'])
def searchcar():
    if request.method == 'POST':
        query = request.form.get('query', '')
        cars = Car.select().where(
            (Car.brand.contains(query)) |
            (Car.model.contains(query)) |
            (Car.color.contains(query))
        )
```

---

## 📊 DATABASE SCHEMA

### Table: cars

```sql
CREATE TABLE cars (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  brand TEXT NOT NULL,
  model TEXT NOT NULL,
  year INTEGER NOT NULL,
  color TEXT NOT NULL,
  price REAL NOT NULL
);
```

### Sample Data

```
id | brand  | model   | year | color | price
---|--------|---------|------|-------|----------
1  | Toyota | Avanza  | 2023 | Merah | 150000000
2  | Honda  | Civic   | 2022 | Putih | 250000000
3  | Nissan | X-Trail | 2021 | Hitam | 350000000
```

---

## 🔍 FITUR-FITUR UTAMA

### Backend:
- ✅ Flask Web Framework
- ✅ Peewee ORM untuk database abstraction
- ✅ SQLite database
- ✅ Error handling dan flash messages
- ✅ Route handling lengkap
- ✅ Data validation

### Frontend:
- ✅ Responsive Bootstrap 5 design
- ✅ Navigation menu
- ✅ Data table dengan aksi
- ✅ Form validation
- ✅ Color badge untuk warna mobil
- ✅ Jinja2 template engine

### Database:
- ✅ SQLite (embedded, no installation needed)
- ✅ Auto-create table on startup
- ✅ CRUD operations lengkap
- ✅ Search dengan LIKE query

---

## 📖 DOKUMENTASI YANG DISEDIAKAN

1. **README.md**
   - Penjelasan project
   - Instalasi dan setup
   - Penjelasan CRUD
   - Database schema
   - Learning outcomes

2. **PANDUAN_IMPLEMENTASI.md**
   - Pemahaman konsep (Monolith, MVC, CRUD)
   - Step-by-step implementasi
   - Workflow application
   - File structure lengkap
   - Checklist pemenuhan requirement

3. **RINGKASAN_SOLUSI.md** (file ini)
   - Ringkasan file yang dibuat
   - Requirement pemenuhan
   - Cara menggunakan
   - Code highlights
   - Troubleshooting

---

## ⚙️ TROUBLESHOOTING

### Error: "No module named 'flask'"
```bash
pip install -r requirements.txt
```

### Error: "Port 5000 already in use"
```bash
# Linux/Mac: Kill process di port 5000
lsof -i :5000
kill -9 <PID>

# Windows: Jalankan di port berbeda
python app.py --port 5001
```

### Error: "Database is locked"
- Tutup semua instance aplikasi
- Hapus file `*.db-journal` jika ada

### Form tidak menerima input
- Pastikan form method adalah POST
- Pastikan input name sesuai dengan form['name']

---

## 🎯 LEARNING OUTCOMES

Setelah menggunakan solusi ini, Anda akan mengerti:

1. ✅ Monolith Web Architecture
2. ✅ MVC Pattern implementation
3. ✅ CRUD Operations dengan database
4. ✅ Flask framework basics
5. ✅ Peewee ORM usage
6. ✅ Jinja2 templating
7. ✅ HTML form handling
8. ✅ Database design
9. ✅ Search/Filter functionality
10. ✅ Full-stack web development

---

## 📝 NOTES PENTING

### Untuk Assignment:

1. **Pastikan semua file ada**:
   - app.py ✓
   - requirements.txt ✓
   - Folder templates dengan 6 file HTML ✓

2. **Fitur UPDATE dan SEARCH harus jalan**:
   - UPDATE: `/updatecar/<id>` harus bisa ubah data
   - SEARCH: `/searchcar` harus bisa cari by brand/model/color

3. **Database**:
   - SQLite (carsweb.db) akan otomatis dibuat
   - Gunakan Peewee ORM

4. **Presentasi**:
   - Show demo UPDATE functionality
   - Show demo SEARCH functionality
   - Jelaskan MVC architecture
   - Jelaskan CRUD operations

---

## 🔗 RESOURCES

- **GitHub**: https://github.com/hepidad/c003-monolith
- **Flask Docs**: https://flask.palletsprojects.com/
- **Peewee Docs**: https://docs.peewee-orm.com/
- **Bootstrap**: https://getbootstrap.com/
- **Jinja2**: https://jinja.palletsprojects.com/

---

## ✨ SUMMARY

Solusi ini menyediakan:
- ✅ Aplikasi Flask lengkap dengan CRUD + Search
- ✅ UPDATE dan SEARCH functionality (requirement PBL0301)
- ✅ SQLite database dengan Peewee ORM (requirement PBL0302)
- ✅ Responsive UI dengan Bootstrap 5
- ✅ Dokumentasi lengkap (3 file markdown)
- ✅ Ready to deploy

**Status**: ✅ SIAP DIGUNAKAN

---

**Dibuat oleh**: Claude (AI Assistant)  
**Untuk**: PBL0301 & PBL0302 - Web Framework Course  
**Universitas**: Muhammadiyah Sidoarjo  
**Tanggal**: 2026

**Instruktur**: Irwan Kautsar, Ph.D (Assoc. Prof.)  
**Email**: hepidad@umsida.ac.id  
**Link**: https://bit.ly/hepidad
