# 📚 PANDUAN IMPLEMENTASI LENGKAP
## PBL0301 & PBL0302 - Monolith Web Application dengan Flask

---

## 📖 BAGIAN 1: PEMAHAMAN KONSEP

### A. Apa itu Monolith Architecture?

**Definisi:**
Monolith adalah aplikasi yang dibangun sebagai **satu kesatuan** (unified unit) yang mandiri dan independen dari aplikasi lain.

**Karakteristik:**
1. Single Codebase - semua kode dalam satu project
2. Single Database - satu database untuk seluruh aplikasi
3. Front-end + Back-end dalam satu aplikasi
4. Deploy sebagai satu unit

**Kelebihan:**
- Sederhana untuk development awal
- Mudah di-deploy
- Testing lebih straightforward
- Cocok untuk aplikasi kecil-menengah

**Kekurangan:**
- Susah scale (scaling horizontal)
- Sulit untuk update sebagian kecil
- Single point of failure

**Visualisasi:**
```
┌─────────────────────────────────────┐
│         MONOLITH APPLICATION        │
├─────────────────────────────────────┤
│  FRONT-END (HTML, CSS, JavaScript)  │
│  BACK-END (Python Flask)            │
│  DATABASE (SQLite)                  │
└─────────────────────────────────────┘
         ↓ Deploy as ONE
    Single Server
```

---

### B. MVC Architecture (Model-View-Controller)

**Struktur:**

```
┌──────────────────────────────────┐
│         USER REQUEST             │
└──────────────┬───────────────────┘
               │
               ↓
        ┌──────────────┐
        │  CONTROLLER  │ ← Routes, Business Logic
        │  (app.py)    │
        └──┬───────┬───┘
           │       │
      ┌────┴┐   ┌──┴────┐
      ↓     │   │       ↓
   ┌──────┐│   │  ┌─────────────┐
   │MODEL ││   │  │    VIEW     │
   │ (DB) ││   │  │(Templates)  │
   └──────┘│   │  └─────────────┘
           │   │
      Data │   → HTML to User
           │
        ┌──┴────┐
        ↓       ↓
     ┌──────────────────┐
     │  USER SEES PAGE  │
     └──────────────────┘
```

**Komponen:**

1. **MODEL** (Database Layer)
   - Struktur data
   - Business logic untuk data
   - Komunikasi dengan database
   - File: `app.py` - Class `Car`

2. **VIEW** (Presentation Layer)
   - Tampilan untuk user
   - HTML + CSS + JavaScript
   - Template engine (Jinja2)
   - Folder: `templates/`

3. **CONTROLLER** (Logic Layer)
   - Menerima request dari user
   - Memanggil model untuk data
   - Memanggil view untuk display
   - File: `app.py` - @app.route functions

---

### C. CRUD Operations

**CRUD = Create, Read, Update, Delete**

| Operasi | HTTP | SQL | Fungsi |
|---------|------|-----|--------|
| **CREATE** | POST | INSERT | Membuat data baru |
| **READ** | GET | SELECT | Menampilkan data |
| **UPDATE** | PUT/POST | UPDATE | Mengubah data |
| **DELETE** | DELETE | DELETE | Menghapus data |

**Tambahan untuk Assignment:**
- **SEARCH** = Mencari dengan kriteria tertentu

---

## 🔨 BAGIAN 2: IMPLEMENTASI

### Step 1: Setup Environment

```bash
# 1. Buat virtual environment
python3 -m venv monolith-env

# 2. Aktivasi
source monolith-env/bin/activate  # Linux/Mac
# atau
monolith-env\Scripts\activate     # Windows

# 3. Install dependencies
pip install -r requirements.txt

# Dependencies:
# - Flask: Web framework
# - Peewee: ORM untuk database
# - Werkzeug: WSGI utilities
```

### Step 2: Database Setup

```python
# Bagian 1: Koneksi Database
from peewee import *

db = SqliteDatabase('carsweb.db')

# Bagian 2: Define Model
class Car(Model):
    id = AutoField()
    brand = CharField()
    model = CharField()
    year = IntegerField()
    color = CharField()
    price = FloatField()
    
    class Meta:
        database = db
        table_name = 'cars'

# Bagian 3: Create table jika belum ada
db.create_tables([Car], safe=True)
```

### Step 3: Controller - CRUD Operations

#### CREATE - Tambah Data Baru

```python
@app.route('/createcar', methods=['GET', 'POST'])
def createcar():
    if request.method == 'POST':
        # Ambil data dari form
        brand = request.form['brand']
        model = request.form['model']
        year = request.form['year']
        color = request.form['color']
        price = request.form['price']
        
        # INSERT ke database
        Car.create(
            brand=brand,
            model=model,
            year=int(year),
            color=color,
            price=float(price)
        )
        
        flash('Mobil berhasil ditambahkan', 'success')
        return redirect(url_for('index'))
    
    # Tampilkan form create
    return render_template('createcar.html')
```

**Flow:**
```
User → Click "Tambah Mobil"
  ↓
GET /createcar → Tampilkan Form
  ↓
User fill form → Submit
  ↓
POST /createcar → Data diproses
  ↓
Car.create() → INSERT ke database
  ↓
Redirect ke /index → Tampilkan semua data
```

---

#### READ - Tampilkan Data

```python
# 1. Read semua data
@app.route('/')
def index():
    cars = Car.select()  # SELECT * FROM cars
    return render_template('index.html', cars=cars)

# 2. Read detail satu data
@app.route('/readcar/<int:car_id>')
def readcar(car_id):
    car = Car.get_by_id(car_id)  # SELECT * FROM cars WHERE id = ?
    return render_template('readcar.html', car=car)
```

**SQL yang dijalankan:**
```sql
-- Read semua
SELECT * FROM cars;

-- Read satu
SELECT * FROM cars WHERE id = 1;
```

---

#### UPDATE - Ubah Data ⭐ REQUIREMENT PBL0301

```python
@app.route('/updatecar/<int:car_id>', methods=['GET', 'POST'])
def updatecar(car_id):
    # Ambil data yang akan diupdate
    car = Car.get_by_id(car_id)
    
    if request.method == 'POST':
        # Update field-field
        car.brand = request.form['brand']
        car.model = request.form['model']
        car.year = int(request.form['year'])
        car.color = request.form['color']
        car.price = float(request.form['price'])
        
        # SAVE ke database
        car.save()
        
        flash('Mobil berhasil diupdate', 'success')
        return redirect(url_for('readcar', car_id=car.id))
    
    # Tampilkan form dengan data lama
    return render_template('updatecar.html', car=car)
```

**SQL yang dijalankan:**
```sql
-- UPDATE
UPDATE cars 
SET brand = ?, model = ?, year = ?, color = ?, price = ?
WHERE id = ?;
```

---

#### DELETE - Hapus Data

```python
@app.route('/deletecar/<int:car_id>', methods=['POST'])
def deletecar(car_id):
    car = Car.get_by_id(car_id)
    car.delete_instance()  # DELETE FROM cars WHERE id = ?
    
    flash('Mobil berhasil dihapus', 'success')
    return redirect(url_for('index'))
```

**SQL yang dijalankan:**
```sql
-- DELETE
DELETE FROM cars WHERE id = ?;
```

---

#### SEARCH - Cari Data ⭐ REQUIREMENT PBL0301

```python
@app.route('/searchcar', methods=['GET', 'POST'])
def searchcar():
    cars = []
    search_query = ''
    
    if request.method == 'POST':
        search_query = request.form.get('query', '')
        
        if search_query:
            # Search di brand, model, atau color
            cars = Car.select().where(
                (Car.brand.contains(search_query)) |
                (Car.model.contains(search_query)) |
                (Car.color.contains(search_query))
            )
    
    return render_template('searchcar.html', cars=cars, search_query=search_query)
```

**SQL yang dijalankan:**
```sql
-- SEARCH (Case-insensitive)
SELECT * FROM cars 
WHERE 
  brand LIKE '%query%' OR 
  model LIKE '%query%' OR 
  color LIKE '%query%';
```

**Contoh:**
- Search "Toyota" → Tampilkan semua mobil Toyota
- Search "Avanza" → Tampilkan semua Avanza
- Search "Merah" → Tampilkan semua mobil berwarna merah

---

### Step 4: Views - Template HTML

#### Base Template (base.html)

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Default Title{% endblock %}</title>
    <link href="bootstrap.css" rel="stylesheet">
</head>
<body>
    <!-- Navigation -->
    <nav>
        <ul>
            <li><a href="{{ url_for('index') }}">Data Mobil</a></li>
            <li><a href="{{ url_for('createcar') }}">Tambah Mobil</a></li>
            <li><a href="{{ url_for('searchcar') }}">Cari Mobil</a></li>
        </ul>
    </nav>

    <!-- Flash Messages -->
    {% with messages = get_flashed_messages() %}
        {% for message in messages %}
            <div class="alert">{{ message }}</div>
        {% endfor %}
    {% endwith %}

    <!-- Content -->
    <div class="container">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
```

#### List/Index Template (index.html)

```html
{% extends "base.html" %}

{% block content %}
<h2>Daftar Mobil</h2>

<table>
    <thead>
        <tr>
            <th>Brand</th>
            <th>Model</th>
            <th>Tahun</th>
            <th>Warna</th>
            <th>Harga</th>
            <th>Aksi</th>
        </tr>
    </thead>
    <tbody>
        {% for car in cars %}
        <tr>
            <td>{{ car.brand }}</td>
            <td>{{ car.model }}</td>
            <td>{{ car.year }}</td>
            <td>{{ car.color }}</td>
            <td>Rp {{ car.price }}</td>
            <td>
                <a href="{{ url_for('readcar', car_id=car.id) }}">Lihat</a>
                <a href="{{ url_for('updatecar', car_id=car.id) }}">Edit</a>
                <form method="POST" action="{{ url_for('deletecar', car_id=car.id) }}">
                    <button type="submit">Hapus</button>
                </form>
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>
{% endblock %}
```

---

## 📊 BAGIAN 3: WORKFLOW APPLICATION

### Workflow: CREATE Mobil Baru

```
1. User buka http://localhost:5000/createcar (GET)
   ↓
2. Server: @app.route('/createcar', methods=['GET', 'POST'])
   - request.method == 'GET' → render createcar.html
   ↓
3. User lihat form dengan field:
   - Brand: [     ]
   - Model: [     ]
   - Tahun: [     ]
   - Warna: [     ]
   - Harga: [     ]
   ↓
4. User isi form dan klik "Simpan" (POST /createcar)
   ↓
5. Server: request.method == 'POST'
   - brand = request.form['brand']
   - model = request.form['model']
   - year = request.form['year']
   - color = request.form['color']
   - price = request.form['price']
   ↓
6. Database Operation:
   Car.create(
       brand=brand,
       model=model,
       year=int(year),
       color=color,
       price=float(price)
   )
   ↓ INSERT INTO cars (brand, model, year, color, price)
   ↓ VALUES (?, ?, ?, ?, ?)
   ↓
7. Database: mobil baru ditambahkan
   ↓
8. Server: redirect(url_for('index'))
   → GET /
   ↓
9. @app.route('/')
   cars = Car.select()  ← READ semua data
   ↓ SELECT * FROM cars
   ↓
10. render_template('index.html', cars=cars)
    ↓
11. User melihat tabel dengan mobil terbaru
```

---

### Workflow: SEARCH Mobil

```
1. User klik "Cari Mobil" → /searchcar (GET)
   ↓
2. Tampilkan form pencarian:
   [Search Box] [Tombol Cari]
   ↓
3. User ketik "Toyota" dan klik "Cari" (POST /searchcar)
   ↓
4. Server: request.method == 'POST'
   query = request.form.get('query')  → "Toyota"
   ↓
5. Database Query:
   cars = Car.select().where(
       (Car.brand.contains('Toyota')) |
       (Car.model.contains('Toyota')) |
       (Car.color.contains('Toyota'))
   )
   ↓ SELECT * FROM cars WHERE
   ↓ brand LIKE '%Toyota%' OR
   ↓ model LIKE '%Toyota%' OR
   ↓ color LIKE '%Toyota%'
   ↓
6. Hasil:
   - Toyota Avanza 2023 Merah
   - Toyota Fortuner 2022 Hitam
   - (mobil lain yang cocok)
   ↓
7. render_template('searchcar.html', cars=cars, search_query=query)
   ↓
8. User lihat hasil pencarian
```

---

## 📁 BAGIAN 4: FILE STRUCTURE LENGKAP

```
Monolith/
│
├── app.py                          ← CONTROLLER + MODEL
│   ├── Database setup
│   ├── Model definition (Car)
│   ├── Routes definition
│   └── CRUD functions
│
├── carsweb.db                      ← DATABASE (SQLite)
│   └── Table: cars
│       ├── id (INTEGER, PK)
│       ├── brand (TEXT)
│       ├── model (TEXT)
│       ├── year (INTEGER)
│       ├── color (TEXT)
│       └── price (REAL)
│
├── templates/                      ← VIEWS
│   ├── base.html
│   │   └── Navigation, layout base
│   ├── index.html
│   │   └── List semua cars (READ)
│   ├── createcar.html
│   │   └── Form tambah car (CREATE)
│   ├── readcar.html
│   │   └── Detail car (READ)
│   ├── updatecar.html
│   │   └── Form edit car (UPDATE) ⭐
│   └── searchcar.html
│       └── Form cari car (SEARCH) ⭐
│
├── static/                         ← FRONT-END RESOURCES
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│
├── requirements.txt
│   ├── Flask==2.3.2
│   ├── peewee==3.16.2
│   └── ...
│
└── README.md
    └── Dokumentasi lengkap
```

---

## 🎯 CHECKLIST IMPLEMENTASI

### PBL0301 - Complete CRUDS (UPDATE & SEARCH)

- [x] **CREATE** - Fungsi menambah data mobil baru
  - [x] Route `/createcar` GET & POST
  - [x] Form HTML (createcar.html)
  - [x] Validasi input
  - [x] Insert ke database

- [x] **READ** - Fungsi menampilkan data
  - [x] Route `/` GET - List semua
  - [x] Route `/readcar/<id>` GET - Detail
  - [x] Template index.html
  - [x] Template readcar.html

- [x] **UPDATE** ⭐ **REQUIREMENT**
  - [x] Route `/updatecar/<id>` GET & POST
  - [x] Form HTML (updatecar.html)
  - [x] Pre-fill form dengan data lama
  - [x] Update database

- [x] **DELETE** - Fungsi hapus data
  - [x] Route `/deletecar/<id>` POST
  - [x] Delete dari database

- [x] **SEARCH** ⭐ **REQUIREMENT**
  - [x] Route `/searchcar` GET & POST
  - [x] Form pencarian HTML
  - [x] Search by brand
  - [x] Search by model
  - [x] Search by color

---

### PBL0302 - Car Data CRUDS dengan Framework

- [x] Framework: **Flask**
- [x] Database: **SQLite** (carsweb.db)
- [x] ORM: **Peewee**
- [x] CRUD Operations: **Semua lengkap**
  - [x] Create (Insert)
  - [x] Read (Select)
  - [x] Update (Modify)
  - [x] Delete (Remove)
  - [x] Search (Filter)

---

## 🚀 CARA MENJALANKAN

```bash
# 1. Setup
python3 -m venv monolith-env
source monolith-env/bin/activate
pip install -r requirements.txt

# 2. Jalankan
python app.py

# 3. Buka browser
# http://localhost:5000
```

---

## 📝 NOTES PENTING

1. **MVC Architecture**: Pemisahan antara Model (database), View (template), Controller (routes)

2. **Monolith**: Front-end dan Back-end dalam satu aplikasi

3. **CRUD**: Empat operasi dasar + Search

4. **Peewee ORM**: Abstraksi database, lebih clean dari raw SQL

5. **Jinja2 Template**: Template engine untuk render HTML dinamis

6. **Flask Routing**: @app.route untuk define URL patterns

7. **Database Schema**: Perencanaan struktur data sebelum implementasi

---

## 🎓 LEARNING OUTCOMES

Setelah menyelesaikan assignment ini, Anda akan mengerti:

1. ✅ Konsep Monolith Architecture
2. ✅ MVC Pattern dan implementasinya
3. ✅ CRUD Operations dengan database
4. ✅ Flask framework basics
5. ✅ Peewee ORM usage
6. ✅ HTML template dengan Jinja2
7. ✅ Form handling dan validation
8. ✅ Database design dan normalization
9. ✅ Search/Filter functionality
10. ✅ Full-stack web development basics

---

**Dibuat oleh**: Irwan Kautsar, Ph.D  
**Untuk**: PBL0301 & PBL0302 - Web Framework Course  
**Universitas**: Muhammadiyah Sidoarjo
