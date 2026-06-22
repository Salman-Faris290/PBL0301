from flask import Flask, render_template, request, redirect, url_for, flash
from peewee import *
import os

# Inisialisasi Flask
app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Koneksi Database SQLite
db = SqliteDatabase('carsweb.db')

# Model Database - Car
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

# Buat table jika belum ada
db.create_tables([Car], safe=True)

# ===== ROUTES =====

# 1. READ - Tampilkan semua data cars
@app.route('/')
def index():
    cars = Car.select()
    return render_template('index.html', cars=cars)

# 2. CREATE - Buat data car baru
@app.route('/createcar', methods=['GET', 'POST'])
def createcar():
    if request.method == 'POST':
        try:
            brand = request.form['brand']
            model = request.form['model']
            year = request.form['year']
            color = request.form['color']
            price = request.form['price']
            
            Car.create(
                brand=brand,
                model=model,
                year=int(year),
                color=color,
                price=float(price)
            )
            flash(f'Mobil {brand} {model} berhasil ditambahkan!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')
    
    return render_template('createcar.html')

# 3. READ - Detail satu data car
@app.route('/readcar/<int:car_id>')
def readcar(car_id):
    try:
        car = Car.get_by_id(car_id)
        return render_template('readcar.html', car=car)
    except:
        flash('Mobil tidak ditemukan', 'danger')
        return redirect(url_for('index'))

# 4. UPDATE - Update data car (ASSIGNMENT REQUIREMENT)
@app.route('/updatecar/<int:car_id>', methods=['GET', 'POST'])
def updatecar(car_id):
    try:
        car = Car.get_by_id(car_id)
    except:
        flash('Mobil tidak ditemukan', 'danger')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        try:
            car.brand = request.form['brand']
            car.model = request.form['model']
            car.year = int(request.form['year'])
            car.color = request.form['color']
            car.price = float(request.form['price'])
            car.save()
            
            flash(f'Mobil {car.brand} {car.model} berhasil diperbarui!', 'success')
            return redirect(url_for('readcar', car_id=car.id))
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')
    
    return render_template('updatecar.html', car=car)

# 5. DELETE - Hapus data car
@app.route('/deletecar/<int:car_id>', methods=['POST'])
def deletecar(car_id):
    try:
        car = Car.get_by_id(car_id)
        brand_model = f"{car.brand} {car.model}"
        car.delete_instance()
        flash(f'Mobil {brand_model} berhasil dihapus!', 'success')
    except:
        flash('Mobil tidak ditemukan', 'danger')
    
    return redirect(url_for('index'))

# 6. SEARCH - Cari data car (ASSIGNMENT REQUIREMENT)
@app.route('/searchcar', methods=['GET', 'POST'])
def searchcar():
    cars = []
    search_query = ''
    
    if request.method == 'POST':
        search_query = request.form.get('query', '')
        
        if search_query:
            # Search by brand, model, atau color
            cars = Car.select().where(
                (Car.brand.contains(search_query)) |
                (Car.model.contains(search_query)) |
                (Car.color.contains(search_query))
            )
            
            if not cars.exists():
                flash(f'Tidak ada mobil yang cocok dengan "{search_query}"', 'info')
        else:
            flash('Masukkan kata kunci pencarian', 'warning')
    
    return render_template('searchcar.html', cars=cars, search_query=search_query)

# Error handling
@app.errorhandler(404)
def not_found(e):
    flash('Halaman tidak ditemukan', 'danger')
    return redirect(url_for('index'))

@app.errorhandler(500)
def server_error(e):
    flash('Terjadi kesalahan server', 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
