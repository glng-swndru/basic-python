# Variabel di Python

# 1. Definisi Variabel
# Variabel adalah tempat untuk menyimpan data yang bisa digunakan dan dimodifikasi sepanjang program.
# Di Python, Anda tidak perlu mendeklarasikan tipe data secara eksplisit.

# Deklarasi variabel
nama = "Gilang"
umur = 23
tinggi = 175.5

print(f"Nama: {nama}")
print(f"Umur: {umur}")
print(f"Tinggi: {tinggi}")

# 2. Tipe Data Variabel
# Python adalah bahasa pemrograman yang dinamis, artinya tipe data variabel bisa berubah-ubah.

# Mengubah tipe data
umur = 25  # integer
print(f"Umur (integer): {umur}")

umur = "Dua puluh lima"  # string
print(f"Umur (string): {umur}")

# 3. Penamaan Variabel
# Penamaan variabel harus mengikuti aturan berikut:
# - Nama variabel hanya boleh mengandung huruf, angka, dan garis bawah (_)
# - Nama variabel tidak boleh dimulai dengan angka
# - Nama variabel bersifat case-sensitive (misalnya, `nama` dan `Nama` dianggap berbeda)

# Contoh penamaan variabel yang valid
nama_depan = "Gilang"
namaBelakang = "Hadi"
_namaLengkap = "Gilang Hadi"
nama2 = "Gilang"

print(nama_depan)
print(namaBelakang)
print(_namaLengkap)
print(nama2)

# 4. Variabel Global dan Lokal
# Variabel global dideklarasikan di luar fungsi dan dapat diakses di seluruh bagian program.
# Variabel lokal dideklarasikan di dalam fungsi dan hanya dapat diakses di dalam fungsi tersebut.

# Variabel global
x = 10

def fungsi():
    # Variabel lokal
    y = 5
    print(f"Variabel lokal y: {y}")
    print(f"Variabel global x di dalam fungsi: {x}")

fungsi()
print(f"Variabel global x di luar fungsi: {x}")

# 5. Konstanta
# Meskipun Python tidak memiliki tipe data konstan, konvensi menggunakan huruf kapital untuk variabel yang tidak diubah.

PI = 3.14159
GRAVITY = 9.8

print(f"PI: {PI}")
print(f"Gravity: {GRAVITY}")

# 6. Multiple Assignment
# Anda bisa menginisialisasi beberapa variabel dalam satu baris.

a, b, c = 1, 2, 3
print(f"a: {a}, b: {b}, c: {c}")

# 7. Variabel Dinamis
# Di Python, Anda bisa mengubah nilai variabel menjadi tipe data lain di kemudian hari.

x = 10  # integer
print(f"x (integer): {x}")

x = "Hello"  # string
print(f"x (string): {x}")

# 8. Variabel dan Memori
# Python mengelola memori secara otomatis dan mengumpulkan sampah (garbage collection) untuk variabel yang tidak lagi digunakan.

import sys

x = "Hello, Python!"
print(f"ID x: {id(x)}")
print(f"Ukuran x dalam bytes: {sys.getsizeof(x)}")

x = None  # Menghapus referensi
print(f"ID x setelah dihapus: {id(x)}")


# Penjelasan tambahan:
# Definisi Variabel: Menyimpan data dengan nama untuk digunakan dalam program.
# Tipe Data Variabel: Variabel di Python bisa berubah tipe data.
# Penamaan Variabel: Aturan untuk nama variabel dan contoh nama yang valid.
# Variabel Global dan Lokal: Perbedaan antara variabel yang dideklarasikan di luar dan di dalam fungsi.
# Konstanta: Konvensi untuk variabel yang tidak berubah menggunakan huruf kapital.
# Multiple Assignment: Inisialisasi beberapa variabel dalam satu baris.
# Variabel Dinamis: Kemampuan Python untuk mengubah tipe data variabel.
# Variabel dan Memori: Manajemen memori dan cara Python mengelola memori untuk variabel.
