# Car Management System dengan Flask
## Solusi PBL0301 dan PBL0302

Ini adalah aplikasi **Monolith Web Application** menggunakan **Flask Framework** untuk manajemen data mobil dengan implementasi **MVC Architecture** dan **CRUD Operations**.

---

## 📋 Daftar Isi
1. [Struktur Proyek](#struktur-proyek)
2. [Requirement PBL0301](#requirement-pbl0301)
3. [Requirement PBL0302](#requirement-pbl0302)
4. [Instalasi](#instalasi)
5. [Menjalankan Aplikasi](#menjalankan-aplikasi)
6. [Fitur-Fitur](#fitur-fitur)
7. [Penjelasan Kode](#penjelasan-kode)

---

## 📂 Struktur Proyek

```
Monolith/
├── app.py                      # Main Flask application (CONTROLLER)
├── carsweb.db                  # SQLite Database (MODEL)
├── requirements.txt            # Python dependencies
├── templates/                  # HTML Templates (VIEW)
│   ├── base.html              # Base template
│   ├── index.html             # Tampil semua mobil (READ)
│   ├── createcar.html         # Tambah mobil baru (CREATE)
│   ├── readcar.html           # Tampil detail mobil (READ)
│   ├── updatecar.html         # Edit data mobil (UPDATE)
│   └── searchcar.html         # Cari mobil (SEARCH)
└── static/                     # CSS, JS, Images (FRONT-END)
    ├── css/
    ├── js/
    └── fonts/
```

---

## ✅ Requirement PBL0301

### Assignment: Complete CRUDS function (UPDATE and SEARCH) dengan Flask Framework

**Fungsi yang telah diimplementasikan:**

#### 1. **CREATE** - Menambah Data Mobil Baru
- **Route**: `/createcar` (GET, POST)
- **Template**: `createcar.html`
- **Fungsi**: Form untuk menambah mobil dengan field:
  - Brand (text)
  - Model (text)
  - Tahun Produksi (number)
  - Warna (select)
  - Harga (number)

```python
@app.route('/createcar', methods=['GET', 'POST'])
def createcar():
    if request.method == 'POST':
        # Insert ke database
        Car.create(
            brand=request.form['brand'],
            model=request.form['model'],
            year=int(request.form['year']),
            color=request.form['color'],
            price=float(request.form['price'])
        )
```

#### 2. **READ** - Membaca/Menampilkan Data
- **Route**: `/` (semua mobil) dan `/readcar/<id>` (detail)
- **Template**: `index.html`, `readcar.html`
- **Fungsi**: Menampilkan data mobil dalam bentuk tabel dan detail

```python
@app.route('/')
def index():
    cars = Car.select()
    return render_template('index.html', cars=cars)
```

#### 3. **UPDATE** - Mengubah Data Mobil ⭐ **REQUIREMENT**
- **Route**: `/updatecar/<int:car_id>` (GET, POST)
- **Template**: `updatecar.html`
- **Fungsi**: Form untuk mengubah/edit data mobil yang sudah ada

```python
@app.route('/updatecar/<int:car_id>', methods=['GET', 'POST'])
def updatecar(car_id):
    car = Car.get_by_id(car_id)
    if request.method == 'POST':
        car.brand = request.form['brand']
        car.model = request.form['model']
        car.year = int(request.form['year'])
        car.color = request.form['color']
        car.price = float(request.form['price'])
        car.save()  # UPDATE database
```

#### 4. **DELETE** - Menghapus Data Mobil
- **Route**: `/deletecar/<int:car_id>` (POST)
- **Fungsi**: Menghapus data mobil dari database

```python
@app.route('/deletecar/<int:car_id>', methods=['POST'])
def deletecar(car_id):
    car = Car.get_by_id(car_id)
    car.delete_instance()  # DELETE dari database
```

#### 5. **SEARCH** - Mencari Data Mobil ⭐ **REQUIREMENT**
- **Route**: `/searchcar` (GET, POST)
- **Template**: `searchcar.html`
- **Fungsi**: Pencarian mobil berdasarkan:
  - Brand (nama merek)
  - Model (tipe mobil)
  - Color (warna mobil)

```python
@app.route('/searchcar', methods=['GET', 'POST'])
def searchcar():
    if request.method == 'POST':
        search_query = request.form.get('query', '')
        cars = Car.select().where(
            (Car.brand.contains(search_query)) |
            (Car.model.contains(search_query)) |
            (Car.color.contains(search_query))
        )
```

---

## ✅ Requirement PBL0302

### Assignment: Create CAR DATA CRUDS dari Chosen Frameworks menggunakan carsweb.db

**Implementasi:**

1. ✅ **Framework yang dipilih**: Flask (Microframework Python)
2. ✅ **Database**: SQLite (`carsweb.db`)
3. ✅ **CRUD Operations**: Semua fitur CRUD telah diimplementasikan
4. ✅ **Model Database**:
   ```python
   class Car(Model):
       id = AutoField()           # ID unik
       brand = CharField()         # Merek mobil
       model = CharField()         # Model mobil
       year = IntegerField()       # Tahun produksi
       color = CharField()         # Warna
       price = FloatField()        # Harga
   ```

5. ✅ **ORM**: Menggunakan Peewee ORM untuk koneksi dengan SQLite

---

## 🚀 Instalasi

### Prasyarat:
- Python 3.7+
- pip (Python Package Manager)
- Virtual Environment

### Langkah-langkah:

#### 1. Clone Repository
```bash
cd Monolith
# atau
git clone https://github.com/hepidad/c003-monolith
```

#### 2. Buat Virtual Environment
```bash
python3 -m venv monolith-env
```

#### 3. Aktivasi Virtual Environment

**Windows:**
```bash
monolith-env\Scripts\activate
```

**Linux/Mac:**
```bash
source monolith-env/bin/activate
```

#### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 5. Jalankan Aplikasi
```bash
python app.py
```

#### 6. Buka Browser
```
http://localhost:5000
```

---

## 📱 Menjalankan Aplikasi

### Mode Development:
```bash
# Terminal 1: Aktivasi venv
source monolith-env/bin/activate  # Linux/Mac
# atau
monolith-env\Scripts\activate     # Windows

# Terminal 2: Jalankan Flask
python app.py

# Buka di browser: http://localhost:5000
```

### Mode Production (Optional):
Menggunakan Gunicorn atau Uvicorn:

```bash
# Install Gunicorn
pip install gunicorn

# Jalankan dengan Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

---

## ✨ Fitur-Fitur

### Frontend:
- ✅ Responsive Design (Bootstrap 5)
- ✅ Navigation Bar dengan menu
- ✅ Flash Messages (Success, Warning, Error)
- ✅ Data Table yang interaktif
- ✅ Form Validation
- ✅ Color Badge untuk warna mobil

### Backend:
- ✅ Flask Web Framework
- ✅ Peewee ORM untuk database
- ✅ SQLite Database
- ✅ MVC Architecture
- ✅ Error Handling
- ✅ CRUD Operations lengkap

---

## 💻 Penjelasan Kode

### 1. **Model (app.py - Database Layer)**

```python
class Car(Model):
    id = AutoField()           # Primary Key
    brand = CharField()         # Tipe data text
    model = CharField()
    year = IntegerField()       # Tipe data integer
    color = CharField()
    price = FloatField()        # Tipe data decimal
    
    class Meta:
        database = db           # Koneksi ke database
        table_name = 'cars'     # Nama tabel
```

### 2. **View (Templates - User Interface)**

```html
<!-- Menggunakan Jinja2 Template Engine -->
{% for car in cars %}
    <tr>
        <td>{{ car.brand }}</td>
        <td>{{ car.model }}</td>
        <!-- Menampilkan data dari database -->
    </tr>
{% endfor %}
```

### 3. **Controller (app.py - Business Logic)**

```python
@app.route('/updatecar/<int:car_id>', methods=['GET', 'POST'])
def updatecar(car_id):
    # Ambil data dari database
    car = Car.get_by_id(car_id)
    
    # Process form POST
    if request.method == 'POST':
        # Update data
        car.brand = request.form['brand']
        car.save()  # Simpan ke database
        
    # Render template dengan data
    return render_template('updatecar.html', car=car)
```

---

## 🗄️ Database Schema

### Tabel: `cars`

| Field | Type | Constraint | Keterangan |
|-------|------|-----------|-----------|
| id | INTEGER | PRIMARY KEY | ID unik mobil |
| brand | TEXT | NOT NULL | Merek mobil |
| model | TEXT | NOT NULL | Model mobil |
| year | INTEGER | NOT NULL | Tahun produksi |
| color | TEXT | NOT NULL | Warna mobil |
| price | REAL | NOT NULL | Harga (Rupiah) |

---

## 📝 Contoh Data

```
ID | Brand  | Model   | Tahun | Warna | Harga
---|--------|---------|-------|-------|----------
1  | Toyota | Avanza  | 2023  | Merah | 150000000
2  | Honda  | Civic   | 2022  | Putih | 250000000
3  | Nissan | X-Trail | 2021  | Hitam | 350000000
```

---

## 🔗 Links Penting

- **GitHub Repository**: https://github.com/hepidad/c003-monolith
- **Flask Documentation**: https://flask.palletsprojects.com/
- **Peewee Documentation**: https://docs.peewee-orm.com/
- **Bootstrap**: https://getbootstrap.com/

---

## 📖 MVC Architecture Explanation

### Model (DATABASE)
- File: `app.py` - Class `Car`
- Bertanggung jawab untuk struktur data dan database operations
- Peewee ORM menghubungkan Python dengan SQLite

### View (FRONTEND)
- File: `templates/*.html`
- Menampilkan data kepada user
- Menggunakan Jinja2 Template Engine
- Bootstrap 5 untuk styling

### Controller (BACKEND LOGIC)
- File: `app.py` - @app.route functions
- Menangani request dari user
- Memanggil model untuk operasi database
- Merender view dengan data yang sesuai

---

## 🎓 Pembelajaran Penting

### Konsep Monolith:
Aplikasi ini adalah **Monolithic Architecture** dimana:
- Front-end dan Back-end dalam satu codebase
- Satu database untuk semua fitur
- Scalability terbatas (cocok untuk aplikasi kecil-menengah)

### MVC Pattern:
- **Separation of Concerns**: Model, View, Controller terpisah
- **Reusable Code**: Mudah dimodifikasi dan di-maintain
- **Testing**: Lebih mudah untuk unit testing

### CRUD Operations:
- **Create**: INSERT data baru
- **Read**: SELECT data untuk ditampilkan
- **Update**: MODIFY data yang ada
- **Delete**: REMOVE data dari database
- **Search**: FILTER data berdasarkan kriteria

---

## 🐛 Troubleshooting

### Error: ModuleNotFoundError: No module named 'flask'
```bash
pip install flask
pip install -r requirements.txt
```

### Error: Database is locked
- Tutup semua koneksi database
- Hapus file `*.db-journal` jika ada

### Error: Port 5000 sudah digunakan
```bash
python app.py --port 5001
```

---

## 📞 Support

Jika ada pertanyaan, hubungi:
- **Dosen**: Irwan Kautsar, Ph.D (Assoc. Prof.)
- **Email**: hepidad@umsida.ac.id
- **Link**: https://bit.ly/hepidad

---

## 📄 License

Dokumentasi untuk keperluan pembelajaran di Universitas Muhammadiyah Sidoarjo

**Dibuat oleh**: Irwan Kautsar, Ph.D  
**Revisi**: Version 15102025.16.12
