import os
import shutil

# Daftar file HTML yang harus dipindahkan
html_files = [
    'base.html',
    'createcar.html',
    'index.html',
    'readcar.html',
    'searchcar.html',
    'updatecar.html'
]

# Buat folder templates jika belum ada
if not os.path.exists('templates'):
    os.makedirs('templates')
    print("✅ Folder 'templates' dibuat")
else:
    print("✅ Folder 'templates' sudah ada")

# Pindahkan semua file HTML
for file in html_files:
    source = file
    destination = f'templates/{file}'
    
    if os.path.exists(source):
        # Jika file sudah ada di destination, hapus dulu
        if os.path.exists(destination):
            os.remove(destination)
        
        shutil.move(source, destination)
        print(f"✅ Dipindahkan: {file} → templates/{file}")
    elif os.path.exists(destination):
        print(f"✅ Sudah ada: {file} di templates/{file}")
    else:
        print(f"⚠️  File tidak ditemukan: {file}")

print("\n" + "="*50)
print("✅ Setup selesai!")
print("="*50)
print("\nJalankan sekarang:")
print("  python app.py")
print("\nLalu buka browser:")
print("  http://localhost:5000")
