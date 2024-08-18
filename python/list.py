# List di Python

# 1. Pengertian List
# List adalah struktur data yang dapat menampung berbagai jenis elemen dan bersifat mutable (dapat diubah).
# List dapat menyimpan elemen-elemen dengan tipe data yang berbeda, dan elemen-elemen tersebut diakses menggunakan indeks.

# Membuat list kosong
list_kosong = []

# Membuat list dengan beberapa elemen
buah = ["apel", "jeruk", "pisang"]
angka = [1, 2, 3, 4, 5]
campuran = ["apel", 2, True, 3.5]

print(buah)
print(angka)
print(campuran)

# 2. Mengakses Elemen List
# Elemen-elemen dalam list dapat diakses menggunakan indeks. Indeks di Python dimulai dari 0.

print(buah[0])  # Mengakses elemen pertama
print(angka[2])  # Mengakses elemen ketiga
print(campuran[-1])  # Mengakses elemen terakhir

# 3. Mengubah Elemen List
# Karena list bersifat mutable, kita bisa mengubah elemen di dalamnya.

buah[0] = "mangga"
print(buah)

# 4. Menambahkan Elemen ke List
# Elemen dapat ditambahkan ke list menggunakan metode `append()`, `insert()`, atau `extend()`.

# Menggunakan append() untuk menambahkan elemen di akhir list
buah.append("stroberi")
print(buah)

# Menggunakan insert() untuk menambahkan elemen pada indeks tertentu
buah.insert(1, "durian")
print(buah)

# Menggunakan extend() untuk menambahkan beberapa elemen dari iterable lain
buah_lain = ["kiwi", "nanas"]
buah.extend(buah_lain)
print(buah)

# 5. Menghapus Elemen dari List
# Elemen dapat dihapus dari list menggunakan metode `remove()`, `pop()`, atau kata kunci `del`.

# Menggunakan remove() untuk menghapus elemen pertama yang cocok
buah.remove("durian")
print(buah)

# Menggunakan pop() untuk menghapus elemen pada indeks tertentu (atau elemen terakhir jika indeks tidak ditentukan)
buah.pop(2)  # Menghapus elemen ketiga
print(buah)

# Menggunakan del untuk menghapus elemen pada indeks tertentu
del buah[0]  # Menghapus elemen pertama
print(buah)

# 6. Slicing pada List
# List dapat diiris (slicing) untuk mendapatkan sublist dari list asli.

sublist = angka[1:4]  # Mengambil elemen dari indeks 1 hingga 3
print(sublist)

# Mengiris dengan langkah (step)
sublist_step = angka[::2]  # Mengambil elemen dengan langkah 2
print(sublist_step)

# 7. Menggabungkan dan Menggandakan List
# Dua list dapat digabungkan menggunakan operator `+`, dan list dapat digandakan menggunakan operator `*`.

gabungan = buah + buah_lain
print(gabungan)

gandakan = angka * 3
print(gandakan)

# 8. Memeriksa Keanggotaan Elemen
# Anda dapat memeriksa apakah suatu elemen ada di dalam list menggunakan kata kunci `in` atau `not in`.

ada_jeruk = "jeruk" in buah
print(ada_jeruk)

tidak_ada_melon = "melon" not in buah
print(tidak_ada_melon)

# 9. List Comprehensions
# List comprehensions adalah cara singkat dan efisien untuk membuat list baru dengan menggunakan for loop.

# Membuat list baru dari list yang sudah ada
angka_kuadrat = [x**2 for x in angka]
print(angka_kuadrat)

# List comprehension dengan kondisi
angka_genap = [x for x in angka if x % 2 == 0]
print(angka_genap)

# 10. Fungsi-fungsi Built-in untuk List
# Python menyediakan beberapa fungsi built-in yang dapat digunakan dengan list.

panjang = len(angka)  # Menghitung jumlah elemen dalam list
print(panjang)

nilai_terbesar = max(angka)  # Mendapatkan nilai terbesar dalam list
print(nilai_terbesar)

nilai_terkecil = min(angka)  # Mendapatkan nilai terkecil dalam list
print(nilai_terkecil)

total = sum(angka)  # Menghitung total dari elemen-elemen numerik dalam list
print(total)

urutan = sorted(angka, reverse=True)  # Mengurutkan elemen-elemen dalam list
print(urutan)

# 11. Metode-meteode List
# Python memiliki berbagai metode yang dapat digunakan dengan list untuk memanipulasi data.

angka.reverse()  # Membalik urutan elemen dalam list
print(angka)

angka.sort()  # Mengurutkan elemen-elemen dalam list
print(angka)

indeks_angka = angka.index(3)  # Mendapatkan indeks pertama dari nilai tertentu
print(indeks_angka)

jumlah_angka = angka.count(3)  # Menghitung jumlah kemunculan nilai tertentu
print(jumlah_angka)
