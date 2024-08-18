# Seleksi Kondisi di Python

# if statement
# if digunakan untuk menjalankan blok kode jika kondisi yang diberikan adalah benar (True)
nilai = 85
if nilai > 75:
    print("Nilai Anda di atas rata-rata!")

# if-else statement
# if-else digunakan untuk memilih antara dua blok kode: satu dijalankan jika kondisi benar, dan lainnya dijalankan jika kondisi salah
nilai = 60
if nilai >= 75:
    print("Selamat, Anda lulus!")
else:
    print("Maaf, Anda belum lulus.")

# if-elif-else statement
# if-elif-else digunakan untuk memeriksa beberapa kondisi yang berbeda
nilai = 85
if nilai >= 90:
    print("Nilai Anda A")
elif nilai >= 80:
    print("Nilai Anda B")
elif nilai >= 70:
    print("Nilai Anda C")
else:
    print("Nilai Anda D atau lebih rendah")

# Nested if
# Nested if adalah if statement yang berada di dalam if statement lain, digunakan untuk memeriksa kondisi yang lebih kompleks
umur = 25
pendapatan = 50000

if umur > 18:
    if pendapatan >= 40000:
        print("Anda memenuhi syarat untuk pinjaman.")
    else:
        print("Pendapatan Anda belum memenuhi syarat untuk pinjaman.")
else:
    print("Anda belum cukup umur untuk mengajukan pinjaman.")

# Ternary Operator
# Ternary operator adalah cara singkat untuk menulis if-else dalam satu baris
# Format: <nilai jika benar> if <kondisi> else <nilai jika salah>
nilai = 80
hasil = "Lulus" if nilai >= 75 else "Tidak Lulus"
print(hasil)

# Contoh yang lebih kompleks menggunakan Ternary Operator
umur = 20
izin = True
status = "Boleh masuk" if umur >= 18 and izin else "Tidak boleh masuk"
print(status)

# Logical Operators
# Logical operators seperti and, or, not sering digunakan dalam kondisi if
# and - kondisi benar jika semua operand benar
# or - kondisi benar jika salah satu operand benar
# not - membalikkan nilai boolean

# Contoh dengan and
nilai_teori = 80
nilai_praktek = 85
if nilai_teori >= 75 and nilai_praktek >= 75:
    print("Anda lulus ujian teori dan praktek!")

# Contoh dengan or
hari = "Minggu"
if hari == "Sabtu" or hari == "Minggu":
    print("Selamat, ini adalah akhir pekan!")

# Contoh dengan not
cuaca = "hujan"
if not cuaca == "cerah":
    print("Bawa payung!")

# Contoh penggunaan kombinasi kondisi dan operator logika
umur = 18
izin_orang_tua = False
if umur >= 18 or izin_orang_tua:
    print("Anda diizinkan menonton film.")
else:
    print("Anda tidak diizinkan menonton film.")

# Penjelasan Tambahan:
# if statement: Digunakan untuk menjalankan blok kode jika suatu kondisi terpenuhi.
# if-else statement: Memilih antara dua jalur eksekusi berdasarkan kondisi.
# if-elif-else statement: Untuk memeriksa beberapa kondisi bertingkat.
# Nested if: Menggunakan if di dalam if untuk memeriksa kondisi lebih lanjut.
# Ternary Operator: Cara singkat untuk if-else dalam satu baris.
# Logical Operators: and, or, dan not untuk menggabungkan beberapa kondisi.